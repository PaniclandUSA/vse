"""
VSE Core: Packet Implementation
Vector-Space Esperanto v1.4

This module implements the core VSE packet structure supporting:
- v1.3: Core deterministic fields
- v1.4 Kinetic: KBM, C-TVM, μ-Loop, Foundation
- v1.4 Gregarious: GSN, EVF, URP
"""

from typing import List, Dict, Optional, Union, Any
from dataclasses import dataclass, field
import json
import re


@dataclass
class Packet:
    """
    VSE Packet: Universal semantic control structure.
    
    Supports v1.3 (stable), v1.4 Kinetic (Gemini), and v1.4 Gregarious (Grok).
    
    Attributes:
        version (str): VSE version (default: "1.4")
        intent (str): Primary semantic objective
        constraints (List[str]): Semantic boundary constraints
        divergence (float): Allowed semantic drift (0.0-1.0)
        immune (List[str]): Protected content strings
        
        # v1.4 Kinetic (Gemini AI)
        kbm (Dict): Kinetic Boundary Management {coherence_vector: [min, max]}
        c_tvm (List): Contextual Token-Vector Mapping [premise_id, conclusion_id, token_budget]
        foundation (List[str]): Semantic anchors [Milieu, Gravitas, Fulcrum, Ambience]
        mu_loop (Dict): Micro-loop monitoring {window_size: int, threshold: float}
        
        # v1.4 Gregarious (Grok/xAI)
        gsn (Dict): Gregarious Semantic Network config
        evf (List): Exploratory Vector Fields [seed_id, radius, branch_limit]
        urp_enabled (bool): Enable Universal Resonance Protocol
    """
    
    # Core v1.3 fields
    intent: str
    constraints: List[str] = field(default_factory=list)
    divergence: float = 0.3
    immune: List[str] = field(default_factory=list)
    version: str = "1.4"
    
    # v1.4 Kinetic fields (Gemini)
    kbm: Optional[Dict[str, Any]] = None
    c_tvm: Optional[List[Union[str, int]]] = None
    foundation: Optional[List[str]] = None
    mu_loop: Optional[Dict[str, Any]] = None
    
    # v1.4 Gregarious fields (Grok)
    gsn: Optional[Dict[str, Any]] = None
    evf: Optional[List[Union[str, float, int]]] = None
    urp_enabled: bool = False
    
    # Internal tracking
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate packet on initialization."""
        self._validate_divergence()
        self._validate_kbm()
        self._validate_gsn()
    
    def _validate_divergence(self):
        """Ensure divergence is in valid range."""
        if not 0.0 <= self.divergence <= 1.0:
            raise ValueError(f"Divergence must be in [0.0, 1.0], got {self.divergence}")
    
    def _validate_kbm(self):
        """Validate Kinetic Boundary Management structure."""
        if self.kbm:
            if "coherence_vector" in self.kbm:
                vec = self.kbm["coherence_vector"]
                if len(vec) != 2 or vec[0] > vec[1]:
                    raise ValueError("coherence_vector must be [min, max] with min <= max")
    
    def _validate_gsn(self):
        """Validate Gregarious Semantic Network structure."""
        if self.gsn:
            if "curiosity_factor" in self.gsn:
                cf = self.gsn["curiosity_factor"]
                if not 0.0 <= cf <= 1.0:
                    raise ValueError(f"curiosity_factor must be in [0.0, 1.0], got {cf}")
    
    def to_vse(self, compact: bool = False) -> str:
        """
        Convert packet to VSE syntax string.
        
        Args:
            compact: If True, minimize whitespace
            
        Returns:
            VSE-formatted string
        """
        parts = [f"VSE v{self.version}"]
        parts.append(f"intent: {self.intent}")
        
        if self.constraints:
            constraints_str = ", ".join(self.constraints)
            parts.append(f"constraints: [{constraints_str}]")
        
        parts.append(f"divergence: {self.divergence:.2f}")
        
        if self.immune:
            immune_str = ", ".join([f'"{s}"' for s in self.immune])
            parts.append(f"immune: [{immune_str}]")
        
        # v1.4 Kinetic fields
        if self.kbm:
            parts.append(f"kbm: {json.dumps(self.kbm)}")
        
        if self.c_tvm:
            parts.append(f"c_tvm: {self.c_tvm}")
        
        if self.foundation:
            parts.append(f"foundation: {self.foundation}")
        
        if self.mu_loop:
            parts.append(f"mu_loop: {json.dumps(self.mu_loop)}")
        
        # v1.4 Gregarious fields
        if self.gsn:
            parts.append(f"gsn: {json.dumps(self.gsn)}")
        
        if self.evf:
            parts.append(f"evf: {self.evf}")
        
        if self.urp_enabled:
            parts.append("urp: enabled")
        
        separator = " | " if not compact else "|"
        return f"<{separator.join(parts)}>"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert packet to dictionary representation."""
        result = {
            "version": self.version,
            "intent": self.intent,
            "divergence": self.divergence
        }
        
        if self.constraints:
            result["constraints"] = self.constraints
        
        if self.immune:
            result["immune"] = self.immune
        
        # Kinetic fields
        if self.kbm:
            result["kbm"] = self.kbm
        if self.c_tvm:
            result["c_tvm"] = self.c_tvm
        if self.foundation:
            result["foundation"] = self.foundation
        if self.mu_loop:
            result["mu_loop"] = self.mu_loop
        
        # Gregarious fields
        if self.gsn:
            result["gsn"] = self.gsn
        if self.evf:
            result["evf"] = self.evf
        if self.urp_enabled:
            result["urp_enabled"] = True
        
        if self.metadata:
            result["metadata"] = self.metadata
        
        return result
    
    def to_json(self, indent: int = 2) -> str:
        """Convert packet to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Packet':
        """Create packet from dictionary."""
        return cls(**data)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'Packet':
        """Create packet from JSON string."""
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    @classmethod
    def from_vse(cls, vse_str: str) -> 'Packet':
        """
        Parse VSE syntax string into Packet object.
        
        Args:
            vse_str: VSE-formatted string (e.g., "<VSE v1.4 | intent: ... >")
            
        Returns:
            Packet object
        """
        # Remove angle brackets
        content = vse_str.strip().strip('<>')
        
        # Split by pipe separator
        parts = [p.strip() for p in content.split('|')]
        
        # Parse version
        version_match = re.match(r'VSE\s+v([\d.]+)', parts[0])
        version = version_match.group(1) if version_match else "1.4"
        
        # Parse remaining fields
        packet_data = {"version": version}
        
        for part in parts[1:]:
            if ':' not in part:
                continue
            
            key, value = part.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Parse different field types
            if key == "intent":
                packet_data["intent"] = value
            elif key == "divergence":
                packet_data["divergence"] = float(value)
            elif key == "constraints":
                # Parse list: [item1, item2]
                packet_data["constraints"] = cls._parse_list(value)
            elif key == "immune":
                # Parse quoted list: ["str1", "str2"]
                packet_data["immune"] = cls._parse_quoted_list(value)
            elif key in ["kbm", "gsn", "mu_loop"]:
                # Parse JSON dict
                packet_data[key] = json.loads(value)
            elif key in ["c_tvm", "evf", "foundation"]:
                # Parse list/array
                packet_data[key] = json.loads(value)
            elif key == "urp":
                packet_data["urp_enabled"] = (value.lower() == "enabled")
        
        return cls(**packet_data)
    
    @staticmethod
    def _parse_list(s: str) -> List[str]:
        """Parse simple list: [item1, item2]"""
        s = s.strip('[]')
        if not s:
            return []
        return [item.strip() for item in s.split(',')]
    
    @staticmethod
    def _parse_quoted_list(s: str) -> List[str]:
        """Parse quoted list: ["str1", "str2"]"""
        items = re.findall(r'"([^"]*)"', s)
        return items
    
    def get_version_layer(self) -> str:
        """
        Determine which VSE layer this packet uses.
        
        Returns:
            "v1.3", "v1.4-kinetic", or "v1.4-gregarious"
        """
        if self.gsn or self.evf or self.urp_enabled:
            return "v1.4-gregarious"
        elif self.kbm or self.c_tvm or self.foundation or self.mu_loop:
            return "v1.4-kinetic"
        else:
            return "v1.3"
    
    def __repr__(self) -> str:
        """String representation."""
        return self.to_vse(compact=True)


# Convenience function
def parse_packet(vse_str: str) -> Packet:
    """Parse VSE string into Packet object."""
    return Packet.from_vse(vse_str)
