---
name: engineering-knowledge-governance
description: "Govern durable engineering knowledge when repository knowledge must be persisted or reconciled: create, update, move, supersede, or retire canonical specs, designs, runbooks, conventions, or coordination state; or when current work makes a maintained source stale or contradictory. Do not invoke merely because engineering work occurred."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Knowledge Governance

Keep durable engineering knowledge authoritative, discoverable, maintainable, and proportionate to its future value.

This skill governs **knowledge persistence and document discipline**, not the task-specific workflow used to implement code, review changes, investigate a system, conduct research, or run an experiment. It may compose with any of those tasks.

The default is not "write documentation." The default is **decide deliberately whether anything should persist, then preserve one trustworthy home for what does**.

## Universal consideration, conditional invocation

In a long-lived engineering system, every meaningful engineering task should perform a lightweight **knowledge-impact check**: did the work create a durable fact, constraint, accepted design decision, operational truth, or continuity need; or did it make a maintained canonical source stale, contradictory, or incomplete?

That consideration is universal. **Invocation of this Skill is not.** Invoke only when the check identifies a concrete persistence, canonicality, reconciliation, supersession, retirement, or continuity decision. Do not turn "documentation is first-class" into "every task must create documentation."

## Core invariants

- **Persistence must earn its place.** Do not create durable artifacts merely because work occurred, a session is ending, or a finding was interesting.
- **Prefer canonical homes over parallel narratives.** Update an existing authoritative source when its scope already owns the knowledge.
- **Separate durable truth from transient coordination.** Current state, target state, decisions, facts, and plans can coexist, but their authority and lifecycle must remain distinguishable.
- **Preserve provenance and uncertainty.** A durable claim should carry enough basis for a future reader to judge trust, scope, and freshness when those are not obvious.
- **Reconcile contradictions.** Consequential work is not documentation-complete while the repository presents materially conflicting current truths about the same subject.
- **Follow repository convention before inventing taxonomy.** Local canonical structures, naming, and lifecycle conventions outrank generic neatness.
- **Minimize duplication.** Link to primary sources instead of restating authoritative claims unless a maintained secondary representation is intentionally required.
- **Let version control be history by default.** Do not retain stale files solely as an archive when their continued presence would confuse current truth.

## Persistence decision

Before creating or expanding durable engineering knowledge, ask whether at least one is true:

- another capable engineer or agent would likely make a materially worse decision without it;
- reconstructing it later would be expensive, ambiguous, or risky;
- an existing trusted source would otherwise remain incomplete, stale, or misleading;
- cross-context or cross-agent continuity requires explicit coordination state.

If none apply, keep the result transient: report it in the current task, leave it represented by code/tests/history, or discard temporary experimental notes and artifacts when safe.

The fact that a task is read-only does not by itself make its findings durable. The fact that a task changes code does not by itself require new documentation.

## Canonicality and placement

Before creating, renaming, moving, splitting, merging, or retiring durable engineering documentation, inspect the repository's existing documentation system and apply `references/knowledge-model.md`.

Prefer, in order:

1. update an existing canonical artifact;
2. extend an existing maintained artifact whose scope already owns the claim;
3. create a new artifact only when the knowledge has a distinct durable scope, audience, lifecycle, or maintenance owner.

Do not create a new document merely to mirror the current task type, agent, ticket, session, or workflow stage.

## Task-specific application

Apply the same governance discipline without importing another task's workflow:

- **Implementation / refactoring:** reconcile durable contracts, design decisions, constraints, runbooks, or other maintained knowledge invalidated by the change.
- **Code review:** findings normally remain in the review unless they reveal durable repository knowledge that would otherwise remain missing, stale, or misleading. Do not create repository documents merely to archive review comments.
- **Investigation / research:** persist conclusions only when they are stable enough and valuable enough to guide future work; retain provenance, uncertainty, and freshness where material.
- **Experiments:** distinguish temporary probes and measurements from durable conclusions. Persist the conclusion, method, or constraint only when future decisions depend on it; do not preserve disposable experiment scaffolding as documentation by default.
- **Specification / design work:** keep accepted target state distinguishable from current implementation state; preserve governing requirements, constraints, and accepted design where future work must obey them, while avoiding permanent copies of change-local discussion.
- **Plans / handoffs:** persist only the minimum coordination state required for continuity, and retire it when its coordination value ends unless part of it has become durable design or operational knowledge.

## Reconciliation

When consequential work changes what a maintained artifact claims:

1. identify the canonical source that owns the affected claim;
2. update, supersede, or retire it rather than adding a competing explanation;
3. update inbound references when names or locations change;
4. keep current-state, target-state, status, provenance, and freshness distinctions accurate;
5. remove or clearly supersede stale coordination material whose continued presence would mislead future work.

Do not preserve an old statement merely because it was once authoritative. Do not silently rewrite a durable contract unless the underlying task has authority to change that contract.

## Boundaries

This skill does not grant authority to modify code, deploy, publish, push, merge, change remote state, or perform other external effects. Documentation or coordination mutation must remain within the authority granted by the underlying task and applicable higher-priority instructions.

If the underlying task is explicitly read-only with respect to repository state, follow the persistence decision but do not write or reorganize repository documents unless the task separately authorizes that mutation. Report the durable-knowledge need instead.

## Final checks

Before finishing work that touched or evaluated durable engineering knowledge, verify:

- Did anything actually need to persist?
- Is each durable claim in the repository's best canonical home?
- Did the work avoid creating a parallel source of truth?
- Can a future reader distinguish current state, target state, decisions, and transient coordination where it matters?
- Is provenance, uncertainty, or freshness explicit when needed to judge trust?
- Did consequential changes leave any maintained artifact materially stale or contradictory?
- Were obsolete transient artifacts retired when keeping them would mislead future work?
- Did documentation activity stay within the underlying task's mutation and external-effect authority?
