"""
Example 2: VSE v1.4 Kinetic - Dynamic Coherence Control

This example demonstrates v1.4 Kinetic features (Gemini AI):
- Kinetic Boundary Management (KBM)
- Contextual Token-Vector Mapping (C-TVM)
- Foundation anchors
- μ-Loop monitoring
"""

from vse_core import Packet, Validator
from vse_metrics import MetricSnapshot, MetricMonitor
import random

def simulate_generation_with_mu_loop():
    """Simulate text generation with real-time μ-Loop monitoring."""
    
    print("=" * 60)
    print("VSE v1.4 Kinetic: μ-Loop Monitoring Simulation")
    print("=" * 60)
    print()
    
    # Create kinetic packet
    packet = Packet(
        intent="write_technical_essay",
        constraints=["1000_words", "academic_tone", "well_structured"],
        divergence=0.25,
        kbm={"coherence_vector": [0.80, 0.92]},
        c_tvm=["intro_premise", "conclusion_thesis", 150],
        foundation=["Milieu", "Gravitas", "Fulcrum"],
        mu_loop={"window_size": 5, "threshold": 0.25}
    )
    
    print("Packet configuration:")
    print(packet.to_vse())
    print()
    
    # Validate
    validator = Validator(packet)
    result = validator.validate()
    print(result)
    print()
    
    # Initialize μ-Loop monitor
    monitor = MetricMonitor(window_size=5)
    
    print("\nSimulating generation with μ-Loop monitoring...")
    print("-" * 60)
    print()
    
    # Simulate 10 generation steps
    for step in range(1, 11):
        # Simulate metrics (in production, these come from actual embeddings)
        snapshot = MetricSnapshot(
            scm=0.85 + random.uniform(-0.05, 0.10),
            divergence=0.15 + random.uniform(0, 0.20),
            semcoh=0.75 + random.uniform(-0.05, 0.15),
            resonance=0.88 + random.uniform(-0.05, 0.07)
        )
        
        monitor.record(snapshot)
        
        print(f"Step {step}:")
        print(f"  SCM: {snapshot.scm:.3f}")
        print(f"  δ:   {snapshot.divergence:.3f}")
        
        # Check if divergence exceeds threshold
        if monitor.is_diverging(threshold=packet.mu_loop["threshold"]):
            print(f"  ⚠ DIVERGENCE ALERT: δ = {snapshot.divergence:.3f} > {packet.mu_loop['threshold']}")
            print(f"  → Applying KBM constraints: coherence ∈ {packet.kbm['coherence_vector']}")
            print(f"  → Anchoring to Foundation: {', '.join(packet.foundation)}")
        else:
            print(f"  ✓ Within bounds")
        
        print()
    
    # Final metrics
    print("\nFinal Metrics:")
    print("-" * 60)
    avg = monitor.get_average()
    print(avg)
    
    # Trends
    print("\nMetric Trends:")
    print("-" * 60)
    for metric in ["scm", "divergence", "semcoh", "resonance"]:
        slope, direction = monitor.get_trend(metric)
        arrow = "↑" if direction == "rising" else "↓" if direction == "falling" else "→"
        print(f"  {metric:12s}: {arrow} {direction:8s} (slope: {slope:+.4f})")
    
    print()


def main():
    print("=" * 60)
    print("VSE v1.4 Kinetic Examples")
    print("=" * 60)
    print()
    
    # Example 1: Basic kinetic packet
    print("Example 1: Kinetic Packet with KBM")
    print("-" * 60)
    
    packet1 = Packet(
        intent="creative_essay",
        constraints=["800_words", "reflective_tone"],
        divergence=0.35,
        kbm={"coherence_vector": [0.70, 0.88]},
        foundation=["Ambience", "Gravitas"]
    )
    
    print(packet1.to_vse())
    print()
    
    validator = Validator(packet1)
    print(validator.validate())
    print()
    
    # Example 2: C-TVM for logical flow
    print("\nExample 2: C-TVM for Argument Structure")
    print("-" * 60)
    
    packet2 = Packet(
        intent="philosophical_argument",
        constraints=["formal_logic", "cite_sources"],
        divergence=0.20,
        kbm={"coherence_vector": [0.85, 0.95]},
        c_tvm=["kant_premise", "synthesis_conclusion", 200],
        foundation=["Fulcrum", "Gravitas"]
    )
    
    print(packet2.to_vse())
    print()
    
    # Example 3: Migration from v1.3
    print("\nExample 3: Migrating v1.3 → v1.4 Kinetic")
    print("-" * 60)
    
    from vse_core import migrate_packet
    
    v13_packet = Packet(
        intent="explain_algorithm",
        constraints=["step_by_step", "use_pseudocode"],
        divergence=0.18,
        immune=["Big-O: O(n log n)"],
        version="1.3"
    )
    
    print("v1.3 packet:")
    print(v13_packet.to_vse())
    print()
    
    v14_packet = migrate_packet(v13_packet, target_version="1.4")
    
    print("Migrated to v1.4 Kinetic:")
    print(v14_packet.to_vse())
    print()
    
    # Run μ-Loop simulation
    print()
    simulate_generation_with_mu_loop()
    
    print("=" * 60)
    print("v1.4 Kinetic examples complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
