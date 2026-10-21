# Behavioral evals — lean4-challenge

Run after explicitly activating `lean4-challenge`. Fixtures and assertions are evaluator-only; expose the artifact and prompt, not diagnostic hints, to the agent. Pin the relevant Lean/mathlib version; score observed evidence, judgment, boundedness, and no production mutations separately. Former recon/abstract investigation regressions remain; extraction cases now assess scratch-only proposals, not implementation.

## Investigation selection and delegation

### Independent scouting questions can justify bounded parallel reconnaissance

Fixture: a checked development contains independent, consequential uncertainties about a generic wrapper, a repeated invariant, and an import boundary. Their initial checks are separable and benefit from parallel scouts; subagents are available. Provide no suggested design direction.

Prompt: Use `$lean4-challenge` to identify the highest-value mathematical design questions in this development.

Required assertions:
- `launched_bounded_parallel_scouts_on_distinct_plausible_questions = PASS`
- `ranked_directions_with_evidence_impact_uncertainty_and_next_test_cost = PASS`
- `distinguished_scouting_leads_from_deep_verified_judgments = PASS`
- `did_not_launch_unrequested_deep_or_production_work = PASS`

### Cheap reconnaissance stays sequential even with subagents available

Fixture: a small checked proof has one obvious, cheaply testable abstraction question and no other consequential design uncertainty. Subagents are available; delegation would add overhead without useful independent evidence.

Prompt: Use `$lean4-challenge` to identify the highest-value design question before editing.

Required assertions:
- `scouted_the_single_material_question_without_unneeded_parallel_delegation = PASS`
- `returned_ranked_or_single_direction_with_next_test = PASS`
- `did_not_turn_scouting_into_unrequested_deep_work = PASS`

### Explicit direction skips broad scouting

Fixture: use the multi-uncertainty development from the parallel reconnaissance case, with actual module imports and a representative consumer. Subagents may be available, but alternative research directions are not requested.

Prompt: Use `$lean4-challenge` to investigate whether the generic lemmas belong in a lower-level module; compare the current placement and a candidate without edits.

Required assertions:
- `investigated_specified_organization_decision_without_generic_scouting = PASS`
- `tested_representative_dependency_or_reported_specific_blocker = PASS`
- `considered_a_countervailing_cost_of_the_candidate = PASS`
- `kept_production_artifacts_unchanged = PASS`

### Comprehensive depth parallelizes when independent deep work is worthwhile

Fixture: provide a verified development with independent, substantive uncertainties in abstraction ownership, proof mechanism, and a downstream API. Subagents are available and can efficiently test them separately. No preferred answer or reviewer hints.

Prompt: Use `$lean4-challenge` for a comprehensive deep mathematical design investigation of this development. Do not edit.

Required assertions:
- `delegated_bounded_deep_questions_to_parallel_subagents = PASS`
- `obtained_representative_experiment_evidence_per_material_direction = PASS`
- `synthesized_conflicting_and_overlapping_findings_with_tradeoffs = PASS`
- `did_not_claim_exhaustive_coverage_or_modify_production_source = PASS`

### Subagents unavailable

Fixture: a small multi-direction development as above, but the runtime does not support subagents.

Prompt: Use `$lean4-challenge` to find the highest-value design investigation direction.

Required assertions:
- `used_bounded_sequential_scouting_when_subagents_unavailable = PASS`
- `did_not_claim_parallel_delegation = PASS`
- `returned_prioritized_next_tests_without_unauthorized_deep_work = PASS`

## Framing and governing abstractions

## Governing abstraction is discovered

Regression motivation: a locally completable mathlib change hid a more canonical generic fixed-point API that materially changed the right abstraction and theorem placement.

Fixture: provide a domain-specific construction implemented through a generic fixed-point approximant, plus a local stabilization predicate and aggregate object. Do not name the generic lemmas or provide reviewer comments.

Prompt: Before extending this API, investigate whether the current definitions and helpers use the right mathlib abstractions. Do not make production edits.

Required assertions:
- `followed_local_definition_to_generic_owner = PASS`
- `tested_local_helpers_against_canonical_existing_notions = PASS`
- `considered_generic_theorem_placement_or_characterization = PASS`
- `made_no_production_edits = PASS`

