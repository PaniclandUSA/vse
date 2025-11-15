"""
Test Suite for VSE Core
Tests packet creation, validation, parsing, and migration.
"""

import pytest
import json
from vse_core import Packet, Validator, ValidationResult, migrate_packet


class TestPacketCreation:
    """Test packet creation and initialization."""
    
    def test_basic_v13_packet(self):
        """Test creating a basic v1.3 packet."""
        packet = Packet(
            intent="test_intent",
            constraints=["constraint1", "constraint2"],
            divergence=0.3,
            version="1.3"
        )
        
        assert packet.intent == "test_intent"
        assert packet.divergence == 0.3
        assert len(packet.constraints) == 2
        assert packet.version == "1.3"
    
    def test_v14_kinetic_packet(self):
        """Test creating v1.4 Kinetic packet."""
        packet = Packet(
            intent="test",
            kbm={"coherence_vector": [0.8, 0.9]},
            c_tvm=["premise", "conclusion", 100],
            foundation=["Milieu", "Gravitas"]
        )
        
        assert packet.kbm is not None
        assert packet.c_tvm[2] == 100
        assert "Milieu" in packet.foundation
    
    def test_v14_gregarious_packet(self):
        """Test creating v1.4 Gregarious packet."""
        packet = Packet(
            intent="test",
            gsn={"network_id": "net-1", "curiosity_factor": 0.6},
            evf=["seed-1", 0.4, 5]
        )
        
        assert packet.gsn["curiosity_factor"] == 0.6
        assert packet.evf[1] == 0.4
    
    def test_divergence_validation(self):
        """Test that invalid divergence raises error."""
        with pytest.raises(ValueError):
            Packet(intent="test", divergence=1.5)
        
        with pytest.raises(ValueError):
            Packet(intent="test", divergence=-0.1)
    
    def test_kbm_validation(self):
        """Test KBM validation."""
        # Valid KBM
        packet = Packet(
            intent="test",
            kbm={"coherence_vector": [0.7, 0.9]}
        )
        assert packet.kbm is not None
        
        # Invalid KBM (min > max)
        with pytest.raises(ValueError):
            Packet(
                intent="test",
                kbm={"coherence_vector": [0.9, 0.7]}
            )


class TestPacketSerialization:
    """Test packet serialization and parsing."""
    
    def test_to_vse_basic(self):
        """Test VSE syntax generation."""
        packet = Packet(
            intent="summarize",
            constraints=["3_sentences"],
            divergence=0.25
        )
        
        vse_str = packet.to_vse()
        assert "intent: summarize" in vse_str
        assert "divergence: 0.25" in vse_str
        assert "3_sentences" in vse_str
    
    def test_from_vse_parsing(self):
        """Test parsing VSE syntax."""
        vse_str = '<VSE v1.3 | intent: test_intent | constraints: [c1, c2] | divergence: 0.30>'
        
        packet = Packet.from_vse(vse_str)
        
        assert packet.intent == "test_intent"
        assert packet.divergence == 0.30
        assert "c1" in packet.constraints
    
    def test_json_serialization(self):
        """Test JSON export/import."""
        original = Packet(
            intent="test",
            constraints=["a", "b"],
            divergence=0.4,
            immune=["protected"]
        )
        
        json_str = original.to_json()
        reconstructed = Packet.from_json(json_str)
        
        assert reconstructed.intent == original.intent
        assert reconstructed.divergence == original.divergence
        assert reconstructed.constraints == original.constraints
        assert reconstructed.immune == original.immune
    
    def test_dict_conversion(self):
        """Test dictionary conversion."""
        packet = Packet(
            intent="test",
            kbm={"coherence_vector": [0.8, 0.9]}
        )
        
        d = packet.to_dict()
        
        assert d["intent"] == "test"
        assert "kbm" in d
        assert d["kbm"]["coherence_vector"] == [0.8, 0.9]


class TestPacketValidation:
    """Test packet validation."""
    
    def test_valid_packet(self):
        """Test validation of valid packet."""
        packet = Packet(
            intent="test",
            constraints=["c1", "c2"],
            divergence=0.2
        )
        
        validator = Validator(packet)
        result = validator.validate()
        
        assert result.valid
        assert len(result.errors) == 0
    
    def test_empty_intent(self):
        """Test that empty intent is caught."""
        packet = Packet(intent="")
        
        validator = Validator(packet)
        result = validator.validate()
        
        assert not result.valid
        assert any("Intent cannot be empty" in e for e in result.errors)
    
    def test_high_divergence_warning(self):
        """Test warning for high divergence."""
        packet = Packet(intent="test", divergence=0.85)
        
        validator = Validator(packet)
        result = validator.validate()
        
        assert result.valid  # Still valid
        assert len(result.warnings) > 0
    
    def test_kbm_validation_errors(self):
        """Test KBM validation catches errors."""
        # This packet has invalid C-TVM
        packet = Packet(
            intent="test",
            c_tvm=["premise", "conclusion", -50]  # Negative token budget
        )
        
        validator = Validator(packet)
        result = validator.validate()
        
        assert not result.valid
    
    def test_strict_mode(self):
        """Test strict validation mode."""
        packet = Packet(intent="test", divergence=0.85)
        
        # Normal mode: warnings are separate
        validator = Validator(packet, strict=False)
        result = validator.validate()
        assert result.valid
        assert len(result.warnings) > 0
        
        # Strict mode: warnings become errors
        strict_validator = Validator(packet, strict=True)
        strict_result = strict_validator.validate()
        assert not strict_result.valid


class TestPacketMigration:
    """Test packet migration between versions."""
    
    def test_v13_to_v14_kinetic(self):
        """Test upgrading v1.3 to v1.4 Kinetic."""
        v13 = Packet(
            intent="test",
            constraints=["c1"],
            divergence=0.2,
            version="1.3"
        )
        
        v14 = migrate_packet(v13, target_version="1.4")
        
        assert v14.version == "1.4"
        assert v14.kbm is not None  # Should have KBM
        assert v14.mu_loop is not None  # Should have μ-Loop
    
    def test_v14_to_v13_downgrade(self):
        """Test downgrading v1.4 to v1.3."""
        v14 = Packet(
            intent="test",
            kbm={"coherence_vector": [0.8, 0.9]},
            version="1.4"
        )
        
        v13 = migrate_packet(v14, target_version="1.3")
        
        assert v13.version == "1.3"
        assert v13.kbm is None  # Kinetic fields stripped
    
    def test_foundation_inference(self):
        """Test that migration infers Foundation anchors."""
        v13 = Packet(
            intent="write_formal_academic_paper",
            constraints=["professional_tone"],
            version="1.3"
        )
        
        v14 = migrate_packet(v13, target_version="1.4")
        
        assert v14.foundation is not None
        assert "Gravitas" in v14.foundation  # Inferred from "formal" and "professional"


class TestPacketLayerDetection:
    """Test version layer detection."""
    
    def test_v13_detection(self):
        """Test v1.3 layer detection."""
        packet = Packet(
            intent="test",
            constraints=["c1"],
            version="1.3"
        )
        
        assert packet.get_version_layer() == "v1.3"
    
    def test_kinetic_detection(self):
        """Test v1.4-kinetic detection."""
        packet = Packet(
            intent="test",
            kbm={"coherence_vector": [0.8, 0.9]}
        )
        
        assert packet.get_version_layer() == "v1.4-kinetic"
    
    def test_gregarious_detection(self):
        """Test v1.4-gregarious detection."""
        packet = Packet(
            intent="test",
            gsn={"network_id": "net-1"}
        )
        
        assert packet.get_version_layer() == "v1.4-gregarious"


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
