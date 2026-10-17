# Behavioral evals — lean4-review

Cross-cutting verification regressions live in `../../evals/integrity-evals.md`.

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
