#!/usr/bin/env python3
"""
VSE Quick Demo
Demonstrates all VSE v1.4 features in one script.
"""

from vse_core import Packet, Validator, migrate_packet
from vse_metrics import MetricSnapshot, MetricComputer

def print_section(title):
    """Print a section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def demo_v13():
    """Demonstrate v1.3 core functionality."""
    print_section("VSE v1.3: Core Semantic Control")
    
    packet = Packet(
        intent="summarize_research_paper",
        constraints=["3_sentences", "formal_tone", "highlight_findings"],
        divergence=0.2,
        immune=["Table 1", "p < 0.01"],
        version="1.3"
    )
    
    print("📦 Packet created:")
    print(packet.to_vse())
    print()
    
    validator = Validator(packet)
    result = validator.validate()
    print(result)


def demo_v14_kinetic():
    """Demonstrate v1.4 Kinetic features."""
    print_section("VSE v1.4 Kinetic: Dynamic Coherence (Gemini AI)")
    
    packet = Packet(
        intent="write_philosophical_essay",
        constraints=["1000_words", "argumentative"],
        divergence=0.30,
        kbm={"coherence_vector": [0.75, 0.90]},
        c_tvm=["premise_identity", "conclusion_consciousness", 200],
        foundation=["Fulcrum", "Gravitas", "Ambience"],
        mu_loop={"window_size": 10, "threshold": 0.30}
    )
    
    print("📦 Kinetic packet:")
    print(packet.to_vse())
    print()
    
    validator = Validator(packet)
    result = validator.validate()
    print(result)
    
    print("\n🔄 μ-Loop Configuration:")
    print(f"  Window Size: {packet.mu_loop['window_size']}")
    print(f"  Threshold: {packet.mu_loop['threshold']}")
    print(f"  KBM Coherence Bounds: {packet.kbm['coherence_vector']}")
    print(f"  Foundation Anchors: {', '.join(packet.foundation)}")


def demo_v14_gregarious():
    """Demonstrate v1.4 Gregarious features."""
    print_section("VSE v1.4 Gregarious: Semantic Networks (Grok/xAI)")
    
    packet = Packet(
        intent="collaborative_research",
        constraints=["exploratory", "interdisciplinary"],
        divergence=0.40,
        kbm={"coherence_vector": [0.70, 0.85]},
        gsn={
            "network_id": "research-swarm-001",
            "link_vectors": ["node-alpha", "node-beta"],
            "curiosity_factor": 0.65
        },
        evf=["seed-vector-quantum", 0.35, 7],
        urp_enabled=True
    )
    
    print("📦 Gregarious packet:")
    print(packet.to_vse())
    print()
    
    validator = Validator(packet)
    result = validator.validate()
    print(result)
    
    print("\n🌐 GSN Configuration:")
    print(f"  Network ID: {packet.gsn['network_id']}")
    print(f"  Curiosity Factor: {packet.gsn['curiosity_factor']}")
    print(f"  Linked Nodes: {len(packet.gsn['link_vectors'])}")
    print(f"  EVF Exploration Radius: {packet.evf[1]}")
    print(f"  EVF Branch Limit: {packet.evf[2]}")
    print(f"  URP Enabled: {packet.urp_enabled}")


def demo_migration():
    """Demonstrate packet migration."""
    print_section("Packet Migration: v1.3 → v1.4")
    
    # Start with v1.3
    v13_packet = Packet(
        intent="explain_neural_networks",
        constraints=["beginner_friendly", "use_analogies"],
        divergence=0.25,
        immune=["backpropagation", "gradient descent"],
        version="1.3"
    )
    
    print("Original v1.3 packet:")
    print(v13_packet.to_vse())
    print()
    
    # Migrate to v1.4 Kinetic
    v14_packet = migrate_packet(v13_packet, target_version="1.4")
    
    print("✨ Migrated to v1.4 Kinetic:")
    print(v14_packet.to_vse())
    print()
    
    print("🔍 Migration added:")
    print(f"  ✓ KBM with coherence bounds: {v14_packet.kbm['coherence_vector']}")
    print(f"  ✓ μ-Loop monitoring (window: {v14_packet.mu_loop['window_size']})")
    if v14_packet.foundation:
        print(f"  ✓ Foundation anchors: {', '.join(v14_packet.foundation)}")


def demo_metrics():
    """Demonstrate metric computation."""
    print_section("VSE Metrics: Real-time Measurement")
    
    # Simulate some output
    output_text = """
    Neural networks are computational models inspired by the human brain.
    They consist of interconnected nodes organized in layers.
    Through backpropagation and gradient descent, they learn patterns from data.
    """
    
    constraints = ["3_sentences", "beginner_friendly"]
    
    # Compute metrics
    scm = MetricComputer.compute_scm(output_text, constraints)
    semcoh = MetricComputer.compute_semcoh(output_text)
    
    snapshot = MetricSnapshot(
        scm=scm,
        divergence=0.18,
        semcoh=semcoh,
        resonance=0.89
    )
    
    print("📊 Computed Metrics:")
    print(snapshot)
    
    print("\n🎯 Target Ranges:")
    print("  SCM    > 0.85  (constraint adherence)")
    print("  δ      < 0.30  (semantic drift)")
    print("  SemCoh > 0.70  (logical coherence)")
    print("  ℜ      > 0.85  (human-AI alignment)")


def demo_json_interop():
    """Demonstrate JSON interoperability."""
    print_section("JSON Interoperability")
    
    packet = Packet(
        intent="generate_api_docs",
        constraints=["include_examples", "professional"],
        divergence=0.15,
        kbm={"coherence_vector": [0.85, 0.95]}
    )
    
    # Export to JSON
    json_str = packet.to_json()
    print("📄 Packet as JSON:")
    print(json_str)
    print()
    
    # Import from JSON
    reconstructed = Packet.from_json(json_str)
    print("✅ Reconstructed from JSON:")
    print(reconstructed.to_vse())


def main():
    """Run all demos."""
    print("\n" + "█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + "  VSE v1.4 - Vector-Space Esperanto".center(68) + "█")
    print("█" + "  Universal Semantic Control Protocol".center(68) + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)
    
    demo_v13()
    demo_v14_kinetic()
    demo_v14_gregarious()
    demo_migration()
    demo_metrics()
    demo_json_interop()
    
    print("\n" + "=" * 70)
    print("  Demo Complete! 🎉")
    print("=" * 70)
    print("\n📚 Next steps:")
    print("  • Run examples: python examples/v1.3_deterministic.py")
    print("  • Run tests: pytest tests/")
    print("  • Read docs: see docs/ directory")
    print("  • Build apps: import vse_core, vse_metrics")
    print("\n💡 Control the vector. Shape the future.\n")


if __name__ == "__main__":
    main()
