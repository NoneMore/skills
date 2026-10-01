---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

# Implement

Implement the work described by the user in the spec or tickets. Keep the session bounded: implementation may finish before repository delivery finishes.

When the user supplies a persisted tracker reference, use the repo's configured issue tracker as the source of truth for execution coordination and delivery. If that configuration is missing or does not define the implementation execution/delivery capabilities below, stop before mutation and tell the user to invoke the user-invoked `setup-matt-pocock-skills` workflow explicitly. If no tracker item is supplied, skip tracker lifecycle mutations and use the code lifecycle below with the user's supplied contract.

## Process

### 1. Load the execution contract

For a supplied tracker item, read its full body, comments, work-item role, triage state, parent/children, blockers, claim/execution state, existing Implementation Result, and configured repository delivery policy. Do not mutate the tracker while deciding whether the item can run.

Apply normal execution-frontier eligibility only to items that do not already carry a durable implementation lifecycle outcome. A normal execution candidate is an open, ready execution leaf under the configured tracker semantics. A decomposed spec with implementation-ticket children is not an execution leaf even if its readiness metadata remains `ready-for-agent`.

An explicitly selected item with persisted `blocked`, `awaiting-delivery`, `delivered`, or `abandoned` state may be outside the normal frontier; continue to Step 2 so that persisted lifecycle state decides re-entry. Otherwise, if the item is ineligible or claimed by another execution session, stop before code/test mutation and report the persisted reason/state.

**Completion condition:** the execution contract and current lifecycle state are known, and either the item is eligible for new execution, is eligible for lifecycle re-entry in Step 2, or the workflow has stopped without mutation.

### 2. Resume durable lifecycle state

If a canonical Implementation Result already exists, continue from its persisted outcome and `Next action` rather than replaying completed work:

- `delivered`: if the tracker is already finalized, re-read the result and terminal state, report them, and stop. If the result is delivered but tracker finalization is incomplete, re-check the configured delivery evidence. When that evidence still proves delivery, run the configured finalization idempotently, verify the terminal state and canonical result, and stop. If delivery evidence no longer proves delivery, report the inconsistent persisted state and stop without replaying implementation or downgrading the result.
- `awaiting-delivery`: claim the item using the configured execution claim operation, then inspect the configured delivery evidence. If delivery is still pending, release the active claim while preserving awaiting-delivery state and stop. If delivery is complete, upsert the result to `delivered`, finalize the item, verify both writes, and stop. Do not rerun TDD, review, or commit.
- `blocked`: first re-check the persisted blocker/suspension condition. If the explicitly selected item still cannot proceed, report the persisted blocker and stop without mutation. Otherwise claim it, clear/update the configured suspension state, and continue from `Next action`; do not redo completed phases without a concrete reason.
- `abandoned`: report the persisted terminal outcome and stop.

**Completion condition:** a resumable item is either finalized from persisted evidence, left safely pending, or positioned at the first unfinished lifecycle action.

### 3. Claim before implementation mutation

For a tracker-backed item that will continue into implementation, use the configured claim operation before writing tests or implementation code. Claim must be the first tracker mutation in the session. Re-read the item and verify the claim persisted and the item no longer appears through the normal execution frontier.

If claim verification fails or reveals a conflicting claimant, make no code/test mutation.

**Completion condition:** this session durably owns the execution item and normal frontier discovery will skip it.

### 4. Implement and verify

After any required claim, record the current `HEAD` as the review fixed point unless the execution contract already supplied a different fixed point. Keep that value for the final review.

Before writing any test or implementation code, call the Skill tool with "tdd" and follow it. If the spec or ticket explicitly names testing seams, treat those seams as already agreed. If it does not, follow `tdd` and get the user's confirmation before writing tests.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once implementation and tests are complete, call the Skill tool with "code-review" exactly once. Pass both the captured review fixed point and the known originating execution contract explicitly; review must not rediscover a contract the enclosing workflow already knows.

Address the review before committing. For tracker-backed work, commit the verified work according to the repository's configured delivery policy rather than assuming that a commit alone means delivery is complete. For standalone work, commit to the current branch after review unless the user supplied different delivery instructions.

**Completion condition:** implementation is verified, review findings are addressed, and the resulting commit SHA(s) are known.

### 5. Publish delivery and the durable result

For standalone work with no persisted tracker item, report the commit plus verification/review outcome after the commit and stop; the rest of this section applies only to tracker-backed execution.

Use the configured repository delivery operation. In a direct-commit repository, delivery is complete only when the configured evidence shows the verified commit on the configured target branch. In a PR/MR repository, publish or identify the delivery request, record its link, and inspect its configured evidence; do not wait indefinitely for external review or merge.

Before the session ends, upsert exactly one canonical Implementation Result on the execution item. Updating an existing result is required on re-entry; do not append duplicate result records.

Use this semantic result shape regardless of the tracker's physical representation:

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

If configured delivery evidence is complete, write `Outcome: delivered`, then finalize/close the tracker item with the configured operation. Re-read the item and verify there is one canonical result, it records delivered evidence, and the tracker terminal state persisted.

If delivery is pending, write `Outcome: awaiting-delivery`, transition the item to the configured awaiting-delivery representation, then release the active claim. Re-read the item and verify it is durable, open, unclaimed, and excluded from the normal execution frontier. End the session.

### 6. Clean up blocked or abandoned work

If work cannot continue, do not leave an active claim behind.

- **Blocked:** upsert `Outcome: blocked` with the blocker, completed verification/commits, and concrete `Next action`; persist the configured blocked/suspended representation (and a real blocking relationship when one exists), then release the claim. Verify the item remains excluded from the normal frontier until resumed.
- **Abandoned:** upsert `Outcome: abandoned` with the reason and material partial work, use the configured terminal-abandon operation, release any active claim, and verify the terminal state plus canonical result.

A failure before a tracker-backed item was successfully claimed is read-only from the tracker's perspective; do not create a cleanup mutation for a claim that never existed.

