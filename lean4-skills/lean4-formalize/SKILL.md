---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when designing or revising an individual declaration, choosing canonical types or hypotheses, deciding intended generality, or evaluating whether an existing helper should become a reusable public statement."
license: MIT
---

# Lean 4 Formalize

## Workflow

1. Resolve the claim and intended generality.
2. Search local and imported APIs before broader mathlib for canonical types, definitions, and theorem shapes; validate candidates in context.
3. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis change.
4. Check that the declaration skeleton elaborates. Statement-design-only work may retain an explicitly reported proof hole.
5. Revise an existing declaration only when statement revision is explicitly authorized.

If proving exposes a statement mismatch or evidence that the claim is false, report it rather than silently weakening the statement. If a checked proof is requested, settle the declaration first and then verify the affected scope.

## Existing declarations

When assessing a private helper or existing theorem, search for a more general
declaration and distinguish mathematical generality from a useful specialized
wrapper or elaboration boundary. Recommend public exposure only for a real API
benefit; do not force generalization or edit an existing declaration without
authorization. Use `lean4-abstract` when the goal is shared structure and
migration across multiple proofs.

## Completion

- **Draft:** the intended claim is represented faithfully and the declaration skeleton elaborates apart from reported proof holes.
- **Checked:** the declaration and requested proof elaborate under the verification gate actually claimed.

Report unresolved statement ambiguity or proof holes as partial results.
