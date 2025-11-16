# vse_metrics/cost_engine.py

from dataclasses import dataclass
from typing import Optional


@dataclass
class SemanticCostVector:
    """
    \vec{C}_{cost}: thermodynamic signature of semantic production.

    All components MUST be non-negative magnitudes.
    """
    E_cycles: float = 0.0  # CPU/GPU cycle count
    T_tokens: int = 0      # Token throughput
    M_memory: float = 0.0  # Peak RAM footprint (MB or normalized)
    A_alloc: float = 0.0   # Allocation cost (normalized resource units)


def compute_simulated_cost(payload_size: int) -> SemanticCostVector:
    """
    Simulated semantic cost function for testing and sandbox use.

    Real implementations should hook into actual telemetry.
    """
    cycles = payload_size * 1e6
    tokens = payload_size * 5
    mem = cycles * 1e-4
    alloc = cycles * 1e-6

    return SemanticCostVector(
        E_cycles=cycles,
        T_tokens=tokens,
        M_memory=mem,
        A_alloc=alloc
    )


def calculate_cost_fidelity(packet, scm: float) -> float:
    """
    Implements the Semantic Work Law:

        Quality  ∝  (SCM / δ) · ||C_cost||

    where ||C_cost|| is a weighted linear combination.
    """
    if scm <= 0:
        scm = 1e-12  # avoid degenerate zero

    # Fidelity term
    if packet.observed_delta is None or packet.observed_delta == 0.0:
        # Treat perfect Δ as extremely high fidelity but with a floor
        fidelity = scm / 1e-6
    else:
        fidelity = scm / packet.observed_delta

    # Weighted cost magnitude
    w = {
        "E_cycles": 1.0,
        "T_tokens": 0.05,
        "M_memory": 2.0,
        "A_alloc": 3.0,
    }

    C = packet.cost

    cost_magnitude = (
        C.E_cycles * w["E_cycles"] +
        C.T_tokens * w["T_tokens"] +
        C.M_memory * w["M_memory"] +
        C.A_alloc * w["A_alloc"]
    )

    return fidelity * cost_magnitude
