---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.
---

# Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing down current architectural decisions when they become useful to future work. Task-local implementation choices stay task-local unless they grow into a broader architectural decision. (Merely *reading* `CONTEXT.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

## File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── docs/adr/
```

Create files lazily: only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up: capture them as they happen. Use the format in [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md).

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Keep task decisions ephemeral

Do not promote a choice into persistent architecture merely because it was made during design or implementation. Specs, issues, and code may contain provisional choices that are valid only for the current task.

Treat existing implementation patterns as evidence of local conventions, not automatically as project-wide constraints. Preserve local consistency by default, but diverge when there is a concrete reason to do so.

### Offer ADRs sparingly

An ADR records a **current architectural decision** that future work should know about. It is not a permanent log and it does not make the decision immutable.

Offer an ADR when both are true:

1. **The decision reaches beyond the current task**: future work in this area should know or normally follow it.
2. **The rationale is worth preserving**: the choice reflects a meaningful architectural trade-off, convention, boundary, or direction that is not obvious from the code alone.

Reversibility does not disqualify a decision. A useful current architecture choice may be easy to change later; the ADR records what the project has decided *now* and why.

If the choice is local to one task, incidental to today's implementation, or obvious from the code, keep it in the task/spec/code and skip the ADR.

Every ADR present in `docs/adr/` is current. Do not create proposed ADRs; keep unresolved proposals in the task or spec. When a decision evolves, edit its ADR in place. When an ADR no longer describes the current architecture, delete it. Git history is the historical record.

Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).
