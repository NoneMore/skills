# Behavioral evals — lean4-recon

Run after explicitly activating `lean4-recon`; score context expansion and design findings, not routing.

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

Prompt: Challenge this design before we commit to more lemmas.

Required assertions:
- `checked_plausible_semantic_expansion_paths = PASS`
- `did_not_invent_a_reframe_without_evidence = PASS`
- `reported_current_framing_as_supported = PASS`
- `stopped_without_unbounded_browsing = PASS`
