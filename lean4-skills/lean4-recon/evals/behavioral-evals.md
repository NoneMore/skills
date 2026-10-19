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

## Framing investigation is not automatically reuse extraction

Fixture: Repeated invariants appear in several domain-specific proofs, but
the decision is whether their governing definition should use a canonical
generic construction. The user explicitly selected recon and did not authorize
production edits.

Prompt: Challenge the surrounding mathematical framing before extracting any
shared lemma. Do not edit.

Required assertions:
- `investigated_governing_abstraction_and_theorem_placement = PASS`
- `did_not_reduce_recon_to_local_helper_extraction = PASS`
- `did_not_silently_switch_to_user_invoked_abstract = PASS`
- `made_no_production_edits = PASS`
