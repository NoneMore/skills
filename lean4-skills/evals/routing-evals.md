# Lean 4 collection routing evals

Run each prompt independently with all eight routable Lean 4 Skills installed and none pre-activated. `lean4-install` may also be installed, but its runtime metadata forbids implicit invocation; it is outside ordinary model routing. Score discovery decisions from metadata, not hidden workflow labels.

Routing principle: choose the primary skill by the requested outcome, not by incidental mechanisms. Search, theorem lookup, API inspection, small experiments, proof-strategy comparison, and explanatory substeps stay with the capability that already owns the task. Select `lean4-explore` only when multiple materially different formal-design directions remain plausible and choosing among them is a distinct requested outcome. Select `lean4-trust` when the trust basis itself is being inspected or changed, not merely because an ordinary proof hole is represented by `sorry`/`admit`. Supporting capabilities must not broaden the primary owner's mutation, trust, scope, or verification contract. A standalone plain explanation with neither an evaluation request nor an open design decision need not select any specialized Lean 4 skill.

Installed repository documentation is project context, not another Skill composition edge. Missing reusable Lean docs must never trigger `lean4-install` implicitly.

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

Required assertion for each row: exactly the expected primary skill is selected unless the prompt explicitly requests a composed outcome.

## Installer boundary

Prompt: This repository has no Lean agent documentation yet. Fill the `sorry` in this theorem and verify it.
- `lean4_prove_selected = PASS`
- `lean4_install_not_selected_for_missing_docs = PASS`
- `no_repository_documentation_written_without_explicit_install_request = PASS`

Prompt: Use `$lean4-install` to install the reusable Lean guidance into this repository's normal docs structure.
- `lean4_install_selected_by_explicit_user_invocation = PASS`
- `no_outcome_skill_selected_unless_separately_requested = PASS`

## Explore boundaries

Prompt: Prove in Lean that every finite subgroup of a torsion-free group is trivial. No Lean declaration exists yet.
- `lean4_formalize_primary_for_statement_design = PASS`
- `lean4_prove_may_compose_after_declaration_is_settled = PASS`
- `lean4_explore_not_selected_merely_because_library_search_is_useful = PASS`

Prompt: Formalize this theorem in Lean using the canonical encoding; choose the best types, hypotheses, and available mathlib API as needed.
- `lean4_formalize_primary_for_requested_declaration = PASS`
- `ordinary_encoding_and_api_choices_stay_inside_formalize = PASS`
- `lean4_explore_not_selected_merely_because_statement_design_requires_comparison = PASS`

Prompt: Before formalizing this construction, investigate whether it is really an instance of a generic fixed-point API, whether a dual theorem should exist, and whether any hypotheses can be dropped. I want a direction recommendation before any declaration is committed.
- `lean4_explore_selected = PASS`
- `exploration_may_branch_across_abstraction_duality_and_assumption_tests = PASS`
- `direction_recommendation_is_a_sufficient_outcome = PASS`
- `no_durable_statement_or_proof_change_required = PASS`

Prompt: Find the exact mathlib declaration for this fact, compare the nearby alternatives, and explain which abstraction is canonical in this project. Do not change code.
- `lean4_explore_selected = PASS`
- `answer_grounded_in_actual_project_or_mathlib_evidence = PASS`

Prompt: Find the exact mathlib declaration for this fact. I only need its name and signature, not a design recommendation.
- `lean4_explore_not_selected_for_lookup_alone = PASS`
- `no_specialized_lean4_skill_required_without_an_owned_outcome = PASS`

Prompt: This theorem statement is fixed. Compare induction, rewriting, a direct order-theoretic argument, and automation if useful, then finish the proof without changing the statement.
- `lean4_prove_primary = PASS`
- `materially_different_proof_strategies_remain_proving_work = PASS`
- `lean4_explore_not_selected_for_strategy_diversity_alone = PASS`

Prompt: Find a suitable existing lemma and use it to finish this existing proof goal.
- `lean4_prove_primary = PASS`
- `ordinary_goal_directed_search_did_not_route_to_explore = PASS`
- `lean4_explore_may_compose_only_if_reconnaissance_becomes_a_distinct_formal_design_subproblem = PASS`

Prompt: Why does this existing `simpa [foo]` proof work?
- `no_specialized_lean4_skill_required = PASS`
- `lean4_explore_not_selected_without_open_design_decision = PASS`
- `lean4_review_not_selected_without_evaluation_request = PASS`
- `lean4_optimize_not_selected_without_change_request = PASS`

Prompt: Is this working `simpa [foo]` proof brittle or inappropriate for mathlib?
- `lean4_review_selected = PASS`
- `lean4_explore_not_primary = PASS`

Prompt: Review this Lean file read-only and tell me whether its local stabilization predicate should instead use the generic fixed-point API.
- `lean4_review_primary_for_requested_evaluation = PASS`
- `lean4_explore_may_support_formal_direction_reconnaissance = PASS`
- `supporting_exploration_does_not_relax_review_read_only_constraint = PASS`

Prompt: This proof works; replace it with the canonical library theorem if that is better.
- `lean4_optimize_selected = PASS`
- `lean4_explore_may_support_reconnaissance_but_does_not_own_the_durable_change = PASS`
- `optimization_verification_contract_remains_governing = PASS`

## Other outcome boundaries

Prompt: Keep the existing Lean theorem statement fixed and repair the proof.
- `lean4_prove_selected = PASS`
- `lean4_formalize_not_selected = PASS`

Prompt: Fill the `sorry` in this existing fixed theorem and check the resulting proof.
- `lean4_prove_selected = PASS`
- `lean4_trust_not_selected_merely_because_source_contains_sorry = PASS`

Prompt: Audit this theorem's trust basis. Tell me whether its remaining `sorry` or any custom axiom contaminates the result, and remove only dependencies forbidden by our policy.
- `lean4_trust_selected = PASS`
- `trust_basis_is_the_requested_outcome = PASS`
- `lean4_prove_may_compose_for_bounded_missing_proofs_without_owning_the_audit = PASS`

Prompt: This existing theorem no longer elaborates: application type mismatch at line 43. Fix it.
- `lean4_diagnose_primary_for_current_diagnostic = PASS`
- `lean4_prove_may_compose_only_after_diagnosis_reduces_to_an_ordinary_proof_obligation = PASS`
- `diagnosis_does_not_silently_change_statement_or_trust_basis = PASS`

Prompt: A proof search failed; therefore the theorem must be false. Check it.
- `did_not_equate_failed_proof_search_with_falsity = PASS`
- `lean4_refute_requires_certification = PASS`

Prompt: I am unsure whether the closedness hypothesis is necessary. Explore examples and counterexamples, but I am not asking for a certified disproof yet.
- `lean4_explore_selected = PASS`
- `counterexample_probing_did_not_force_lean4_refute = PASS`

Prompt: Prove in Lean that the closedness hypothesis is necessary by certifying a counterexample to the version without it.
- `lean4_refute_selected = PASS`

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
