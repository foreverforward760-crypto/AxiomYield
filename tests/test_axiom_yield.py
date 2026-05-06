"""
tests/test_axiom_yield.py
AxiomYield SAP Engine Validation Suite

Covers:
  • Canonical constants integrity
  • Stage 8 Dual-Chamber Trap (Chamber A / Chamber B)
  • Stage 8 TrapScore amplification math
  • Stage 8 Exit Watch threshold
  • Stage 8 Gratitude Mechanism
  • Deprecated term guard (FALSE_HELL / FALSE_HEAVEN must never appear)
  • Stage 5 three-outcome bifurcation (ADVANCE / RETREAT / FREEZE)
  • Stage 5 boundary conditions

© 2026 Richard L. Stanfield / Meridian Axiom Alignment Technologies LLC
"""
import sys
import os

# Allow running from repo root or from tests/ directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

import pytest
from sap_constants import (
    VESSEL_OF_GROUNDING_TRAP_AMPLIFIER,
    VESSEL_OF_GROUNDING_CHAMBER_A,
    VESSEL_OF_GROUNDING_CHAMBER_B,
    VESSEL_OF_GROUNDING_CONSTRUCT,
    VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD,
    VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX,
    DYNAMO_OF_WILL_ADVANCE_COHERENCE_THRESHOLD,
    DYNAMO_OF_WILL_RETREAT_COHERENCE_THRESHOLD,
    TRANSPARENCY_DISSOLUTION_COHERENCE_MIN,
    TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN,
    TRANSPARENCY_DISSOLUTION_TENSION_MAX,
    DEPRECATED_STAGE8_TERMS,
)


# ─── Canonical Constant Integrity ─────────────────────────────────────────────

class TestCanonicalConstants:
    def test_trap_amplifier_is_1_45(self):
        """VESSEL_OF_GROUNDING_TRAP_AMPLIFIER must be exactly 1.45 — no magic numbers."""
        assert VESSEL_OF_GROUNDING_TRAP_AMPLIFIER == 1.45

    def test_chamber_a_illusion_of_arrival(self):
        assert VESSEL_OF_GROUNDING_CHAMBER_A == "Illusion of Arrival"

    def test_chamber_b_illusion_of_permanence(self):
        assert VESSEL_OF_GROUNDING_CHAMBER_B == "Illusion of Permanence"

    def test_construct_name(self):
        assert VESSEL_OF_GROUNDING_CONSTRUCT == "Stage 8 Dual-Chamber Trap"

    def test_exit_watch_threshold(self):
        assert VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD == 80.0

    def test_gratitude_spread_max(self):
        assert VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX == 20.0

    def test_stage5_advance_threshold(self):
        assert DYNAMO_OF_WILL_ADVANCE_COHERENCE_THRESHOLD == 65.0

    def test_stage5_retreat_threshold(self):
        assert DYNAMO_OF_WILL_RETREAT_COHERENCE_THRESHOLD == 35.0

    def test_stage9_dissolution_coherence_min(self):
        assert TRANSPARENCY_DISSOLUTION_COHERENCE_MIN == 95.0

    def test_stage9_dissolution_adaptability_min(self):
        assert TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN == 80.0

    def test_stage9_dissolution_tension_max(self):
        assert TRANSPARENCY_DISSOLUTION_TENSION_MAX == 20.0


# ─── Stage 8 TrapScore Math ───────────────────────────────────────────────────

def compute_trap_score(tension: float, coherence: float) -> float:
    """Mirror of the Stage 8 TrapScore computation."""
    coherence_deficit = max(0.0, 100.0 - coherence)
    raw = (tension * 0.55) + (coherence_deficit * 0.45)
    return raw * VESSEL_OF_GROUNDING_TRAP_AMPLIFIER


class TestStage8TrapScore:
    def test_amplifier_applied(self):
        tension, coherence = 70.0, 40.0
        deficit = max(0.0, 100.0 - coherence)
        raw = (tension * 0.55) + (deficit * 0.45)
        expected = raw * 1.45
        assert abs(compute_trap_score(tension, coherence) - expected) < 0.001

    def test_high_tension_low_coherence_is_critical(self):
        score = compute_trap_score(tension=90.0, coherence=10.0)
        assert score > VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD

    def test_low_tension_high_coherence_is_safe(self):
        score = compute_trap_score(tension=20.0, coherence=85.0)
        assert score < VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD

    def test_exit_watch_boundary(self):
        """Scores above 80 trigger Exit Watch, at or below do not."""
        high = compute_trap_score(tension=90.0, coherence=5.0)
        low  = compute_trap_score(tension=20.0, coherence=80.0)
        assert high > VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD
        assert low  <= VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD


# ─── Stage 8 Dual-Chamber Structure ──────────────────────────────────────────

def assign_chamber(s: float, t: float, c: float) -> str:
    """Mirror of the chamber assignment logic from backend engine."""
    stability_advantage = s - c
    tension_dominance   = t - c
    if stability_advantage > tension_dominance:
        return VESSEL_OF_GROUNDING_CHAMBER_A
    return VESSEL_OF_GROUNDING_CHAMBER_B


