#!/usr/bin/env python3
"""
VSE SENTINEL v0.2
Deterministic Shot Card linter. Twelve laws. No model in the loop.

  sentinel.py xsheet   <card.vse>       # the exposure sheet - see the holes
  sentinel.py lint     <card.vse>
  sentinel.py compile  <card.vse>       # refuses on ERROR or RESTAGE
  sentinel.py limits   <platform>
  sentinel.py explain  <LAW_ID>
  sentinel.py test                      # the only claim you need not trust

LAW STATUS
  L2 L3 L4 L5 L7 L8 L9 L10 L11    enforced
  L12                             enforced on the platform manifest
  L1  Projection                  NOT IMPLEMENTED - needs emission profiles
  L6  Bounded Repair              NOT IMPLEMENTED - workflow, not lint
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field

# ─────────────────────────────────────────────────────────────
# PLATFORM MANIFEST
# Law 12: every numeral carries its denominator.
# `triggers` gates each advisory so evidence does not decay into noise.
# ─────────────────────────────────────────────────────────────

PLATFORMS = {
    "veo": {
        "owns_duration": True,
        "dur_grade": "F",
        "dur_observed": [10],
        "dur_evidence": "8s requested 2/2, 10s delivered 2/2. No other value tested.",
        "observations": {
            "camera_stop_midclip": dict(
                s=0, n=2, triggers=["CAMERA_REST"],
                note="n=2 - insufficient. Do not treat as established."),
            "bounded_angle": dict(
                s=0, n=2, triggers=["ANGLE"],
                note="8deg specified -> full crane delivered. n=2."),
            "fine_texture_stable": dict(
                s=0, n=3, triggers=["LEGIBLE_DETAIL"],
                note="dial numerals unstable across clip. n=3."),
            "ambient_suppression": dict(
                s=2, n=2, triggers=["INERT_CLASS"],
                note="positive enumeration held. n=2."),
            "causal_ordering": dict(
                s=1, n=1, triggers=["CAUSAL_DEP"],
                note="held when evidence was staged foreground. n=1."),
        },
    }
}

PROVENANCE = {
    "L7":  "CLOCKBIRD_v1.0 - camera budgeted past t_p; the clip could not settle.",
    "L8":  "CLOCKBIRD_v1.0 - 8s requested, 10s delivered; every timestamp rescaled 1.25x.",
    "L9":  "CLOCKBIRD_v1.1 - the dolly evicted the meter from frame before its held state could be verified.",
    "L10": "CLOCKBIRD_v1.0 - the needle had no assigned state for the first 22% of the clip and rendered as an unresolved variable.",
    "L11": "Channel Economy. Redundant manifestation is BUD.AMBIENT for meaning.",
    "L12": "Numerical Provenance. No numeral without a denominator.",
}

LAW_NAMES = {
    "L1": "Projection", "L2": "Backed Locks", "L3": "Positive Motion",
    "L4": "Graded Emission", "L5": "Declared Arrival", "L6": "Bounded Repair",
    "L7": "Total Resolution", "L8": "Normalized Time", "L9": "Frame Custody",
    "L10": "Continuous State Coverage", "L11": "Channel Economy",
    "L12": "Numerical Provenance",
}

# ─────────────────────────────────────────────────────────────
# MODEL
# ─────────────────────────────────────────────────────────────

TRANSITIONAL = re.compile(
    r"\b(RISE|FALL|TURN|ORIENT|MOVE|DOLLY|PUSH|PULL|TILT|PAN|TRANSITION|"
    r"TWITCH|OPEN|CLOSE|FOCUS|CRANE|ZOOM|TRUCK)", re.I)
STATIC_HEAD = re.compile(
    r"^\s*(HOLD|INERT|STATIC|DORMANT|REST|ZERO_HOLD|RAISED_HOLD|OUT_OF_FRAME|LOOP|DRIFT)", re.I)


@dataclass
class Interval:
    a: float
    b: float
    label: str = ""

    def moving(self) -> bool:
        if STATIC_HEAD.match(self.label):
            return False
        return bool(TRANSITIONAL.search(self.label))

    def __repr__(self):
        return f"[{self.a:.2f}-{self.b:.2f}]"


@dataclass
class Element:
    name: str
    cst: int = 0
    vis: int = 0
    states: list[Interval] = field(default_factory=list)
    locked: list[str] = field(default_factory=list)
    ref: list[str] = field(default_factory=list)


@dataclass
class RelEvent:
    """  EVT03  AFTER EVT02+0.03  DUR 0.15  overhead light rises  """
    id: str
    dep: str
    offset: float = 0.0
    dur: float = 0.0
    label: str = ""
    raw: str = ""


@dataclass
class Card:
    shot: str = "untitled"
    platform: str = "veo"
    dur: float | None = None
    dur_grade: str = "E"
    t_p: float | None = None
    mode: str = "SHIFT"
    terminus: str | None = None
    default_state: str | None = None
    elements: dict[str, Element] = field(default_factory=dict)
    bud: list[Interval] = field(default_factory=list)
    time: list[Interval] = field(default_factory=list)      # anchored + resolved
    rel: list[RelEvent] = field(default_factory=list)       # relational, pre-resolution
    sal: list[Interval] = field(default_factory=list)
    coverage: dict[str, list[Interval]] = field(default_factory=dict)
    intents: dict[str, list[str]] = field(default_factory=dict)
    prose: str = ""
    abs_time_lines: list[str] = field(default_factory=list)
    unparsed: list[str] = field(default_factory=list)


@dataclass
class Finding:
    sev: str
    law: str
    msg: str
    fix: str = ""


# ─────────────────────────────────────────────────────────────
# PARSER
# ─────────────────────────────────────────────────────────────

TIME_ABS = re.compile(r"(?<![\d.])(\d{1,2}:\d{2}(?:\.\d+)?|\d+(?:\.\d+)?\s*s\b)")
ARROW = r"(?:->|\u2192|\u2013|\u2014|-)"
IV = re.compile(r"([\d.]+)\s*" + ARROW + r"\s*([\d.]+)\s*(.*)")

# EVT01  0.00-0.22  chamber holds        (anchored, named)
ANCHORED = re.compile(r"(\w+)\s+([\d.]+)\s*" + ARROW + r"\s*([\d.]+)\s*(.*)")
# EVT03  AFTER EVT02+0.03  DUR 0.15  overhead light rises
RELATIONAL = re.compile(
    r"(\w+)\s+AFTER\s+(\w+)(?:\s*\+\s*([\d.]+s?))?"           # id, dep, optional offset
    r"(?:\s+DUR\s+([\d.]+s?))?"                               # optional duration
    r"\s*(.*)", re.I)
# EVT05  AT t_p
AT_TP = re.compile(r"(\w+)\s+AT\s+t_p\s*(.*)", re.I)

BLOCKS = {"BUD", "SAL", "COVERAGE", "INTENT", "PROSE", "TIME"}


def parse(text: str) -> Card:
    c = Card()
    section = None
    cur_el: Element | None = None

    for raw in text.splitlines():
        line = raw.split("#")[0].rstrip()
        if not line.strip():
            continue
        indented = line[0] in " \t"
        t = line.strip()

        if not indented:
            head, *rest = t.split(None, 1)
            head = head.upper()
            val = rest[0].strip() if rest else ""
            cur_el, section = None, None

            if head == "SHOT":
                c.shot = val
            elif head == "PLATFORM":
                c.platform = val.lower()
            elif head == "DUR":
                m = re.search(r"([\d.]+)", val)
                c.dur = float(m.group(1)) if m else None
                g = re.search(r"[<\u27e8]([EBRF])[>\u27e9]", val)
                c.dur_grade = g.group(1) if g else "E"
            elif head in ("T_P", "TP"):
                c.t_p = None if val.upper() == "NONE" else float(val)
            elif head == "MODE":
                c.mode = val.upper()
            elif head == "TERMINUS":
                c.terminus = val.strip()
            elif head == "INERT":
                c.default_state = val or "unlisted elements"
            elif head == "ELEMENT":
                cur_el = Element(name=val)
                c.elements[val] = cur_el
                section = "ELEMENT"
            elif head in BLOCKS:
                section = head
            continue

        if section == "ELEMENT" and cur_el is not None:
            k, *v = t.split(None, 1)
            k, v = k.upper(), (v[0].strip() if v else "")
            if k == "CST":
                cur_el.cst = int(v)
            elif k == "VIS":
                cur_el.vis = int(v)
            elif k == "LOCKED":
                cur_el.locked = [x.strip() for x in v.split(",") if x.strip()]
            elif k == "REF":
                cur_el.ref = [] if v.upper() == "NONE" else [x.strip() for x in v.split(",")]
            elif k == "STATE":
                iv = _iv(v)
                if iv:
                    cur_el.states.append(iv)
                _abs(c, v)
        elif section == "TIME":
            _parse_time_line(c, t)
        elif section in ("BUD", "SAL"):
            iv = _iv(t)
            if iv:
                getattr(c, section.lower()).append(iv)
            _abs(c, t)
        elif section == "COVERAGE":
            iv = _iv(t)
            if iv:
                c.coverage.setdefault(iv.label, []).append(iv)
        elif section == "INTENT":
            if ":" in t:
                k, v = t.split(":", 1)
                c.intents[k.strip()] = [x.strip() for x in v.split(",") if x.strip()]
        elif section == "PROSE":
            c.prose += t + " "

    return c


def _parse_time_line(c: Card, t: str) -> None:
    """TIME accepts three forms. Anything else is a parse failure, and says so."""
    _abs(c, t)

    m = AT_TP.match(t)
    if m:
        c.rel.append(RelEvent(id=m.group(1), dep="__t_p__", offset=0.0, dur=0.0,
                              label=m.group(2).strip(), raw=t))
        return

    m = RELATIONAL.match(t)
    if m and m.group(2):
        c.rel.append(RelEvent(
            id=m.group(1), dep=m.group(2),
            offset=_num(m.group(3)), dur=_num(m.group(4)),
            label=(m.group(5) or "").strip(), raw=t))
        return

    m = ANCHORED.match(t)
    if m:
        c.time.append(Interval(float(m.group(2)), float(m.group(3)),
                               m.group(4).strip() or m.group(1)))
        c.time[-1].eid = m.group(1)          # type: ignore[attr-defined]
        return

    iv = _iv(t)
    if iv:
        c.time.append(iv)
        return

    c.unparsed.append(t)


def _num(s):
    return float(re.sub(r"[^\d.]", "", s)) if s else 0.0


def resolve_dag(c: Card) -> list[Finding]:
    """
    Relational events resolve against anchored ones. Gemini's loop, plus the two
    things it was missing: it must TERMINATE with an accounting, and it must
    refuse cycles. A silently dropped event is a false accusation waiting to
    happen under Law 10.
    """
    f: list[Finding] = []
    anchors: dict[str, Interval] = {}
    for iv in c.time:
        eid = getattr(iv, "eid", None)
        if eid:
            anchors[eid.upper()] = iv
    if c.t_p is not None:
        anchors["__T_P__"] = Interval(c.t_p, c.t_p, "t_p")

    pending = {e.id.upper(): e for e in c.rel}

    # Law 8: an offset in seconds inside a normalized timeline undoes the normalization.
    for e in c.rel:
        if re.search(r"[\d.]\s*s\b", e.raw, re.I):
            f.append(Finding("ERROR", "L8",
                "Relational offset uses absolute units: \u201c%s\u201d" % e.raw,
                "Offsets are fractions too. '+0.4s' does not survive quantization; '+0.04' does."))

    changed = True
    while changed and pending:
        changed = False
        for eid in list(pending):
            e = pending[eid]
            dep = e.dep.upper()
            if dep in anchors:
                start = anchors[dep].b + e.offset
                anchors[eid] = Interval(start, start + e.dur, e.label or e.id)
                c.time.append(anchors[eid])
                del pending[eid]
                changed = True

    for eid, e in pending.items():
        known = set(anchors) | set(pending)
        if e.dep.upper() in pending:
            f.append(Finding("ERROR", "L8",
                "Circular dependency: %s waits on %s, which is itself unresolved."
                % (e.id, e.dep),
                "A dependency chain must terminate at an anchored interval."))
        else:
            f.append(Finding("ERROR", "L8",
                "%s depends on %s, which is never defined." % (e.id, e.dep),
                "Anchor the chain: give %s a normalized interval, or t_p." % e.dep))
        del known
    return f


def _iv(s: str) -> Interval | None:
    m = IV.match(s)
    return Interval(float(m.group(1)), float(m.group(2)), m.group(3).strip()) if m else None


def _abs(c: Card, s: str) -> None:
    if TIME_ABS.search(s):
        c.abs_time_lines.append(s.strip())


# ─────────────────────────────────────────────────────────────
# LAWS
# ─────────────────────────────────────────────────────────────

NEGATIONS = re.compile(
    r"\b(no|not|never|without|does not|do not|don't|avoid|refrain)\b\s+"
    r"(\w+\s+){0,3}?(sway|swaying|drift|drifting|breath|breathing|blink|blinking|"
    r"flutter|glow|glowing|motion|movement|moving|oscillat\w*|loop\w*|slide|sliding)",
    re.I,
)

ANGLE = re.compile(r"\b\d+\s*(deg|\u00b0)\b|\b[RLUD]\d{1,3}\b", re.I)
DETAIL = re.compile(r"\b(dial|numeral|text|gauge|meter|label|readout|display|sign)\b", re.I)


def features(c: Card) -> set[str]:
    """Which platform advisories are relevant to THIS card. Evidence must not become noise."""
    f: set[str] = set()
    if c.t_p is not None:
        for b in c.bud:
            if "camera" in b.label.lower() or "dolly" in b.label.lower():
                if abs(b.b - c.t_p) < 1e-9:
                    f.add("CAMERA_REST")
    blob = " ".join(iv.label for el in c.elements.values() for iv in el.states)
    if ANGLE.search(blob):
        f.add("ANGLE")
    if c.default_state:
        f.add("INERT_CLASS")
    for el in c.elements.values():
        if el.cst >= 2 and DETAIL.search(el.name):
            f.add("LEGIBLE_DETAIL")
    if len([e for e in c.elements.values() if e.cst >= 2]) > 1:
        f.add("CAUSAL_DEP")
    return f


def lint(c: Card) -> list[Finding]:
    f: list[Finding] = []
    p = PLATFORMS.get(c.platform, {})

    # A line the parser could not read must never become a silent gap.
    # The linter says "I could not read this", never "you did not write this".
    for u in c.unparsed:
        f.append(Finding("ERROR", "PARSE",
            "Could not read TIME line: \u201c%s\u201d" % u,
            "Accepted forms: 'EVT01 0.00-0.22 label' | "
            "'EVT03 AFTER EVT02+0.03 DUR 0.15 label' | 'EVT05 AT t_p'"))

    f += resolve_dag(c)      # relational events become anchored intervals
    feats = features(c)

    # L5 Declared Arrival
    if c.mode == "DRIFT":
        if c.t_p is not None:
            f.append(Finding("ERROR", "L5", "MODE:DRIFT declared with a t_p.",
                             "A drifting clip has no arrival. Set t_p NONE."))
        elif (c.terminus or "").upper() != "OPEN":
            f.append(Finding("ERROR", "L5",
                             "MODE:DRIFT requires TERMINUS OPEN (found: %s)." % (c.terminus or "none"),
                             "Declare the openness. Drift is permitted, never assumed."))
        else:
            f.append(Finding("PASS", "L5", "DRIFT declared, TERMINUS OPEN. Arrival defects suspended."))
    else:
        if c.t_p is None:
            f.append(Finding("ERROR", "L5", "No t_p and no MODE:DRIFT.",
                             "Every traversal declares where it arrives."))
        elif not c.terminus:
            f.append(Finding("ERROR", "L5", "MODE:%s declares t_p but no TERMINUS." % c.mode,
                             "A traversal needs a destination, not only a moment."))
        else:
            f.append(Finding("PASS", "L5", "Arrival declared: t_p %.2f -> %s" % (c.t_p, c.terminus)))

    # L4 / L8
    if p.get("owns_duration"):
        if c.dur_grade == "E" and c.dur is not None:
            obs = p["dur_observed"]
            if c.dur not in obs:
                likely = obs[0]
                sc = likely / c.dur
                f.append(Finding("ERROR", "L4",
                    "DUR %gs emitted <E>. %s owns duration (grade <F>)." % (c.dur, c.platform.upper()),
                    "%s Expect %gs. Absolute timing rescales x%.2f. Emit DUR <F> %gs."
                    % (p["dur_evidence"], likely, sc, likely)))
            else:
                f.append(Finding("WARN", "L4",
                    "DUR %gs graded <E>, but duration is platform-owned." % c.dur,
                    "Grade it <F>. You select from a set; you do not choose a value."))
        if c.abs_time_lines:
            f.append(Finding("ERROR", "L8",
                "Absolute timestamps in %d line(s) - first: \u201c%s\u201d"
                % (len(c.abs_time_lines), c.abs_time_lines[0]),
                "Platform owns duration. Author time as fractions t in [0.00, 1.00]."))
        else:
            f.append(Finding("PASS", "L8", "Time is normalized. Survives platform quantization."))

    # L7 Total Resolution - BUD, element transitions, and TIME events
    if c.t_p is not None and c.mode != "DRIFT":
        late = [(b.label or "unnamed", b.b, "BUD") for b in c.bud if b.b > c.t_p + 1e-9]
        for el in c.elements.values():
            for iv in el.states:
                if iv.moving() and iv.b > c.t_p + 1e-9:
                    late.append(("%s: %s" % (el.name, iv.label), iv.b, "STATE"))
        for iv in c.time:
            if iv.moving() and iv.b > c.t_p + 1e-9:
                late.append((iv.label, iv.b, "TIME"))
        if late:
            for lbl, end, src in late:
                f.append(Finding("ERROR", "L7",
                    "%s '%s' runs to %.2f; t_p is %.2f." % (src, lbl, end, c.t_p),
                    "Motion outstanding at arrival. The clip cannot petrify. "
                    "End it at %.2f, or declare MODE:DRIFT." % c.t_p))
        else:
            f.append(Finding("PASS", "L7",
                             "All motion - budgeted, state, and event - resolves by t_p."))

    # L10 Continuous State Coverage: bounds, overlaps, gaps
    for el in c.elements.values():
        if el.cst < 2:
            continue
        bad = [iv for iv in el.states if iv.a < 0 or iv.b > 1.0 + 1e-9 or iv.b <= iv.a]
        for iv in bad:
            f.append(Finding("ERROR", "L10",
                "%s has a malformed interval %r." % (el.name.upper(), iv),
                "Intervals are ordered and lie within [0.00, 1.00]."))
        if bad:
            continue
        ov = _overlaps(el.states)
        for x, y in ov:
            f.append(Finding("ERROR", "L10",
                "%s holds two states at once: %r '%s' overlaps %r '%s'."
                % (el.name.upper(), x, x.label, y, y.label),
                "One element, one state, at every instant."))
        gaps = _gaps(el.states)
        if gaps:
            f.append(Finding("ERROR", "L10",
                "%s has no assigned state at %s."
                % (el.name.upper(), ", ".join(repr(g) for g in gaps)),
                "Where authorship leaves a vacuum, the renderer becomes the author. "
                "Assign it - HOLD, TRANSITION, LOOP, DRIFT, or OUT_OF_FRAME."))
        if not gaps and not ov:
            f.append(Finding("PASS", "L10",
                             "%s coverage continuous, no conflicts." % el.name.upper()))
    if not c.default_state:
        f.append(Finding("WARN", "L10", "No class-level INERT declared for unlisted elements.",
                         "Stillness is assigned, never inferred. Declare INERT once, explicitly."))

    # L9 Frame Custody
    for el in c.elements.values():
        if el.cst >= 3 and el.vis <= 1:
            f.append(Finding("RESTAGE", "L9",
                "%s  CST:%d  VIS:%d  - STAGING EMERGENCY." % (el.name.upper(), el.cst, el.vis),
                "The scene depends on this and the frame barely shows it. "
                "This is a composition problem. Prose cannot fix it."))
    for span in c.sal:
        held = c.coverage.get(span.label, [])
        if not _covers(held, span):
            f.append(Finding("RESTAGE", "L9",
                "%s is on the witness path %r but custody is %s."
                % (span.label.upper(), span, held or "none"),
                "The camera cannot testify to evidence it has already evicted."))
    for el in c.elements.values():
        if el.cst >= 3 and el.name in c.coverage and c.t_p is not None:
            if not _covers(c.coverage[el.name], Interval(0.0, c.t_p)):
                f.append(Finding("RESTAGE", "L9",
                    "%s (CST:3) leaves frame before t_p." % el.name.upper(),
                    "The terminus frame must contain every element the terminus requires."))

    # L2 Backed Locks
    for el in c.elements.values():
        if el.locked and not el.ref:
            f.append(Finding("WARN", "L2",
                "%s declares LOCKED %s with no reference asset." % (el.name.upper(), el.locked),
                "Prose advises; only an image locks. Compiling as ADVISORY."))

    # L3 Positive Motion
    m = NEGATIONS.search(c.prose)
    if m:
        f.append(Finding("ERROR", "L3",
            "Emission contains a prohibition: \u201c...%s...\u201d" % m.group(0).strip(),
            "Naming a forbidden motion puts that motion in the renderer's mouth. "
            "Enumerate what holds still, positively."))
    elif c.prose:
        f.append(Finding("PASS", "L3", "Emission is free of prohibitions."))

    # L11 Channel Economy
    for intent, chans in c.intents.items():
        if len(chans) > 2:
            f.append(Finding("WARN", "L11",
                "%s manifests across %d channels: %s." % (intent.upper(), len(chans), ", ".join(chans)),
                "Redundant manifestation is BUD.AMBIENT for meaning. Retain two."))

    # Platform advisories - gated by relevance
    for beh, o in p.get("observations", {}).items():
        if not (set(o["triggers"]) & feats):
            continue
        if o["n"] and o["s"] / o["n"] < 0.5:
            f.append(Finding("WARN", "PLAT",
                "%s - %s: observed %d/%d (rate %.2f)."
                % (c.platform.upper(), beh, o["s"], o["n"], o["s"] / o["n"]),
                o["note"]))

    return f


def _gaps(states):
    if not states:
        return [Interval(0.0, 1.0)]
    s, gaps, cur = sorted(states, key=lambda i: i.a), [], 0.0
    for iv in s:
        if iv.a > cur + 1e-9:
            gaps.append(Interval(cur, iv.a))
        cur = max(cur, iv.b)
    if cur < 1.0 - 1e-9:
        gaps.append(Interval(cur, 1.0))
    return gaps


def _overlaps(states):
    s, out = sorted(states, key=lambda i: i.a), []
    for i in range(len(s) - 1):
        if s[i].b > s[i + 1].a + 1e-9:
            out.append((s[i], s[i + 1]))
    return out


def _covers(held, span):
    cur = span.a
    for iv in sorted(held, key=lambda i: i.a):
        if iv.a > cur + 1e-9:
            return False
        cur = max(cur, iv.b)
        if cur >= span.b - 1e-9:
            return True
    return cur >= span.b - 1e-9


# ─────────────────────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────────────────────

GLYPH = {"ERROR": "\u2717", "RESTAGE": "\u2691", "WARN": "\u26a0", "PASS": "\u2713"}
ORDER = {"ERROR": 0, "RESTAGE": 1, "WARN": 2, "PASS": 3}


def report(c, fs):
    e = sum(1 for x in fs if x.sev == "ERROR")
    r = sum(1 for x in fs if x.sev == "RESTAGE")
    w = sum(1 for x in fs if x.sev == "WARN")
    print("\n  SENTINEL v0.2   %s   platform:%s" % (c.shot, c.platform))
    print("  " + "-" * 66)
    for x in sorted(fs, key=lambda x: (ORDER[x.sev], x.law)):
        if x.sev == "PASS":
            continue
        print("\n  %s %-8s %-5s %s" % (GLYPH[x.sev], x.sev, x.law, LAW_NAMES.get(x.law, "Platform")))
        print("      " + x.msg)
        for ln in _wrap(x.fix, 62):
            print("      \u2192 " + ln)
    ps = [x for x in fs if x.sev == "PASS"]
    if ps:
        print()
        for x in ps:
            print("  %s %-5s %s" % (GLYPH["PASS"], x.law, x.msg))
    print("\n  " + "-" * 66)
    verdict = "REFUSED" if e else ("RESTAGE" if r else "PASS")
    print("  %d ERROR   %d RESTAGE   %d WARN        \u2192  %s" % (e, r, w, verdict))
    if e or r:
        print("  EMIT unavailable. The Shot Card returns to the author.")
    print()
    return 1 if (e or r) else 0


def _wrap(s, w):
    if not s:
        return []
    out, line = [], ""
    for word in s.split():
        if len(line) + len(word) + 1 > w:
            out.append(line)
            line = word
        else:
            line = (line + " " + word).strip()
    if line:
        out.append(line)
    return out


# ─────────────────────────────────────────────────────────────
# X-SHEET  — the exposure sheet
#
# Animation solved this in the 1930s. A dope sheet is a grid: rows are time,
# columns are the things that can change, and every cell has an owner.
#
# The whole of Law 10 is: no cell is blank.
# The whole of Law 7 is: nothing is still moving on the KEY row.
#
# We paid a render to find a blank cell with interval algebra.
# An animator would have seen it before lunch, because their tool draws the gap.
# ─────────────────────────────────────────────────────────────

VACUUM = "\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591\u2591"   # a hole you can see
COLLIDE = "\u2573"                                                    # two owners, one instant


def _lanes(c: Card) -> list[tuple[str, list[Interval], bool]]:
    """Columns: registered elements (must own every cell), then budget lanes (need not)."""
    lanes: list[tuple[str, list[Interval], bool]] = []
    for el in c.elements.values():
        lanes.append((el.name, el.states, el.cst >= 2))   # True = coverage required
    for b in c.bud:
        key = (b.label or "budget").split(",")[0].strip()
        lanes.append(("~" + key, [b], False))
    return lanes


def _rows(c: Card, lanes) -> list[float]:
    """Every instant at which anything changes hands."""
    ts = {0.0, 1.0}
    for _, ivs, _ in lanes:
        for iv in ivs:
            ts.add(round(iv.a, 4))
            ts.add(round(iv.b, 4))
    for iv in c.time:
        ts.add(round(iv.a, 4))
        ts.add(round(iv.b, 4))
    if c.t_p is not None:
        ts.add(round(c.t_p, 4))
    return sorted(t for t in ts if 0.0 <= t <= 1.0)


def _owner(ivs: list[Interval], a: float, b: float) -> tuple[str, int]:
    """Who owns [a,b)? n=0 is a vacuum, n>1 a collision."""
    hits = [iv for iv in ivs if iv.a <= a + 1e-9 and iv.b >= b - 1e-9]
    if not hits:
        return "", 0
    return (hits[0].label or "\u2022"), len(hits)


def xsheet(c: Card, width: int = 13) -> None:
    lanes = _lanes(c)
    if not lanes:
        print("\n  (no elements or budget lines to sheet)\n")
        return
    rows = _rows(c, lanes)

    def cell(s, w=width):
        return s[: w - 1].ljust(w)

    print("\n  X-SHEET   %s" % c.shot)
    if c.dur:
        tail = "  (\u2248 %.1f s)" % (c.t_p * c.dur) if c.t_p else ""
        print("  DUR %g s  \u00b7  KEY at \u03c4 %.2f%s" % (c.dur, c.t_p or 0, tail))
    print("  \u2591 = unowned cell   \u2573 = collision   ~ = budget lane   \u00b7 = unbudgeted")
    print()

    hdr = "  " + "\u03c4".ljust(8) + "".join(cell(n.upper()) for n, _, _ in lanes)
    print(hdr)
    print("  " + "\u2500" * (len(hdr) - 2))

    vacuums, collisions, late = [], [], []

    for i, t in enumerate(rows[:-1]):
        a, b = t, rows[i + 1]
        is_key = c.t_p is not None and abs(a - c.t_p) < 1e-9
        at_or_past_key = c.t_p is not None and a >= c.t_p - 1e-9

        line = "  " + ("%.2f" % a).ljust(8)
        for name, ivs, required in lanes:
            lab, n = _owner(ivs, a, b)
            if n == 0:
                if required:
                    line += cell(VACUUM)
                    vacuums.append((name, a, b))
                else:
                    line += cell("\u00b7")            # legitimately unbudgeted
            elif n > 1:
                line += cell(COLLIDE + " " + lab)
                collisions.append((name, a, b))
            else:
                line += cell(lab)
                if at_or_past_key and Interval(a, b, lab).moving():
                    late.append((name, lab, b))
        print(line + ("  \u25c0 KEY" if is_key else ""))

    print("  " + "1.00".ljust(8) + "".join(cell("\u2014") for _ in lanes))
    print("  " + "\u2500" * (len(hdr) - 2))
    print()

    if vacuums:
        print("  \u2717 L10  %d UNOWNED CELL(S) \u2014 the renderer will author these:" % len(vacuums))
        for n, a, b in vacuums[:6]:
            print("        %-14s \u03c4 %.2f\u2013%.2f" % (n.upper(), a, b))
    if collisions:
        print("  \u2717 L10  %d COLLISION(S) \u2014 two states, one instant:" % len(collisions))
        for n, a, b in collisions[:6]:
            print("        %-14s \u03c4 %.2f\u2013%.2f" % (n.upper(), a, b))
    if late:
        print("  \u2717 L7   STILL MOVING AT THE KEY \u2014 the clip cannot settle:")
        for n, lab, b in late[:6]:
            print("        %-14s %s  \u2192 \u03c4 %.2f" % (n.upper(), lab[:18], b))
    if not (vacuums or collisions or late):
        print("  \u2713 Every cell owned. Nothing moving at the key. The sheet is clean.")
    print()


# ─────────────────────────────────────────────────────────────
# REGRESSION SUITE - executable project history
# ─────────────────────────────────────────────────────────────

def _has(fs, law, sev):
    return any(x.law == law and x.sev == sev for x in fs)


def run_tests():
    import pathlib
    here = pathlib.Path(__file__).parent
    fails = []

    def check(name, cond, detail=""):
        mark = "\u2713" if cond else "\u2717"
        print("  %s %s%s" % (mark, name, "" if cond else "   <-- %s" % detail))
        if not cond:
            fails.append(name)

    print("\n  REGRESSION SUITE\n  " + "-" * 66)

    v10 = lint(parse((here / "clockbird_v1.0.vse").read_text()))
    print("\n  clockbird_v1.0 - the card that produced the broken render")
    check("L10 refuses the needle's assignment vacuum", _has(v10, "L10", "ERROR"))
    check("L7  refuses the camera budgeted past t_p", _has(v10, "L7", "ERROR"))
    check("L4  refuses <E> duration on a platform that owns it", _has(v10, "L4", "ERROR"))
    check("L3  refuses the prohibition list", _has(v10, "L3", "ERROR"))
    check("L9  flags the meter as a staging emergency", _has(v10, "L9", "RESTAGE"))
    check("verdict is REFUSED", any(x.sev == "ERROR" for x in v10))

    v12 = lint(parse((here / "clockbird_v1.2.vse").read_text()))
    print("\n  clockbird_v1.2 - every defect closed")
    check("no errors", not any(x.sev == "ERROR" for x in v12),
          [x.law + ":" + x.msg for x in v12 if x.sev == "ERROR"])
    check("no restages", not any(x.sev == "RESTAGE" for x in v12),
          [x.law + ":" + x.msg for x in v12 if x.sev == "RESTAGE"])
    check("L7  passes", _has(v12, "L7", "PASS"))
    check("L10 passes", _has(v12, "L10", "PASS"))

    print("\n  synthetic - laws no render has exercised yet")

    ov = parse("SHOT o\nT_P 0.8\nTERMINUS X\nINERT all\nELEMENT m\n  CST 3\n  VIS 3\n"
               "  STATE 0.00-0.60 HOLD\n  STATE 0.40-1.00 HOLD\n")
    check("L10 catches contradictory overlapping states", _has(lint(ov), "L10", "ERROR"))

    dr = parse("SHOT d\nMODE DRIFT\nT_P NONE\nTERMINUS PCM(1,2)\nINERT all\n")
    check("L5  requires TERMINUS OPEN under DRIFT", _has(lint(dr), "L5", "ERROR"))

    ok = parse("SHOT d2\nMODE DRIFT\nT_P NONE\nTERMINUS OPEN\nINERT all\n")
    check("L5  accepts a properly declared DRIFT", _has(lint(ok), "L5", "PASS"))

    nt = parse("SHOT n\nT_P 0.8\nINERT all\n")
    check("L5  refuses t_p without a terminus", _has(lint(nt), "L5", "ERROR"))

    ar = parse("SHOT a\nT_P 0.8\nTERMINUS X\nINERT all\nTIME\n  0.00 \u2192 0.22  hold\n")
    check("unicode arrow parses", len(ar.time) == 1, "got %r" % ar.time)

    ab = parse("SHOT b\nPLATFORM veo\nDUR 10 <F>\nT_P 0.8\nTERMINUS X\nINERT all\n"
               "TIME\n  0.00-0.22  needle rests until 00:02.0\n")
    check("L8  catches absolute time inside a TIME block", _has(lint(ab), "L8", "ERROR"))

    lt = parse("SHOT l\nPLATFORM veo\nDUR 10 <F>\nT_P 0.80\nTERMINUS X\nINERT all\n"
               "TIME\n  0.40-0.95  camera dolly in\n")
    check("L7  catches a late TIME event, not only a late BUD line",
          _has(lint(lt), "L7", "ERROR"))

    quiet = parse("SHOT q\nPLATFORM veo\nDUR 10 <F>\nT_P 0.80\nTERMINUS X\nINERT all\n"
                  "ELEMENT wall\n  CST 3\n  VIS 3\n  STATE 0.00-1.00 HOLD\n")
    fs = lint(quiet)
    check("platform advisories stay silent when the shot doesn't trigger them",
          not any(x.law == "PLAT" for x in fs),
          [x.msg for x in fs if x.law == "PLAT"])

    print("\n  relational time — the DAG (Gemini's catch)")

    HEAD = "SHOT g\nPLATFORM veo\nDUR 10 <F>\nT_P 0.80\nTERMINUS X\nINERT all\nTIME\n"

    dag = parse(HEAD +
                "  EVT01  0.00-0.22   chamber holds\n"
                "  EVT02  0.22-0.40   needle rises\n"
                "  EVT03  AFTER EVT02  DUR 0.10   overhead light rises\n"
                "  EVT04  AFTER EVT03+0.03  DUR 0.10   dust descends\n"
                "  EVT05  AT t_p   all motion resolves\n")
    fs = lint(dag)
    got = sorted((round(i.a, 2), round(i.b, 2)) for i in dag.time)
    check("AFTER resolves against its anchor",
          (0.4, 0.5) in got, "got %s" % got)
    check("AFTER+offset chains through a resolved event",
          (0.53, 0.63) in got, "got %s" % got)
    check("AT t_p anchors on the singularity",
          (0.8, 0.8) in got, "got %s" % got)
    check("a resolved DAG produces no phantom Law 10 gap",
          not any(x.law == "L10" and x.sev == "ERROR" for x in fs))

    orphan = parse(HEAD + "  EVT01  0.00-1.00  hold\n  EVT09  AFTER EVT77  DUR 0.1  x\n")
    check("unresolvable dependency is named, not dropped",
          _has(lint(orphan), "L8", "ERROR"))

    cyc = parse(HEAD + "  EVT01  0.00-1.00  hold\n"
                       "  EVT02  AFTER EVT03  DUR 0.1  a\n"
                       "  EVT03  AFTER EVT02  DUR 0.1  b\n")
    fs = lint(cyc)
    check("circular dependency is refused, not spun on",
          any("Circular" in x.msg for x in fs))

    secs = parse(HEAD + "  EVT01  0.00-0.22  hold\n  EVT02  AFTER EVT01+0.4s  DUR 0.1  x\n")
    check("L8  catches an absolute offset inside a normalized chain",
          _has(lint(secs), "L8", "ERROR"))

    junk = parse(HEAD + "  EVT01 sometime after the light, probably\n")
    check("an unreadable TIME line is reported, never silently dropped",
          any(x.law == "PARSE" for x in lint(junk)))

    print("\n  " + "-" * 66)
    if fails:
        print("  %d FAILED\n" % len(fails))
        return 1
    print("  ALL PASS\n")
    return 0


# ─────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]
    if cmd == "test":
        return run_tests()
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    arg = sys.argv[2]

    if cmd == "explain":
        law = arg.upper()
        print("\n  %s  %s" % (law, LAW_NAMES.get(law, "?")))
        print("  found by: %s\n" % PROVENANCE.get(law, "(canon, not render)"))
        return 0

    if cmd == "limits":
        p = PLATFORMS.get(arg.lower(), {})
        print("\n  %s - observed behaviour  (every numeral carries n)\n" % arg.upper())
        print("  duration        %s  <%s>" % (p["dur_observed"], p["dur_grade"]))
        print("                  %s\n" % p["dur_evidence"])
        for beh, o in p.get("observations", {}).items():
            print("  %-22s %d/%d  rate %.2f   triggers:%s"
                  % (beh, o["s"], o["n"], o["s"] / o["n"], o["triggers"]))
            print("  %-22s %s" % ("", o["note"]))
        print()
        return 0

    card = parse(open(arg).read())

    if cmd == "xsheet":
        xsheet(card)
        return 0

    rc = report(card, lint(card))
    if cmd == "compile" and rc == 0:
        print("  EMIT \u2192 (serializer: NOT IMPLEMENTED)\n")
    return rc


if __name__ == "__main__":
    sys.exit(main())
