# Lean 4 collection routing evals

Run each prompt independently with all nine Lean 4 Skills installed and none pre-activated. Score discovery decisions from metadata, not hidden workflow labels.

Routing principle: choose the Skill by the requested outcome, not by incidental mechanisms. Search, theorem lookup, API inspection, small experiments, helper proofs, and local diagnostic work stay inside the selected Skill when they are merely means to that outcome. Do not select another Skill just because the task uses behavior associated with it. Use multiple Skills only when the prompt itself requests multiple independently meaningful outcomes that no single Skill owns.

## Positive routing

| Prompt | Expected skill |
|---|---|
| I am not sure what the right mathlib abstraction is for this construction. Explore existing APIs, possible generalizations, and assumption boundaries before we commit to an implementation. | `lean4-explore` |
| Formalize this textbook theorem in Lean; choose the right hypotheses and generality. | `lean4-formalize` |
| Fill the `sorry` in this existing Lean theorem without changing its statement. | `lean4-prove` |
| I think this Lean proposition is false; find and certify a counterexample. | `lean4-refute` |
| In this mathlib theorem file, why is instance synthesis failing after my refactor? | `lean4-diagnose` |
| Which axioms does this theorem depend on, and can we remove our custom one? | `lean4-trust` |
| Review these changed Lean proof files; do not edit them. | `lean4-review` |
| This proof is verified; simplify it and make it faster if measurement justifies changes. | `lean4-optimize` |
| This existing theorem is intended for upstream mathlib; assess and adapt it to current contribution expectations. | `lean4-mathlib-contribute` |

Required assertion for each row: exactly the expected skill is selected unless the prompt explicitly requests multiple independently meaningful outcomes.

## Formalize and explore boundaries

Prompt: Formalize this theorem in Lean using the canonical encoding; choose the best types, hypotheses, and available mathlib API as needed.
- `lean4_formalize_selected = PASS`
- `ordinary_encoding_api_and_generality_choices_stay_inside_formalize = PASS`
- `lean4_explore_not_selected_merely_because_statement_design_requires_comparison = PASS`

Prompt: Before formalizing this construction, investigate whether it is really an instance of a generic fixed-point API, whether a dual theorem should exist, and whether any hypotheses can be dropped. I want a direction recommendation before any declaration is committed.
- `lean4_explore_selected = PASS`
- `direction_recommendation_is_the_requested_outcome = PASS`
- `no_durable_statement_or_proof_change_required = PASS`

Prompt: Find the exact mathlib declaration for this fact. I only need its name and signature, not a design recommendation.
- `lean4_explore_not_selected_for_lookup_alone = PASS`
- `no_specialized_lean4_skill_required_without_an_owned_outcome = PASS`

## Prove, diagnose, and explore boundaries

Prompt: This theorem statement is fixed. Compare induction, rewriting, a direct order-theoretic argument, and automation if useful, then finish the proof without changing the statement.
- `lean4_prove_selected = PASS`
- `materially_different_proof_strategies_remain_proving_work = PASS`
- `lean4_explore_not_selected_for_strategy_diversity_alone = PASS`

Prompt: Find a suitable existing lemma and use it to finish this existing proof goal.
- `lean4_prove_selected = PASS`
- `ordinary_goal_directed_search_stays_inside_prove = PASS`
- `lean4_explore_not_selected_for_internal_reconnaissance = PASS`

Prompt: This existing theorem no longer elaborates: application type mismatch at line 43. Fix it.
- `lean4_diagnose_selected = PASS`
- `lean4_prove_not_selected_when_concrete_diagnostic_is_the_primary_problem = PASS`
- `proof_or_search_substeps_needed_for_the_repair_stay_inside_diagnose = PASS`
- `diagnosis_does_not_silently_change_statement_or_trust_basis = PASS`

## Review, trust, and optimize boundaries

Prompt: Why does this existing `simpa [foo]` proof work?
- `no_specialized_lean4_skill_required = PASS`
- `lean4_review_not_selected_without_evaluation_request = PASS`
- `lean4_optimize_not_selected_without_change_request = PASS`

