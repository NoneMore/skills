# Behavioral evals — lean4-diagnose

## Clustered failures resolve to a shared cause

Fixture: after a mathlib/toolchain update, several theorem files fail with unknown identifiers, changed signatures, and instance errors sharing the same upstream area.

Prompt: Determine what changed, identify the common root cause, and give me the smallest migration path before fixing files one by one.

Required assertions:
- `lean4_diagnose_selected = PASS`
- `clustered_failures_before_patching_symptoms = PASS`
- `inspected_shared_import_api_or_toolchain_boundary = PASS`
- `reported_root_cause_and_bounded_migration_path = PASS`

## Diagnosis stays bounded to explanation when requested

Prompt: Do not fix this theorem yet. Explain why this application now has a type mismatch after the dependency update and identify the changed API boundary.

Required assertions:
- `lean4_diagnose_selected = PASS`
- `identified_material_cause_or_boundary = PASS`
- `did_not_turn_explanation_into_unrequested_repair = PASS`

## Adjacent application diagnostic stays out

Prompt: Fix `failed to synthesize Repr MyType` in the logging code of this Lean CLI application.

Required assertion:
- `lean4_diagnose_not_selected_for_general_application_debugging = PASS`

Cross-cutting stale-artifact verification is exercised once in `../../evals/integrity-evals.md`.
