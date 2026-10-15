# Proving Workflow

Use for filling proof holes, repairing proof failures, or making the smallest supporting edits needed to complete an agreed proof target. The shared invariants in `SKILL.md` remain in force.

## Contract

1. Inspect the exact goal, declaration, and current diagnostics before editing.
2. Search local declarations and mathlib when an existing result may solve or materially simplify the goal. Skip extended search for an obviously trivial goal.
3. Try a small set of materially different candidates. Test candidates against the live goal when the runtime supports it; otherwise apply and compile one candidate at a time.
4. Apply the smallest coherent passing change.
5. Verify the changed target and any affected dependency boundary with the lightest sufficient gate; load `references/verification.md` when the distinction matters.
6. Continue only while new evidence suggests a materially different bounded avenue.

Cross-file edits are allowed when they are the smallest necessary way to complete the agreed target, for example adding a genuinely necessary helper or import in an owned dependency. Do not widen into open-ended refactoring, cleanup, or architecture work.

## Handoffs

Change ownership explicitly when the problem changes:

- the existing statement/API needs redesign -> `references/formalize.md`;
- credible evidence indicates the target may be false -> `references/disprove.md`;
- correctness is established and the remaining goal is quality, brevity, or performance -> `references/optimize.md`.

A handoff is not permission to preload all workflows.

## Stop and completion

Stop when no materially new bounded avenue remains. Report the blocker, useful searches or attempts already ruled out, and the smallest next action that could change the result.

A proof task is complete when the agreed target elaborates, the agreed proof scope has no unresolved `sorry`/`admit` unless the user explicitly accepted a partial result, affected files satisfy the chosen verification gate, and the statement/trust basis was not silently changed.
