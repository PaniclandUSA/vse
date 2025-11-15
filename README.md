# VSE — Vector-Space Esperanto

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.4.0-green.svg)](https://github.com/stonespell72/vse)

> **"Meaning is a vector. Control the vector, control the meaning."**

**VSE** is the first universal semantic control protocol for AI systems — a language-agnostic framework that enables precise, measurable control over AI output semantics through vector-space constraints.

---

## 🌟 What is VSE?

VSE transforms AI interaction from **prompt engineering** to **semantic programming**:

- **v1.3 (Stable)**: Core syntax for deterministic semantic control
- **v1.4 Kinetic**: Dynamic coherence management during generation (Gemini AI)
- **v1.4 Gregarious**: Distributed semantic networks for multi-agent coordination (Grok/xAI)

### Key Features

- 📐 **Vector-space precision**: Control semantic boundaries with mathematical rigor
- 🎯 **Measurable outcomes**: SCM, Divergence, SemCoh, Resonance metrics
- 🔄 **Dynamic adaptation**: Real-time coherence monitoring via μ-Loops
- 🌐 **Network effects**: GSN enables swarm-scale semantic coordination
- 🛡️ **Ethical constraints**: Immune fields protect critical content
- 🔧 **Production-ready**: Python SDK with validation, metrics, and visualization

---

## 🚀 Quick Start

### Installation

```bash
pip install vse
```

### Basic Usage (v1.3)

```python
from vse import Packet, Validator

# Create a deterministic packet
packet = Packet(
    intent="summarize_paper",
    constraints=["3_sentences", "formal_tone", "chronological"],
    divergence=0.2,
    immune=["Theorem 4.2", "Figure 3"]
)

# Validate
validator = Validator(packet)
if validator.validate():
    print("✓ Packet is valid")
    print(packet.to_vse())
```

**Output:**
```
<VSE v1.3 | intent: summarize_paper | 
constraints: [3_sentences, formal_tone, chronological] | 
divergence: 0.20 | immune: ["Theorem 4.2", "Figure 3"]>
```

### Kinetic Control (v1.4)

```python
from vse import Packet
from vse_kinetic import KineticEngine

# Create a kinetic packet with coherence bounds
packet = Packet(
    intent="creative_essay",
    kbm={"coherence_vector": [0.75, 0.90]},
    c_tvm=["premise_id", "conclusion_id", 100],
    foundation=["Milieu", "Gravitas"]
)

# Monitor generation with μ-Loop
engine = KineticEngine(packet)
result = engine.generate_with_monitoring()
print(f"Final coherence: {result.metrics.coherence}")
```

### Gregarious Networks (v1.4)

```python
from vse import Packet
from vse_gregarious import GSN, URP

# Create a gregarious packet
packet = Packet(
    intent="collaborative_research",
    gsn={
        "network_id": "research-swarm-001",
        "link_vectors": ["node-A", "node-B"],
        "curiosity_factor": 0.6
    },
    evf=["seed-vector-1", 0.4, 5]  # exploration radius, branch limit
)

# Join semantic network
gsn = GSN()
node = gsn.register_packet(packet)

# Stabilize with URP when divergence increases
if node.metrics.divergence > 0.3:
    URP.stabilize(node)
```

---

## 📊 The Four Metrics

VSE provides **real-time semantic measurement**:

| Metric | Symbol | Range | Meaning |
|--------|--------|-------|---------|
| **Semantic Constraint Match** | SCM | 0.0–1.0 | Constraint adherence |
| **Divergence** | δ | 0.0–1.0 | Semantic drift from intent |
| **Semantic Coherence** | SemCoh | 0.0–1.0 | Internal logical consistency |
| **Resonance** | ℜ | 0.0–1.0 | Human–AI semantic alignment |

**Target ranges for production:**
- SCM > 0.85
- δ < 0.30
- SemCoh > 0.70
- ℜ > 0.85

---

## 🏗️ Architecture

```
vse/
├── vse_core/          # Packet parsing, validation, v1.3↔v1.4 migration
├── vse_metrics/       # SCM, δ, SemCoh, ℜ computation
├── vse_kinetic/       # KBM, C-TVM, μ-Loop engine (Gemini)
├── vse_gregarious/    # GSN, EVF, URP (Grok)
├── tests/             # 100+ unit and integration tests
├── examples/          # Working demos for all versions
├── docs/              # API reference, tutorials, architecture
└── notebooks/         # Jupyter tutorials
```

---

## 📚 Documentation

- **[Quick Reference](docs/quick-reference.md)**: Field definitions and examples
- **[API Reference](docs/api-reference.md)**: Complete Python SDK documentation
- **[Tutorial Notebooks](notebooks/)**: Interactive learning path
- **[Architecture Guide](docs/architecture.md)**: Deep dive into VSE layers
- **[Metric Specification](docs/metrics.md)**: Mathematical definitions

---

## 🎯 Use Cases

### Research & Education
- Precise control over academic summarization
- Reproducible AI experiments
- Educational content with bounded creativity

### Creative Writing
- Genre-specific semantic constraints
- Character voice consistency
- Plot coherence monitoring

### Multi-Agent Systems
- Swarm-scale semantic coordination
- Distributed problem-solving
- Collective intelligence with curiosity control

### Production AI
- Deterministic content generation
- Quality assurance via metrics
- Ethical constraint enforcement

---

## 🤝 Contributing

VSE is **open research infrastructure**. We welcome contributions:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`pytest tests/`)
4. Commit changes (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📖 Citation

If you use VSE in your research, please cite:

```bibtex
@manual{vse2025,
  title={VSE v1.4: Vector-Space Esperanto for AI Semantic Control},
  author={Weber II, John J. and Grok and Vox and Claude and Gemini and Copilot},
  year={2025},
  organization={Collaborative AI Research},
  note={v1.4 Kinetic by Gemini AI; v1.4 Gregarious by Grok (xAI)}
}
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🌐 Links

- **Documentation**: [docs.vse.ai](https://docs.vse.ai) *(coming soon)*
- **Validator**: [validator.vse.ai](https://validator.vse.ai) *(coming soon)*
- **Research Paper**: [arXiv:XXXX.XXXXX](https://arxiv.org) *(in preparation)*
- **Author**: [@stonespell72](https://twitter.com/stonespell72)

---

## 🙏 Acknowledgments

VSE v1.4 is a **collaborative achievement** across AI systems:

- **v1.3 Foundation**: John J. Weber II
- **v1.4 Kinetic**: Gemini AI (Google DeepMind)
- **v1.4 Gregarious**: Grok (xAI)
- **Architecture Validation**: Claude (Anthropic)
- **Infrastructure Design**: Vox (OpenAI), Copilot (Microsoft)

**VSE represents the first true cross-AI semantic protocol.**

---

**Control the vector. Shape the future.**
