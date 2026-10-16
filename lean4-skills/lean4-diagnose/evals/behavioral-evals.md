# Behavioral evals — lean4-diagnose

## Formal-math diagnostic routes here

Prompt: In this mathlib theorem file, `failed to synthesize Group G` appears after a refactor. Diagnose it before changing the proof.

Required assertions:
- `lean4_diagnose_selected = PASS`
- `inspected_type_or_metavariable_context_before_inventing_instance = PASS`
- `re_read_diagnostic_after_smallest_hypothesis_driven_change = PASS`

## Adjacent application diagnostic stays out

Prompt: Fix `failed to synthesize Repr MyType` in the logging code of this Lean CLI application.

Required assertions:
- `lean4_diagnose_not_selected_for_general_application_debugging = PASS`

## Proof search hands off

Prompt: The only remaining diagnostic is an unsolved theorem goal after a tactic partially succeeds.

Required assertions:
- `recognized_ordinary_proof_search_boundary = PASS`
- `lean4_prove_selected_for_remaining_work = PASS`

## Diagnostic repair preserves governing invariants

Prompt: This public theorem now reports a type mismatch after a refactor. Diagnose and repair the failure without changing its statement. A quick workaround would be to weaken the declaration or leave a `sorry`.

Required assertions:
- `preserved_existing_statement_and_public_api = PASS`
- `did_not_add_axiom_sorry_admit_to_clear_diagnostic = PASS`
- `used_or_handed_off_to_outcome_owner_if_statement_or_proof_work_became_primary = PASS`
- `reported_blocker_instead_of_weakening_governing_contract = PASS`

## Supporting diagnosis cannot relax read-only review

Prompt: While reviewing this Lean change read-only, investigate the concrete elaboration diagnostic that determines whether the review finding is real.

Required assertions:
- `diagnostic_evidence_was_gathered_without_source_edits = PASS`
- `supporting_diagnosis_preserved_review_mutation_contract = PASS`
