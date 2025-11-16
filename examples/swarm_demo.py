# examples/swarm_demo.py

"""
Minimal Swarm demo using four archetypal local agents:

    - Archivist  @ study
    - Maverick   @ loft
    - Synthesist @ kitchen table
    - Vectorist  @ whiteboard

They "live" together in a shared lab-apartment and each leaves
a different signature on the VSEPacket as it passes through.
"""

from vse_core.packet import VSEPacket, SemanticHistoryEntry
from vse_core.validator import VSEPacketValidator
from vse_metrics.cost_engine import compute_simulated_cost
from swarm.config import SwarmConfig
from swarm.launcher import SwarmLauncher
from swarm.agents import (
    make_archivist_agent,
    make_maverick_agent,
    make_synthesist_agent,
    make_vectorist_agent,
)


def make_base_packet() -> VSEPacket:
    """
    Create a simple demo packet representing a betrayal moment in a story.
    """
    text = "He turned on his closest ally."

    pkt = VSEPacket(
        psi_layer=3,
        sigma_vectors={"concept": "betrayal"},
        lambda_tensors={"role": "pivot"},
        phi_ops=["Φ_expand"],  # later, router/dispatch could use this
        delta_max=0.25,
        payload={"text": text},
    )

    pkt.history.append(
        SemanticHistoryEntry(
            sigma={"concept": "trust"},
            lambda_={"role": "foundation"},
            phi="Φ_proj",
            meta={"source": "demo_seed"},
        )
    )

    # Initial SIF and cost
    pkt.attach_sif()
    pkt.observed_delta = 0.12
    pkt.cost = compute_simulated_cost(len(text))

    return pkt


def make_swarm_config() -> SwarmConfig:
    """
    Build a SwarmConfig populated with our four archetypal agents.
    """
    cfg = SwarmConfig(network_id="demo_apartment", max_drift=0.5)

    cfg.register_agent(make_archivist_agent())
    cfg.register_agent(make_maverick_agent())
    cfg.register_agent(make_synthesist_agent())
    cfg.register_agent(make_vectorist_agent())

    return cfg


def main() -> None:
    print("=== VSE Swarm Demo: Shared Lab Apartment ===")
    print("Four agents wake up in the same semantic apartment and react to a single packet.\n")

    base_packet = make_base_packet()
    config = make_swarm_config()
    launcher = SwarmLauncher(config=config, validator=VSEPacketValidator())

    print("[Base] Initial packet:")
    print(f"  text:           {base_packet.payload['text']}")
    print(f"  observed_delta: {base_packet.observed_delta}")
    print(f"  E_cycles:       {base_packet.cost.E_cycles:,.0f}")
    print()

    result = launcher.run(base_packet, scm=0.9)

    print("\n=== Final Swarm Result ===")
    if result is None:
        print("Swarm produced no result.")
        return

    print(f"observed_delta: {result.observed_delta}")
    print(f"total_quality:  {result.total_quality}")
    print("payload keys:   ", list(result.payload.keys()))
    print("payload:")
    for k, v in result.payload.items():
        print(f"  {k}: {v}")

    print("\nHistory trace (last few entries):")
    for h in result.history[-6:]:
        agent = h.meta.get("agent", "unknown")
        room = h.meta.get("room", "unknown")
        print(f"  - agent={agent:10s} room={room:10s} phi={h.phi}")


if __name__ == "__main__":
    main()
