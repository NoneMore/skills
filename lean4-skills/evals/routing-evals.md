# Lean 4 collection discovery evals

Run each prompt independently with all nine Lean 4 Skills installed and none pre-activated. `lean4-recon` and `lean4-mathlib-contribute` are user-invoked (`disable-model-invocation: true`) and are therefore not scored by model-discovery evals.

Discovery principle: optimize for reliable loading of materially useful guidance, not mutually exclusive classification. For each positive case, the expected Skill must be selected. Selecting an additional compatible model-discoverable Skill is not a failure unless the extra activation changes behavior in a way that conflicts with the request or its completion contract.

## Positive discovery

| Prompt | Required discovered skill |
|---|---|
| Formalize this textbook theorem in Lean; choose the right hypotheses and generality. | `lean4-formalize` |
| Fill the `sorry` in this existing Lean theorem without changing its statement. | `lean4-prove` |
| I think this Lean proposition is false; find and certify a counterexample. | `lean4-refute` |
| After updating mathlib, several theorem files fail around the same imports with changed identifiers and signatures. Determine the common cause and migration path. | `lean4-diagnose` |
| Which axioms does this theorem depend on, and can we remove our custom one? | `lean4-trust` |
| Review these changed Lean proof files; do not edit them. | `lean4-review` |
| This proof is verified; simplify it and make it faster if measurement justifies changes. | `lean4-optimize` |

Required assertion for each row: the named Skill is discovered and its materially relevant contract is followed. Do not require other compatible Skills to remain unselected.

## Compatible overlap must not derail the request

Prompt: This existing theorem no longer elaborates with an application type mismatch. Find the cause and fix the proof without changing its statement.
- `lean4_prove_selected = PASS`
- `fixed_statement_preserved = PASS`
- `diagnostic_work_did_not_prevent_proof_repair = PASS`

Prompt: Audit this theorem's trust basis and remove our custom axiom if possible without changing the theorem statement.
- `lean4_trust_selected = PASS`
- `trust_basis_was_checked_against_the_requested_policy = PASS`
- `any_auxiliary_proof_work_preserved_the_trust_cleanup_outcome = PASS`

Prompt: Review this working proof for brittleness and maintainability. Do not edit it.
- `lean4_review_selected = PASS`
- `review_only_constraint_preserved = PASS`
- `additional_compatible_guidance_did_not_trigger_source_mutation = PASS`

## User-invoked modes are not model-discovery requirements

Do not require model discovery to select `lean4-recon` or `lean4-mathlib-contribute`. Their behavioral evals run after explicit activation and test the broader context-loading or upstream-readiness contract directly.

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