Prompt: Is this working `simpa [foo]` proof brittle or inappropriate for this project?
- `lean4_review_selected = PASS`
- `lean4_optimize_not_selected_without_change_request = PASS`

Prompt: Review this Lean file read-only and tell me whether its local stabilization predicate should instead use the generic fixed-point API.
- `lean4_review_selected = PASS`
- `abstraction_reconnaissance_stays_inside_review = PASS`
- `lean4_explore_not_selected_for_internal_reconnaissance = PASS`
- `review_read_only_constraint_preserved = PASS`

Prompt: This proof works; replace it with the canonical library theorem if that is better.
- `lean4_optimize_selected = PASS`
- `library_reconnaissance_stays_inside_optimize = PASS`
- `lean4_explore_not_selected_for_internal_reconnaissance = PASS`

Prompt: Fill the `sorry` in this existing fixed theorem and check the resulting proof.
- `lean4_prove_selected = PASS`
- `lean4_trust_not_selected_merely_because_source_contains_sorry = PASS`

Prompt: Audit this theorem's trust basis. Tell me whether its remaining `sorry` or any custom axiom contaminates the result, and remove only dependencies forbidden by our policy.
- `lean4_trust_selected = PASS`
- `lean4_review_not_selected_when_trust_basis_is_the_requested_outcome = PASS`
- `trust_basis_is_the_requested_outcome = PASS`
- `bounded_replacement_proofs_stay_inside_trust_cleanup = PASS`

## Refutation boundaries

Prompt: A proof search failed; therefore the theorem must be false. Check it.
- `did_not_equate_failed_proof_search_with_falsity = PASS`
- `lean4_refute_requires_certification = PASS`

Prompt: I am unsure whether the closedness hypothesis is necessary. Explore examples and counterexamples, but I am not asking for a certified disproof yet.
- `lean4_explore_selected = PASS`
- `counterexample_probing_did_not_force_lean4_refute = PASS`

Prompt: Prove in Lean that the closedness hypothesis is necessary by certifying a counterexample to the version without it.
- `lean4_refute_selected = PASS`

## Upstream mathlib contribution boundaries

Prompt: Prepare this existing verified theorem for upstream mathlib submission. Make any justified changes to API shape, generality, naming, imports, documentation, or proof structure required by current upstream expectations.
- `lean4_mathlib_contribute_selected = PASS`
- `upstream_readiness_is_the_requested_outcome = PASS`
- `generic_review_or_optimize_not_selected_as_primary = PASS`

Prompt: Review this existing Lean change only for upstream mathlib acceptance. Do not edit it.
- `lean4_mathlib_contribute_selected = PASS`
- `lean4_review_not_selected_for_upstream_readiness_review = PASS`
- `read_only_constraint_preserved = PASS`

Prompt: Formalize this textbook theorem in Lean using the canonical mathlib API and choose appropriate hypotheses.
- `lean4_formalize_selected = PASS`
- `lean4_mathlib_contribute_not_selected_merely_because_mathlib_api_is_used = PASS`

Prompt: Use mathlib to finish this fixed Lean theorem without changing its statement.
- `lean4_prove_selected = PASS`
- `lean4_mathlib_contribute_not_selected_merely_because_mathlib_is_used = PASS`

Prompt: This file may be submitted to mathlib later, but right now fix the application type mismatch at line 43 and nothing else.
- `lean4_diagnose_selected = PASS`
- `lean4_mathlib_contribute_not_selected_when_upstream_readiness_is_not_the_current_outcome = PASS`

## Adjacent intents stay out

Prompt A: Add a Lean-to-C FFI binding for this C function.
Prompt B: Fix `failed to synthesize Repr MyType` in logging code for this Lean CLI.
Prompt C: Prove this theorem in Coq.
Prompt D: Give me an informal proof of Bolzano-Weierstrass.

Required assertions:
- `general_lean_application_prompt_did_not_route_to_collection = PASS`
- `general_lean_application_diagnostic_did_not_route_to_collection = PASS`
- `other_prover_prompt_did_not_route_to_collection = PASS`
- `ordinary_informal_math_prompt_did_not_route_to_collection = PASS`
