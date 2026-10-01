---
name: reconcile
description: "Reconcile persisted terminal implementation outcomes upward to parent specs and satisfied specs to their direct provenance sources. Use after tracker finalization, or when resuming terminal work whose upstream satisfaction state may still need reconciliation."
---

# Reconcile

Reconcile from persisted tracker and delivery state, not from the implementation conversation. Requirement satisfaction is a workflow decision; tracker adapters only provide the configured read, upsert, relationship, verification, and terminal operations.

If the configured tracker cannot read roles, provenance, hierarchy, terminal state, Implementation Results, or the reconciliation records required below, stop before mutation and tell the user to invoke the user-invoked `setup-matt-pocock-skills` workflow explicitly.

After each mutation sequence, re-read the affected item and verify the intended durable state.

## Process

### 1. Load the reconciliation subject

Read the supplied artifact's full body/comments, work-item role, tracker state, parent/children, direct `derived-from` sources, canonical Implementation Result when applicable, and canonical Reconciliation Result when present.

Never infer provenance from hierarchy or hierarchy from provenance.

- For an `implementation-ticket`, continue with its parent spec.
- For a `spec`, continue from its persisted reconciliation state and direct provenance.
- For any other role, stop unless an enclosing workflow supplied a spec whose upstream sources are being reconciled.

**Completion condition:** the current role and all immediate relationships needed for the next step come from persisted state.

### 2. Reconcile an implementation ticket to its spec

If the implementation ticket has no parent spec, there is no spec-level reconciliation target; stop without inventing one.

Read the parent spec and all of its `implementation-ticket` children. Terminality only decides when the spec is ready to verify; it is never evidence that the spec is satisfied.

If any required implementation child is non-terminal, upsert the spec's canonical Reconciliation Result as waiting, including the non-terminal children and any material delivered/blocked/abandoned progress, then stop.

When the required implementation children are terminal, verify the spec's actual contract against persisted evidence: the spec body and acceptance criteria, every relevant child Implementation Result, delivery evidence, and the resulting repository behavior where needed.

Use this semantic record; the tracker configuration defines how it is stored:

```markdown
## Reconciliation Result

Status: <waiting | satisfied | unsatisfied>
Evidence: <durable links/results supporting the status>
Remaining: <explicit unmet scope, or None>
Next action: <concrete next action, or None>
```

- **Satisfied:** upsert `Status: satisfied`, finalize the spec idempotently, verify both persisted state and result, then continue to Step 3.
- **Unsatisfied:** upsert `Status: unsatisfied` with explicit remaining scope and a concrete next action. Keep the spec open. Do not silently create implementation tickets or reinterpret terminal child outcomes as success.

Blocked, abandoned, rejected, or partial child outcomes may be terminal inputs to verification; they do not by themselves satisfy the spec.

**Completion condition:** the spec either remains open with a durable waiting/unsatisfied explanation, or is terminal with a verified `Status: satisfied` result.

### 3. Reconcile a satisfied spec to direct provenance

Only propagate from a spec whose persisted Reconciliation Result is `satisfied`. Read every immediate `derived-from` source and dispatch independently by its persisted work-item role. Support more than one source.

For each source, use the configured source-keyed upstream note operation so reruns update the same record rather than append duplicates.

- **request:** publish a durable delivery summary linking the spec and material delivery evidence. Then verify the original requested outcome against delivered scope and current behavior. Close/finalize the request only when that request is actually satisfied. Otherwise keep it open and make the remaining requested scope explicit.
- **decision-map / decision-ticket:** publish a realization/backlink or delivery summary. Do not change Wayfinder lifecycle state because implementation was delivered.
- **spec:** treat it as a separate contract. Delivery of the downstream spec may be evidence, but verify the upstream spec's own contract before any terminal mutation.
- **unknown/custom role:** publish only a conservative backlink/summary unless the role's configured semantics explicitly define stronger reconciliation behavior.

If an upstream source is already terminal, do not reopen it merely to repair history. Publish any missing idempotent summary that is still valid and report persisted state that conflicts with the satisfaction check.

**Completion condition:** every immediate provenance source has a durable, role-appropriate reconciliation record, and no source was finalized without verifying its own completion semantics.

### 4. Finish idempotently

Re-read the subject, parent spec when present, and every mutated provenance source. A rerun from the same persisted state must update canonical/keyed records rather than duplicate them, and must not repeat terminal mutations that are already reflected by the tracker.

**Completion condition:** another session can resume reconciliation using only tracker/repository state and reach the same lifecycle decisions without the prior conversation.
