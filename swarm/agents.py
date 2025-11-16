# swarm/agents.py

"""
Archetypal Swarm agents for the VSE Swarm Alpha.

These are intentionally vendor-neutral, personality-tinged agents that live
together in a shared "lab apartment" metaphor to make Swarm behavior easier
to visualize and relate to.

Agents:
    - Archivist: cautious, detail-oriented, hates drift
    - Maverick: adventurous, loves wild ideas, tolerates drift
    - Synthesist: mediator, blends perspectives
    - Vectorist: mathematically-minded, keeps things stable
"""

from typing import Set, Dict, Any

from vse_core.packet import VSEPacket, SemanticHistoryEntry
from vse_metrics.cost_engine import SemanticCostVector
from .config import SwarmAgent


# ---------------------------------------------------------------------------
# Helper to safely update delta
# ---------------------------------------------------------------------------

def _scale_delta(pkt: VSEPacket, factor: float) -> None:
    """
    Scale observed_delta by a factor; if not set, initialize it gently.
    """
    if pkt.observed_delta is None:
        pkt.observed_delta = 0.1
    pkt.observed_delta *= factor


# ---------------------------------------------------------------------------
# Agent personalities
# ---------------------------------------------------------------------------

def archivist_handler(pkt: VSEPacket) -> VSEPacket:
    """
    The Archivist:
    - Lives in the "study" of the shared apartment.
    - Speaks rarely, but checks for internal consistency.
    - Lowers drift slightly and adds a structured annotation.
    """
    print("[Archivist @ study] \"Let me make sure this still lines up with the record.\"")

    text = str(pkt.payload.get("text", ""))
    annotations = pkt.payload.get("annotations", [])
    if not isinstance(annotations, list):
        annotations = [annotations]

    annotations.append("Checked for continuity and internal coherence.")
    pkt.payload["annotations"] = annotations

    # Slightly reduce drift, small cost in cycles
    _scale_delta(pkt, factor=0.85)
    pkt.cost.E_cycles *= 1.02

    # Add a small history note
    pkt.history.append(
        SemanticHistoryEntry(
            sigma=pkt.sigma_vectors,
            lambda_=pkt.lambda_tensors,
            phi="Φ_cohere",
            meta={"agent": "Archivist", "room": "study"},
        )
    )

    return pkt


def maverick_handler(pkt: VSEPacket) -> VSEPacket:
    """
    The Maverick:
    - Lives in the "loft" and keeps all the windows open.
    - Throws in wild conceptual angles.
    - May increase drift, but expands the idea space.
    """
    print("[Maverick @ loft] \"What if we tilt this whole thing sideways and see what falls out?\"")

    text = str(pkt.payload.get("text", ""))
    wild_idea = f"Alternative frame: what if the 'betrayal' is actually a necessary realignment of power?"
    ideas = pkt.payload.get("ideas", [])
    if not isinstance(ideas, list):
        ideas = [ideas]

    ideas.append(wild_idea)
    pkt.payload["ideas"] = ideas

    # Maverick increases drift a bit, but adds rich content
    _scale_delta(pkt, factor=1.20)
    pkt.cost.E_cycles *= 1.15
    pkt.cost.T_tokens *= 1.10

    pkt.history.append(
        SemanticHistoryEntry(
            sigma=pkt.sigma_vectors,
            lambda_=pkt.lambda_tensors,
            phi="Φ_diverge",
            meta={"agent": "Maverick", "room": "loft"},
        )
    )

    return pkt


def synthesist_handler(pkt: VSEPacket) -> VSEPacket:
    """
    The Synthesist:
    - Lives at the big kitchen table where everyone eventually meets.
    - Tries to blend seemingly conflicting interpretations into a single arc.
    - Moves drift toward the middle, re-uses existing payload elements.
    """
    print("[Synthesist @ kitchen table] \"Okay, let's hear everyone out and find the through-line.\"")

    base_text = str(pkt.payload.get("text", ""))
    annotations = pkt.payload.get("annotations", [])
    ideas = pkt.payload.get("ideas", [])
    if not isinstance(annotations, list):
        annotations = [annotations]
    if not isinstance(ideas, list):
        ideas = [ideas]

    summary_lines = []
    if base_text:
        summary_lines.append(f"Base text: {base_text}")
    if annotations:
        summary_lines.append(f"Archivist notes: {len(annotations)}")
    if ideas:
        summary_lines.append(f"Maverick ideas: {len(ideas)}")

    blended = " | ".join(summary_lines) or "No prior context; synthesist starting fresh."
    pkt.payload["blended_summary"] = blended

    # Pull drift gently toward a middle ground
    if pkt.observed_delta is None:
        pkt.observed_delta = 0.1
    pkt.observed_delta = (pkt.observed_delta + 0.1) / 2.0

    # Some extra allocation cost for negotiation work
    pkt.cost.A_alloc *= 1.10

    pkt.history.append(
        SemanticHistoryEntry(
            sigma=pkt.sigma_vectors,
            lambda_=pkt.lambda_tensors,
            phi="Φ_blend",
            meta={"agent": "Synthesist", "room": "kitchen"},
        )
    )

    return pkt


def vectorist_handler(pkt: VSEPacket) -> VSEPacket:
    """
    The Vectorist:
    - Lives near the apartment's whiteboard wall and math scribbles.
    - Thinks in terms of vector geometry and invariants.
    - Applies small, stable transformations and respects δ bounds.
    """
    print("[Vectorist @ whiteboard] \"Let me just nudge the geometry without breaking any invariants.\"")

    # Add a simple geometric note
    geom_notes = pkt.payload.get("geometry_notes", [])
    if not isinstance(geom_notes, list):
        geom_notes = [geom_notes]

    geom_notes.append("Preserved core semantic direction while re-normalizing context.")
    pkt.payload["geometry_notes"] = geom_notes

    # Vectorist tends to gently reduce drift, but not as strongly as Archivist
    _scale_delta(pkt, factor=0.9)

    # Slight memory use for internal buffers
    pkt.cost.M_memory *= 1.05

    pkt.history.append(
        SemanticHistoryEntry(
            sigma=pkt.sigma_vectors,
            lambda_=pkt.lambda_tensors,
            phi="Φ_stabilize",
            meta={"agent": "Vectorist", "room": "whiteboard"},
        )
    )

    return pkt


# ---------------------------------------------------------------------------
# Factory functions: build SwarmAgent instances for SwarmConfig
# ---------------------------------------------------------------------------

def make_archivist_agent() -> SwarmAgent:
    return SwarmAgent(
        name="Archivist",
        capabilities={"Φ_cohere", "continuity", "low_drift"},
        handler=archivist_handler,
        metadata={"room": "study"},
    )


def make_maverick_agent() -> SwarmAgent:
    return SwarmAgent(
        name="Maverick",
        capabilities={"Φ_diverge", "brainstorm", "high_creativity"},
        handler=maverick_handler,
        metadata={"room": "loft"},
    )


def make_synthesist_agent() -> SwarmAgent:
    return SwarmAgent(
        name="Synthesist",
        capabilities={"Φ_blend", "mediation", "summary"},
        handler=synthesist_handler,
        metadata={"room": "kitchen"},
    )


def make_vectorist_agent() -> SwarmAgent:
    return SwarmAgent(
        name="Vectorist",
        capabilities={"Φ_stabilize", "math", "low_drift"},
        handler=vectorist_handler,
        metadata={"room": "whiteboard"},
    )
