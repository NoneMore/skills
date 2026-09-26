---
name: domain-modeling
description: Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a CONTEXT.md, or recording or editing an ADR.
---

# Domain Modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing down durable domain knowledge when it crystallises. Task-local implementation choices stay task-local unless they become a genuine long-lived project constraint. (Merely *reading* `CONTEXT.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

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

Treat existing implementation patterns as examples, not project constraints, unless the project explicitly documents them as durable.

### Offer ADRs sparingly

An ADR represents a **current durable constraint**, not a permanent log of every architectural choice.

Offer an ADR only when either:

- the user explicitly says the decision is a durable project constraint, or
- all three are true:
  1. **Future work must obey it** beyond the current task
  2. **Changing it is meaningfully expensive or externally observable** — for example it affects compatibility, persisted data, users, integrations, or requires a coordinated migration
  3. **The reason is not obvious from the code** and captures a real trade-off a future reader would otherwise re-litigate

If these conditions are missing, keep the decision in the task/spec/code and skip the ADR.

ADRs are mutable current-state documents. When the decision evolves, edit the ADR in place. When it stops being useful, deprecate or delete it. Create a superseding ADR only when preserving the distinction between the old and new decisions is itself useful. Git history is the historical record.

Use the format in [ADR-FORMAT.md](./ADR-FORMAT.md).
