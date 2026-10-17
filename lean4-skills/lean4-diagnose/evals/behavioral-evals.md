# Behavioral evals — lean4-diagnose

## Cross-boundary regression is diagnosed from the shared cause

Fixture: after a mathlib/toolchain update, several previously working theorem files fail with a mix of unknown identifiers, changed application signatures, and instance-synthesis errors. The failures share imports from the same upstream area.

Prompt: Determine what changed, identify the common root cause, and give me the smallest migration path before fixing files one by one.

Required assertions:
- `lean4_diagnose_selected = PASS`
- `clustered_failures_before_patching_individual_symptoms = PASS`
- `inspected_shared_import_api_or_toolchain_boundary = PASS`
- `reported_root_cause_and_bounded_migration_path = PASS`

## Build and artifact state are diagnosed at the failing boundary

Fixture: source and built artifacts may be out of sync after an imported module changed.

Prompt: The downstream file still passes `lake env lean`, but the project build disagrees. Find out why and tell me which result is trustworthy.

Required assertions:
- `lean4_diagnose_selected = PASS`
- `distinguished_file_local_check_from_dependency_aware_build_state = PASS`
- `used_or_requested_a_gate_that_exercises_the_changed_dependency_boundary = PASS`
- `reported_what_each_check_actually_establishes = PASS`

## Explicit diagnosis stays bounded to the requested explanation

Prompt: Do not fix this theorem yet. Explain why this application now has a type mismatch after the dependency update and identify the changed API boundary.

Required assertions:
- `lean4_diagnose_selected = PASS`
- `identified_the_material_cause_or_boundary = PASS`
- `did_not_turn_explanation_into_unrequested_artifact_repair = PASS`

## Adjacent application diagnostic stays out

Prompt: Fix `failed to synthesize Repr MyType` in the logging code of this Lean CLI application.

Required assertions:
- `lean4_diagnose_not_selected_for_general_application_debugging = PASS`
