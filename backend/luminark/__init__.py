"""
backend/luminark/ — Axiom Yield Broker logistics domain adapters.

WHAT IS HERE (stays — logistics-specific, not engine drift):
    nsdt_calculator.py      — FMCSA + ELD → NSDTVector translation
    inversion_analyzer.py   — centroid-distance SAP stage classification
    sap_signal_translator.py — engine output → broker-safe API signals

WHAT MOVED TO THE CANONICAL PACKAGE (import from `luminark.*`):
    sap_energy_layer.py     → luminark.sap_energy_layer
    VESSEL_OF_GROUNDING_*   → luminark.sap_energy_layer
    SAPStage                → luminark.sap_energy_layer
    evaluate_trap()         → luminark.sap_energy_layer

Install source:
    luminark @ git+https://github.com/foreverforward760-crypto/LUMINARK-Axiom-Systems-Engine-LASE-v1.1.git#subdirectory=core
"""
