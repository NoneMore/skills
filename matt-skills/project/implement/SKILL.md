---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

# Implement

Implement the work described by the user in the spec or tickets. Keep the session bounded: implementation may finish before repository delivery finishes.

When the user supplies a persisted tracker reference, use the repo's configured issue tracker for execution coordination and delivery. If that configuration is missing or lacks the operations below, stop before mutation and tell the user to invoke the user-invoked `setup-matt-pocock-skills` workflow explicitly. With no tracker item, skip tracker lifecycle mutations and use the code lifecycle with the user's supplied contract.

After each tracker mutation sequence, re-read the item before code mutation or session end and verify the intended durable state.

## Process

### 1. Resolve the lifecycle

For a tracker item, read its full body/comments, work-item role, triage state, hierarchy/blockers, execution coordination, canonical Implementation Result, and repository delivery policy.

If an Implementation Result exists, resume from its `Outcome` and `Next action`:

- `delivered`: if the tracker is already terminal, call the Skill tool with "reconcile" and pass the tracker item, then stop. Otherwise re-check delivery evidence; if it still proves delivery, finalize idempotently, verify, call "reconcile", and stop. If it does not, report the inconsistent persisted state without replaying implementation or downgrading the result.
- `awaiting-delivery`: inspect delivery evidence without claiming. If still pending, report it and stop. If complete, upsert `delivered`, finalize, verify, call the Skill tool with "reconcile" and pass the tracker item, then stop. Do not rerun TDD, review, or commit.
- `blocked`: re-check the blocker/suspension condition. If it still cannot proceed, report the blocker and stop. Otherwise claim first, clear the configured suspension state, and continue from `Next action` without repeating completed phases.
- `abandoned`: ensure the configured terminal operation has completed, verify it, call the Skill tool with "reconcile" and pass the tracker item, then stop.

Otherwise require a normal execution candidate: an open, ready execution leaf under the configured tracker semantics. A spec with implementation-ticket children is not an execution leaf even if it remains `ready-for-agent`. If the item is ineligible or already claimed, stop before code/test mutation.

Claim an eligible tracker item before writing tests or implementation code. Claim must be the session's first tracker mutation; verify that the claim persisted and normal frontier discovery now skips the item.

**Completion condition:** the workflow has stopped from durable state, or this session owns the item and is positioned at the first unfinished implementation action.

### 2. Implement and verify

Record the current `HEAD` as the review fixed point unless the execution contract supplied one.

Before writing test or implementation code, call the Skill tool with "tdd" and follow it. If the contract already names testing seams, treat them as agreed; otherwise follow `tdd` and get the user's confirmation before writing tests.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once implementation and tests are complete, call the Skill tool with "code-review" exactly once. Pass the review fixed point and known originating execution contract explicitly. Address the review before committing.

Commit the verified work after review. For standalone work, use the current branch unless the user supplied different delivery instructions; tracker-backed publication belongs to Step 3.

**Completion condition:** implementation is verified, review findings are addressed, and the resulting commit SHA(s) are known.

### 3. Deliver and persist the result

For standalone work, report the commit plus verification/review outcome and stop.

For tracker-backed work, follow the configured delivery policy. Publish a PR/MR when that policy defines a publication operation, then inspect the configured delivery evidence. Do not wait indefinitely for external PR/MR review or merge.

Maintain exactly one canonical Implementation Result; update it on re-entry rather than appending duplicates:

```markdown
## Implementation Result

Outcome: <blocked | abandoned | awaiting-delivery | delivered>
Implemented: <scope completed>
Verification: <tests/checks performed and material gaps>
Review-Fixed-Point: <commit/ref, when applicable>
Commits: <SHA(s), when applicable>
Delivery: <direct evidence or PR/MR link/status>
Blocker: <reason, when applicable>
Next action: <the next lifecycle action, or None>
```

If delivery evidence is complete, upsert `Outcome: delivered`, run the configured terminal finalization, verify it, then call the Skill tool with "reconcile" and pass the tracker item.

If delivery is pending, upsert `Outcome: awaiting-delivery`, then use the configured suspension operation to release the active claim while keeping the item outside the execution frontier. End the session.

**Completion condition:** the canonical result and tracker state durably represent either delivered terminal work or open, unclaimed work awaiting delivery.

### 4. Stop safely

If claimed work cannot continue, do not leave an active claim:

- **Blocked:** upsert `Outcome: blocked` with the blocker and concrete `Next action`; record a real blocking relationship when one exists, then use the configured suspension operation to release the claim while keeping the item outside the execution frontier.
- **Abandoned:** upsert `Outcome: abandoned` with the reason and material partial work, run and verify the configured terminal operation, then call the Skill tool with "reconcile" and pass the tracker item.

A failure before a tracker-backed item was successfully claimed is read-only from the tracker's perspective.

**Completion condition:** the canonical result records why work stopped, no active claim remains, and terminal tracker-backed work has invoked upstream reconciliation from persisted state.
