---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when translating mathematical intent into a Lean declaration, choosing canonical types or hypotheses, deciding intended generality, or explicitly revising a statement."
license: MIT
---

# Lean 4 Formalize

Turn mathematical intent into a faithful Lean declaration whose statement design is explicit rather than accidental.

## Workflow

1. Resolve the claim and intended level of generality.
2. Search local code and active imports before widening to mathlib for canonical types, definitions, and theorem shapes; validate candidates in the project context.
3. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis change.
4. Check that the declaration skeleton elaborates. A statement-design-only result may retain an explicitly reported proof hole.
5. Revise existing declarations only when the user explicitly authorized statement work on them.

If proving exposes a statement mismatch or evidence that the claim is false, report it rather than silently weakening the statement. If a checked proof is also requested, settle the declaration first and then verify the proof at the affected scope.

## Completion

- **Draft:** the intended claim is represented faithfully and the declaration skeleton elaborates apart from reported proof holes.
- **Checked:** the declaration and requested proof elaborate under the verification gate actually claimed.

Unresolved statement ambiguity or proof holes make the result partial and must be reported.
