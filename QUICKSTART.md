# VSE Quick Start Guide

## Installation

```bash
pip install vse
```

## 5-Minute Tutorial

### 1. Create Your First Packet (v1.3)

```python
from vse_core import Packet, Validator

# Create a packet
packet = Packet(
    intent="summarize_article",
    constraints=["3_sentences", "neutral_tone"],
    divergence=0.2
)

# Validate it
validator = Validator(packet)
if validator.validate():
    print("✓ Valid packet!")
    print(packet.to_vse())
```

**Output:**
```
<VSE v1.3 | intent: summarize_article | 
constraints: [3_sentences, neutral_tone] | divergence: 0.20>
```

### 2. Add Kinetic Control (v1.4)

```python
packet = Packet(
    intent="creative_writing",
    constraints=["500_words", "fantasy_genre"],
    divergence=0.4,
    kbm={"coherence_vector": [0.70, 0.90]},
    foundation=["Ambience", "Gravitas"]
)

print(packet.to_vse())
```

The **KBM** (Kinetic Boundary Management) keeps coherence between 0.70 and 0.90 during generation.

### 3. Enable Network Coordination (v1.4 Gregarious)

```python
packet = Packet(
    intent="swarm_research",
    gsn={
        "network_id": "research-001",
        "curiosity_factor": 0.6
    },
    evf=["seed-1", 0.4, 5]  # Explore with radius 0.4, max 5 branches
)
```

**GSN** connects your packet to a semantic network for multi-agent collaboration.

### 4. Measure Output Quality

```python
from vse_metrics import MetricComputer, MetricSnapshot

# After generation (with actual embeddings)
scm = MetricComputer.compute_scm(output, constraints)
semcoh = MetricComputer.compute_semcoh(output)

metrics = MetricSnapshot(
    scm=scm,
    divergence=0.18,
    semcoh=semcoh,
    resonance=0.89
)

print(metrics)  # Shows if output is healthy
```

### 5. Migrate Existing Packets

```python
from vse_core import migrate_packet

# Upgrade v1.3 to v1.4
v13_packet = Packet(intent="test", divergence=0.2, version="1.3")
v14_packet = migrate_packet(v13_packet, target_version="1.4")

print(v14_packet.to_vse())
# Now has KBM, μ-Loop, and more!
```

## Common Patterns

### Academic Writing
```python
packet = Packet(
    intent="write_research_paper",
    constraints=["formal_tone", "cite_sources", "apa_style"],
    divergence=0.15,
    immune=["Hypothesis 1", "Table 2"],
    kbm={"coherence_vector": [0.85, 0.95]}
)
```

### Creative Content
```python
packet = Packet(
    intent="write_short_story",
    constraints=["1000_words", "mystery_genre", "first_person"],
    divergence=0.6,  # Higher for creativity
    kbm={"coherence_vector": [0.65, 0.85]},
    foundation=["Ambience", "Gravitas"]
)
```

### Technical Documentation
```python
packet = Packet(
    intent="document_api",
    constraints=["include_examples", "beginner_friendly"],
    divergence=0.10,  # Very precise
    immune=["endpoint: /api/v1/users"],
    kbm={"coherence_vector": [0.90, 0.98]}
)
```

### Multi-Agent Collaboration
```python
packet = Packet(
    intent="collaborative_problem_solving",
    divergence=0.35,
    gsn={
        "network_id": "swarm-alpha",
        "curiosity_factor": 0.7
    },
    evf=["exploration_seed", 0.5, 10],
    urp_enabled=True
)
```

## Metric Targets

For production use, aim for:
- **SCM** > 0.85 (constraint adherence)
- **δ** < 0.30 (semantic drift)
- **SemCoh** > 0.70 (coherence)
- **ℜ** > 0.85 (resonance)

## Next Steps

- **Examples**: See `examples/` directory
- **Full Demo**: Run `python demo.py`
- **Tests**: Run `pytest tests/`
- **Docs**: See `docs/` directory

## Resources

- [API Reference](docs/api-reference.md)
- [Architecture Guide](docs/architecture.md)
- [Metric Specification](docs/metrics.md)
- [GitHub Repository](https://github.com/stonespell72/vse)

---

**Control the vector. Shape the future.**
