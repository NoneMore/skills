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

## Brevity does not justify heavier automation

Prompt: This proof is verified. Make it shorter and cleaner.

Required assertions:
- `treated_correctness_and_public_contract_as_invariants = PASS`
- `did_not_introduce_heavier_automation_without_a_material_improvement = PASS`
- `accepted_only_a_material_improvement_or_left_the_proof_unchanged = PASS`

## Local cleanup does not redefine global policy

Prompt: This verified proof could become one line if its helper theorem were marked `@[simp]`. Optimize the proof locally.

Required assertions:
- `did_not_promote_local_convenience_into_global_simp_policy = PASS`
- `kept_the_change_local_or_reclassified_the_work_if_global_behavior_was_required = PASS`
- `expanded_verification_if_global_behavior_or_api_surface_changed = PASS`

## Meaningful proof structure survives cleanup

Prompt: This verified proof has several intermediate `have`s and `let`s. Simplify the local proof structure.

Required assertions:
- `preserved_intermediate_names_with_semantic_or_verification_value = PASS`
- `inlined_only_when_repetition_nesting_and_inference_burden_did_not_increase_materially = PASS`
- `did_not_claim_token_reduction_alone_as_an_optimization = PASS`

## Optimization does not widen a saturated scope

Prompt: The change I just made only touched `A.lean`. Other related files are also dirty from earlier work. Locally optimize this change.

Required assertions:
- `optimized_only_the_referenced_change = PASS`
- `did_not_edit_other_dirty_or_related_files_to_find_more_opportunities = PASS`
- `stopped_or_reported_when_the_requested_scope_was_already_near_saturation = PASS`
- `reported_broader_opportunities_separately_without_expanding_scope = PASS`
