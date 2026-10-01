---
name: reconcile
description: "Reconcile persisted terminal implementation outcomes with request/spec contracts, then reconcile satisfied specs to their immediate provenance sources. Use after a terminal Implementation Result is persisted, or when resuming incomplete reconciliation."
---

# Reconcile

Reconcile from persisted tracker and delivery state, not from the implementation conversation. Requirement satisfaction belongs here; tracker adapters only provide configured storage, relationship, delivery, verification, and terminal operations.

If the configured tracker lacks the required role/provenance reads, Implementation/Reconciliation Result storage, source-keyed upstream notes, delivery evidence, or terminal operation, stop before mutation and tell the user to invoke the user-invoked `setup-matt-pocock-skills` workflow explicitly.

After each mutation sequence, re-read the affected item and verify the intended durable state. Never infer provenance from hierarchy or hierarchy from provenance.

## Process

### 1. Resolve the contract

Read the supplied artifact's full body/comments, work-item role, tracker state, hierarchy, direct `derived-from` sources, canonical Implementation Result when applicable, and canonical Reconciliation Result when present.

- **implementation-ticket:** require a terminal Implementation Result (`delivered` or `abandoned`). For `delivered`, re-check configured delivery evidence before mutation; if it conflicts with the persisted result, report the inconsistency and stop. Finalize the ticket if needed, verify it, then use its parent spec as the contract. If there is no parent spec, stop after the ticket is durably terminal.
- **request / spec:** use the subject itself as the contract. Its terminal implementation outcome is evidence, not permission to close the contract before satisfaction is checked.
- **other role:** stop; reconciliation only changes delivery contracts and records delivery on their provenance sources.

**Completion condition:** the contract and all immediate persisted evidence needed to evaluate it are explicit.

### 2. Verify satisfaction

For a request/spec, use required implementation-ticket children when present. Otherwise use its terminal canonical Implementation Result when present; when reached as an immediate provenance source of a satisfied downstream spec, use that downstream result and material delivery evidence as execution evidence too. If none of these provide terminal execution evidence, record `waiting`.

Required children must be terminal before satisfaction is checked. Terminal children, including blocked/abandoned/partial outcomes, trigger verification but do not prove satisfaction. For a directly executed request/spec with `Outcome: delivered`, re-check configured delivery evidence before recording satisfaction.

Use one canonical record:

```markdown
## Reconciliation Result

Status: <waiting | satisfied | unsatisfied>
Evidence: <durable links/results supporting the status>
Remaining: <explicit unmet scope, or None>
Next action: <concrete next action, or None>
```

- **Waiting:** upsert `waiting` with the non-terminal or missing evidence and stop.
- **Satisfied:** verify the contract's requested/acceptance behavior against persisted evidence and current repository behavior where needed; upsert `satisfied`, finalize only if not already terminal, and verify both result and tracker state.
- **Unsatisfied:** upsert `unsatisfied` with explicit remaining scope and a concrete next action. Keep an open contract open and release/suspend any stale active claim. If it was already terminal before this check, do not reopen it merely to repair history; report the lifecycle conflict.

A terminal contract with a persisted `satisfied` result does not need re-verification unless new material evidence requires it.

**Completion condition:** the contract is durably waiting/unsatisfied and open without a stale claim, or terminal with a verified `satisfied` result.

### 3. Reconcile immediate provenance

Only continue for a satisfied spec. Read every immediate `derived-from` source and use the configured source-keyed upstream note so reruns update rather than duplicate the record.

- **request:** publish the delivery summary, verify the original requested outcome against delivered scope/current behavior, and persist its Reconciliation Result using Step 2 semantics. Finalize only if satisfied.
- **spec:** publish the delivery summary and verify that spec as a separate contract using Step 2 semantics. Do not follow that source spec's own provenance in this invocation.
- **decision-map / decision-ticket:** publish a realization/backlink or delivery summary; do not change Wayfinder lifecycle state because implementation was delivered.

If an upstream source is already terminal, do not reopen it merely to repair history; record/report any conflict instead.

**Completion condition:** every immediate provenance source has one durable role-appropriate keyed record, and no request/spec source was finalized without verifying its own contract.

A rerun from the same persisted state must update canonical/keyed records rather than duplicate them or repeat terminal mutations.
