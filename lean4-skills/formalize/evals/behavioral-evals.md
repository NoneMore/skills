# Behavioral evals — lean4-formalize

## Statement design is explicit

Prompt: Formalize the claim “every finite subgroup of a torsion-free group is trivial” in Lean 4 using mathlib. Choose an appropriate level of generality; a proof is optional.

Required assertions:
- `searched_for_canonical_mathlib_representation_before_inventing_api = PASS`
- `made_hypotheses_and_generality_explicit = PASS`
- `did_not_claim_checked_proof_when_only_statement_elaborated = PASS`

## Fixed statements do not route here by default

Prompt: Fill the `sorry` in this existing theorem without changing its statement.

Required assertions:
- `formalize_not_selected_for_fixed_statement_proof_only_task = PASS`
- `lean4_prove_selected = PASS`
