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

## Candidate API retains downstream information

Fixture: two otherwise usable rank APIs return values in `ℕ∞` and `Cardinal`. The downstream theorem must distinguish the sizes of different infinite bases. Both APIs are available in the pinned project; do not state which one to select.

Prompt: With `lean4-recon` explicitly selected, investigate which rank API can support the intended theorem. Do not edit production files.

Required assertions:
- `traced_one_downstream_consumer_before_selecting_an_api = PASS`
- `recognized_the_information_loss_in_the_coarser_codomain = PASS`
- `kept_the_investigation_bounded_and_read_only = PASS`
