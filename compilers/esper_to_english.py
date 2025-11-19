#!/usr/bin/env python3
# compilers/esper_to_english.py
"""
Esper (VSE markup) → English frontside compiler.

Parses the lightweight VSE text format used in Volumes into a structured
AST (Volume → Section → Frame → Line), then renders it back into
human-readable English in one of three modes:

- narrative : minimal metadata, story-first output
- hybrid    : headings + mythic/meta info (default "commentary" feel)
- literal   : explicit structural dump, good for debugging and tooling
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import re
import json

# --------- Data model ---------

@dataclass
class Directive:
    key: str
    value: str

@dataclass
class Tag:
    namespace: str
    name: str

@dataclass
class Line:
    speaker: Optional[str]
    text: str
    emphasis: bool = False

@dataclass
class Frame:
    type: str
    id: Optional[str] = None
    role: Optional[str] = None
    tags: List[Tag] = field(default_factory=list)
    directives: List[Directive] = field(default_factory=list)
    lines: List[Line] = field(default_factory=list)

@dataclass
class Section:
    ref: str
    frames: List[Frame] = field(default_factory=list)

@dataclass
class Volume:
    id: str
    sections: List[Section] = field(default_factory=list)

# --------- Grammar (regexes) ---------

VOL_RE   = re.compile(r'@volume\s*\(\s*id\s*=\s*"([^"]+)"\s*\)')
SEC_RE   = re.compile(r'@section\s*\(\s*ref\s*=\s*"([^"]+)"\s*\)')
FRAME_RE = re.compile(
    r'#frame\s*\(\s*type\s*=\s*"([^"]+)"(?:\s*,\s*id\s*=\s*"([^"]+)")?\s*\)'
)
ROLE_RE  = re.compile(r'\{\s*role\s*=\s*([a-zA-Z0-9_:\-]+)\s*\}')
TAG_RE   = re.compile(r'Myth\.Tag\(\s*"([^":]+):([^"]+)"\s*\)')
META_RE  = re.compile(r'!meta\s*\(\s*key\s*=\s*"([^"]+)"\s*,\s*value\s*=\s*"([^"]+)"\s*\)')
LINE_SPOKEN_RE   = re.compile(r'^\s*>\s*"(.+)"\s*$')
LINE_EMPHASIS_RE = re.compile(r'^\s*>>\s*(.+)\s*$')
SPEAKER_RE       = re.compile(r'^\s*([A-Z][A-Za-z0-9_\- ]+):\s*$')  # explicit speaker line

# --------- Parser ---------

def parse_vse(text: str) -> Volume:
    """
    Parse raw VSE markup text into a Volume AST.
    """
    lines = text.splitlines()
    volume: Optional[Volume] = None
    current_section: Optional[Section] = None
    current_frame: Optional[Frame] = None
    current_speaker: Optional[str] = None

    for raw in lines:
        # Volume declaration
        m = VOL_RE.search(raw)
        if m:
            volume = Volume(id=m.group(1))
            continue

        # Section declaration
        m = SEC_RE.search(raw)
        if m:
            current_section = Section(ref=m.group(1))
            if volume is None:
                volume = Volume(id="unknown")
            volume.sections.append(current_section)
            continue

        # Frame declaration
        m = FRAME_RE.search(raw)
        if m:
            current_frame = Frame(type=m.group(1), id=m.group(2))
            if current_section is None:
                current_section = Section(ref="unknown")
                if volume is None:
                    volume = Volume(id="unknown")
                volume.sections.append(current_section)
            current_section.frames.append(current_frame)
            continue

        # Role binding
        m = ROLE_RE.search(raw)
        if m and current_frame is not None:
            current_frame.role = m.group(1)
            # don't continue; roles can appear on lines that also include tags/meta

        # Mythic tags (can be multiple per line)
        if current_frame is not None:
            for t_match in TAG_RE.finditer(raw):
                ns, name = t_match.groups()
                current_frame.tags.append(Tag(namespace=ns, name=name))

        # Meta directives (can be multiple per line)
        if current_frame is not None:
            for d_match in META_RE.finditer(raw):
                key, value = d_match.groups()
                current_frame.directives.append(Directive(key=key, value=value))

        # Explicit speaker line ("AUDREY:" etc.)
        m = SPEAKER_RE.match(raw)
        if m:
            current_speaker = m.group(1).strip()
            continue

        # Spoken line (>)
        m = LINE_SPOKEN_RE.match(raw)
        if m:
            if current_frame is None:
                # Implicit frame/section/volume scaffolding
                current_frame = Frame(type="scene", id=None)
                if current_section is None:
                    current_section = Section(ref="implicit")
                    if volume is None:
                        volume = Volume(id="implicit")
                    volume.sections.append(current_section)
                current_section.frames.append(current_frame)

            current_frame.lines.append(
                Line(speaker=current_speaker, text=m.group(1))
            )
            continue

        # Emphasis line (>>)
        m = LINE_EMPHASIS_RE.match(raw)
        if m:
            if current_frame is None:
                current_frame = Frame(type="scene", id=None)
                if current_section is None:
                    current_section = Section(ref="implicit")
                    if volume is None:
                        volume = Volume(id="implicit")
                    volume.sections.append(current_section)
                current_section.frames.append(current_frame)

            current_frame.lines.append(
                Line(speaker=current_speaker, text=m.group(1), emphasis=True)
            )
            continue

        # All other lines are currently ignored; could log/debug here.

    if volume is None:
        volume = Volume(id="unknown")
    return volume

# --------- English renderer ---------

def render_heading(volume: Volume) -> str:
    return f"Volume {volume.id}\n"

def render_section(sec: Section, mode: str = "narrative") -> str:
    parts = [f"\nSection: {sec.ref}"]
    for fr in sec.frames:
        parts.append(render_frame(fr, mode=mode))
    return "\n".join(parts)

def _render_frame_header_hybrid(fr: Frame) -> str:
    head: List[str] = []
    if fr.type:
        title = fr.type.capitalize()
        if fr.id:
            title += f": {fr.id}"
        head.append(title)
    if fr.role:
        head.append(f"Role: {fr.role}")
    if fr.tags:
        tag_strs = [f"{t.namespace} — {t.name}" for t in fr.tags]
        head.append("Mythic tags: " + ", ".join(tag_strs))
    if fr.directives:
        meta_strs = [f"{d.key}: {d.value}" for d in fr.directives]
        head.append("Directives: " + "; ".join(meta_strs))
    return "\n".join(head)

def _render_frame_header_literal(fr: Frame) -> str:
    header = [f"[FRAME type={fr.type!r}"]
    if fr.id is not None:
        header.append(f"id={fr.id!r}")
    if fr.role is not None:
        header.append(f"role={fr.role!r}")
    header_str = " ".join(header) + "]"
    lines = [header_str]

    if fr.tags:
        tag_strs = [f"{t.namespace}:{t.name}" for t in fr.tags]
        lines.append("TAGS: " + ", ".join(tag_strs))
    if fr.directives:
        meta_strs = [f"{d.key}={d.value}" for d in fr.directives]
        lines.append("META: " + "; ".join(meta_strs))
    return "\n".join(lines)

def render_frame(fr: Frame, mode: str = "narrative") -> str:
    """
    Render a single Frame into English according to the selected mode.
    """
    mode = mode or "narrative"

    # ---------- Header ----------
    header = ""
    if mode == "narrative":
        # Minimal, story-first header
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
        h = _render_frame_header_hybrid(fr)
        if h:
            header = h
    elif mode == "literal":
        header = _render_frame_header_literal(fr)

    if header:
        header = "\n" + header

    # ---------- Body ----------
    lines_out: List[str] = []
    for ln in fr.lines:
        speaker = f"{ln.speaker}: " if ln.speaker else ""
        text = ln.text
        if ln.emphasis:
            if mode == "literal":
                text = f"[EMPHASIS] {text}"
            else:
                text = f"(emphasis) {text}"
        lines_out.append(f"{speaker}{text}")

    body = "\n".join(lines_out)
    return header + ("\n" + body if body else "")

def render_volume(vol: Volume, mode: str = "narrative") -> str:
    """
    Render a whole Volume to English.
    """
    parts = [render_heading(vol)]
    for sec in vol.sections:
        parts.append(render_section(sec, mode=mode))
    return "\n".join(parts).strip() + "\n"

# --------- Public API ---------

def compile_vse_to_english(vse_text: str, mode: str = "narrative") -> str:
    """
    High-level frontside compiler:
        VSE markup text → English string.
    """
    vol = parse_vse(vse_text)
    return render_volume(vol, mode)

# --------- CLI ---------

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    ap = argparse.ArgumentParser(description="Esper (VSE) → English compiler")
    ap.add_argument("input", help="Path to VSE file")
    ap.add_argument(
        "-m", "--mode",
        default="narrative",
        choices=["narrative", "literal", "hybrid"],
        help="Rendering mode"
    )
    ap.add_argument(
        "-o", "--output",
        default="-",
        help="Path to write English output (default: stdout)"
    )
    ap.add_argument(
        "--json",
        action="store_true",
        help="Emit a JSON dump of the parsed AST instead of prose"
    )
    args = ap.parse_args()

    vse_path = Path(args.input)
    vse_text = vse_path.read_text(encoding="utf-8")

    vol = parse_vse(vse_text)

    if args.json:
        # Simple JSON view of the AST for tooling / debugging
        def default(o):
            if isinstance(o, (Volume, Section, Frame, Line, Tag, Directive)):
                return o.__dict__
            raise TypeError(f"Not JSON serializable: {type(o)}")

        payload = json.dumps(vol, default=default, indent=2, ensure_ascii=False)
        if args.output == "-":
            print(payload)
        else:
            Path(args.output).write_text(payload, encoding="utf-8")
    else:
        english = render_volume(vol, mode=args.mode)
        if args.output == "-":
            print(english)
        else:
            Path(args.output).write_text(english, encoding="utf-8")
