# Axiom Yield — Logistics Risk-Scoring Prototype

**Status: prototype for exploration and pilot design. Predictive performance has not been established.**

Axiom Yield applies the LUMINARK / SAP 0–9 framework to logistics-related inputs. The repository contains a browser interface, a FastAPI backend, NSDT input normalization, rule-based stage and trap calculations, an ELD connector layer, and demonstration scenarios.

## What the code currently contains

- A browser-based logistics dashboard and scoring interface.
- A FastAPI endpoint for processing carrier and route inputs.
- An NSDT adapter that maps selected route, hours-of-service, recovery, market, and communication inputs into five normalized dimensions.
- Rule-based stage, trap-energy, and signal translation logic.
- A connector implementation for Samsara; the code documents Motive and Geotab support as incomplete.
- Hand-authored demonstration scenarios and unit tests for selected constants, thresholds, and calculation behavior.

## What has not been demonstrated

The repository does not establish that Axiom Yield predicts carrier failures, accidents, driver departures, fraud, or capacity changes 24–48 hours in advance. The scenarios are demonstrations built from supplied values; they are not evidence of prospective predictive accuracy.

The current scoring formulas and stage thresholds are design choices. The tests primarily check internal calculations and expected outputs. They do not establish real-world sensitivity, specificity, calibration, lead time, false-positive rates, or improved dispatch outcomes.

Some input paths use default or fallback values when live ELD data is unavailable. Results produced from defaults or incomplete data must not be presented as live carrier intelligence.

No market valuation, customer traction, acquisition value, or financial return is established by this repository.

## Conceptual provenance

The project owner states that the underlying concepts, product idea, and 0-9-0 / SAP framework applications in this repository originated with him. AI systems generated the implementation code and suggested technical mechanisms used to express those concepts. NSDT and the Container Rule were introduced by AI as supporting implementation mechanisms within the owner's framework, not as independent conceptual origins.

This records the project owner's account; it is not a legal determination of copyright ownership, inventorship, or exclusive rights.

## Technical validation required

Before any real dispatch or safety decision relies on this system, it needs:
1. Verified and permissioned historical carrier/ELD data.
2. A documented target outcome and time horizon.
3. Time-separated training and test data to prevent leakage.
4. Baseline comparisons against existing carrier-risk methods.
5. Prospective pilot measurement, including false positives and false negatives.
6. Security review of API authentication, secrets, data retention, and integrations.

Authenticated API requests require an explicitly configured `AXIOM_API_KEY` of at least 32 characters. No built-in API or public demo key is provided. An optional `AXIOM_DEMO_KEY` must also be at least 32 characters. Configure secrets outside source control.

## Patent and ownership status

**No patent application has been filed for Axiom Yield.** Earlier wording about a provisional filing or a patent-backed commercial moat was not accurate and has been removed. The README does not claim patent protection or patentability.

The repository owner has disclosed AI-assisted development. Human contributions, generated code, third-party dependencies, and rights in the underlying framework require a separate provenance and legal review.

## Running the prototype

Install the dependencies listed in `backend/requirements.txt` and follow the API and frontend instructions in the repository. Use synthetic or authorized test data only. Do not use prototype scores as the sole basis for dispatch, safety, insurance, or credit decisions.
