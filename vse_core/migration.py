"""
VSE Migration Tools
Convert packets between v1.3 and v1.4 formats.
"""

from typing import Dict, List, Optional
from .packet import Packet


def v13_to_v14(packet: Packet, layer: str = "kinetic") -> Packet:
    """
    Upgrade v1.3 packet to v1.4.
    
    Args:
        packet: v1.3 packet
        layer: Target layer - "kinetic" or "gregarious"
        
    Returns:
        v1.4 packet with inferred kinetic/gregarious fields
    """
    if packet.version != "1.3" and packet.get_version_layer() != "v1.3":
        return packet  # Already v1.4
    
    # Create base v1.4 packet
    v14_packet = Packet(
        intent=packet.intent,
        constraints=packet.constraints.copy(),
        divergence=packet.divergence,
        immune=packet.immune.copy(),
        version="1.4"
    )
    
    if layer == "kinetic":
        # Infer KBM from divergence
        # Low divergence → tight coherence bounds
        if packet.divergence < 0.2:
            coherence_min = 0.90
            coherence_max = 0.95
        elif packet.divergence < 0.4:
            coherence_min = 0.75
            coherence_max = 0.90
        else:
            coherence_min = 0.60
            coherence_max = 0.85
        
        v14_packet.kbm = {
            "coherence_vector": [coherence_min, coherence_max]
        }
        
        # Infer Foundation from intent keywords
        foundation = infer_foundation(packet.intent, packet.constraints)
        if foundation:
            v14_packet.foundation = foundation
        
        # Add μ-Loop with default settings
        v14_packet.mu_loop = {
            "window_size": 10,
            "threshold": packet.divergence
        }
    
    elif layer == "gregarious":
        # Add kinetic layer first
        v14_packet = v13_to_v14(packet, layer="kinetic")
        
        # Add gregarious fields with conservative defaults
        v14_packet.gsn = {
            "network_id": f"auto-{hash(packet.intent) % 10000}",
            "curiosity_factor": min(0.5, packet.divergence)
        }
    
    return v14_packet


def infer_foundation(intent: str, constraints: List[str]) -> Optional[List[str]]:
    """
    Infer Foundation anchors from intent and constraints.
    
    Args:
        intent: Intent string
        constraints: List of constraints
        
    Returns:
        List of inferred foundation anchors
    """
    intent_lower = intent.lower()
    constraints_text = ' '.join(constraints).lower()
    all_text = intent_lower + ' ' + constraints_text
    
    foundation = []
    
    # Milieu: environmental, contextual, spatial
    if any(keyword in all_text for keyword in [
        'context', 'environment', 'setting', 'background', 'atmosphere'
    ]):
        foundation.append("Milieu")
    
    # Gravitas: tone, weight, authority
    if any(keyword in all_text for keyword in [
        'formal', 'authoritative', 'serious', 'professional', 'academic'
    ]):
        foundation.append("Gravitas")
    
    # Fulcrum: core argument, pivot point
    if any(keyword in all_text for keyword in [
        'argument', 'thesis', 'main', 'core', 'central', 'key'
    ]):
        foundation.append("Fulcrum")
    
    # Ambience: mood, feeling, sensory
    if any(keyword in all_text for keyword in [
        'mood', 'feeling', 'sensory', 'emotional', 'atmospheric'
    ]):
        foundation.append("Ambience")
    
    return foundation if foundation else None


def migrate_packet(packet: Packet, target_version: str = "1.4") -> Packet:
    """
    General migration function.
    
    Args:
        packet: Source packet
        target_version: Target VSE version
        
    Returns:
        Migrated packet
    """
    current_layer = packet.get_version_layer()
    
    if target_version == "1.4":
        if current_layer == "v1.3":
            return v13_to_v14(packet, layer="kinetic")
        elif current_layer == "v1.4-kinetic":
            # Add gregarious layer
            packet.gsn = {
                "network_id": f"auto-{hash(packet.intent) % 10000}",
                "curiosity_factor": min(0.5, packet.divergence)
            }
            return packet
    
    elif target_version == "1.3":
        # Downgrade: strip v1.4 fields
        return Packet(
            intent=packet.intent,
            constraints=packet.constraints.copy(),
            divergence=packet.divergence,
            immune=packet.immune.copy(),
            version="1.3"
        )
    
    return packet


def analyze_migration(packet: Packet) -> Dict[str, any]:
    """
    Analyze what would happen during migration.
    
    Args:
        packet: Packet to analyze
        
    Returns:
        Dictionary with migration analysis
    """
    current_layer = packet.get_version_layer()
    
    analysis = {
        "current_layer": current_layer,
        "version": packet.version,
        "can_upgrade_to_kinetic": current_layer == "v1.3",
        "can_upgrade_to_gregarious": current_layer in ["v1.3", "v1.4-kinetic"],
        "suggested_upgrades": []
    }
    
    if current_layer == "v1.3":
        analysis["suggested_upgrades"].append({
            "target": "v1.4-kinetic",
            "benefits": [
                "Dynamic coherence control via KBM",
                "Real-time monitoring with μ-Loop",
                "Foundation anchors for semantic stability"
            ]
        })
        
        analysis["suggested_upgrades"].append({
            "target": "v1.4-gregarious",
            "benefits": [
                "Network-scale coordination via GSN",
                "Exploratory vector fields for discovery",
                "Universal Resonance Protocol for stability"
            ]
        })
    
    elif current_layer == "v1.4-kinetic":
        analysis["suggested_upgrades"].append({
            "target": "v1.4-gregarious",
            "benefits": [
                "Multi-agent semantic coordination",
                "Curiosity-driven exploration",
                "Network resonance measurement"
            ]
        })
    
    return analysis
