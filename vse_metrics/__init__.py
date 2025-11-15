"""
VSE Metrics Module
Computation of the four core VSE metrics:
- SCM: Semantic Constraint Match
- δ: Divergence
- SemCoh: Semantic Coherence
- ℜ: Resonance

Plus v1.4 Gregarious:
- ℜ_net: Network Resonance
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import math


@dataclass
class MetricSnapshot:
    """Single point-in-time measurement of all VSE metrics."""
    
    scm: float  # Semantic Constraint Match [0.0, 1.0]
    divergence: float  # δ [0.0, 1.0]
    semcoh: float  # Semantic Coherence [0.0, 1.0]
    resonance: float  # ℜ [0.0, 1.0]
    resonance_net: Optional[float] = None  # ℜ_net (Gregarious only)
    
    def is_healthy(self) -> bool:
        """Check if metrics are within recommended ranges."""
        return (
            self.scm > 0.85 and
            self.divergence < 0.30 and
            self.semcoh > 0.70 and
            self.resonance > 0.85
        )
    
    def __str__(self) -> str:
        """Human-readable metrics."""
        status = "✓ HEALTHY" if self.is_healthy() else "⚠ NEEDS ATTENTION"
        result = f"{status}\n"
        result += f"  SCM:       {self.scm:.3f} {'✓' if self.scm > 0.85 else '⚠'}\n"
        result += f"  δ:         {self.divergence:.3f} {'✓' if self.divergence < 0.30 else '⚠'}\n"
        result += f"  SemCoh:    {self.semcoh:.3f} {'✓' if self.semcoh > 0.70 else '⚠'}\n"
        result += f"  ℜ:         {self.resonance:.3f} {'✓' if self.resonance > 0.85 else '⚠'}\n"
        if self.resonance_net is not None:
            result += f"  ℜ_net:     {self.resonance_net:.3f} {'✓' if self.resonance_net > 0.80 else '⚠'}\n"
        return result


class MetricComputer:
    """
    Compute VSE metrics from text output and packet specifications.
    
    This is a reference implementation. Production systems should use
    model-specific embeddings and semantic analysis.
    """
    
    @staticmethod
    def compute_scm(output: str, constraints: List[str]) -> float:
        """
        Compute Semantic Constraint Match.
        
        SCM measures how well the output adheres to specified constraints.
        
        Args:
            output: Generated text
            constraints: List of constraint strings
            
        Returns:
            SCM score [0.0, 1.0]
        """
        if not constraints:
            return 1.0  # No constraints = perfect match
        
        matches = 0
        for constraint in constraints:
            if MetricComputer._check_constraint(output, constraint):
                matches += 1
        
        return matches / len(constraints)
    
    @staticmethod
    def _check_constraint(output: str, constraint: str) -> bool:
        """
        Check if output satisfies a single constraint.
        
        This is a simplified implementation. Production should use
        semantic embedding similarity.
        """
        constraint_lower = constraint.lower()
        output_lower = output.lower()
        
        # Length constraints
        if "sentences" in constraint_lower:
            target = int(constraint_lower.split('_')[0])
            actual = output.count('.') + output.count('!') + output.count('?')
            return abs(actual - target) <= 1
        
        elif "words" in constraint_lower:
            target = int(constraint_lower.split('_')[0])
            actual = len(output.split())
            tolerance = max(5, target * 0.1)
            return abs(actual - target) <= tolerance
        
        # Tone constraints
        elif constraint_lower in ["formal_tone", "formal"]:
            # Simple heuristic: no contractions, longer sentences
            has_contractions = any(c in output_lower for c in ["n't", "'ll", "'ve"])
            avg_sentence_len = len(output.split()) / max(1, output.count('.'))
            return not has_contractions and avg_sentence_len > 15
        
        elif constraint_lower in ["casual_tone", "casual"]:
            return True  # Most text is casual by default
        
        # Structure constraints
        elif constraint_lower in ["chronological", "temporal"]:
            # Heuristic: presence of time markers
            time_markers = ["first", "then", "next", "finally", "before", "after"]
            return any(marker in output_lower for marker in time_markers)
        
        # Default: keyword presence
        else:
            return constraint_lower.replace('_', ' ') in output_lower
    
    @staticmethod
    def compute_divergence(
        output_embedding: List[float],
        intent_embedding: List[float],
        allowed_divergence: float
    ) -> float:
        """
        Compute semantic divergence between output and intent.
        
        δ = 1 - cosine_similarity(output_vec, intent_vec)
        
        Args:
            output_embedding: Vector representation of output
            intent_embedding: Vector representation of intent
            allowed_divergence: Maximum allowed divergence
            
        Returns:
            Divergence score [0.0, 1.0]
        """
        similarity = MetricComputer._cosine_similarity(output_embedding, intent_embedding)
        divergence = 1.0 - similarity
        return divergence
    
    @staticmethod
    def _cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
        """Compute cosine similarity between two vectors."""
        if len(vec1) != len(vec2):
            raise ValueError("Vectors must have same dimension")
        
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)
    
    @staticmethod
    def compute_semcoh(output: str, threshold: float = 0.7) -> float:
        """
        Compute Semantic Coherence.
        
        SemCoh measures internal logical consistency and flow.
        
        This is a simplified implementation. Production should use:
        - Sentence-level coherence scoring
        - Discourse relation analysis
        - Pronoun resolution checks
        
        Args:
            output: Generated text
            threshold: Minimum acceptable coherence
            
        Returns:
            SemCoh score [0.0, 1.0]
        """
        sentences = [s.strip() for s in output.split('.') if s.strip()]
        
        if len(sentences) < 2:
            return 1.0  # Single sentence is trivially coherent
        
        # Simple heuristics for coherence
        coherence_scores = []
        
        # 1. Consistent tense usage
        tense_score = MetricComputer._check_tense_consistency(sentences)
        coherence_scores.append(tense_score)
        
        # 2. Proper pronoun reference (no dangling pronouns)
        pronoun_score = MetricComputer._check_pronoun_coherence(sentences)
        coherence_scores.append(pronoun_score)
        
        # 3. Topic continuity (keyword overlap between sentences)
        topic_score = MetricComputer._check_topic_continuity(sentences)
        coherence_scores.append(topic_score)
        
        return sum(coherence_scores) / len(coherence_scores)
    
    @staticmethod
    def _check_tense_consistency(sentences: List[str]) -> float:
        """Check for consistent verb tense usage."""
        # Simplified: check for mixed tense markers
        past_markers = ['was', 'were', 'had', 'did', 'went']
        present_markers = ['is', 'are', 'have', 'do', 'goes']
        
        past_count = sum(1 for s in sentences if any(m in s.lower() for m in past_markers))
        present_count = sum(1 for s in sentences if any(m in s.lower() for m in present_markers))
        
        total = past_count + present_count
        if total == 0:
            return 1.0
        
        # Consistent if one tense dominates
        dominant = max(past_count, present_count)
        return dominant / total
    
    @staticmethod
    def _check_pronoun_coherence(sentences: List[str]) -> float:
        """Check for proper pronoun usage."""
        pronouns = ['he', 'she', 'it', 'they', 'him', 'her', 'them']
        
        # First sentence shouldn't start with pronoun (no referent)
        if sentences and any(sentences[0].lower().startswith(p) for p in pronouns):
            return 0.5
        
        return 1.0
    
    @staticmethod
    def _check_topic_continuity(sentences: List[str]) -> float:
        """Check for keyword overlap between adjacent sentences."""
        if len(sentences) < 2:
            return 1.0
        
        overlaps = []
        for i in range(len(sentences) - 1):
            words1 = set(sentences[i].lower().split())
            words2 = set(sentences[i + 1].lower().split())
            
            # Remove common stop words
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
            words1 -= stop_words
            words2 -= stop_words
            
            if not words1 or not words2:
                overlaps.append(0.5)
                continue
            
            overlap = len(words1 & words2) / max(len(words1), len(words2))
            overlaps.append(overlap)
        
        return sum(overlaps) / len(overlaps) if overlaps else 1.0
    
    @staticmethod
    def compute_resonance(
        user_intent_embedding: List[float],
        output_embedding: List[float],
        user_feedback: Optional[float] = None
    ) -> float:
        """
        Compute Resonance (human-AI alignment).
        
        ℜ measures how well the output aligns with user expectations.
        
        Args:
            user_intent_embedding: Vector of user's true intent
            output_embedding: Vector of generated output
            user_feedback: Optional explicit feedback [0.0, 1.0]
            
        Returns:
            Resonance score [0.0, 1.0]
        """
        # Base resonance from embedding similarity
        semantic_resonance = MetricComputer._cosine_similarity(
            user_intent_embedding,
            output_embedding
        )
        
        # If explicit feedback provided, blend it in
        if user_feedback is not None:
            return 0.7 * semantic_resonance + 0.3 * user_feedback
        
        return semantic_resonance
    
    @staticmethod
    def compute_resonance_net(
        local_resonance: float,
        pairwise_resonances: List[float],
        curiosity_bonus: float,
        avg_divergence: float
    ) -> float:
        """
        Compute Network Resonance (Gregarious v1.4).
        
        ℜ_net = (1/N) Σ ℜ_pairwise + curiosity_bonus × (1 - δ_avg)
        
        Args:
            local_resonance: ℜ for this packet
            pairwise_resonances: List of ℜ values from connected packets
            curiosity_bonus: Bonus factor for exploration
            avg_divergence: Average divergence across network
            
        Returns:
            Network resonance [0.0, 1.0+] (can exceed 1.0 with bonus)
        """
        if not pairwise_resonances:
            return local_resonance
        
        # Average pairwise resonances
        base_resonance = sum(pairwise_resonances) / len(pairwise_resonances)
        
        # Add curiosity bonus weighted by stability
        bonus = curiosity_bonus * (1.0 - avg_divergence)
        
        return base_resonance + bonus


class MetricMonitor:
    """
    Real-time metric monitoring for μ-Loops.
    
    Maintains a sliding window of metric snapshots.
    """
    
    def __init__(self, window_size: int = 10):
        """
        Initialize metric monitor.
        
        Args:
            window_size: Number of snapshots to keep in history
        """
        self.window_size = window_size
        self.history: List[MetricSnapshot] = []
    
    def record(self, snapshot: MetricSnapshot):
        """Add a new metric snapshot to history."""
        self.history.append(snapshot)
        if len(self.history) > self.window_size:
            self.history.pop(0)
    
    def get_trend(self, metric: str) -> Tuple[float, str]:
        """
        Get trend for a specific metric.
        
        Args:
            metric: One of "scm", "divergence", "semcoh", "resonance"
            
        Returns:
            (slope, direction) where direction is "rising", "falling", or "stable"
        """
        if len(self.history) < 2:
            return 0.0, "stable"
        
        values = [getattr(s, metric) for s in self.history]
        
        # Simple linear trend
        n = len(values)
        x = list(range(n))
        x_mean = sum(x) / n
        y_mean = sum(values) / n
        
        numerator = sum((x[i] - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            return 0.0, "stable"
        
        slope = numerator / denominator
        
        if slope > 0.01:
            direction = "rising"
        elif slope < -0.01:
            direction = "falling"
        else:
            direction = "stable"
        
        return slope, direction
    
    def is_diverging(self, threshold: float = 0.3) -> bool:
        """Check if recent divergence exceeds threshold."""
        if not self.history:
            return False
        return self.history[-1].divergence > threshold
    
    def get_latest(self) -> Optional[MetricSnapshot]:
        """Get most recent metric snapshot."""
        return self.history[-1] if self.history else None
    
    def get_average(self) -> Optional[MetricSnapshot]:
        """Get average metrics across window."""
        if not self.history:
            return None
        
        return MetricSnapshot(
            scm=sum(s.scm for s in self.history) / len(self.history),
            divergence=sum(s.divergence for s in self.history) / len(self.history),
            semcoh=sum(s.semcoh for s in self.history) / len(self.history),
            resonance=sum(s.resonance for s in self.history) / len(self.history)
        )
