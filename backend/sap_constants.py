"""
backend/sap_constants.py
SAP Canonical Constants — AxiomYield Backend

All numeric amplifiers, thresholds, and canonical string labels must reference
these constants. Never hardcode 1.45 or other SAP values in application code.

Stage 8 Constitutional Directives:
  • Chamber A = "Illusion of Arrival"     (never "False Heaven" / "FALSE_HEAVEN")
  • Chamber B = "Illusion of Permanence"  (never "False Hell"   / "FALSE_HELL")
  • Construct = "Stage 8 Dual-Chamber Trap"
  • Amplifier = VESSEL_OF_GROUNDING_TRAP_AMPLIFIER (1.45×)

© 2026 Richard L. Stanfield / Meridian Axiom Alignment Technologies LLC
Contact: LuminarkMeridian@gmail.com
"""

# ─── Stage 8 — VESSEL OF GROUNDING ───────────────────────────────────────────

VESSEL_OF_GROUNDING_TRAP_AMPLIFIER: float = 1.45
"""
Stage 8 TrapScore amplifier. The 1.45× factor compresses accumulated tension
against the dual-chamber trap structure.

ALWAYS reference this constant — never write `raw * 1.45` in application code.
The CI pipeline will fail the build if hardcoded 1.45 is detected in backend Python.
"""

VESSEL_OF_GROUNDING_CHAMBER_A: str = "Illusion of Arrival"
"""
Stage 8 Chamber A.
Triggered when stability is high but coherence is suppressed.
The system believes it has arrived at the destination — rigid, refuses to adapt.
(Ascending arc trap — surface calm masking zero margin)
"""

VESSEL_OF_GROUNDING_CHAMBER_B: str = "Illusion of Permanence"
"""
Stage 8 Chamber B.
Triggered when tension is high and coherence is suppressed.
The system believes the current suffering will never end.
(Descending arc trap — despair, inability to see exit)
"""

VESSEL_OF_GROUNDING_CONSTRUCT: str = "Stage 8 Dual-Chamber Trap"
"""Canonical name for the full Stage 8 trap structure."""

VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD: float = 80.0
"""TrapScore above this value triggers Exit Watch — critical escalation protocol."""

VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX: float = 20.0
"""
When |S − T| ≤ this value, the Gratitude Mechanism becomes available.
Gratitude — acknowledging both chambers simultaneously — releases polarity tension
and allows resonance with Stage 9 (TRANSPARENCY OF THE GUIDE).
"""

# ─── Stage 5 — DYNAMO OF WILL ─────────────────────────────────────────────────

DYNAMO_OF_WILL_ADVANCE_COHERENCE_THRESHOLD: float = 65.0
"""
Stage 5: Coherence at or above this value opens the Middle Path Gateway.
Outcome: ADVANCE → ascending arc toward Stage 6 (NEXUS OF HARMONY).
"""

DYNAMO_OF_WILL_RETREAT_COHERENCE_THRESHOLD: float = 35.0
"""
Stage 5: Coherence at or below this value triggers the backward doorway.
Outcome: RETREAT → regression toward Stage 4 (CRUCIBLE OF EQUILIBRIUM).
Stage 5 is the ONLY stage where the doorway opens backward.
"""

# ─── Stage 9 — TRANSPARENCY OF THE GUIDE — Dissolution Triggers ───────────────

TRANSPARENCY_DISSOLUTION_COHERENCE_MIN: float = 95.0
"""Stage 9: minimum coherence (C) required to trigger DISSOLVE_TO_PLENARA."""

TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN: float = 80.0
"""Stage 9: minimum adaptability (D) required to trigger DISSOLVE_TO_PLENARA."""

TRANSPARENCY_DISSOLUTION_TENSION_MAX: float = 20.0
"""Stage 9: maximum tension (T) allowed to trigger DISSOLVE_TO_PLENARA."""

# ─── NSDT Vector Bounds ────────────────────────────────────────────────────────

NSDT_MIN: float = 0.0
NSDT_MAX: float = 100.0
"""All five NSDT dimensions (N, S, D, T, C) must be normalized to [0.0, 100.0]."""

# ─── Deprecated Terms Guard ────────────────────────────────────────────────────
# These terms must NEVER appear in any output, label, or UI copy.

DEPRECATED_STAGE8_TERMS: tuple = (
    "FALSE_HELL",
    "FALSE_HEAVEN",
    "False Hell",
    "False Heaven",
    "F-HELL",
)
