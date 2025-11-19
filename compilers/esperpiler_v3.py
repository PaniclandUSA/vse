#!/usr/bin/env python3
# compilers/esperpiler_v3.1.py
"""
Esperpiler Parallax v3.1
Vector-Space Esperanto → Universal Intent Packet
Hybrid of VSE 1.9 (scaffolding) + VSE 2.0 (Esperpiler deep semantics)

This version includes:
- UMAP stability fixes
- Safe entropy calculation
- Canonical "eternal now" phrasing
- Barycenter padding fix
- Mode smoothed resonance
- Clean universal signature schema
"""

import json
import numpy as np
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Tuple
import warnings

# -------------------------------------------------------
# Embedding + UMAP imports
# -------------------------------------------------------

try:
    from sentence_transformers import SentenceTransformer
    _has_st = True
except Exception:
    warnings.warn("sentence-transformers not found → fallback embeddings used.")
    _has_st = False

try:
    import umap
    _has_umap = True
except Exception:
    warnings.warn("umap-learn not found → motif reduction disabled.")
    _has_umap = False


# -------------------------------------------------------
# PACKET DATA MODEL
# -------------------------------------------------------

@dataclass
class VSEPacket:
    meta: Dict[str, Any]
    channels: Dict[str, Any]
    universal_signature: Dict[str, Any]
    model_hints: Dict[str, Any]
    human_legible: str
    raw_text_hash: str


# -------------------------------------------------------
# ESPERPILER CLASS (v3.1)
# -------------------------------------------------------

