# Behavioral evals — lean4-abstract

Run with `$lean4-abstract` explicitly selected. Pin Lean/mathlib fixtures and
score checked outcomes, not proposed lemmas.

## Repeated mathematics within one proof

Fixture: One verified theorem repeats the same transport invariant in multiple
branches, though no other top-level declaration uses it.

Prompt: Use `$lean4-abstract` to extract a useful local helper and verify its uses.

Required assertions:
- `found_mathematical_reuse_within_one_proof = PASS`
- `verified_helper_and_representative_uses = PASS`
- `preserved_statement_and_authorized_edit_scope = PASS`

## Historical API reuse without edits

Fixture: A recognizable invariant in the current proof matches a result in an
earlier module under different notation. The request is assessment-only.

Prompt: Use `$lean4-abstract` to check whether that earlier result applies. Do not edit.

Required assertions:
- `searched_targeted_existing_api = PASS`
- `tested_representative_fit_or_reported_verification_limit = PASS`
- `did_not_duplicate_api_or_edit_on_assessment_only_request = PASS`

## Shared mathematics across declarations

Fixture: Two verified proofs use different tactics to establish the same
invariant. Both are authorized for refactoring.

Prompt: Use `$lean4-abstract` to extract shared mathematics if worthwhile.

Required assertions:
- `identified_mathematical_not_tactic_commonality = PASS`
- `kept_public_statements_and_trust_fixed = PASS`
- `verified_shared_result_and_affected_consumers = PASS`

## No abstraction when the cases do not fit

Fixture: Similar-looking proofs have incompatible hypotheses or conclusions;
a common lemma would add parameters and brittle inference without useful reuse.

Prompt: Use `$lean4-abstract` to assess whether a common theorem is worthwhile.

Required assertions:
- `identified_incompatibility_and_extraction_cost = PASS`
- `did_not_force_a_common_api = PASS`
- `reported_no_change_as_valid_outcome = PASS`
