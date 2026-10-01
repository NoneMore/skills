---
name: reconcile
description: "Reconcile persisted terminal implementation outcomes to their contracts and satisfied specs to direct provenance sources. Use after a terminal Implementation Result is persisted, or when resuming reconciliation whose durable upstream state may be incomplete."
---

# Reconcile

Reconcile from persisted tracker and delivery state, not from the implementation conversation. Requirement satisfaction is a workflow decision; tracker adapters only provide the configured read, upsert, relationship, coordination, verification, and terminal operations.

If the configured tracker cannot read roles, provenance, hierarchy, terminal state, Implementation Results, Reconciliation Results, source-keyed upstream notes, or the coordination/finalization operations required below, stop before mutation and tell the user to invoke the user-invoked `setup-matt-pocock-skills` workflow explicitly.

After each mutation sequence, re-read the affected item and verify the intended durable state. While following spec-to-spec provenance, carry both the active ancestry path and a processed-spec set. A spec already on the active path is a provenance cycle; a spec already processed outside that path is a converging path and reuses its persisted result instead of traversing its provenance again.

## Process

### 1. Load and normalize the reconciliation subject

Read the supplied artifact's full body/comments, work-item role, tracker state, parent/children, direct `derived-from` sources, canonical Implementation Result when applicable, and canonical Reconciliation Result when present.

Never infer provenance from hierarchy or hierarchy from provenance.

- For an `implementation-ticket`, require a terminal Implementation Result (`delivered` or `abandoned`). For `delivered`, re-check configured delivery evidence before any terminal mutation; if the persisted result conflicts with delivery evidence, report the inconsistency and stop. If the ticket is not already terminal, run the configured terminal operation and verify it. Then use its parent spec as the contract to reconcile. If it has no parent spec, stop after the ticket's own terminal state is durable; do not invent a parent.
- For a `spec` or `request`, use the subject itself as the contract. Do not close it merely because its own implementation attempt reached a terminal outcome; contract satisfaction decides its tracker finalization.
- For any other role, stop unless an enclosing reconciliation step supplied a spec whose upstream sources are being reconciled.

**Completion condition:** the subject role and immediate relationships come from persisted state, any implementation-ticket terminalization is verified, and the contract to check is explicit.

### 2. Reconcile the contract

A terminal contract with a persisted `Status: satisfied` Reconciliation Result is already reconciled: for a spec continue to Step 3; for a request finish. A terminal contract without that result is not proof of satisfaction. Verify from available persisted evidence, but do not reopen an already-terminal artifact merely to repair history.

Determine the execution evidence for the contract:

- **Direct request:** use its canonical Implementation Result, configured delivery evidence when applicable, and current repository behavior. A missing or non-terminal direct result is waiting, not satisfied.
- **Spec with implementation-ticket children:** treat those children as required unless the spec explicitly says otherwise. If any required child is non-terminal, the spec is waiting. Terminality only decides when the spec is ready to verify; it is never evidence that the spec is satisfied.
- **Direct spec:** when there are no implementation-ticket children, use its own canonical Implementation Result and delivery evidence. A missing or non-terminal direct result is waiting.
- **Upstream spec reached from Step 3:** the satisfied downstream spec and its material delivery evidence are explicit additional persisted evidence. Absence of the upstream spec's own Implementation Result or implementation children does not by itself make it waiting.

When waiting, upsert the contract's canonical Reconciliation Result with the missing/non-terminal work, material delivered/blocked/abandoned progress, and a concrete next action, then stop that reconciliation branch.

Once the relevant execution evidence is terminal, verify the contract's actual requested/acceptance behavior against its body and acceptance criteria, every relevant Implementation/Reconciliation Result, material delivery evidence, and resulting repository behavior where needed.

Use this semantic record; the tracker configuration defines how it is stored:

```markdown
## Reconciliation Result

Status: <waiting | satisfied | unsatisfied>
Evidence: <durable links/results supporting the status>
Remaining: <explicit unmet scope, or None>
Next action: <concrete next action, or None>
```

- **Satisfied:** upsert `Status: satisfied`, finalize the contract only if it is not already terminal, and verify both persisted state and result. A satisfied request finishes here; a satisfied spec continues to Step 3.
- **Unsatisfied:** upsert `Status: unsatisfied` with explicit remaining scope and a concrete next action. If the contract is open, keep it open. If the contract itself has a terminal Implementation Result, use the configured suspension operation to release any active claim and keep that completed attempt outside the normal execution frontier. If the contract was already terminal before this check, do not reopen it solely for repair; report the persisted lifecycle conflict instead.

Blocked, abandoned, rejected, or partial implementation outcomes may be terminal inputs to verification; they do not by themselves satisfy the contract.

**Completion condition:** the contract is open with a durable waiting/unsatisfied explanation and no stale active claim, terminal with a verified `Status: satisfied` result, or a pre-existing terminal lifecycle conflict has been durably recorded and reported without reopening history.

### 3. Reconcile a satisfied spec to direct provenance

Only propagate from a spec whose persisted Reconciliation Result is `satisfied`. Add the current spec to the active ancestry path and processed-spec set, read every immediate `derived-from` source, and dispatch each independently by its persisted work-item role. Support more than one source. Remove the current spec from the active path after its sources are reconciled; keep it in the processed set for the rest of this invocation.

For each source, first use the configured source-keyed upstream note operation so reruns update the same record rather than append duplicates.

- **request:** publish a durable delivery summary linking the spec and material delivery evidence. Then verify the original requested outcome against delivered scope and current behavior. Close/finalize the request only when that request is actually satisfied. Otherwise keep an open request open and make the remaining requested scope explicit. If it was already terminal, do not reopen it merely to repair history; report any conflict with the satisfaction check.
- **decision-map / decision-ticket:** publish a realization/backlink or delivery summary. Do not change Wayfinder lifecycle state because implementation was delivered.
- **spec:** if the source spec is already on the active ancestry path, report the provenance cycle and skip lifecycle mutation on that edge. If it is already in the processed-spec set outside the active path, keep the edge's keyed note but skip duplicate traversal of that spec's own provenance. Otherwise apply Step 2 to that upstream spec, supplying this satisfied downstream spec and its material delivery evidence as explicit additional evidence. If the upstream spec becomes satisfied, apply this step to its own immediate provenance.
- **unknown/custom role:** publish only a conservative backlink/summary unless the role's configured semantics explicitly define stronger reconciliation behavior.

Do not reopen an upstream source merely to repair history. Publish any missing idempotent summary that is still valid and report persisted state that conflicts with the satisfaction check.

**Completion condition:** every immediate provenance edge has a durable, role-appropriate keyed record, each reachable satisfied upstream spec's own provenance is traversed at most once in this invocation, and no source was finalized without verifying its own completion semantics.

### 4. Finish idempotently

Re-read the subject, contract, and every mutated provenance source. A rerun from the same persisted state must update canonical/keyed records rather than duplicate them, must not repeat terminal mutations already reflected by the tracker, and must terminate even if persisted spec provenance contains cycles or converging paths.

**Completion condition:** another session can resume reconciliation using only tracker/repository state and reach the same lifecycle decisions without the prior conversation.
