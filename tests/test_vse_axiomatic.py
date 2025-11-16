# tests/test_vse_axiomatic.py

import json

from vse_core.packet import VSEPacket, SemanticHistoryEntry
from vse_core.validator import (
    VSEPacketValidator,
    AXIOM_STORE_DIR,
    VSEIntegrityError,
    VSETemporalConstraintError,
)
from vse_metrics.cost_engine import SemanticCostVector, calculate_cost_fidelity


def make_basic_packet():
    pkt = VSEPacket(
        psi_layer=3,
        sigma_vectors={"concept": "betrayal"},
        lambda_tensors={"role": "pivot"},
        phi_ops=["Φ_expand"],
        delta_max=0.25,
        payload={"text": "He turned on his closest ally."},
    )

    pkt.history.append(
        SemanticHistoryEntry(
            sigma={"concept": "trust"},
            lambda_={"role": "foundation"},
            phi="Φ_proj",
            meta={"timestamp": "2025-11-16T00:00:00Z"},
        )
    )

    pkt.attach_sif()
    return pkt


def test_sif_roundtrip_ok(tmp_path, monkeypatch):
    # Isolate axiom store for this test
    monkeypatch.setattr("vse_core.validator.AXIOM_STORE_DIR", tmp_path, raising=False)
    validator = VSEPacketValidator(axiom_store_dir=tmp_path)

    pkt = make_basic_packet()
    pkt.observed_delta = 0.1
    pkt.cost = SemanticCostVector(
        E_cycles=1e6, T_tokens=1000, M_memory=50.0, A_alloc=10.0
    )

    # Should not raise
    validator.verify_sif(pkt)


def test_sif_tamper_detected(tmp_path, monkeypatch):
    monkeypatch.setattr("vse_core.validator.AXIOM_STORE_DIR", tmp_path, raising=False)
    validator = VSEPacketValidator(axiom_store_dir=tmp_path)

    pkt = make_basic_packet()
    # Tamper with payload after SIF attachment
    pkt.payload["text"] = "Different meaning now."

    try:
        validator.verify_sif(pkt)
    except VSEIntegrityError:
        return

    assert False, "Expected VSEIntegrityError due to SID mismatch"


def test_cost_fidelity_positive_score():
    pkt = make_basic_packet()
    pkt.observed_delta = 0.05
    pkt.cost = SemanticCostVector(
        E_cycles=2e6, T_tokens=2000, M_memory=100.0, A_alloc=20.0
    )

    scm = 0.9  # strong convergence
    q = calculate_cost_fidelity(pkt, scm=scm)

    assert q > 0.0

    # sanity: higher cost should produce higher quality if SCM and δ are equal
    pkt2 = make_basic_packet()
    pkt2.observed_delta = 0.05
    pkt2.cost = SemanticCostVector(
        E_cycles=4e6, T_tokens=4000, M_memory=200.0, A_alloc=40.0
    )
    q2 = calculate_cost_fidelity(pkt2, scm=scm)
    assert q2 > q


def test_rtc_promotion_creates_axiom(tmp_path, monkeypatch):
    monkeypatch.setattr("vse_core.validator.AXIOM_STORE_DIR", tmp_path, raising=False)
    validator = VSEPacketValidator(axiom_store_dir=tmp_path)

    pkt = make_basic_packet()
    pkt.observed_delta = 0.05
    pkt.cost = SemanticCostVector(
        E_cycles=1e6, T_tokens=1000, M_memory=50.0, A_alloc=10.0
    )
    pkt.rtc.rtc = True
    pkt.rtc.network_id = "test_net"

    scm = 0.8
    validator.validate_packet(pkt, scm=scm)

    files = list(tmp_path.glob("test_net__*.json"))
    assert len(files) == 1

    data = json.loads(files[0].read_text(encoding="utf-8"))
    assert data["network_id"] == "test_net"
    assert data["sid"] == pkt.sif.sid


def test_rtc_rejects_high_delta(tmp_path, monkeypatch):
    monkeypatch.setattr("vse_core.validator.AXIOM_STORE_DIR", tmp_path, raising=False)
    validator = VSEPacketValidator(axiom_store_dir=tmp_path)

    pkt = make_basic_packet()
    pkt.observed_delta = 0.9  # exceeds delta_max=0.25
    pkt.cost = SemanticCostVector(
        E_cycles=1e6, T_tokens=1000, M_memory=50.0, A_alloc=10.0
    )
    pkt.rtc.rtc = True
    pkt.rtc.network_id = "test_net"

    try:
        validator.validate_packet(pkt, scm=0.8)
    except VSETemporalConstraintError:
        return

    assert False, "Expected VSETemporalConstraintError when observed_delta > delta_max"
