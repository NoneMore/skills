---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when translating mathematical intent into a Lean declaration, choosing canonical types or hypotheses, deciding intended generality, or explicitly revising a statement."
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

## Completion

- **Draft:** the intended claim is represented faithfully and the declaration skeleton elaborates apart from reported proof holes.
- **Checked:** the declaration and requested proof elaborate under the verification gate actually claimed.

Report unresolved statement ambiguity or proof holes as partial results.
