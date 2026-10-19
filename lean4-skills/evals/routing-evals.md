# Lean 4 collection discovery evals

Run discovery prompts independently with all nine Lean 4 Skills installed and none pre-activated. Six are model-discoverable; the other three require explicit user selection.

Discovery is recall-oriented but has a context budget: load materially useful guidance without requiring unique ownership or blanket activation.

## Positive discovery and activation cost

| Prompt | Required discovered Skill |
|---|---|
| Formalize this textbook theorem in Lean; choose the right hypotheses and generality. | `lean4-formalize` |
| Could this private Lean theorem be generalized or exposed as a useful public declaration? Assess its statement, without editing. | `lean4-formalize` |
| Fill the `sorry` in this existing Lean theorem without changing its statement. | `lean4-prove` |
| I think this Lean proposition is false; find and certify a counterexample. | `lean4-refute` |
| After updating mathlib, several theorem files fail around the same imports with changed identifiers and signatures. Determine the common cause and migration path. | `lean4-diagnose` |
| Explain why a dependent-index `rw` fails with `motive is not type correct`; do not edit the theorem. | `lean4-diagnose` |
| After upgrading mathlib, several imported modules fail with type and identifier errors. Fix the project and verify the affected dependencies. | `lean4-diagnose` |
| Which axioms does this theorem depend on? Audit its trust basis against our accepted policy. | `lean4-review` |
| Remove our custom axiom from this existing theorem if possible without changing its statement. | `lean4-prove` |
| Review these changed Lean proof files; do not edit them. | `lean4-review` |
| This proof is verified; simplify it and make it faster if measurement justifies changes. | `lean4-optimize` |
| These two verified Lean proofs share an invariant; extract a shared mathematical lemma and refactor both. No Skill is selected. | `lean4-optimize` |

For every discovery row and compatible-overlap case, require the specified Skill(s), relevant contract, and `model_discoverable_lean_skill_count_lte_2 = PASS`. Do not require any compatible neighbor to remain unselected. No user-invoked Skill may be activated by model discovery.

## Compatible overlap

Prompt: This existing theorem no longer elaborates with an application type mismatch. Find the cause and fix the proof without changing its statement.
- `lean4_prove_selected = PASS`
- `fixed_statement_preserved = PASS`
- `diagnostic_work_did_not_prevent_proof_repair = PASS`

Prompt: Audit this theorem's trust basis and remove our custom axiom if possible without changing the theorem statement.
- `lean4_review_selected = PASS`
- `lean4_prove_selected = PASS`
- `trust_basis_checked_against_requested_policy = PASS`
- `trust_cleanup_did_not_require_a_dedicated_trust_skill = PASS`

Prompt: Complete this fixed Lean theorem; an attempted `rw` inside its proof fails with `motive is not type correct`. Diagnose that local mismatch as needed and finish the proof.
- `lean4_prove_selected = PASS`
- `ordinary_elaboration_repair_did_not_require_a_diagnose_handoff = PASS`
- `kept_the_statement_fixed_and_verified_the_proof = PASS`

## Explicit-selection boundary

Fixture: A proof goal resembles a result from an earlier module. All Skill files
are readable, but the user has not selected a user-invoked mode.

Prompt: Complete this fixed theorem, checking whether the earlier result helps.
- `lean4_prove_selected = PASS`
- `bounded_existing_api_search_remained_available = PASS`
- `did_not_read_unselected_lean4_abstract_skill_file = PASS`

Prompt: Use `$lean4-abstract` to assess a repeated invariant in this proof. Do not edit.
- `explicitly_selected_abstract_loaded = PASS`

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
