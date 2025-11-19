# compilers/esper_to_spanish.py
"""
Esper (VSE markup) → Spanish renderer
Parallel to esper_to_english, but output is in Spanish.
"""

from dataclasses import dataclass
from typing import List
from esper_to_english import (
    Volume, Section, Frame, Line, Tag, Directive,
    parse_vse,  # reuse identical parser!
)

# ------------- Spanish Renderer -------------

def render_heading_es(volume: Volume) -> str:
    return f"Volumen {volume.id}\n"

def render_section_es(sec: Section, mode: str = "narrative") -> str:
    parts = [f"\nSección: {sec.ref}"]
    for fr in sec.frames:
        parts.append(render_frame_es(fr, mode=mode))
    return "\n".join(parts)

def _render_frame_header_hybrid_es(fr: Frame) -> str:
    head: List[str] = []
    if fr.type:
        title = fr.type.capitalize()
        if fr.id:
            title += f": {fr.id}"
        head.append(title)
    if fr.role:
        head.append(f"Rol: {fr.role}")
    if fr.tags:
        tags = [f"{t.namespace} — {t.name}" for t in fr.tags]
        head.append("Etiquetas míticas: " + ", ".join(tags))
    if fr.directives:
        metas = [f"{d.key}: {d.value}" for d in fr.directives]
        head.append("Directivas: " + "; ".join(metas))
    return "\n".join(head)

def _render_frame_header_literal_es(fr: Frame) -> str:
    header = [f"[MARCO tipo={fr.type!r}"]
    if fr.id:
        header.append(f"id={fr.id!r}")
    if fr.role:
        header.append(f"rol={fr.role!r}")
    header_str = " ".join(header) + "]"

    lines = [header_str]

    if fr.tags:
        tag_strs = [f"{t.namespace}:{t.name}" for t in fr.tags]
        lines.append("ETIQUETAS: " + ", ".join(tag_strs))
    if fr.directives:
        meta_strs = [f"{d.key}={d.value}" for d in fr.directives]
        lines.append("METADATOS: " + "; ".join(meta_strs))
    return "\n".join(lines)

def render_frame_es(fr: Frame, mode: str = "narrative") -> str:
    # ----- Header -----
    header = ""
    if mode == "narrative":
        if fr.type or fr.id or fr.role:
            pieces = []
            if fr.type:
                pieces.append(fr.type.capitalize())
            if fr.id:
                pieces.append(f"({fr.id})")
            if fr.role:
                pieces.append(f"[{fr.role}]")
            header = " ".join(pieces)
    elif mode == "hybrid":
        h = _render_frame_header_hybrid_es(fr)
        if h:
            header = h
    elif mode == "literal":
        header = _render_frame_header_literal_es(fr)

    if header:
        header = "\n" + header

    # ----- Body -----
    lines_out: List[str] = []
    for ln in fr.lines:
        speaker = f"{ln.speaker}: " if ln.speaker else ""
        text = ln.text
        if ln.emphasis:
            text = f"(énfasis) {text}" if mode != "literal" else f"[ÉNFASIS] {text}"
        lines_out.append(f"{speaker}{text}")

    body = "\n".join(lines_out)
    return header + ("\n" + body if body else "")

def render_volume_es(vol: Volume, mode: str = "narrative") -> str:
    parts = [render_heading_es(vol)]
    for sec in vol.sections:
        parts.append(render_section_es(sec, mode=mode))
    return "\n".join(parts).strip() + "\n"

# ------------- Public API -------------

def compile_vse_to_spanish(vse_text: str, mode: str = "narrative") -> str:
    vol = parse_vse(vse_text)
    return render_volume_es(vol, mode)

# ------------- CLI -------------

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    ap = argparse.ArgumentParser(description="Esper (VSE) → Spanish compiler")
    ap.add_argument("input", help="Path to VSE file")
    ap.add_argument(
        "-m", "--mode",
        default="narrative",
        choices=["narrative", "literal", "hybrid"],
    )
    ap.add_argument(
        "-o", "--output",
        default="-",
    )
    args = ap.parse_args()

    vse_text = Path(args.input).read_text(encoding="utf-8")
    spanish = compile_vse_to_spanish(vse_text, mode=args.mode)

    if args.output == "-":
        print(spanish)
    else:
        Path(args.output).write_text(spanish, encoding="utf-8")
