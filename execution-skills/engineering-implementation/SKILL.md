---
name: engineering-implementation
description: "Implement, fix, or refactor repository code when persistent changes are authorized. For conditional fixes, join only after evidence establishes the condition and the fix is being pursued. Excludes review-only and investigation-only work."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Implementation

Use **Intent → Feedback → Evidence** to achieve a proven, scoped outcome. These are reasoning roles, not mandatory phases.

## Invocation and authority

Use for authorized persistent implementation. For "investigate/review, then fix if X", first establish X under read-only authority; invoke this skill only when the qualifying fix is being pursued. If X is false or unresolved, report the finding without mutation. Investigation and review skills can help when available; neither is required to establish this boundary.

Permission to edit the working tree does not itself authorize staging, commits, history/ref changes, branch switching, deployment, publication, remote changes, credentials, or destructive data operations. Those require authority from the underlying task or an applicable higher-priority workflow. Specialized skills do not expand that authority.

Inspect baseline state before material changes. Preserve unrelated user work; avoid broad formatting, generation, or cleanup that rewrites it. In read-only subtasks, ordinary contained caches/build outputs are allowed, but intentional tracked edits, snapshot acceptance, and dependency/lockfile updates are not. If verification unexpectedly changes files, distinguish task-created changes from pre-existing work before targeted cleanup.

## Intent and decisions

Establish the observable outcome, material non-goals, and constraints that must remain true. Use relevant code, tests, maintained contracts, and accepted decisions to resolve facts before asking the user.

- Current user intent can authorize changing an existing contract; an old contract is not an automatic veto. Account for compatibility, migration, and data consequences.
- Tests and runtime behaviour show what happens, not necessarily what should happen. Do not promote stale plans or implementation accidents into authority.
- Preserve **Fixed** product, architecture, compatibility, and scope decisions. Choose **Local**, reversible, externally equivalent mechanics autonomously. Return consequential **Open** choices to their decision owner after gathering available evidence.
- Follow accepted plans while their assumptions hold. Stop extending a falsified direction; re-plan or escalate if continuation changes fixed decisions, scope, contracts, or consequential risk.

For conflicting governing sources or a plan invalidated during execution, read [references/governing-decisions.md](references/governing-decisions.md).

## Feedback and rigor

Test direction-changing assumptions before costly implementation depends on them. Prefer discriminating reproductions or focused experiments over broad exploration. Stop investigating when more evidence would not change the next decision or proof strategy.

Scale rigor with uncertainty, consequence, reversibility, blast radius, and coordination needs. Public contracts, persistent data, security, concurrency, and difficult rollback warrant stronger evidence even for a tiny edit. Preserve any upstream capacity label; it neither starts a workflow nor sets the proof bar.

A bounded change can proceed through inspection, implementation, direct verification, and diff review without a written plan. Add planning or continuity state only when needed for the authorized outcome. Fix incidental issues only when they block that outcome or violate a relevant invariant; otherwise report material findings without expanding scope.

## Capacity feedback

When observed progress, necessary work, or verification needs materially undermine a supplied capacity assumption or threaten a known time/context/budget limit, report evidence, completed/remaining work, estimated impact and uncertainty, and a recommended option to the user or authorized upstream owner. Preserve the workload label; do not invent missing limits or telemetry. Routine difficulty alone does not require escalation.

While awaiting a decision, continue only bounded authorized work within existing limits that does not depend on that decision. Before a known limit, preserve permitted resume state and stop at a safe boundary; do not start a unit that cannot reasonably fit with verification/recovery. Silence grants no extension. Apply an explicit owner decision within its bounds without restarting valid work or asking again absent a material forecast change. Do not weaken proof, reduce scope, or invoke a new orchestration mode merely to fit the estimate.

## Evidence

Choose evidence closest to the claim:

- Reproduce the failure or exercise the changed behaviour; when practical, show the check distinguishes the broken and corrected states.
- Run relevant repository-native tests, type checks, builds, or integration probes. Broaden verification when consequence or blast radius warrants it.
- Probe important boundaries and error paths, and inspect the resulting diff for regressions, forbidden dependencies, accidental scope, weakened invariants, and unjustified complexity.

A new test that mirrors the implementation can share its mistaken assumption. Seek independent evidence where material. Do not remove meaningful tests, suppress errors, or weaken verification just to pass; change a faulty check only when authoritative intent or direct evidence establishes the check is wrong.

Distinguish baseline failures from introduced regressions. If a baseline or relevant environment is unavailable, state the gap instead of claiming attribution or success.

Verification commands are executable code: inspect uncertain scripts/hooks or constrain execution before running checks with possible consequential side effects. A command called "test" grants no additional authority.

## Knowledge and continuity

Before completion, check whether maintained knowledge became stale or a durable fact/decision emerged. Reconcile within task authority using the existing canonical home; do not create a task diary. For a concrete lifecycle decision, use `engineering-knowledge-governance` when available; otherwise apply these local rules.

At an actual agent/session/context handoff, use `engineering-handoff` when available. Otherwise carry outcome/scope, governing sources and fixed decisions, current state, remaining work, observed verification results and gaps, and the next action. Reference existing artifacts, preserve unrelated work, and persist only when continuity needs it.

## Completion

Stop when the requested outcome is supported by positive behaviour evidence and materially relevant negative evidence against regressions, constraint violations, and unnecessary complexity. Report what changed, supporting checks, and material gaps or out-of-scope findings. Do not turn routine completion into additional work.
