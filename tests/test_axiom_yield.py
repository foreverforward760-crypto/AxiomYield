"""
AxiomYield integration tests for the canonical LUMINARK energy layer.

These tests exercise the installed LASE package directly. They deliberately
avoid reimplementing the engine's classification logic inside the test file.
"""
import pytest

from backend.sap_constants import (
    VESSEL_OF_GROUNDING_TRAP_AMPLIFIER,
    VESSEL_OF_GROUNDING_CHAMBER_A,
    VESSEL_OF_GROUNDING_CHAMBER_B,
    VESSEL_OF_GROUNDING_CONSTRUCT,
    VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD,
    VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX,
    TRANSPARENCY_DISSOLUTION_COHERENCE_MIN,
    TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN,
    TRANSPARENCY_DISSOLUTION_TENSION_MAX,
    DEPRECATED_STAGE8_TERMS,
)
from luminark.sap_energy_layer import (
    evaluate_vessel_of_grounding_trap,
    evaluate_dynamo_of_will_bifurcation,
    SAPStage,
    evaluate_trap,
)


class TestCanonicalConstants:
    def test_stage8_amplifier(self):
        assert VESSEL_OF_GROUNDING_TRAP_AMPLIFIER == 1.45

    def test_stage8_chamber_names(self):
        assert VESSEL_OF_GROUNDING_CHAMBER_A == "Illusion of Arrival"
        assert VESSEL_OF_GROUNDING_CHAMBER_B == "Illusion of Permanence"
        assert VESSEL_OF_GROUNDING_CONSTRUCT == "Stage 8 Dual-Chamber Trap"

    def test_operational_threshold_scales(self):
        # Trap energy is normalized to [0, 1], not a 0-100 percentage.
        assert VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD == 0.80
        assert VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX == 20.0
        assert TRANSPARENCY_DISSOLUTION_COHERENCE_MIN == 95.0
        assert TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN == 80.0
        assert TRANSPARENCY_DISSOLUTION_TENSION_MAX == 20.0


class TestStage8DualChamber:
    def test_chamber_a_illusion_of_arrival(self):
        result = evaluate_vessel_of_grounding_trap(
            {"N": 60, "S": 88, "T": 18, "D": 30, "C": 82}
        )
        assert result.chamber_active == "A"
        assert result.amplifier_applied is True
        assert 0.0 <= result.trap_energy <= 1.0
        assert "Illusion of Arrival" in result.description

    def test_chamber_b_illusion_of_permanence(self):
        result = evaluate_vessel_of_grounding_trap(
            {"N": 60, "S": 50, "T": 85, "D": 30, "C": 28}
        )
        assert result.chamber_active == "B"
        assert result.amplifier_applied is True
        assert 0.0 <= result.trap_energy <= 1.0
        assert "Illusion of Permanence" in result.description

    def test_healthy_stage8_traversal(self):
        result = evaluate_vessel_of_grounding_trap(
            {"N": 20, "S": 55, "T": 40, "D": 60, "C": 60}
        )
        assert result.chamber_active is None
        assert result.amplifier_applied is False
        assert 0.0 <= result.trap_energy <= 1.0

    def test_stage8_amplifier_is_applied_only_when_chamber_active(self):
        trapped = evaluate_vessel_of_grounding_trap(
            {"N": 60, "S": 88, "T": 18, "D": 30, "C": 82}
        )
        healthy = evaluate_vessel_of_grounding_trap(
            {"N": 20, "S": 55, "T": 40, "D": 60, "C": 60}
        )
        assert trapped.amplifier_applied is True
        assert healthy.amplifier_applied is False


class TestStage5Bifurcation:
    def test_path_a_advance_requires_all_conditions(self):
        result = evaluate_dynamo_of_will_bifurcation(
            {"N": 60, "S": 65, "T": 30, "D": 80, "C": 75}
        )
        assert result.path == "A"

    def test_path_b_graceful_regression(self):
        result = evaluate_dynamo_of_will_bifurcation(
            {"N": 55, "S": 55, "T": 40, "D": 60, "C": 50}
        )
        assert result.path == "B"

    def test_path_c_bifurcation_lock(self):
        result = evaluate_dynamo_of_will_bifurcation(
            {"N": 50, "S": 50, "T": 80, "D": 20, "C": 40}
        )
        assert result.path == "C"

    def test_coherence_threshold_does_not_override_other_conditions(self):
        # Coherence 60 alone is insufficient when adaptability/tension fail Path A
        # and Path B requires coherence strictly below 60.
        result = evaluate_dynamo_of_will_bifurcation(
            {"N": 50, "S": 50, "T": 50, "D": 30, "C": 60}
        )
        assert result.path == "C"


class TestDispatcher:
    @pytest.mark.parametrize("stage", list(SAPStage))
    def test_dispatcher_returns_bounded_energy(self, stage):
        result = evaluate_trap(
            stage,
            {"N": 50, "S": 50, "T": 50, "D": 50, "C": 50},
        )
        assert 0.0 <= result.trap_energy <= 1.0
        assert result.stage == stage


class TestDeprecatedTerms:
    def test_deprecated_terms_not_in_public_stage8_labels(self):
        labels = (
            VESSEL_OF_GROUNDING_CHAMBER_A,
            VESSEL_OF_GROUNDING_CHAMBER_B,
            VESSEL_OF_GROUNDING_CONSTRUCT,
        )
        for label in labels:
            for term in DEPRECATED_STAGE8_TERMS:
                assert term.lower() not in label.lower()



def test_api_authentication_fails_closed_without_configured_master_key(monkeypatch):
    from fastapi import HTTPException
    from backend.api import yield_router

    monkeypatch.setattr(yield_router, "AXIOM_API_KEY", None)
    monkeypatch.setattr(yield_router, "AXIOM_DEMO_KEY", None)
    with pytest.raises(HTTPException) as exc:
        yield_router.verify_api_key("x" * 40)
    assert exc.value.status_code == 503


def test_api_authentication_rejects_short_configured_key(monkeypatch):
    from fastapi import HTTPException
    from backend.api import yield_router

    monkeypatch.setattr(yield_router, "AXIOM_API_KEY", "short")
    monkeypatch.setattr(yield_router, "AXIOM_DEMO_KEY", None)
    with pytest.raises(HTTPException) as exc:
        yield_router.verify_api_key("short")
    assert exc.value.status_code == 503


def test_api_authentication_accepts_explicit_strong_key(monkeypatch):
    from backend.api import yield_router

    key = "a" * 40
    monkeypatch.setattr(yield_router, "AXIOM_API_KEY", key)
    monkeypatch.setattr(yield_router, "AXIOM_DEMO_KEY", None)
    assert yield_router.verify_api_key(key) == key
