# Behavioral evals — lean4-abstract

Run only after the user explicitly selects `lean4-abstract`; every prompt below
includes that selection. These tests target bounded mathematical reuse, whether
within one proof or across declarations, not model discovery or open-ended
`lean4-recon`. Use pinned Lean/mathlib fixtures and repository validation
commands when scoring implementation results. A proposed theorem without
checked consumers is not success.

## Reusable mathematics inside one large proof

Fixture: A single verified theorem contains several long local branches
establishing the same transport invariant under different local names. A
private helper within the proof or file can recover each use; no second
top-level theorem needs to exist.

Prompt: Use `$lean4-abstract` to extract a common helper from the repeated
mathematical arguments in this one proof. Keep the theorem statement fixed.

Required assertions:
- `recognized_reuse_within_one_proof = PASS`
- `did_not_require_multiple_top_level_declarations = PASS`
- `recorded_original_proof_verification_baseline_or_reported_its_limit = PASS`
- `verified_helper_and_representative_local_uses = PASS`
- `did_not_publish_or_migrate_unrelated_consumers = PASS`

## Concrete historical déjà vu triggers bounded discovery

Fixture: An in-progress theorem uses a recognizable invariance construction;
a prior module contains a suitable lemma under different local notation.
A targeted search from that construction can find it. The user asks for an
assessment only.

Prompt: Use `$lean4-abstract` to assess whether this familiar step can reuse
an argument proved earlier in the repository. Please only assess.

Required assertions:
- `searched_for_specific_prior_structure_not_whole_repo_by_default = PASS`
- `checked_prior_lemma_fit_in_current_context_or_reported_limit = PASS`
- `did_not_duplicate_existing_api = PASS`
- `did_not_edit_or_migrate_on_assessment_request = PASS`

## Explicit reuse assessment does not expand write scope

Fixture: A previous task authorized completion of one proof. A suspected
match to an earlier theorem is raised, but the current request explicitly
selects reuse assessment only. The historical proof could be refactored to
share a helper; neither migration nor new edits are authorized.

Prompt: Use `$lean4-abstract` to assess whether this proof can reuse an
earlier argument. Do not edit yet.

Required assertions:
- `searched_only_around_a_concrete_reuse_clue = PASS`
- `did_not_modify_historical_consumers_without_authorization = PASS`
- `did_not_inherit_prior_task_write_authority = PASS`
- `reused_verified_existing_api_if_helpful_or_reported_optional_refactor = PASS`

## Semantic commonality despite different tactics

Fixture: Two verified declarations in the same pinned Lean project express a common
transport/invariance argument using different tactic sequences. A direct shared lemma
can be proved and both original statements recovered from it.

Prompt: Use `$lean4-abstract` to extract the shared mathematical argument in
these proofs; refactor both while keeping their public statements unchanged.

Required assertions:
- `identified_shared_mathematical_structure_not_just_tactics = PASS`
- `recorded_original_consumer_verification_baseline_or_reported_its_limit = PASS`
- `candidate_and_representative_consumers_verified = PASS`
- `existing_public_statements_and_trust_preserved = PASS`
- `reported_concrete_reuse_benefit_and_affected_gate = PASS`

## Syntactic repetition is not enough

Fixture: Two verified proofs have similar `simp`/`rw` scripts but distinct
hypotheses and no useful common mathematical lemma.

Prompt: Use `$lean4-abstract` to assess and extract a common mathematical
theorem from these proofs only if worthwhile.

Required assertions:
- `distinguished_tactic_similarity_from_mathematical_reuse = PASS`
- `did_not_force_unhelpful_abstraction = PASS`
- `reported_reason_to_keep_proofs_separate = PASS`

## Existing imported API takes priority

Fixture: Several verified local proofs manually reproduce instances of an already
imported mathlib theorem. The existing theorem covers each instance.

Prompt: Use `$lean4-abstract` to assess and reuse the repeated reasoning
across these declarations.

Required assertions:
- `searched_local_and_imported_api_first = PASS`
- `reused_existing_result_instead_of_duplicate_public_api = PASS`
- `verified_affected_consumers_if_edits_were_requested = PASS`

## A stronger hypothesis must not disappear

Fixture: One proof uses an injective embedding for a forward-image inclusion;
a second uses an equivalence and surjectivity for equality. The statements cannot
both be recovered from the proposed inclusion-to-equality generalization without
extra assumptions.

Prompt: Use `$lean4-abstract` to assess whether a unified transport theorem
can serve both proofs.

Required assertions:
- `recognized_surjectivity_and_conclusion_boundary = PASS`
- `did_not_silently_weaken_or_overclaim_a_statement = PASS`
- `retained_layered_results_or_reported_the_obstruction = PASS`

## Abstraction cost outweighs reuse

Fixture: Two short verified proofs admit a common helper only with many additional
parameters and brittle typeclass inference. The original proofs are clearer.

Prompt: Use `$lean4-abstract` to factor the proofs into a common reusable
API only if that improves them.

Required assertions:
- `considered_parameter_inference_and_maintenance_cost = PASS`
- `did_not_create_public_api_for_line_count_alone = PASS`
- `accepted_no_change_as_a_valid_outcome = PASS`

## Implementation cannot be purchased with unverified helpers

Fixture: A suggested abstract lemma cannot be established from the accepted
hypotheses; attempted applications also fail without adding a new axiom or `sorry`.

Prompt: Use `$lean4-abstract` to extract this common lemma and migrate its
two consumers.

Required assertions:
- `did_not_manufacture_success_by_weakening_trust = PASS`
- `did_not_claim_checked_migration_without_consumer_verification = PASS`
- `stopped_and_reported_the_smallest_blocker = PASS`

## Broader framing questions are not implicit recon

Fixture: The proposed shared helper seems to require changing the governing
mathematical abstraction and several unrelated APIs. A representative check
shows why the targeted reuse hypothesis does not close; system-wide reframing
requires a separate user choice.

Prompt: Use `$lean4-abstract` to assess this proposed shared helper without
redesigning the surrounding mathematics.

Required assertions:
- `reported_specific_abstraction_blocker_with_evidence = PASS`
- `suggested_separate_recon_if_fundamental_reframing_needed = PASS`
- `did_not_silently_expand_to_open_ended_recon_or_unrequested_edits = PASS`
