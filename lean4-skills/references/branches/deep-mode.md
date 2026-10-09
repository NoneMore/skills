# Deep Proof Escalation

Load only after the normal proving path is demonstrably stuck or when the user explicitly requests deeper work.

Deep work may search more broadly, extract helpers, or span additional files, but it must remain bounded.

## Entry requirements

- State the blocker and evidence from the normal path.
- Define owned files and a change budget before editing.
- Capture a recoverable baseline for every owned file when the runtime supports deterministic snapshots/baselines.

## Invariants

- Existing declaration headers remain immutable unless statement work was explicitly handed to the formalization workflow.
- Do not absorb unrelated working-tree changes into the baseline.
- After each meaningful edit, compare diagnostics and proof-hole state against the pre-deep baseline.
- New errors, more sorries, or newly introduced blockers are regressions. Roll back deep-owned changes when a safe rollback mechanism exists; otherwise stop and report the regression instead of continuing to mutate.

## Exit

Exit on success, budget exhaustion, regression, or a repeated blocker with no new evidence. Return the files changed, verification result, failed approaches, and the next useful action.