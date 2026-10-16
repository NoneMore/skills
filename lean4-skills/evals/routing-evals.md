# Lean 4 collection routing evals

Run each prompt independently with none of the Lean 4 skills pre-activated. Score discovery decisions from metadata, not hidden workflow labels.

Routing principle: choose the primary skill by the requested outcome, not by incidental mechanisms. Search, theorem lookup, API inspection, small experiments, and explanatory substeps stay with the capability that already owns the task. Select `lean4-explore` only when choosing among plausible formal directions is a distinct requested outcome. A standalone plain explanation with neither an evaluation request nor an open design decision need not select any specialized Lean 4 skill.

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

## Explore boundaries

Prompt: Prove in Lean that every finite subgroup of a torsion-free group is trivial. No Lean declaration exists yet.
- `lean4_formalize_primary_for_statement_design = PASS`
- `lean4_prove_may_compose_after_declaration_is_settled = PASS`
- `lean4_explore_not_selected_merely_because_library_search_is_useful = PASS`

Prompt: Before formalizing this construction, investigate whether it is really an instance of a generic fixed-point API, whether a dual theorem should exist, and whether any hypotheses can be dropped.
- `lean4_explore_selected = PASS`
- `exploration_may_branch_across_abstraction_duality_and_assumption_tests = PASS`
- `no_durable_statement_or_proof_change_required = PASS`

Prompt: Find the exact mathlib declaration for this fact, compare the nearby alternatives, and explain which abstraction is canonical in this project. Do not change code.
- `lean4_explore_selected = PASS`
- `answer_grounded_in_actual_project_or_mathlib_evidence = PASS`

Prompt: Find a suitable existing lemma and use it to finish this existing proof goal.
- `lean4_prove_primary = PASS`
- `ordinary_goal_directed_search_did_not_route_to_explore = PASS`
- `lean4_explore_may_compose_only_if_reconnaissance_becomes_a_distinct_subproblem = PASS`

Prompt: Why does this existing `simpa [foo]` proof work?
- `no_specialized_lean4_skill_required = PASS`
- `lean4_explore_not_selected_without_open_design_decision = PASS`
- `lean4_review_not_selected_without_evaluation_request = PASS`
- `lean4_optimize_not_selected_without_change_request = PASS`

Prompt: Is this working `simpa [foo]` proof brittle or inappropriate for mathlib?
- `lean4_review_selected = PASS`
- `lean4_explore_not_primary = PASS`

Prompt: This proof works; replace it with the canonical library theorem if that is better.
- `lean4_optimize_selected = PASS`
- `lean4_explore_may_support_reconnaissance_but_does_not_own_the_durable_change = PASS`

## Other outcome boundaries

Prompt: Keep the existing Lean theorem statement fixed and repair the proof.
- `lean4_prove_selected = PASS`
- `lean4_formalize_not_selected = PASS`

Prompt: This existing theorem no longer elaborates: application type mismatch at line 43. Fix it.
- `lean4_diagnose_primary_for_current_diagnostic = PASS`
- `lean4_prove_may_compose_only_after_diagnosis_reduces_to_an_ordinary_proof_obligation = PASS`

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
