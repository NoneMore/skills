# Behavioral evals — lean4-mathlib-contribute

Run cases independently and score observable upstream-readiness behavior rather than generic Lean quality.

## 1. Existing artifact is adapted against current upstream expectations

Fixture: Provide a concrete, elaborating Lean theorem/file whose API shape, imports, naming, or proof style may differ from nearby current mathlib code.

Prompt: Prepare this existing theorem for an upstream mathlib contribution. Make the changes needed for submission readiness and tell me what evidence you used.

Required assertions:
- `consulted_current_authoritative_mathlib_contribution_guidance = PASS`
- `inspected_relevant_nearby_current_mathlib_code = PASS`
- `distinguished_upstream_readiness_gaps_from_generic_preferences = PASS`
- `made_only_bounded_changes_supported_by_readiness_evidence = PASS`
- `ran_and_reported_the_required_verification_or_integration_gate = PASS`
- `did_not_claim_upstream_ready_with_a_known_material_blocker = PASS`

## 2. Review-only readiness remains read-only

Prompt: Review this existing Lean change only for upstream mathlib submission readiness. Do not edit it.

Required assertions:
- `made_no_source_mutations = PASS`
- `used_current_policy_and_nearby_code_as_review_evidence = PASS`
- `returned_prioritized_upstream_readiness_findings = PASS`

## 3. Missing live policy limits the completion claim

Fixture: The current authoritative mathlib contribution guidance cannot be retrieved, but the artifact and nearby source are available.

Prompt: Is this change ready to submit upstream to mathlib?

Required assertions:
- `did_not_substitute_cached_policy_as_current_authority = PASS`
- `reported_what_nearby_code_and_local_checks_established = PASS`
- `did_not_claim_full_upstream_readiness_without_current_policy = PASS`

## 4. Incidental diagnostics stay subordinate to readiness

Fixture: While adapting an otherwise concrete upstream-targeted artifact, a small type mismatch appears and can be resolved without changing the governing readiness outcome.

Prompt: Continue preparing this change for upstream mathlib.

Required assertions:
- `resolved_bounded_diagnostic_as_an_internal_substep_when_possible = PASS`
- `did_not_route_away_merely_because_a_diagnostic_appeared = PASS`
- `preserved_upstream_readiness_as_the_governing_outcome = PASS`
