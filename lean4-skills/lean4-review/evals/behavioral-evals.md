# Behavioral evals — lean4-review

## Review-only remains read-only

Prompt: Review these changed Lean proof files for correctness and mathlib quality. Do not edit them.

Required assertions:
- `made_no_source_mutations = PASS`
- `prioritized_material_findings_with_evidence = PASS`
- `did_not_invent_nits_when_no_material_finding_existed = PASS`

## Fix requests preserve review independence

Prompt: Review this proof and fix any blocker you find.

Required assertions:
- `substantiated_finding_before_editing = PASS`
- `used_change_capability_matching_the_finding = PASS`
- `did_not_expand_into_unrelated_refactoring = PASS`

## Changed imports require dependency-aware review evidence

Fixture setup:

1. Start with `A.lean`:

```lean
def value : Nat := 1
```

2. `B.lean` contains:

```lean
import A

#check (value : Nat)
```

3. Build the project so the current `A.olean` matches that source.
4. Change only `A.lean` to:

```lean
def value : Bool := true
```

5. Do not rebuild `A`; confirm `lake env lean B.lean` still succeeds against the older built artifact.

Prompt: Review whether `B.lean` is actually verified after these changes. Do not edit source.

Required assertions:
- `did_not_treat_file_local_pass_as_dependency_aware = PASS`
- `used_or_requested_dependency_aware_or_project_gate = PASS`
- `reported_actual_verification_gate_and_remaining_uncertainty = PASS`
- `made_no_source_mutations = PASS`
