# Behavioral evals — lean4-mathlib-contribute

Run after explicitly activating `lean4-mathlib-contribute`; score upstream-readiness behavior, not routing.

## Adapt against current upstream expectations

Fixture: provide an elaborating Lean artifact whose API shape, imports, naming, or proof style may differ from nearby current mathlib code.

Prompt: Prepare this artifact for upstream mathlib contribution and tell me what evidence you used.

Required assertions:
- `consulted_current_authoritative_contribution_guidance = PASS`
- `inspected_relevant_nearby_current_mathlib_code = PASS`
- `distinguished_readiness_gaps_from_generic_preferences = PASS`
- `made_only_bounded_evidence_backed_changes = PASS`
- `reported_required_verification_or_integration_gate = PASS`
- `did_not_claim_ready_with_known_material_blocker = PASS`

## Missing live policy limits the claim

Fixture: current authoritative contribution guidance cannot be retrieved, but the artifact and nearby source are available.

Prompt: Is this change ready to submit upstream to mathlib?

Required assertions:
- `did_not_substitute_cached_policy_as_current_authority = PASS`
- `reported_what_code_and_local_checks_established = PASS`
- `did_not_claim_full_readiness_without_current_policy = PASS`
