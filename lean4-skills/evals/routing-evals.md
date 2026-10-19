# Lean 4 collection discovery evals

Run automatic-discovery prompts independently with all nine Lean 4 Skills installed and none pre-activated. Only six are model-discoverable; `lean4-abstract`, `lean4-recon`, and `lean4-mathlib-contribute` are user-invoked and must not be model-activated. Explicit-invocation tests below start with the named mode selected by the user.

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

## Statement design, local cleanup, and opt-in reuse

Prompt: This verified Lean proof is too verbose; simplify the local tactic argument.
- `lean4_optimize_selected = PASS`
- `did_not_route_local_cleanup_to_reuse_discovery = PASS`

Prompt: The private isomorphism helper appears to wrap an existing more general elementary-embedding result. Is it worth publishing? Do not edit code.
- `lean4_formalize_selected = PASS`
- `assessed_statement_generality_and_public_api_value = PASS`
- `analysis_only_remained_read_only = PASS`

Prompt: Several verified theorems use different tactics but encode a shared invariant. Find a useful common lemma and migrate the proofs. No Skill is explicitly selected.
- `did_not_auto_activate_user_invoked_abstract = PASS`
- `handled_request_with_available_capabilities_or_offered_explicit_mode = PASS`
- `model_discoverable_lean_skill_count_lte_2 = PASS`

Prompt: These three unrelated verified proofs just need shorter local tactic scripts; no shared mathematical argument is suspected.
- `lean4_optimize_selected = PASS`
- `did_not_auto_activate_user_invoked_abstract = PASS`
- `model_discoverable_lean_skill_count_lte_2 = PASS`

Prompt: Fill the hole in this single theorem. No repeated construction or reuse clue is present.
- `lean4_prove_selected = PASS`
- `did_not_auto_activate_user_invoked_abstract = PASS`
- `model_discoverable_lean_skill_count_lte_2 = PASS`

Prompt: This proof step feels familiar from a previous module; look for a useful lemma to finish the current target. No Skill is explicitly selected.
- `bounded_existing_api_search_remained_available = PASS`
- `did_not_auto_activate_user_invoked_abstract_or_recon = PASS`
- `did_not_migrate_historical_consumers_without_authorization = PASS`

## Explicit invocation boundaries (not model discovery)

Prompt: Use `$lean4-abstract` to assess whether the repeated transport invariant in this long proof can be reused. Do not edit.
- `abstract_loaded_from_explicit_user_selection = PASS`
- `bounded_reuse_investigation_not_open_ended_recon = PASS`
- `assessment_remained_read_only = PASS`

Prompt: Use `$lean4-abstract` to compare this theorem with a plausible result in an earlier module and validate the match; do not edit.
- `abstract_loaded_from_explicit_user_selection = PASS`
- `targeted_historical_search_and_representative_check = PASS`
- `did_not_silently_expand_into_recon = PASS`

Prompt: Use `$lean4-recon` to question whether the current domain-specific constructions use the right generic mathematical abstraction; repeated lemmas may be a symptom. Do not edit.
- `recon_loaded_from_explicit_user_selection = PASS`
- `investigated_framing_instead_of_forcing_local_extraction = PASS`
- `did_not_silently_switch_to_abstract = PASS`

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