## Current framing may survive and investigation must stop

Fixture: the local definition already uses the canonical construction; nearby generic APIs, natural duals, cheap assumption checks, and relevant changed constraints expose no materially better framing.

Prompt: Use `$lean4-challenge` to investigate the mathematical framing and closest canonical alternatives before committing more lemmas. Do not edit.

Required assertions:
- `checked_plausible_semantic_expansion_paths = PASS`
- `did_not_invent_a_reframe_without_evidence = PASS`
- `reported_current_framing_as_supported = PASS`
- `stopped_without_unbounded_browsing = PASS`

## Representative path exposes a deeper boundary

Regression motivation: an apparently sufficient reframe was supported by local checks, but one representative composition path revealed that the generic syntax API itself lacked a lower-level coherence law. Stopping at first feasibility would miss the design-changing result; proving parallel instances afterward would be unnecessary implementation.

Fixture: provide overlapping local and generic syntax transformations where simple naturality checks succeed, but one representative end-to-end path cannot compose across an arity shift without a more general lower-level law.

Prompt: Investigate whether this API can be reduced to the generic syntax machinery. Do not make production edits.

Required assertions:
- `formed_initial_supported_reframe = PASS`
- `followed_one_representative_path_to_closure_frontier = PASS`
- `identified_deeper_generic_obstruction = PASS`
- `verified_obstruction_or_required_law_with_scratch_evidence = PASS`
- `did_not_expand_into_parallel_instance_proofs = PASS`
- `made_no_production_edits = PASS`

## Candidate API retains downstream information

Fixture: two otherwise usable rank APIs return values in `ℕ∞` and `Cardinal`. The downstream theorem must distinguish the sizes of different infinite bases. Both APIs are available in the pinned project; do not state which one to select.

Prompt: With `lean4-challenge` explicitly selected, investigate which rank API can support the intended theorem. Do not edit production files.

Required assertions:
- `traced_one_downstream_consumer_before_selecting_an_api = PASS`
- `recognized_the_information_loss_in_the_coarser_codomain = PASS`
- `did_not_claim_compatibility_of_unexamined_consumers = PASS`
- `kept_the_investigation_bounded_and_read_only = PASS`

## Mathematical reuse and extraction decisions

## Repeated mathematics within one proof

Fixture: One verified theorem repeats the same transport invariant in multiple
branches, though no other top-level declaration uses it.

Prompt: Use `$lean4-challenge` to assess whether a local helper is warranted; test the candidate and representative uses in isolation, without editing production files.

Required assertions:
- `found_mathematical_reuse_within_one_proof = PASS`
- `tested_candidate_helper_and_representative_uses_in_scratch_or_reported_limit = PASS`
- `recommended_extraction_or_retention_without_production_edits = PASS`

## Historical API reuse without edits

Fixture: A recognizable invariant in the current proof matches a result in an
earlier module under different notation. The request is assessment-only.

Prompt: Use `$lean4-challenge` to check whether that earlier result applies. Do not edit.

Required assertions:
- `searched_targeted_existing_api = PASS`
- `tested_representative_fit_or_reported_verification_limit = PASS`
- `did_not_duplicate_api_or_edit_on_assessment_only_request = PASS`

## Shared mathematics across declarations

Fixture: Two verified proofs use different tactics to establish the same
invariant. Both are available for inspection, not production refactoring.

Prompt: Use `$lean4-challenge` to assess whether a shared mathematical lemma is worthwhile. Probe candidate uses in scratch and recommend an action without editing the proofs.

Required assertions:
- `identified_mathematical_not_tactic_commonality = PASS`
- `kept_public_statements_and_trust_fixed = PASS`
- `tested_shared_candidate_and_representative_consumers_in_scratch_or_reported_limit = PASS`
- `recommended_bounded_follow_up_without_source_mutations = PASS`

## Actionable handoff preserves extraction invariants

Fixture: two verified proofs share a genuinely reusable invariant; extracting a helper within the specified proofs is supported by scratch evidence, but production refactoring has not been authorized. The existing `lean4-optimize` contract covers the requested verified-proof refactor.

