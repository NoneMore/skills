# Outcomes and Persistence

> Status: settled design direction for the capability-oriented refactor.

## Skills own outcomes, not files

Every skill must produce a clear local outcome, but not every skill must create a durable artifact.

**Outcome and artifact are different concepts.**

A skill's outcome is the useful result it owns. Persistence is a separate decision based on whether keeping that result beyond the current conversation is itself valuable.

Do not introduce a canonical result block, status record, or per-skill output document merely to prove that a skill ran.

## Ephemeral by default

Conversation context is valid working memory.

For capabilities whose value is primarily a decision, explanation, or judgment, the default output may simply be an explicit result in the current conversation.

Persist the result only when one of these is true:

- the artifact itself is the user's requested product;
- a later session or collaborator needs to reference it directly;
- the result is durable project knowledge that future work should know;
- an existing real source of truth naturally owns the result;
- the user explicitly asks for persistence.

Otherwise, let the result remain ephemeral.

This prevents the suite from accumulating documents whose only purpose is to mirror conversational or workflow state.

## Promote to the natural source of truth

When persistence is useful, write to the place that naturally owns the information rather than to a suite-specific result store.

Examples:

- durable domain vocabulary -> `CONTEXT.md` or the project's existing domain documentation;
- durable architectural decisions -> ADRs or the project's existing architecture documentation;
- requested work and discussion -> issue/tracker item;
- review findings -> PR/review surface when useful;
- diagnosis that matters to future maintainers -> issue, regression test, commit/PR explanation, or other natural project record;
- implemented behavior -> code, tests, commits, PRs, and CI;
- a specification requested as a durable contract -> the spec artifact itself;
- work decomposition intended for execution -> tracker issues or another chosen planning surface.

Do not create a `design-result.md`, `implementation-result`, `reconciliation-result`, or equivalent solely because the suite wants a durable marker.

## Two broad output shapes

This is a design distinction, not a new runtime taxonomy or protocol.

### Outcome-oriented capabilities

The useful result can exist in the conversation and persistence is optional.

Examples:

- `design` -> design decisions and unresolved questions;
- diagnosis/debugging, if retained -> evidence-backed explanation of a concrete failure;
- `review` -> findings and judgments about the thing reviewed.

These capabilities may update durable project knowledge when doing so is independently useful, but persistence is not part of their completion condition by default.

### Artifact-oriented capabilities

A durable or concrete artifact is intrinsic to the user's requested result.

Examples:

- `prototype` -> a concrete throwaway artifact used to learn;
- `implement` -> working production code and proportionate verification;
- `specify` -> a durable specification when the user wants one;
- `decompose` -> an actionable decomposition, persisted when publication/execution is part of the request;
- `handoff`, if retained -> a continuation artifact.

The distinction is about what makes the result valuable, not about imposing a common persistence mechanism.

## `design` output contract

`design` owns **design decisions**, not a design document.

Its default output is an explicit account in the conversation of:

- the decisions reached;
- the important rationale or constraints when they matter;
- any material unresolved questions that remain.

`design` may also:

- inspect code, history, docs, issues, PRs, logs, or external sources;
- run small experiments or write throwaway spikes when they help answer the design question;
- update durable domain vocabulary when a project-wide term has actually been settled;
- update or create an ADR when a project-level architectural decision and its rationale are worth preserving.

It does **not** require:

- a design document;
- a spec;
- an ADR;
- a `CONTEXT.md` change;
- a tracker item;
- a canonical design-result record;
- a downstream capability invocation.

If the user wants the settled design turned into a durable implementation contract, that is a separate `specify` outcome. If the design conclusion is only useful for the current work, it may remain in the conversation and disappear with it.

## Cross-session continuity is not every skill's responsibility

Do not force every capability to persist its result just because a future session might exist.

If continuation across sessions is a real need, use the natural durable project artifact or a dedicated handoff mechanism. Cross-session continuity should not turn every local capability into a document-producing workflow.

## Review test

For each surviving skill, ask two separate questions:

1. **What outcome does this skill own?**
2. **Is persistence intrinsic to the value of that outcome?**

If the first answer is unclear, the skill boundary is unclear.

If the second answer is no, do not invent an artifact requirement.

The governing principle is:

> **Skills own outcomes; artifacts are created only when persistence is part of the value.**
