# Proving Workflow

Use for filling sorries, repairing proof failures, or completing a bounded proof task. The shared invariants in `../../SKILL.md` remain in force.

## Modes

- **Bounded** (default): make one focused pass on the requested target and stop if the same blocker persists.
- **Guided:** run repeated proof cycles, showing the next plan at cycle boundaries and obtaining user direction before continuing.
- **Autonomous:** run repeated cycles only when the user explicitly asks for unattended progress; require explicit stop budgets.

Guided and autonomous modes share the same proof mechanics. Their difference is who owns continuation, not a separate proof algorithm.

## Cycle

1. Inspect the exact goal and current diagnostics.
2. Search local declarations and mathlib before inventing a proof. Skip extended search for an obviously trivial goal.
3. Produce a small candidate set and test candidates against the goal when possible.
4. Apply the smallest passing edit.
5. Re-run diagnostics. Resolve compiler suggestions only after checking that they preserve the intended proof and API.
6. At a cycle boundary, either continue with new evidence, escalate, or stop with a blocker report.

For proof-hole techniques load `../sorry-filling.md`; for a specific diagnostic load `../compilation-errors.md`.

## Stuck and escalation

Treat a target as stuck when repeated attempts reproduce the same blocker without new evidence, or the normal search path is exhausted. Record the search queries, best candidates, and failed attempts that justify the conclusion.

Do not simply repeat the cycle. Choose one:

- load `../branches/deep-mode.md` for bounded deeper work;
- switch to the formalization workflow if the statement shape is the blocker;
- switch to the refutation workflow if evidence suggests the statement may be false;
- stop and hand the blocker evidence to the user.

## Verification and completion

After each edit, use live diagnostics when available. After cross-file edits use a dependency-aware file gate. Use a project build when the requested scope is project-wide or at final integration.

A proof task is complete when the agreed target elaborates, the agreed scope contains no unresolved sorries, no new diagnostics remain in touched files, and the statement/trust basis was not silently changed.