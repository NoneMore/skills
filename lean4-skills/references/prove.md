# Proving Workflow

Use for filling proof holes, repairing proof failures, or making the smallest supporting edits needed to complete an agreed proof target.

## Contract

1. Inspect the exact goal, declaration, and current diagnostics before editing.
2. Search local declarations and mathlib when an existing result may solve or materially simplify the goal. Skip extended search for an obviously trivial goal.
3. Try a small set of materially different candidates. Test candidates against the live goal when available; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change.
5. Verify the changed target and any affected dependency boundary with the lightest sufficient gate; load `references/verification.md` when the distinction matters.

If evidence shows that the real task is statement design, certified refutation, or post-correctness optimization, use `references/formalize.md`, `references/disprove.md`, or `references/optimize.md` respectively.

## Completion

A checked proof is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit`, and the affected scope satisfies the chosen verification gate.
