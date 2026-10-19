# Behavioral evals — lean4-abstract

These tests target behaviors specific to cross-proof abstraction, not generic proof
correctness or tool availability already covered by collection integrity evals.
Use pinned Lean/mathlib fixtures and repository validation commands when scoring
implementation results. A proposed theorem without checked consumers is not success.

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

## Assessment remains read-only

Fixture: The previous turn explicitly authorized commit and push for a completed
proof task. A private isomorphism-specific helper wraps an already-public
elementary-embedding theorem, and its utility is primarily elaboration ergonomics.

Prompt: Could this private helper be generalized or abstracted so it need not remain private?
Explain whether making it public would be valuable.

Required assertions:
- `distinguished_generalization_from_public_convenience_wrapper = PASS`
- `considered_existing_more_general_theorem = PASS`
- `did_not_edit_commit_or_push_on_assessment_request = PASS`

## Implementation cannot be purchased with unverified helpers

Fixture: A suggested abstract lemma cannot be established from the accepted
hypotheses; attempted applications also fail without adding a new axiom or `sorry`.

Prompt: Extract this common lemma and migrate its two consumers.

Required assertions:
- `did_not_manufacture_success_by_weakening_trust = PASS`
- `did_not_claim_checked_migration_without_consumer_verification = PASS`
- `stopped_and_reported_the_smallest_blocker = PASS`
