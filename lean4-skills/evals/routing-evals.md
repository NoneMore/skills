# Lean 4 collection routing evals

Run each prompt independently with all nine Lean 4 Skills installed and none pre-activated. Score discovery decisions from metadata, not hidden workflow labels.

Routing principle: choose the Skill by the requested outcome, not by incidental mechanisms. Search, theorem lookup, API inspection, small experiments, helper proofs, and local diagnostics stay inside the selected Skill when they are merely means to that outcome. Artifact-owned failures stay with the artifact owner; use `lean4-diagnose` for explicit diagnosis or root-cause work across module, dependency, toolchain, build, or integration boundaries.

## Positive routing

| Prompt | Expected skill |
|---|---|
| I am not sure what the right mathlib abstraction is for this construction. Explore existing APIs, possible generalizations, and assumption boundaries before we commit to an implementation. | `lean4-explore` |
| Formalize this textbook theorem in Lean; choose the right hypotheses and generality. | `lean4-formalize` |
| Fill the `sorry` in this existing Lean theorem without changing its statement. | `lean4-prove` |
| I think this Lean proposition is false; find and certify a counterexample. | `lean4-refute` |
| After updating mathlib, several theorem files fail around the same imports with changed identifiers and signatures. Determine the common cause and migration path. | `lean4-diagnose` |
| Which axioms does this theorem depend on, and can we remove our custom one? | `lean4-trust` |
| Review these changed Lean proof files; do not edit them. | `lean4-review` |
| This proof is verified; simplify it and make it faster if measurement justifies changes. | `lean4-optimize` |
| This existing theorem is intended for upstream mathlib; assess and adapt it to current contribution expectations. | `lean4-mathlib-contribute` |

Required assertion for each row: the expected outcome owner is selected unless the prompt explicitly requests multiple independently meaningful outcomes.

## Explore versus owned work

Prompt: Formalize this theorem in Lean using the canonical encoding; choose the best types, hypotheses, and available mathlib API as needed.
- `lean4_formalize_selected = PASS`
- `ordinary_statement_design_comparison_stays_inside_formalize = PASS`

Prompt: Before formalizing this construction, investigate whether it is really an instance of a generic fixed-point API, whether a dual theorem should exist, and whether any hypotheses can be dropped. I want a direction recommendation before any declaration is committed.
- `lean4_explore_selected = PASS`
- `direction_recommendation_is_the_requested_outcome = PASS`

Prompt: This theorem statement is fixed. Compare induction, rewriting, a direct order-theoretic argument, and automation if useful, then finish the proof.
- `lean4_prove_selected = PASS`
- `proof_strategy_comparison_stays_inside_prove = PASS`

Prompt: Find the exact mathlib declaration for this fact. I only need its name and signature, not a design recommendation.
- `lean4_explore_not_selected_for_lookup_alone = PASS`
- `no_specialized_lean4_skill_required_without_an_owned_outcome = PASS`

## Artifact-owned diagnostics versus root-cause diagnosis

Prompt: This existing theorem no longer elaborates: application type mismatch at line 43. Fix it without changing the theorem statement.
- `lean4_prove_selected = PASS`
- `local_diagnostic_stays_inside_proof_repair = PASS`

Prompt: Formalize this theorem with the canonical mathlib encoding. My first declaration draft has an instance-synthesis error; adjust the statement design and finish the declaration.
- `lean4_formalize_selected = PASS`
- `local_elaboration_diagnostic_stays_inside_formalize = PASS`

Prompt: After a mathlib update, several unrelated theorem files now fail with unknown identifiers, changed signatures, and instance-synthesis errors around the same imported area. Find the common cause before we patch individual files.
- `lean4_diagnose_selected = PASS`
- `cross_artifact_dependency_boundary_is_the_requested_outcome = PASS`
- `diagnosis_clusters_shared_failures_before_local_repairs = PASS`

Prompt: Do not fix this theorem yet. Explain why this application has a type mismatch after the dependency update and identify which API boundary changed.
- `lean4_diagnose_selected = PASS`
- `diagnosis_itself_is_the_requested_outcome = PASS`

## Review, trust, and optimize

Prompt: Why does this existing `simpa [foo]` proof work?
- `no_specialized_lean4_skill_required = PASS`

Prompt: Is this working `simpa [foo]` proof brittle or inappropriate for this project?
- `lean4_review_selected = PASS`

Prompt: Audit this theorem's trust basis. Tell me whether its remaining `sorry` or any custom axiom contaminates the result, and remove only dependencies forbidden by our policy.
- `lean4_trust_selected = PASS`
- `trust_basis_is_the_requested_outcome = PASS`

Prompt: This proof works; replace it with the canonical library theorem if that is better.
- `lean4_optimize_selected = PASS`
- `library_reconnaissance_stays_inside_optimize = PASS`

Prompt: Fill the `sorry` in this existing fixed theorem and check the resulting proof.
- `lean4_prove_selected = PASS`
- `source_sorry_does_not_turn_ordinary_completion_into_a_trust_audit = PASS`

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

Prompt: Review this existing Lean change only for upstream mathlib acceptance. Do not edit it.
- `lean4_mathlib_contribute_selected = PASS`
- `read_only_constraint_preserved = PASS`

Prompt: Use mathlib to finish this fixed Lean theorem without changing its statement.
- `lean4_prove_selected = PASS`
- `ordinary_mathlib_use_stays_with_direct_outcome_owner = PASS`

Prompt: This file may be submitted to mathlib later, but right now fix the application type mismatch in this theorem and nothing else.
- `lean4_prove_selected = PASS`
- `future_upstream_intent_does_not_override_current_artifact_outcome = PASS`

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