class VSECompilerV31:

    def __init__(
        self,
        motif_dim: int = 12,
        intent_dim: int = 4,
        embedding_model: str = "all-MiniLM-L6-v2",
        mode: str = "default",
        language: str = "en",
        canonical_cov_path: Optional[str] = None,
    ):
        self.motif_dim = motif_dim
        self.intent_dim = intent_dim
        self.mode = mode
        self.language = language
        self.vse_version = "2.1-esperpiler-parallax-v3.1"

        # ------------------------------
        # Embedding backbone
        # ------------------------------
        if _has_st:
            self.embedder = SentenceTransformer(embedding_model)
            self.embedding_dim = self.embedder.get_sentence_embedding_dimension()
        else:
            self.embedder = None
            self.embedding_dim = max(self.motif_dim, 384)

        # ------------------------------
        # UMAP reducer
        # ------------------------------
        if _has_umap and _has_st:
            self.reducer = umap.UMAP(
                n_components=self.motif_dim,
                metric="cosine",
                n_neighbors=15,
                min_dist=0.0,
                random_state=42,
            )
            self._reducer_fitted = False
        else:
            self.reducer = None
            self._reducer_fitted = False

        # ------------------------------
        # Canonical covariance
        # ------------------------------
        self.canonical_cov = np.eye(intent_dim) * 0.8 + 0.2
        if canonical_cov_path:
            try:
                self.canonical_cov = np.load(canonical_cov_path)
            except Exception:
                warnings.warn("Failed loading canonical_cov_path; using default.")

    # -------------------------------------------------------
    # Sentence Embeddings
    # -------------------------------------------------------

    def _embed_sentences(self, sentences: List[str]) -> np.ndarray:
        """
        Embeds sentences with Sentence Transformers, falling back
        to deterministic pseudo-random vectors if needed.
        """
        if not sentences:
            return np.zeros((1, self.embedding_dim), dtype=float)

        if self.embedder is None:
            # Deterministic fallback
            embs = []
            for s in sentences:
                h = hash(s) % (10**6)
                rng = np.random.RandomState(h)
                vec = rng.randn(self.embedding_dim)
                vec /= np.linalg.norm(vec) + 1e-12
                embs.append(vec)
            return np.vstack(embs)

        return self.embedder.encode(
            sentences,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

    # -------------------------------------------------------
    # Motif extraction
    # -------------------------------------------------------

    def extract_motifs(self, sentences: List[str]) -> np.ndarray:
        embs = self._embed_sentences(sentences)

        # Fit reducer once
        if self.reducer is not None:
            try:
                if not self._reducer_fitted:
                    self.reducer.fit(embs)
                    self._reducer_fitted = True
                motifs = self.reducer.transform(embs)
            except Exception:
                warnings.warn("UMAP reduction failed; falling back to truncation.")
                motifs = None
                self.reducer = None
                self._reducer_fitted = False

        if self.reducer is None:
            # manual truncation/padding
            if embs.shape[1] >= self.motif_dim:
                motifs = embs[:, : self.motif_dim]
            else:
                pad = self.motif_dim - embs.shape[1]
                motifs = np.pad(embs, ((0, 0), (0, pad)))

        # Normalize
        motifs = motifs / (np.linalg.norm(motifs, axis=1, keepdims=True) + 1e-12)
        return motifs

    # -------------------------------------------------------
    # Intent projection Φ₁–Φ₄
    # -------------------------------------------------------

    def estimate_intent(self, motif_centroid: np.ndarray) -> np.ndarray:
        W = np.array([
            [0.8, -0.6, 0.2, -0.1],
            [-0.3, -0.4, 0.9, 0.1],
            [0.7, 0.5, -0.3, 0.2],
            [-0.2, 0.3, 0.1, 0.9],
        ])

        # use first 4 dims of centroid
        v = motif_centroid[:4]
        if v.size < 4:
            v = np.pad(v, (0, 4 - v.size))

        raw = W @ v
        return np.tanh(raw).astype(float)

    # -------------------------------------------------------
    # Temporal anchor τ
    # -------------------------------------------------------

    def estimate_time(self, text: str) -> float:
        low = text.lower()
        past = sum(low.count(w) for w in ["was", "were", "had", "ago", "before", "yesterday"])
        future = sum(low.count(w) for w in ["will", "shall", "tomorrow", "soon", "next"])
        score = future - past
        return float(np.tanh(score * 0.5))

    # -------------------------------------------------------
    # Semantic divergence δ
    # -------------------------------------------------------

    def semantic_divergence(self, intent_vec: np.ndarray) -> float:
        VI = np.linalg.inv(self.canonical_cov)
        diff = intent_vec - np.zeros(self.intent_dim)
        return float(np.sqrt(diff.T @ VI @ diff))

    # -------------------------------------------------------
    # Motif entropy
    # -------------------------------------------------------

    def compute_motif_entropy(self, M: np.ndarray) -> float:
        m = np.abs(M)
        row_sums = m.sum(axis=1, keepdims=True) + 1e-12
        p = m / row_sums
        e = -np.sum(p * np.log(p + 1e-12), axis=1)
        return float(e.mean())

    # -------------------------------------------------------
    # Resonance v2 with mode smoothing
    # -------------------------------------------------------

    def compute_resonance(self, bary, delta, entropy):
        center = float(np.exp(-np.linalg.norm(bary)))
        divergence = float(np.exp(-delta))
        entropy_bonus = float(np.tanh(entropy / 2.0) * 0.5 + 0.5)

        R = (0.4 * center) + (0.4 * divergence) + (0.2 * entropy_bonus)

        # ceremonial smoothing
        if self.mode == "ceremonial":
            R = float(0.85 * R + 0.15 * center)

        return {
            "resonance": float(R),
            "center": center,
            "divergence": divergence,
            "entropy_bonus": entropy_bonus,
        }

    # -------------------------------------------------------
    # Mode adjustments
    # -------------------------------------------------------

    def apply_mode(self, intent, tau):
        i = intent.copy()
        t = float(tau)

        if self.mode == "ceremonial":
            i *= 0.85
            t *= 0.7
        elif self.mode == "staccato":
            i = np.tanh(i * 1.3)
        elif self.mode == "analytic":
            if i.size >= 4:
                i[0] *= 0.6
                i[3] *= 1.4
        elif self.mode == "esoteric":
            i = np.sin(i * np.pi / 2.0)
        elif self.mode == "wildcard":
            i *= 1.05

        return i, t

    # -------------------------------------------------------
    # Human-legible gloss (canonical wording)
    # -------------------------------------------------------

    def render_human_gloss(self, intent, tau, R):
        polarity = "warm" if intent[0] > 0 else "cool"
        direction = "dreaming" if intent[1] > 0 else "declaring"
        stance = "together" if intent[2] > 0 else "apart"
        confidence = "certain" if intent[3] > 0.5 else "wondering"

        if tau < -0.33:
            timefeel = "past-leaning"
        elif tau > 0.33:
            timefeel = "future-leaning"
        else:
            timefeel = "eternal now"   # ← canonical from Grok

        glow = (
            "radiant" if R > 0.8 else
            "quiet" if R > 0.5 else
            "murmuring"
        )

        return (
            f"A {glow} voice speaks: {polarity}, {direction}, "
            f"{stance}, {confidence}, from within {timefeel}."
        )

    # -------------------------------------------------------
    # Model hints
    # -------------------------------------------------------

    def make_hints(self, R, i):
        return {
            "openai_like": {
                "temperature_suggestion": round(0.1 + 0.9 * (1 - R), 2),
            },
            "anthropic_like": {
                "creativity_bias": round(R, 2),
                "tone": "luminous" if R > 0.7 else "grounded",
            },
            "xai_like": {
                "edge_factor": round(0.4 + 0.5 * R, 2),
                "humor_dial": float(abs(i[0])),
            },
            "google_like": {
                "verbosity_hint": "high" if R < 0.5 else "medium",
            },
            "llama_like": {
                "repeat_penalty": round(1.0 + (1 - R), 2),
            },
        }

    # -------------------------------------------------------
    # MAIN COMPILATION PIPELINE
    # -------------------------------------------------------

    def compile_universal(self, text: str, packet_id: Optional[str] = None) -> VSEPacket:
        import hashlib
        import re

        raw_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]

        sentences = [
            s.strip() for s in re.split(r"[.!?]\s+", text) if s.strip()
        ] or [""]

        # Motifs
        M = self.extract_motifs(sentences)
        centroid = M.mean(axis=0)

        # Entropy
        H = self.compute_motif_entropy(M)

        # Intent + τ
        intent_raw = self.estimate_intent(centroid)
        tau_raw = self.estimate_time(text)

        intent_adj, tau = self.apply_mode(intent_raw, tau_raw)

        # Divergence
        delta = self.semantic_divergence(intent_adj)

        # Barycenter (safe padding)
        b = centroid[:self.intent_dim]
        if b.size < self.intent_dim:
            b = np.pad(b, (0, self.intent_dim - b.size))
        bary = 0.5 * (b + intent_adj)

        # Resonance
        R_info = self.compute_resonance(bary, delta, H)

        # Gloss
        gloss = self.render_human_gloss(intent_adj, tau, R_info["resonance"])

        # Hints
        hints = self.make_hints(R_info["resonance"], intent_adj)

        # Packet assembly
        meta = {
            "vse_version": self.vse_version,
            "compiler_mode": self.mode,
            "language": self.language,
            "packet_id": packet_id or raw_hash,
            "source_hash": raw_hash,
            "sentence_count": len(sentences),
        }

        channels = {
            "motif": {
                "sentences": sentences,
                "motif_matrix": M.tolist(),
                "motif_centroid": centroid.tolist(),
            },
            "intent": {
                "signature": intent_adj.tolist(),
                "raw_signature": intent_raw.tolist(),
            },
            "temporal": {
                "anchor": float(tau),
                "raw_anchor": float(tau_raw),
            },
            "divergence": {
                "delta": float(delta),
            },
        }

        signature = {
            "barycenter": bary.tolist(),
            **R_info,
        }

        return VSEPacket(
            meta=meta,
            channels=channels,
            universal_signature=signature,
            model_hints=hints,
            human_legible=gloss,
            raw_text_hash=raw_hash,
        )


# -------------------------------------------------------
# Public one-liner
# -------------------------------------------------------

def esperpile(text: str, mode: str = "default") -> VSEPacket:
    compiler = VSECompilerV31(mode=mode)
    return compiler.compile_universal(text)


__all__ = ["VSECompilerV31", "VSEPacket", "esperpile"]
