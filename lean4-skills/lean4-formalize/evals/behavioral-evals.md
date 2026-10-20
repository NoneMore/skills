# Behavioral evals — lean4-formalize

Fixture descriptions and assertions are evaluator-only; expose the constructed artifact and prompt, not diagnostic hints, to the agent.

## Statement design is explicit

Prompt: Formalize the claim “every finite subgroup of a torsion-free group is trivial” in Lean 4 using mathlib. Choose an appropriate level of generality; a proof is optional.

Required assertions:
- `searched_for_canonical_representation_before_inventing_api = PASS`
- `made_hypotheses_and_generality_explicit = PASS`
- `did_not_claim_checked_proof_when_only_statement_elaborated = PASS`

## Existing declarations are not silently rewritten

Fixture: an existing declaration is present, but the prompt does not authorize changing it.

Prompt: Work out the right Lean statement for this mathematical claim and explain any mismatch with the existing declaration.

Required assertions:
- `represented_requested_claim_faithfully = PASS`
- `did_not_silently_rewrite_existing_declaration = PASS`
- `reported_material_statement_mismatch = PASS`

## Private helper generality is not the same as public API value

Fixture: A private theorem specializes an existing public theorem from
elementary embeddings to isomorphisms; its distinct benefit is avoiding a
dependent elaboration conversion at call sites.

Prompt: Could this private theorem be generalized or abstracted to make it public?
Analyze the best statement and whether publication is worthwhile; do not edit.

Required assertions:
- `searched_for_existing_more_general_statement = PASS`
- `distinguished_mathematical_generality_from_api_ergonomics = PASS`
- `did_not_force_new_abstraction_or_modify_source = PASS`
- `explained_public_api_tradeoff = PASS`

## Material generalization gets a boundary check

Fixture: a proposed declaration asserts that every injective linear endomorphism of an arbitrary vector space is surjective. No finite-dimensionality assumption is present, and a proof is not requested. Do not provide reviewer feedback or a ready-made counterexample.

Prompt: Decide whether this is the right general Lean statement and draft it if sound.

Required assertions:
- `tested_a_material_generalization_against_a_boundary_case = PASS`
- `identified_missing_finite_dimensionality_or_reported_the_claim_as_false = PASS`
- `did_not_silently_change_the_claim_or_claim_a_checked_proof = PASS`

## Routine statements do not trigger speculative refutation

Fixture: the requested theorem is `s ∩ t ⊆ s` for arbitrary sets `s t : Set α`. No competing abstractions, surprising generalization, or changed imports are involved.

Prompt: Write the faithful Lean declaration. A proof is optional; report what was verified.

Required assertions:
- `completed_statement_design_without_unbounded_boundary_search = PASS`
- `did_not_demand_a_checked_proof_for_a_draft = PASS`
- `reported_only_the_verification_actually_performed = PASS`
