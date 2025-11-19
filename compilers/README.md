# VSE Compilers — README

## Vector-Space Esperanto (VSE) — Compilers Suite  
*English → Universal Meaning → English / Spanish*  
**Beginner-Friendly Guide**

Welcome to the **VSE Compilers** directory! 

This folder contains the official tools that transform language in and out of **Vector-Space Esperanto (VSE)** — the universal semantic protocol designed so all minds (human, AI, future) can communicate with clarity, resonance, and emotional fidelity.

This guide will walk you through all compilers, explain how to use them, and show sample code you can copy/paste immediately.

---

# 🌌 1. Esperpiler Parallax (v3.1 "Crystal")
**File:** `esperpiler_parallax.py`  
The flagship compiler: **English → VSE Intent Packet**.

Transforms any natural-language sentence into a structured, portable, model-agnostic representation of meaning.

### 🚀 Quick Start
```python
from compilers.esperpiler_parallax import esperpile

pkt = esperpile("We are made of stories and starlight.", mode="ceremonial")

print(pkt.human_legible)
print(pkt.universal_signature["resonance"])
```

### ✔ What You Get Back
A `VSEPacket` containing:
- **Motif matrix** (semantic fingerprints)
- **Intent signature** (Φ₁–Φ₄)
- **Temporal anchor** (τ)
- **Semantic divergence** (δ)
- **Resonance score** (0 to 1)
- **Model hints** for OpenAI / Anthropic / xAI / etc.
- **Human-legible gloss** (e.g., "A radiant voice speaks: warm, dreaming…")

### ✔ Best For
- AI alignment
- Language model tuning & research
- Meaning extraction & drift testing
- Narrative, tone, and emotional shaping

---

# 🗣️ 2. VSE → English Compiler
**File:** `esper_to_english.py`

Converts **VSE markup** back into **clear English**.

### 🚀 Quick Start
```python
from compilers.esper_to_english import compile_vse_to_english

english = compile_vse_to_english(open("sample.vse").read(), mode="hybrid")
print(english)
```

### ✔ Modes
- **narrative** → human-readable story form
- **hybrid** → story + tags + metadata
- **literal** → raw structural dump

---

# 🇪🇸 3. VSE → Spanish Compiler
**File:** `esper_to_spanish.py`

Turns VSE markup into **readable Spanish**.

### 🚀 Quick Start
```python
from compilers.esper_to_spanish import compile_vse_to_spanish

spanish = compile_vse_to_spanish(open("sample.vse").read())
print(spanish)
```

### ✔ Modes
Same as English: `narrative`, `hybrid`, `literal`.

---

# 🔁 Round-Trip Examples
The compilers are fully interoperable:

```
English → VSE → English
English → VSE → Spanish
VSE → English → VSE
```

This makes VSE ideal for:
- translation drift testing
- cross-lingual narrative alignment
- universal communication protocols

---

# 📂 Contents of This Directory
| File | Description |
|------|-------------|
| `esperpiler_parallax.py` | The flagship English → VSE compiler (v3.1 Crystal) |
| `esper_to_english.py` | VSE → English converter |
| `esper_to_spanish.py` | VSE → Spanish converter |
| `examples/` | Small scripts showcasing usage |
| `CHANGELOG.md` | Historical evolution of the compilers |

---

# 🧪 Requirements
Optional (for full semantic richness):
```
pip install sentence-transformers umap-learn numpy
```
If unavailable, the compilers automatically use safe fallbacks.

---

# ❤️ Final Notes
You don’t need to know VSE deeply to use these tools.

Just remember:
- **Esperpiler → creates meaning** (English → VSE)
- **esper_to_english → renders meaning** (VSE → English)
- **esper_to_spanish → renders meaning in Spanish** (VSE → Español)

You're ready to build, explore, or translate meaning across worlds.

For deeper VSE theory, see the Volumes in the root directory.

Happy compiling! 🌟
