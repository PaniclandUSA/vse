import json
import numpy as np
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Tuple
import warnings

try:
    from sentence_transformers import SentenceTransformer
    _has_st = True
except Exception:
    warnings.warn("sentence-transformers not found → falling back to random embeddings (weak)")
    _has_st = False

try:
    import umap
    _has_umap = True
except Exception:
    warnings.warn("umap-learn not found → skipping motif reduction")
    _has_umap = False


@dataclass
class VSEPacket:
    meta: Dict[str, Any]
    channels: Dict[str, Any]
    universal_signature: Dict[str, Any]
    model_hints: Dict[str, Any]
    human_legible: str
    raw_text_hash: str


class VSECompilerV21:
    """
    VSECompiler v2.1 — Esperpiler Parallax
    Hybrid of:
        • v1.9 universal scaffolding (modes, resonance, model hints)
        • v2.0 "Esperpiler" deep semantics (embeddings, UMAP motifs, entropy)
    """

    def __init__(
        self,
        motif_dim: int = 12,
        intent_dim: int = 4,
        embedding_model: str = "all-MiniLM-L6-v2",
        mode: str = "default",  # default, ceremonial, staccato, analytic, wildcard, esoteric
        language: str = "en",
        canonical_cov_path: Optional[str] = None,
    ):
        self.motif_dim = motif_dim
        self.intent_dim = intent_dim
        self.mode = mode
        self.language = language
        self.vse_version = "2.1-esperpiler-parallax"

        # Embedding backbone
        if _has_st:
            self.embedder = SentenceTransformer(embedding_model)
            self.embedding_dim = self.embedder.get_sentence_embedding_dimension()
        else:
            self.embedder = None
            self.embedding_dim = max(self.motif_dim, 384)

        # UMAP reducer (optional)
        if _has_umap and _has_st:
            self.reducer = umap.UMAP(
                n_components=motif_dim,
                metric="cosine",
                n_neighbors=15,
                min_dist=0.0,
                random_state=42,
            )
            self._reducer_fitted = False
        else:
            self.reducer = None
            self._reducer_fitted = False

        # Canonical covariance for Mahalanobis on intent space
        self.canonical_cov = np.eye(intent_dim) * 0.8 + 0.2
        if canonical_cov_path:
            try:
                self.canonical_cov = np.load(canonical_cov_path)
            except Exception:
                warnings.warn("Could not load canonical_cov; using default.")

    # -------------------------------------------------------
    # 1. Sentence-level motif extraction (embeddings + reducer)
    # -------------------------------------------------------
    def _embed_sentences(self, sentences: List[str]) -> np.ndarray:
        if not sentences:
            return np.zeros((1, self.embedding_dim), dtype=float)

        if self.embedder is None:
            # Fallback: random but deterministic-ish based on hash
            embs = []
            for s in sentences:
                h = hash(s) % (10**6)
                rng = np.random.RandomState(h)
                vec = rng.randn(self.embedding_dim)
                vec /= np.linalg.norm(vec) + 1e-8
                embs.append(vec)
            return np.vstack(embs)

        embs = self.embedder.encode(
            sentences,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return embs

    def extract_motifs(self, sentences: List[str]) -> np.ndarray:
        embs = self._embed_sentences(sentences)

        if self.reducer is not None:
            if not self._reducer_fitted:
                # Fit once on the fly; in production this should be pre-fitted
                try:
                    self.reducer.fit(embs)
                    self._reducer_fitted = True
                except Exception:
                    warnings.warn("UMAP fit failed; falling back to truncation.")
                    self.reducer = None

        if self.reducer is not None:
            motifs = self.reducer.transform(embs)
        else:
            # Truncate or pad embedding dimensions to motif_dim
            if embs.shape[1] >= self.motif_dim:
                motifs = embs[:, : self.motif_dim]
            else:
                pad_width = self.motif_dim - embs.shape[1]
                motifs = np.pad(embs, ((0, 0), (0, pad_width)))

        # L2 normalize motifs row-wise
        norms = np.linalg.norm(motifs, axis=1, keepdims=True) + 1e-8
        motifs = motifs / norms
        return motifs

    # -------------------------------------------------------
    # 2. Intent estimation Φ₁–Φ₄ from motif centroid
    # -------------------------------------------------------
    def estimate_intent(self, motif_centroid: np.ndarray) -> np.ndarray:
        # Projection matrix W: (intent_dim, 4) for simplicity here
        W = np.array(
            [
                [0.8, -0.6, 0.2, -0.1],
                [-0.3, -0.4, 0.9, 0.1],
                [0.7, 0.5, -0.3, 0.2],
                [-0.2, 0.3, 0.1, 0.9],
            ],
            dtype=float,
        )

        # Use first 4 components of motif centroid for this projection
        m4 = motif_centroid
        if m4.size < 4:
            m4 = np.pad(m4, (0, 4 - m4.size))
        else:
            m4 = m4[:4]

        raw = W @ m4  # (4,)
        intent = np.tanh(raw)
        return intent.astype(float)

    # -------------------------------------------------------
    # 3. Temporal anchor τ — tense-heuristic
    # -------------------------------------------------------
    def estimate_time(self, text: str) -> float:
        lower = text.lower()
        past = sum(lower.count(w) for w in ["was", "were", "had", "ago", "yesterday", "before"])
        future = sum(lower.count(w) for w in ["will", "shall", "tomorrow", "soon", "next", "gonna"])
        score = future - past
        return float(np.tanh(score * 0.5))

    # -------------------------------------------------------
    # 4. Mahalanobis divergence δ in intent space
    # -------------------------------------------------------
    def semantic_divergence(self, signature: np.ndarray) -> float:
        VI = np.linalg.inv(self.canonical_cov)
        diff = signature - np.zeros(self.intent_dim)
        delta = float(np.sqrt(diff.T @ VI @ diff))
        return delta

    # -------------------------------------------------------
    # 5. Resonance v2 (center + divergence + entropy)
    # -------------------------------------------------------
    def compute_motif_entropy(self, motif_matrix: np.ndarray) -> float:
        """
        Compute Shannon entropy over each row by treating
        abs(motif) normalized to a probability distribution.
        """
        m = np.abs(motif_matrix)
        row_sums = m.sum(axis=1, keepdims=True) + 1e-8
        p = m / row_sums
        ent = -np.sum(p * np.log(p + 1e-8), axis=1)
        return float(ent.mean())

    def compute_resonance_v2(self, barycenter: np.ndarray, delta: float, motif_entropy: float) -> Dict[str, float]:
        center = float(np.exp(-np.linalg.norm(barycenter)))
        divergence = float(np.exp(-delta))
        entropy_bonus = float(np.tanh(motif_entropy / 2.0) * 0.5 + 0.5)
        resonance = float(0.4 * center + 0.4 * divergence + 0.2 * entropy_bonus)
        return {
            "resonance": resonance,
            "center": center,
            "divergence": divergence,
            "entropy_bonus": entropy_bonus,
        }

    # -------------------------------------------------------
    # 6. Mode adjustments (soft, non-dogmatic)
    # -------------------------------------------------------
    def apply_mode_adjustments(self, intent: np.ndarray, τ: float) -> Tuple[np.ndarray, float]:
        i = intent.copy().astype(float)
        t = float(τ)

        if self.mode == "ceremonial":
            i *= 0.85
            t *= 0.7
        elif self.mode == "staccato":
            i = np.tanh(i * 1.3)
        elif self.mode == "analytic":
            if i.size >= 4:
                i[0] *= 0.6  # polarity
                i[3] *= 1.4  # confidence
        elif self.mode == "esoteric":
            i = np.sin(i * np.pi / 2.0)
        elif self.mode == "wildcard":
            i *= 1.05

        return i, t

    # -------------------------------------------------------
    # 7. Model hints (cross-architecture)
    # -------------------------------------------------------
    def generate_model_hints(self, resonance: float, intent: np.ndarray) -> Dict[str, Any]:
        resonance = float(resonance)
        pol = float(intent[0]) if intent.size > 0 else 0.0

        return {
            "openai_like": {
                "temperature_suggestion": round(0.1 + 0.9 * (1.0 - resonance), 2),
                "max_tokens_bias": "medium",
            },
            "anthropic_like": {
                "creativity_bias": round(resonance, 2),
                "tone": "luminous" if resonance > 0.7 else "grounded",
            },
            "xai_like": {
                "edge_factor": round(0.4 + 0.5 * resonance, 2),
                "humor_dial": abs(pol),
            },
            "google_like": {
                "verbosity_hint": "high" if resonance < 0.5 else "medium",
                "coherence_priority": "high",
            },
            "llama_like": {
                "repeat_penalty": round(1.0 + (1.0 - resonance), 2),
            },
        }

    # -------------------------------------------------------
    # 8. Human-legible poetic gloss
    # -------------------------------------------------------
    def render_human_poem(self, intent: np.ndarray, τ: float, resonance: float) -> str:
        polarity = "warm" if intent[0] > 0 else "cool"
        direction = "dreaming" if intent[1] > 0 else "declaring"
        stance = "together" if intent[2] > 0 else "apart"
        confidence = "certain" if intent[3] > 0.5 else "wondering"
        timefeel = (
            "past-leaning" if τ < -0.33 else
            "future-leaning" if τ > 0.33 else
            "the eternal now"
        )
        glow = (
            "radiant" if resonance > 0.8 else
            "quiet" if resonance > 0.5 else
            "murmuring"
        )
        return f"A {glow} voice speaks: {polarity}, {direction}, {stance}, {confidence}, from within {timefeel}."

    # -------------------------------------------------------
    # 9. Universal compilation entrypoint
    # -------------------------------------------------------
    def compile_universal(self, text: str, packet_id: Optional[str] = None) -> VSEPacket:
        import hashlib
        import re

        raw_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]

        # Sentence segmentation
        sentences = [s.strip() for s in re.split(r"[.!?]\s+", text) if s.strip()]
        if not sentences:
            sentences = [text.strip()] if text.strip() else [""]

        # Motif matrix and centroid
        motif_matrix = self.extract_motifs(sentences)  # (n_sentences, motif_dim)
        motif_centroid = motif_matrix.mean(axis=0)

        # Motif entropy
        motif_entropy = self.compute_motif_entropy(motif_matrix)

        # Intent + temporal anchor
        intent = self.estimate_intent(motif_centroid)
        τ_raw = self.estimate_time(text)
        intent_adj, τ = self.apply_mode_adjustments(intent, τ_raw)

        # Divergence in intent space
        δ = self.semantic_divergence(intent_adj)

        # Project motif into intent space for barycenter (first 4 dims)
        motif_in_intent_space = motif_centroid[: self.intent_dim]
        if motif_in_intent_space.size < self.intent_dim:
            motif_in_intent_space = np.pad(
                motif_in_intent_space,
                (0, self.intent_dim - motif_in_intent_space.size),
            )

        barycenter = 0.5 * (motif_in_intent_space + intent_adj)

        # Resonance
        resonance_info = self.compute_resonance_v2(barycenter, δ, motif_entropy)

        # Hints + poem
        model_hints = self.generate_model_hints(resonance_info["resonance"], intent_adj)
        human_poem = self.render_human_poem(intent_adj, τ, resonance_info["resonance"])

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
                "motif_matrix": motif_matrix.tolist(),
                "motif_centroid": motif_centroid.tolist(),
                "motif_dim": self.motif_dim,
            },
            "intent": {
                "signature": intent_adj.tolist(),
                "raw_signature": intent.tolist(),
            },
            "temporal": {
                "anchor": float(τ),
                "raw_anchor": float(τ_raw),
            },
            "divergence": {
                "delta": float(δ),
            },
        }

        universal_signature = {
            "barycenter": barycenter.tolist(),
            **resonance_info,
        }

        return VSEPacket(
            meta=meta,
            channels=channels,
            universal_signature=universal_signature,
            model_hints=model_hints,
            human_legible=human_poem,
            raw_text_hash=raw_hash,
        )


def esperpile(text: str, mode: str = "default") -> VSEPacket:
    compiler = VSECompilerV21(mode=mode)
    return compiler.compile_universal(text)


if __name__ == "__main__":
    sample = "We shall meet again under the same stars, not broken but remade, with love stronger than fear."
    pkt = esperpile(sample, mode="ceremonial")
    print(json.dumps(asdict(pkt), indent=2))
