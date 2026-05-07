"""
backend/sap_constants.py
SAP Canonical Constants — AxiomYield Backend

All constants are sourced from the canonical luminark pip package (LASE v1.1+).
This module re-exports them for backward compatibility with any existing imports
of the form `from backend.sap_constants import ...`.

Do NOT define constants here. Edit luminark/sap_energy_layer.py in the LASE
repo and re-install to propagate changes.

© 2026 Richard L. Stanfield / Meridian Axiom Alignment Technologies LLC
"""

# Re-export everything from the canonical package
from luminark.sap_energy_layer import (
    VESSEL_OF_GROUNDING_TRAP_AMPLIFIER,
    VESSEL_OF_GROUNDING_CHAMBER_A,
    VESSEL_OF_GROUNDING_CHAMBER_B,
    VESSEL_OF_GROUNDING_CONSTRUCT,
    TRAP_ENERGY_NONE,
    TRAP_ENERGY_LOW,
    TRAP_ENERGY_MODERATE,
    TRAP_ENERGY_HIGH,
    TRAP_ENERGY_MAXIMUM,
)

# Stage 5 thresholds (sourced from luminark)
DYNAMO_OF_WILL_ADVANCE_COHERENCE_THRESHOLD: float = 60.0
"""Stage 5: coherence ≥ this value → ADVANCE (Path A)."""

DYNAMO_OF_WILL_RETREAT_COHERENCE_THRESHOLD: float = 60.0
"""Stage 5: coherence < this value AND adaptability ≥ 40 AND tension < 65 → RETREAT (Path B)."""

# Stage 8 operational thresholds (logistics domain)
VESSEL_OF_GROUNDING_EXIT_WATCH_THRESHOLD: float = 0.80
"""TrapScore above this value triggers Exit Watch in the logistics UI."""

VESSEL_OF_GROUNDING_GRATITUDE_SPREAD_MAX: float = 20.0
"""When |S − T| ≤ this value (0-100 scale), Gratitude Mechanism is available."""

# Stage 9 dissolution triggers
TRANSPARENCY_DISSOLUTION_COHERENCE_MIN: float = 95.0
TRANSPARENCY_DISSOLUTION_ADAPTABILITY_MIN: float = 80.0
TRANSPARENCY_DISSOLUTION_TENSION_MAX: float = 20.0

# Deprecated term guard — must never appear in any output
DEPRECATED_STAGE8_TERMS: tuple = (
    "FALSE_HELL", "FALSE_HEAVEN", "False Hell", "False Heaven", "F-HELL",
)
