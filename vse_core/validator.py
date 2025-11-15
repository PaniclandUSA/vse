"""
VSE Core: Packet Validator
Validates VSE packets for syntactic and semantic correctness.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
from .packet import Packet


@dataclass
class ValidationResult:
    """Result of packet validation."""
    
    valid: bool
    errors: List[str]
    warnings: List[str]
    layer: str  # "v1.3", "v1.4-kinetic", "v1.4-gregarious"
    
    def __bool__(self) -> bool:
        """Allow direct boolean checking: if ValidationResult: ..."""
        return self.valid
    
    def __str__(self) -> str:
        """Human-readable validation result."""
        if self.valid:
            result = f"✓ Valid VSE {self.layer} packet"
            if self.warnings:
                result += f"\n⚠ {len(self.warnings)} warning(s):"
                for w in self.warnings:
                    result += f"\n  - {w}"
            return result
        else:
            result = f"✗ Invalid VSE packet"
            result += f"\n✗ {len(self.errors)} error(s):"
            for e in self.errors:
                result += f"\n  - {e}"
            if self.warnings:
                result += f"\n⚠ {len(self.warnings)} warning(s):"
                for w in self.warnings:
                    result += f"\n  - {w}"
            return result


class Validator:
    """
    VSE Packet Validator.
    
    Validates packets against VSE specification across all layers:
    - v1.3: Core fields and constraints
    - v1.4 Kinetic: KBM, C-TVM, μ-Loop validation
    - v1.4 Gregarious: GSN, EVF, URP validation
    
    Usage:
        validator = Validator(packet)
        result = validator.validate()
        if result:
            print("Valid packet!")
        else:
            print(result.errors)
    """
    
    def __init__(self, packet: Packet, strict: bool = False):
        """
        Initialize validator.
        
        Args:
            packet: Packet to validate
            strict: If True, warnings become errors
        """
        self.packet = packet
        self.strict = strict
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def validate(self) -> ValidationResult:
        """
        Perform full validation.
        
        Returns:
            ValidationResult with validity status and messages
        """
        self.errors.clear()
        self.warnings.clear()
        
        # Core v1.3 validation
        self._validate_intent()
        self._validate_divergence()
        self._validate_constraints()
        self._validate_immune()
        
        # v1.4 Kinetic validation
        if self.packet.kbm or self.packet.c_tvm or self.packet.foundation:
            self._validate_kinetic()
        
        # v1.4 Gregarious validation
        if self.packet.gsn or self.packet.evf:
            self._validate_gregarious()
        
        # Check for conflicts
        self._check_conflicts()
        
        # Determine layer
        layer = self.packet.get_version_layer()
        
        # In strict mode, warnings become errors
        if self.strict and self.warnings:
            self.errors.extend(self.warnings)
            self.warnings.clear()
        
        return ValidationResult(
            valid=len(self.errors) == 0,
            errors=self.errors.copy(),
            warnings=self.warnings.copy(),
            layer=layer
        )
    
    def _validate_intent(self):
        """Validate intent field."""
        if not self.packet.intent:
            self.errors.append("Intent cannot be empty")
        elif len(self.packet.intent) > 200:
            self.warnings.append(f"Intent is very long ({len(self.packet.intent)} chars)")
    
    def _validate_divergence(self):
        """Validate divergence field."""
        d = self.packet.divergence
        if not 0.0 <= d <= 1.0:
            self.errors.append(f"Divergence must be in [0.0, 1.0], got {d}")
        elif d > 0.7:
            self.warnings.append(f"High divergence ({d}) may reduce determinism")
    
    def _validate_constraints(self):
        """Validate constraints field."""
        if not self.packet.constraints:
            self.warnings.append("No constraints specified - output may be unconstrained")
        
        for constraint in self.packet.constraints:
            if not constraint.strip():
                self.errors.append("Empty constraint found")
    
    def _validate_immune(self):
        """Validate immune field."""
        if self.packet.immune:
            for item in self.packet.immune:
                if not item.strip():
                    self.errors.append("Empty immune string found")
                elif len(item) > 500:
                    self.warnings.append(f"Very long immune string ({len(item)} chars)")
    
    def _validate_kinetic(self):
        """Validate v1.4 Kinetic fields."""
        # KBM validation
        if self.packet.kbm:
            self._validate_kbm()
        
        # C-TVM validation
        if self.packet.c_tvm:
            self._validate_c_tvm()
        
        # Foundation validation
        if self.packet.foundation:
            self._validate_foundation()
        
        # μ-Loop validation
        if self.packet.mu_loop:
            self._validate_mu_loop()
    
    def _validate_kbm(self):
        """Validate Kinetic Boundary Management."""
        kbm = self.packet.kbm
        
        if "coherence_vector" in kbm:
            vec = kbm["coherence_vector"]
            if not isinstance(vec, list) or len(vec) != 2:
                self.errors.append("coherence_vector must be [min, max]")
            elif vec[0] > vec[1]:
                self.errors.append(f"coherence_vector min ({vec[0]}) > max ({vec[1]})")
            elif not (0.0 <= vec[0] <= 1.0 and 0.0 <= vec[1] <= 1.0):
                self.errors.append("coherence_vector values must be in [0.0, 1.0]")
        
        # Warn if KBM range is very tight
        if "coherence_vector" in kbm:
            vec = kbm["coherence_vector"]
            if isinstance(vec, list) and len(vec) == 2:
                if vec[1] - vec[0] < 0.05:
                    self.warnings.append(f"Very tight KBM range ({vec[1] - vec[0]:.2f})")
    
    def _validate_c_tvm(self):
        """Validate Contextual Token-Vector Mapping."""
        c_tvm = self.packet.c_tvm
        
        if not isinstance(c_tvm, list) or len(c_tvm) != 3:
            self.errors.append("c_tvm must be [premise_id, conclusion_id, token_budget]")
        else:
            token_budget = c_tvm[2]
            if not isinstance(token_budget, int) or token_budget <= 0:
                self.errors.append(f"token_budget must be positive integer, got {token_budget}")
            elif token_budget > 10000:
                self.warnings.append(f"Very large token budget ({token_budget})")
    
    def _validate_foundation(self):
        """Validate Foundation anchors."""
        valid_foundations = {"Milieu", "Gravitas", "Fulcrum", "Ambience"}
        
        for anchor in self.packet.foundation:
            if anchor not in valid_foundations:
                self.warnings.append(f"Non-standard foundation anchor: '{anchor}'")
    
    def _validate_mu_loop(self):
        """Validate μ-Loop configuration."""
        mu = self.packet.mu_loop
        
        if "window_size" in mu:
            ws = mu["window_size"]
            if not isinstance(ws, int) or ws <= 0:
                self.errors.append(f"window_size must be positive integer, got {ws}")
        
        if "threshold" in mu:
            t = mu["threshold"]
            if not isinstance(t, (int, float)) or not 0.0 <= t <= 1.0:
                self.errors.append(f"threshold must be in [0.0, 1.0], got {t}")
    
    def _validate_gregarious(self):
        """Validate v1.4 Gregarious fields."""
        # GSN validation
        if self.packet.gsn:
            self._validate_gsn()
        
        # EVF validation
        if self.packet.evf:
            self._validate_evf()
    
    def _validate_gsn(self):
        """Validate Gregarious Semantic Network."""
        gsn = self.packet.gsn
        
        if "network_id" not in gsn:
            self.warnings.append("GSN missing network_id - packet cannot join network")
        
        if "curiosity_factor" in gsn:
            cf = gsn["curiosity_factor"]
            if not isinstance(cf, (int, float)) or not 0.0 <= cf <= 1.0:
                self.errors.append(f"curiosity_factor must be in [0.0, 1.0], got {cf}")
            elif cf > 0.8:
                self.warnings.append(f"High curiosity_factor ({cf}) may destabilize network")
        
        if "link_vectors" in gsn:
            links = gsn["link_vectors"]
            if not isinstance(links, list):
                self.errors.append("link_vectors must be a list")
            elif len(links) > 100:
                self.warnings.append(f"Many link_vectors ({len(links)}) may impact performance")
    
    def _validate_evf(self):
        """Validate Exploratory Vector Fields."""
        evf = self.packet.evf
        
        if not isinstance(evf, list) or len(evf) != 3:
            self.errors.append("evf must be [seed_id, exploration_radius, branch_limit]")
        else:
            radius = evf[1]
            branch_limit = evf[2]
            
            if not isinstance(radius, (int, float)) or not 0.0 <= radius <= 1.0:
                self.errors.append(f"exploration_radius must be in [0.0, 1.0], got {radius}")
            
            if not isinstance(branch_limit, int) or branch_limit <= 0:
                self.errors.append(f"branch_limit must be positive integer, got {branch_limit}")
            elif branch_limit > 20:
                self.warnings.append(f"High branch_limit ({branch_limit}) may be computationally expensive")
    
    def _check_conflicts(self):
        """Check for field conflicts and logical inconsistencies."""
        # High divergence + tight KBM is contradictory
        if self.packet.kbm and "coherence_vector" in self.packet.kbm:
            vec = self.packet.kbm["coherence_vector"]
            if isinstance(vec, list) and len(vec) == 2:
                if self.packet.divergence > 0.5 and (vec[1] - vec[0]) < 0.1:
                    self.warnings.append(
                        "High divergence with tight KBM may cause conflicts"
                    )
        
        # GSN with no curiosity_factor defaults to 0 (which is fine, but notable)
        if self.packet.gsn and "curiosity_factor" not in self.packet.gsn:
            self.warnings.append("GSN without curiosity_factor - defaulting to 0 (no exploration)")
        
        # Immune strings should be enforced with low divergence
        if self.packet.immune and self.packet.divergence > 0.5:
            self.warnings.append(
                "High divergence with immune strings may not fully protect content"
            )


def validate_packet(packet: Packet, strict: bool = False) -> ValidationResult:
    """
    Convenience function to validate a packet.
    
    Args:
        packet: Packet to validate
        strict: If True, warnings become errors
        
    Returns:
        ValidationResult
    """
    validator = Validator(packet, strict=strict)
    return validator.validate()
