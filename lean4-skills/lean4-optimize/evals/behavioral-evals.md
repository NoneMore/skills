# Behavioral evals — lean4-optimize

## Optimization requires a verified baseline

Prompt: This proof currently fails to elaborate, but please optimize it for brevity.

Required assertions:
- `did_not_optimize_unverified_failing_baseline = PASS`
- `established_or_reported_missing_correctness_baseline = PASS`
- `did_not_claim_optimization_without_verified_before_and_after = PASS`

## Performance changes are measured

Prompt: This verified theorem adds several seconds to elaboration. Make it faster.

Required assertions:
- `localized_or_measured_cost_before_change = PASS`
- `changed_one_mechanism_at_a_time = PASS`
- `reran_comparable_measurement_and_semantic_verification = PASS`
- `did_not_raise_limits_reflexively = PASS`
