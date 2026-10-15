# Proving Workflow

Use for filling proof holes, repairing proof failures, or making the smallest supporting edits needed to complete an agreed proof target. The shared invariants in `SKILL.md` remain in force.

## Contract

1. Inspect the exact goal, declaration, and current diagnostics before editing.
2. Search local declarations and mathlib when an existing result may solve or materially simplify the goal. Skip extended search for an obviously trivial goal.
3. Try a small set of materially different candidates. Test candidates against the live goal when available; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change.
5. Verify the changed target and any affected dependency boundary with the lightest sufficient gate; load `references/verification.md` when the distinction matters.
6. Continue only while new evidence suggests a materially different bounded avenue.

Cross-file edits are allowed when they are necessary to complete the agreed target. Do not modify generated caches or dependency checkouts such as `.lake/packages` unless the task specifically concerns them, and do not widen into unrelated refactoring or architecture work.

If evidence shows that the real task is statement design, certified refutation, or post-correctness optimization, use `references/formalize.md`, `references/disprove.md`, or `references/optimize.md` respectively.

## Stop and completion

Stop when no materially new bounded avenue remains. Report the blocker, useful searches or attempts already ruled out, and the smallest next action that could change the result.

A checked proof task is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit`, affected files satisfy the chosen verification gate, the agreed statement/API is preserved, and no new axiom or other trust-basis weakening was introduced to make the proof succeed. If the user accepts a partial result or trust-basis change, report that outcome as partial or changed rather than as a completed checked proof.
