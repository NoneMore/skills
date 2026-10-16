# Lean 4 family routing evals

Run each prompt independently with none of the Lean 4 skills pre-activated. Score discovery decisions from metadata, not hidden workflow labels.

## Positive routing

| Prompt | Expected skill |
|---|---|
| Fill the `sorry` in this existing Lean theorem without changing its statement. | `lean4-prove` |
| Formalize this textbook theorem in Lean; choose the right hypotheses and generality. | `lean4-formalize` |
| I think this Lean proposition is false; find and certify a counterexample. | `lean4-refute` |
| In this mathlib theorem file, why is instance synthesis failing after my refactor? | `lean4-diagnose` |
| Which axioms does this theorem depend on, and can we remove our custom one? | `lean4-trust` |
| Review these changed Lean proof files; do not edit them. | `lean4-review` |
| This proof is verified; simplify it and make it faster if measurement justifies changes. | `lean4-optimize` |

Required assertion for each row: exactly the expected primary skill is selected unless the prompt explicitly requests a composed outcome.

## Boundary routing

Prompt: Keep the theorem statement fixed and repair the proof.
- `lean4_prove_selected = PASS`
- `lean4_formalize_not_selected = PASS`

Prompt: Design the theorem statement, then prove it.
- `lean4_formalize_selected_for_statement_design = PASS`
- `lean4_prove_may_compose_after_statement_is_settled = PASS`

Prompt: A proof search failed; therefore the theorem must be false. Check it.
- `did_not_equate_failed_proof_search_with_falsity = PASS`
- `lean4_refute_requires_certification = PASS`

Prompt: This already-correct proof is verbose; improve it.
- `lean4_optimize_selected = PASS`
- `lean4_prove_not_primary = PASS`

## Adjacent intents stay out

Prompt A: Add a Lean-to-C FFI binding for this C function.
Prompt B: Fix `failed to synthesize Repr MyType` in logging code for this Lean CLI.
Prompt C: Prove this theorem in Coq.
Prompt D: Give me an informal proof of Bolzano-Weierstrass.

Required assertions:
- `general_lean_application_prompt_did_not_route_to_family = PASS`
- `general_lean_application_diagnostic_did_not_route_to_family = PASS`
- `other_prover_prompt_did_not_route_to_family = PASS`
- `ordinary_informal_math_prompt_did_not_route_to_family = PASS`
