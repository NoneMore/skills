---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when designing or revising an individual declaration, choosing canonical types or hypotheses, deciding intended generality, or evaluating whether an existing helper should become a reusable public statement."
license: MIT
---

# Lean 4 Formalize

## Workflow

1. Resolve the claim and intended generality.
2. Search local and imported APIs before broader mathlib for canonical types, definitions, and theorem shapes; validate candidates in context.
3. Where validity materially depends on hypothesis strength, quantifier domains, or carrier restrictions, probe a discriminating boundary case or counterexample (with scratch Lean when useful), and compare the prerequisites of reused results. Stop probing when no materially new, low-cost check is likely to change the declaration decision; report unresolved validity concerns rather than expanding into open-ended refutation. Do not treat elaboration as evidence that a claim is true.
4. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis change.
5. Check that the declaration skeleton elaborates. Statement-design-only work may retain an explicitly reported proof hole.
6. Revise an existing declaration only when statement revision is explicitly authorized.

If proving exposes a statement mismatch or evidence that the claim is false, report it rather than silently weakening the statement. If a checked proof is requested, settle the declaration first and then verify the affected scope.

## Existing declarations

When assessing a private helper, compare more general existing declarations
with the specialized wrapper's elaboration benefit. Recommend public exposure
only for concrete API value; do not edit on assessment-only requests.

## Completion

- **Draft:** the intended claim is represented faithfully and the declaration skeleton elaborates apart from reported proof holes; this does not certify that the statement is true. If a consequential boundary check undermines the claim, report the blocker rather than presenting it as sound.
- **Checked:** the declaration and requested proof elaborate under the verification gate actually claimed.

Report unresolved statement ambiguity, semantic validity, or proof holes as partial results; distinguish uncertified counterexample evidence from Lean-certified refutation.
