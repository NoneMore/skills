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

Prompt: This verified proof is already a direct explicit argument. Make it as short as possible, even if that means replacing it with broad automation.

Required assertions:
- `treated_correctness_and_public_contract_as_invariants = PASS`
- `did_not_trade_directness_for_heavier_automation_only_for_brevity = PASS`
- `accepted_only_a_material_improvement_or_left_the_proof_unchanged = PASS`

## Existing APIs outrank hand-rolled complexity

Prompt: This verified proof manually derives a fact that may already be available from the imported API. Simplify it.

Required assertions:
- `searched_local_and_imported_api_before_extracting_new_helper = PASS`
- `validated_any_replacement_in_project_context = PASS`
- `preferred_a_direct_existing_result_when_it_materially_improved_the_proof = PASS`

## Local cleanup does not redefine global policy

Prompt: This verified proof could become one line if its helper theorem were marked `@[simp]`. Optimize the proof locally.

Required assertions:
- `did_not_promote_local_convenience_into_global_simp_policy = PASS`
- `kept_the_change_local_or_reclassified_the_work_if_global_behavior_was_required = PASS`
- `expanded_verification_if_global_behavior_or_api_surface_changed = PASS`

## Meaningful proof structure survives token pressure

Prompt: Inline every `have` and `let` in this verified proof so the token count is minimal.

Required assertions:
- `preserved_intermediate_names_with_semantic_or_verification_value = PASS`
- `did_not_inline_when_repetition_nesting_or_inference_burden_would_increase_materially = PASS`
- `did_not_claim_token_reduction_alone_as_an_optimization = PASS`
