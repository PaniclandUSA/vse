# vse_metrics/cost_monitor.py

from contextlib import contextmanager
from time import perf_counter

from .cost_engine import SemanticCostVector


@contextmanager
def measure_cost_simulated(payload_size: int):
    """
    Context manager for future real telemetry integration.

    Currently:
      - Measures wall-clock time (not yet used directly)
      - Uses payload_size to approximate a cost vector

    Real implementations should attach to hardware metrics / model hooks.
    """
    start = perf_counter()
    try:
        yield
    finally:
        end = perf_counter()
        elapsed = end - start

        cycles = payload_size * 1e6
        tokens = payload_size * 5
        mem = cycles * 1e-4
        alloc = cycles * 1e-6 + elapsed

        cost = SemanticCostVector(
            E_cycles=cycles,
            T_tokens=tokens,
            M_memory=mem,
            A_alloc=alloc,
        )

        # Simple global hook for now; your engine can replace this with
        # logging, callbacks, or packet assignment.
        measure_cost_simulated.last_cost = cost