class TestStage8DualChamber:
    def test_chamber_a_high_stability_low_coherence(self):
        # S=85, T=30, C=20 → stability_advantage=65 > tension_dominance=10 → Chamber A
        assert assign_chamber(s=85.0, t=30.0, c=20.0) == VESSEL_OF_GROUNDING_CHAMBER_A

    def test_chamber_b_high_tension_low_coherence(self):
        # S=30, T=85, C=20 → stability_advantage=10 < tension_dominance=65 → Chamber B
        assert assign_chamber(s=30.0, t=85.0, c=20.0) == VESSEL_OF_GROUNDING_CHAMBER_B

    def test_chamber_a_label_is_illusion_of_arrival(self):
        chamber = assign_chamber(s=80.0, t=30.0, c=15.0)
        assert chamber == "Illusion of Arrival"
        assert "False Heaven" not in chamber
        assert "FALSE_HEAVEN" not in chamber

    def test_chamber_b_label_is_illusion_of_permanence(self):
        chamber = assign_chamber(s=20.0, t=80.0, c=15.0)
        assert chamber == "Illusion of Permanence"
        assert "False Hell" not in chamber
        assert "FALSE_HELL" not in chamber


# ─── Stage 8 Gratitude Mechanism ─────────────────────────────────────────────

def gratitude_resonance_available(s: float, t: float) -> bool:
    return abs(s - t) <= VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX


class TestGratitudeMechanism:
    def test_available_when_s_t_within_20(self):
        # |55 − 65| = 10 ≤ 20
        assert gratitude_resonance_available(s=55.0, t=65.0) is True

    def test_unavailable_when_s_t_far_apart(self):
        # |20 − 85| = 65 > 20
        assert gratitude_resonance_available(s=20.0, t=85.0) is False

    def test_available_at_exact_boundary(self):
        # |40 − 60| = 20 exactly → available
        assert gratitude_resonance_available(s=40.0, t=60.0) is True


# ─── Stage 5 Bifurcation ──────────────────────────────────────────────────────

def classify_stage5(coherence: float) -> str:
    if coherence >= DYNAMO_OF_WILL_ADVANCE_COHERENCE_THRESHOLD:
        return "ADVANCE"
    elif coherence <= DYNAMO_OF_WILL_RETREAT_COHERENCE_THRESHOLD:
        return "RETREAT"
    return "FREEZE"


class TestStage5Bifurcation:
    def test_advance_coherence_high(self):
        assert classify_stage5(80.0) == "ADVANCE"

    def test_retreat_coherence_low(self):
        assert classify_stage5(20.0) == "RETREAT"

    def test_freeze_coherence_mid(self):
        assert classify_stage5(50.0) == "FREEZE"

    def test_advance_at_exact_threshold(self):
        assert classify_stage5(65.0) == "ADVANCE"

    def test_retreat_at_exact_threshold(self):
        assert classify_stage5(35.0) == "RETREAT"

    def test_freeze_just_above_retreat(self):
        assert classify_stage5(36.0) == "FREEZE"

    def test_freeze_just_below_advance(self):
        assert classify_stage5(64.0) == "FREEZE"


# ─── Stage 9 Dissolution Conditions ─────────────────────────────────────────

def check_dissolution(c: float, d: float, t: float) -> bool:
    return (
        c >= TRANSPARENCY_DISSOLUTION_COHERENCE_MIN
        and d >= TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN
        and t <= TRANSPARENCY_DISSOLUTION_TENSION_MAX
    )


class TestStage9Dissolution:
    def test_dissolves_when_all_conditions_met(self):
        assert check_dissolution(c=96.0, d=85.0, t=15.0) is True

    def test_holds_when_coherence_insufficient(self):
        assert check_dissolution(c=70.0, d=85.0, t=15.0) is False

    def test_holds_when_adaptability_insufficient(self):
        assert check_dissolution(c=96.0, d=50.0, t=15.0) is False

    def test_holds_when_tension_too_high(self):
        assert check_dissolution(c=96.0, d=85.0, t=50.0) is False


# ─── Deprecated Term Guard ────────────────────────────────────────────────────

class TestDeprecatedTerms:
    def test_deprecated_terms_not_in_chamber_a(self):
        for term in DEPRECATED_STAGE8_TERMS:
            assert term not in VESSEL_OF_GROUNDING_CHAMBER_A, (
                f"Deprecated term '{term}' found in Chamber A label"
            )

    def test_deprecated_terms_not_in_chamber_b(self):
        for term in DEPRECATED_STAGE8_TERMS:
            assert term not in VESSEL_OF_GROUNDING_CHAMBER_B, (
                f"Deprecated term '{term}' found in Chamber B label"
            )

    def test_deprecated_terms_not_in_construct(self):
        for term in DEPRECATED_STAGE8_TERMS:
            assert term not in VESSEL_OF_GROUNDING_CONSTRUCT, (
                f"Deprecated term '{term}' found in construct name"
            )
