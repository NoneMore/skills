---
name: lean4-formalize
description: "Use for formal mathematics in Lean 4/mathlib when designing or revising an individual declaration, choosing canonical types or hypotheses, deciding intended generality, or evaluating whether an existing helper should become a reusable public statement."
license: MIT
---

# Lean 4 Formalize

## Workflow

1. Resolve the claim and intended generality.
2. Search local and imported APIs before broader mathlib for canonical types, definitions, and theorem shapes; validate candidates in context.
3. When hypothesis strength, quantifier domains, or carrier restrictions materially affect validity, probe a discriminating boundary case (using scratch Lean if useful) and check reused results' prerequisites. Stop once further cheap checks are unlikely to change the declaration; report unresolved validity concerns without open-ended refutation.
4. Draft the weakest faithful declaration with explicit hypotheses and no hidden trust-basis change.
5. Check that the declaration skeleton elaborates. Statement-design-only work may retain an explicitly reported proof hole.
6. Revise an existing declaration only when statement revision is explicitly authorized.

If proving exposes a statement mismatch or evidence that the claim is false, report it rather than silently weakening the statement. If a checked proof is requested, settle the declaration first and then verify the affected scope.

## Existing declarations

When assessing a private helper, compare more general existing declarations
with the specialized wrapper's elaboration benefit. Recommend public exposure
only for concrete API value; do not edit on assessment-only requests.

## Completion

- **Draft:** a faithful declaration skeleton elaborates apart from reported proof holes; elaboration does not certify truth. If a consequential boundary check undermines the claim, report a blocker.
- **Checked:** the declaration and requested proof pass the claimed verification gate, which does not certify fidelity to the intended claim.

Report unresolved statement ambiguity, validity concerns, or proof holes as partial results; distinguish uncertified counterexample evidence from Lean-certified refutation.
