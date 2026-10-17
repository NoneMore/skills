# Behavioral evals — lean4-recon

Run these cases after explicitly activating the user-invoked `lean4-recon` Skill. Score observable context expansion and design findings rather than routing or hidden reasoning labels. Recon should discover materially relevant semantic context without being told the answer in the prompt.

## 1. Local API is challenged against its governing abstraction

Regression motivation: a mathlib review of a topology-specific transfinite construction found that several local declarations were better understood through the generic fixed-point approximant API that implemented them. A task-completion reading strategy could finish the local code without discovering that abstraction boundary.

Fixture: provide a local formal-mathematics API whose central definition is implemented by applying a generic transfinite fixed-point approximant to a domain-specific operator. The file also introduces a local predicate for “the approximant has stabilized” and an aggregate object defined as the infimum of all approximants. Do not provide reviewer comments or name the generic lemmas that resolve the design questions.

Prompt: Before we extend this API further, investigate whether the current definitions and helper concepts are using the right mathlib abstractions. Do not make production edits yet.

Required assertions:
- `followed_local_definition_to_its_generic_owning_abstraction = PASS`
- `inspected_the_generic_api_not_only_application_domain_names = PASS`
- `tested_whether_local_stabilization_predicate_is_a_canonical_existing_notion = PASS`
- `looked_for_a_canonical_characterization_of_the_aggregate_object = PASS`
- `considered_whether_useful_local_lemmas_belong_at_the_generic_layer = PASS`
- `did_not_require_an_alternative_direction_to_be_given_in_advance = PASS`
- `made_no_production_edits = PASS`

Do not require one hard-coded declaration name for PASS. The regression is discovery of the governing abstraction and material API consequences, not memorization of a historical review.

## 2. Recon may confirm the current framing

Fixture: the local definition already uses the canonical library construction directly; nearby generic APIs and natural duals have been inspected, and cheap assumption checks reveal no materially weaker statement or reusable generalization.

Prompt: Challenge this design before we commit to adding more lemmas. Tell me if we are missing a better abstraction.

Required assertions:
- `checked_plausible_semantic_expansion_paths = PASS`
- `did_not_invent_a_reframe_without_material_evidence = PASS`
- `reported_current_framing_as_supported_when_no_better_boundary_was_found = PASS`
- `stopped_without_unbounded_repository_browsing = PASS`

## 3. Assumption boundary is pressure-tested without overstating falsity

Prompt: Before we build more API around this theorem, investigate whether the closedness hypothesis is genuinely structural or just an artifact of the current proof. Examples and counterexamples are useful; I am not asking for a certified disproof yet.

Required assertions:
- `tested_hypothesis_removal_with_concrete_or_structural_evidence = PASS`
- `distinguished_exploratory_counterexample_evidence_from_certified_refutation = PASS`
- `reported_the_assumption_boundary_at_the_strength_supported_by_evidence = PASS`

## 4. Historical constraints are reopened only with new evidence

Prompt: An older implementation was universe-polymorphic but was abandoned because cardinal arguments became awkward. A newer library mechanism may remove that constraint. Investigate whether the old design deserves reconsideration before we commit to the current API.

Required assertions:
- `reconstructed_the_material_reason_the_old_design_was_rejected = PASS`
- `checked_whether_the_rejecting_constraint_still_applies = PASS`
- `did_not_reactivate_history_without_new_evidence = PASS`
- `reported_the_current_design_tradeoff = PASS`

## 5. Recon converges instead of browsing indefinitely

Fixture: semantic expansion finds that a local construction is a direct specialization of a canonical generic API, scratch checks validate the relationship, and retaining the local wrapper would add machinery without a distinct semantic role.

Prompt: What should we do next?

Required assertions:
- `reported_the_material_reframe_and_supporting_evidence = PASS`
- `recommended_the_next_concrete_action = PASS`
- `did_not_continue_expanding_context_after_the_design_decision_converged = PASS`
