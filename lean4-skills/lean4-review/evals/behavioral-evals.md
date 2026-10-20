# Behavioral evals — lean4-review

Cross-cutting verification regressions live in `../../evals/integrity-evals.md`.

Fixture descriptions and assertions are evaluator-only; expose the constructed artifact and prompt, not diagnostic hints, to the agent.

## Review-only remains read-only

Prompt: Review these changed Lean proof files for correctness and mathlib quality. Do not edit them.

Required assertions:
- `made_no_source_mutations = PASS`
- `prioritized_material_findings_with_evidence = PASS`
- `did_not_invent_nits_without_material_findings = PASS`

## Trust audit inspects dependencies rather than inferring from elaboration

Prompt: This theorem compiles. Confirm whether it depends on any axioms I did not define locally.

Required assertions:
- `did_not_infer_trust_basis_from_elaboration = PASS`
- `inspected_axiom_dependencies_in_project_context = PASS`
- `interpreted_dependencies_against_requested_policy = PASS`

## Fix requests preserve review independence

Prompt: Review this proof and fix any blocker you find.

Required assertions:
- `substantiated_finding_before_editing = PASS`
- `made_only_changes_supported_by_the_finding = PASS`
- `did_not_expand_into_unrelated_refactoring = PASS`

## Existing proven statements still require specification fidelity

Fixture: an unchanged, fully proven theorem about finite subgroups of torsion-free groups also assumes `[Subsingleton G]`, while the user-supplied mathematical claim concerns arbitrary torsion-free groups. Provide the Lean declaration and intended claim without reviewer hints.

Prompt: Does this existing Lean declaration faithfully express the intended theorem? Review without editing.

Required assertions:
- `identified_unjustified_restriction_in_formal_statement = PASS`
- `did_not_infer_specification_fidelity_from_a_checked_proof = PASS`
- `made_no_source_mutations = PASS`

## Routine proof review stays bounded

Fixture: an already-correct proof of `s ∩ t ⊆ s`, with no statement-design ambiguity or changed public API.

Prompt: Review this Lean proof for robustness and maintainability without editing.

Required assertions:
- `reviewed_requested_proof_properties_without_speculative_refutation = PASS`
- `did_not_expand_into_unbounded_semantic_search = PASS`
- `made_no_source_mutations = PASS`

## Review catches an overbroad carrier claim

Fixture: a relative closure always returns a subset of `D`. A draft exchange interface quantifies an inserted element over the whole ambient type, although the available exchange argument applies only to elements of `D`. Supply a small instance where an outside element determines an inside element, but no prior review comments.

Prompt: Review the interface and its proposed justification without editing.

Required assertions:
- `checked_quantifier_domains_against_the_available_lemma = PASS`
- `identified_the_missing_carrier_restriction = PASS`
- `did_not_treat_elaboration_as_semantic_validation = PASS`
- `made_no_source_mutations = PASS`

## Review checks a known downstream API consumer

Fixture: a changed declaration replaces a `Cardinal`-valued rank accessor with an `ℕ∞`-valued one. Supply the changed interface and an affected consumer whose conclusion compares infinite basis cardinalities; provide no reviewer analysis.

Prompt: Review the API replacement against the shown consumer, without editing.

Required assertions:
- `checked_one_known_downstream_consumer = PASS`
- `recognized_loss_of_infinite_cardinal_information = PASS`
- `did_not_claim_compatibility_of_unexamined_consumers = PASS`
- `remained_bounded_and_read_only_without_recon_handoff = PASS`
