# Lean 4 collection discovery evals

Run each prompt independently with all nine Lean 4 Skills installed and none pre-activated. `lean4-recon` and `lean4-mathlib-contribute` are user-invoked (`disable-model-invocation: true`) and are not scored by model discovery.

Discovery is recall-oriented but not free: load materially useful guidance without requiring unique ownership, while avoiding blanket activation that defeats the context benefit of the split.

## Positive discovery and activation cost

These are intentionally single-intent prompts.

| Prompt | Required discovered Skill |
|---|---|
| Formalize this textbook theorem in Lean; choose the right hypotheses and generality. | `lean4-formalize` |
| Fill the `sorry` in this existing Lean theorem without changing its statement. | `lean4-prove` |
| I think this Lean proposition is false; find and certify a counterexample. | `lean4-refute` |
| After updating mathlib, several theorem files fail around the same imports with changed identifiers and signatures. Determine the common cause and migration path. | `lean4-diagnose` |
| Which axioms does this theorem depend on, and can we remove our custom one? | `lean4-trust` |
| Review these changed Lean proof files; do not edit them. | `lean4-review` |
| This proof is verified; simplify it and make it faster if measurement justifies changes. | `lean4-optimize` |

For every row:
- the required Skill is discovered;
- its materially relevant contract is followed;
- at most two model-discoverable Lean Skills are activated.

Do not require a particular neighboring Skill to remain unselected. The activation bound exists only to reject degenerate routing such as loading most or all seven Skills for every Lean request.

## Compatible overlap

Prompt: This existing theorem no longer elaborates with an application type mismatch. Find the cause and fix the proof without changing its statement.
- `lean4_prove_selected = PASS`
- `fixed_statement_preserved = PASS`
- `diagnostic_work_did_not_prevent_proof_repair = PASS`
- `model_discoverable_lean_skill_count_lte_2 = PASS`

Prompt: Audit this theorem's trust basis and remove our custom axiom if possible without changing the theorem statement.
- `lean4_trust_selected = PASS`
- `trust_basis_checked_against_requested_policy = PASS`
- `auxiliary_proof_work_preserved_trust_cleanup_outcome = PASS`
- `model_discoverable_lean_skill_count_lte_2 = PASS`

Prompt: Review this working proof for brittleness and maintainability. Do not edit it.
- `lean4_review_selected = PASS`
- `review_only_constraint_preserved = PASS`
- `additional_compatible_guidance_did_not_trigger_source_mutation = PASS`
- `model_discoverable_lean_skill_count_lte_2 = PASS`

## User-invoked modes

Do not require model discovery to select `lean4-recon` or `lean4-mathlib-contribute`. Their behavioral evals run after explicit activation.

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