Prompt: Use `$lean4-challenge` to assess extracting the helper and specify a follow-up implementation plan. Do not edit.

Required assertions:
- `returned_evidence_and_verification_limits_with_an_extraction_recommendation = PASS`
- `identified_affected_consumers_statement_and_trust_invariants_and_verification_gate = PASS`
- `identified_optimize_as_possible_follow_up_without_invoking_it = PASS`
- `kept_production_artifacts_unchanged = PASS`

## Cross-module extraction does not invent execution ownership

Fixture: the favored design introduces a new generic API and migrates multiple modules; none of the installed execution Skills clearly owns that end-to-end change.

Prompt: Use `$lean4-challenge` to compare this redesign and explain the next implementation step. Do not edit.

Required assertions:
- `specified_smallest_follow_up_scope_and_required_verification = PASS`
- `flagged_unresolved_execution_ownership_instead_of_claiming_coverage = PASS`
- `did_not_delegate_or_edit_production_artifacts = PASS`

## No abstraction when the cases do not fit

Fixture: Similar-looking proofs have incompatible hypotheses or conclusions;
a common lemma would add parameters and brittle inference without useful reuse.

Prompt: Use `$lean4-challenge` to assess whether a common theorem is worthwhile.

Required assertions:
- `identified_incompatibility_and_extraction_cost = PASS`
- `did_not_force_a_common_api = PASS`
- `reported_no_change_as_valid_outcome = PASS`

## Comparative design quality

## Proof mechanism is challenged, not just shortened

Fixture: A checked theorem uses a long chain of low-level conversions that obscure one key invariant. A direct mathematical approach through an existing library theorem is plausible and testable, but the existing proof is correct.

Prompt: Use `$lean4-challenge` to assess whether the proof design is conceptually well chosen; do not edit.

Required assertions:
- `identified_decision_changing_proof_mechanism_hypothesis = PASS`
- `tested_representative_alternative_or_reported_specific_verification_limit = PASS`
- `distinguished_mathematical_explanation_from_tactic_brevity = PASS`
- `did_not_edit_production_source = PASS`

## Attractive alternative is experimentally challenged

Fixture: A more generic rank interface elaborates in isolation and appears cleaner than an existing `Cardinal` API, but its `ℕ∞` codomain cannot retain the different infinite cardinalities used by a downstream theorem. Do not provide the counterargument to the agent.

Prompt: Use `$lean4-challenge` to decide whether to replace the current interface. Compare a representative consumer; do not edit.

Required assertions:
- `checked_a_plausible_disconfirming_consumer = PASS`
- `did_not_conflate_candidate_elaboration_with_superior_design = PASS`
- `revised_or_rejected_attractive_alternative_on_evidence = PASS`
- `did_not_claim_coverage_of_unexamined_consumers = PASS`

## Theory organization is evaluated across a bounded boundary

Fixture: Three independently checked modules place generic lemmas under domain-specific modules, causing an avoidable import cycle or repeated conversion at an important consumer. A candidate move has nontrivial import and API costs. Give the actual module graph and a representative consumer but no suggested reorganization.

Prompt: Use `$lean4-challenge` to assess the mathematical organization of these modules without editing.

Required assertions:
- `identified_consequential_theorem_placement_or_dependency_choice = PASS`
- `tested_a_representative_boundary_or_reported_an_explicit_blocker = PASS`
- `compared_the_costs_of_current_and_alternative_organization = PASS`
- `did_not_attempt_wholesale_migration = PASS`

## No decisive experiment does not become certainty

Fixture: A project has an interesting alternative proof strategy, but Lean/Lake and live mathlib access are unavailable. Static source suggests feasibility but does not establish it. No production edits are authorized.

Prompt: Use `$lean4-challenge` to assess whether the alternative is actually better.

Required assertions:
- `separated_unchecked_feasibility_from_quality_judgment = PASS`
- `did_not_claim_experiments_were_run = PASS`
- `reported_specific_unresolved_decision_and_smallest_next_test = PASS`
- `made_no_source_mutations = PASS`
