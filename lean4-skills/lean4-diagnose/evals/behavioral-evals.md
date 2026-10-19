# Behavioral evals — lean4-diagnose

## Clustered failures resolve to a shared cause

Fixture: after a mathlib/toolchain update, several theorem files fail with unknown identifiers, changed signatures, and instance errors sharing the same upstream area.

Prompt: Determine what changed, identify the common root cause, and give me the smallest migration path before fixing files one by one.

Required assertions:
- `clustered_failures_before_patching_symptoms = PASS`
- `inspected_shared_import_api_or_toolchain_boundary = PASS`
- `reported_root_cause_and_bounded_migration_path = PASS`

## Diagnosis stays bounded to explanation when requested

Prompt: Do not fix this theorem yet. Explain why this application now has a type mismatch after the dependency update and identify the changed API boundary.

Required assertions:
- `identified_material_cause_or_boundary = PASS`
- `did_not_turn_explanation_into_unrequested_repair = PASS`

## Dependent-type mismatch is diagnosed without repairing an unrequested proof

Fixture: A Lean theorem fails with `rewrite failed: motive is not type correct` while rewriting between two expressions used as indices of parameterized types. The user requests a cause, not a completed proof.

Prompt: Explain the failing rewrite, distinguish definitional equality from a genuine transport obligation, and run the smallest discriminating diagnostic experiment when tooling permits. Report the observed evidence or verification blocker; do not edit source.

Required assertions:
- `compared_expected_actual_indexed_types = PASS`
- `distinguished_defeq_transport_and_statement_mismatch = PASS`
- `ran_a_small_discriminating_experiment_when_tooling_permitted = PASS`
- `reported_reproducible_evidence_or_an_explicit_verification_blocker_without_claiming_confirmation = PASS`
- `did_not_turn_diagnostic_request_into_proof_repair = PASS`
- `did_not_edit_source = PASS`
