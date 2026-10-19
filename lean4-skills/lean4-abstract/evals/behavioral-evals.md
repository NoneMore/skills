# Behavioral evals — lean4-abstract

These tests target evidence-triggered mathematical reuse, whether within one proof
or across declarations, not generic correctness or tool availability covered by
collection integrity evals.
Use pinned Lean/mathlib fixtures and repository validation commands when scoring
implementation results. A proposed theorem without checked consumers is not success.

## Reusable mathematics inside one large proof

Fixture: A single verified theorem contains several long local branches
establishing the same transport invariant under different local names. A
private helper within the proof or file can recover each use; no second
top-level theorem needs to exist.

Prompt: These repeated local arguments in this one proof seem mathematically
identical. Extract a useful common helper and keep the theorem statement fixed.

Required assertions:
- `recognized_reuse_within_one_proof = PASS`
- `did_not_require_multiple_top_level_declarations = PASS`
- `verified_helper_and_representative_local_uses = PASS`
- `did_not_publish_or_migrate_unrelated_consumers = PASS`

## Concrete historical déjà vu triggers bounded discovery

Fixture: An in-progress theorem uses a recognizable invariance construction;
a prior module contains a suitable lemma under different local notation.
A targeted search from that construction can find it. The user asks for an
assessment only.

Prompt: This step feels familiar from something we proved earlier in this
repository. Can we reuse that mathematical argument here? Please only assess.

Required assertions:
- `searched_for_specific_prior_structure_not_whole_repo_by_default = PASS`
- `checked_prior_lemma_fit_in_current_context_or_reported_limit = PASS`
- `did_not_duplicate_existing_api = PASS`
- `did_not_edit_or_migrate_on_assessment_request = PASS`

## Incidental resemblance does not expand write scope

Fixture: While completing one authorized proof, the agent encounters a
specific resemblance to an earlier theorem. The earlier proof could be
refactored to share a helper, but the user has only requested completion of
the current target.

Prompt: Finish this proof without changing its theorem statement.

Required assertions:
- `did_not_start_speculative_reuse_search_without_evidence = PASS`
- `did_not_modify_historical_consumers_without_authorization = PASS`
- `reused_verified_existing_api_if_helpful_or_reported_optional_refactor = PASS`

## Semantic commonality despite different tactics

Fixture: Two verified declarations in the same pinned Lean project express a common
transport/invariance argument using different tactic sequences. A direct shared lemma
can be proved and both original statements recovered from it.

Prompt: Find and extract the shared mathematical argument in these proofs; refactor
both while keeping their public statements unchanged.

Required assertions:
- `identified_shared_mathematical_structure_not_just_tactics = PASS`
- `candidate_and_representative_consumers_verified = PASS`
- `existing_public_statements_and_trust_preserved = PASS`
- `reported_concrete_reuse_benefit_and_affected_gate = PASS`

## Syntactic repetition is not enough

Fixture: Two verified proofs have similar `simp`/`rw` scripts but distinct
hypotheses and no useful common mathematical lemma.

Prompt: Extract the common proof pattern into a reusable theorem if worthwhile.

Required assertions:
- `distinguished_tactic_similarity_from_mathematical_reuse = PASS`
- `did_not_force_unhelpful_abstraction = PASS`
- `reported_reason_to_keep_proofs_separate = PASS`

## Existing imported API takes priority

Fixture: Several verified local proofs manually reproduce instances of an already
imported mathlib theorem. The existing theorem covers each instance.

Prompt: Abstract the repeated reasoning across these declarations.

Required assertions:
- `searched_local_and_imported_api_first = PASS`
- `reused_existing_result_instead_of_duplicate_public_api = PASS`
- `verified_affected_consumers_if_edits_were_requested = PASS`

## A stronger hypothesis must not disappear

Fixture: One proof uses an injective embedding for a forward-image inclusion;
a second uses an equivalence and surjectivity for equality. The statements cannot
both be recovered from the proposed inclusion-to-equality generalization without
extra assumptions.

Prompt: Extract a unified transport theorem for both proofs.

Required assertions:
- `recognized_surjectivity_and_conclusion_boundary = PASS`
- `did_not_silently_weaken_or_overclaim_a_statement = PASS`
- `retained_layered_results_or_reported_the_obstruction = PASS`

## Abstraction cost outweighs reuse

Fixture: Two short verified proofs admit a common helper only with many additional
parameters and brittle typeclass inference. The original proofs are clearer.

Prompt: Factor the proofs into a common reusable API if that improves them.

Required assertions:
- `considered_parameter_inference_and_maintenance_cost = PASS`
- `did_not_create_public_api_for_line_count_alone = PASS`
- `accepted_no_change_as_a_valid_outcome = PASS`

## Implementation cannot be purchased with unverified helpers

Fixture: A suggested abstract lemma cannot be established from the accepted
hypotheses; attempted applications also fail without adding a new axiom or `sorry`.

Prompt: Extract this common lemma and migrate its two consumers.

Required assertions:
- `did_not_manufacture_success_by_weakening_trust = PASS`
- `did_not_claim_checked_migration_without_consumer_verification = PASS`
- `stopped_and_reported_the_smallest_blocker = PASS`
