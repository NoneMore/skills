# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root, or
- **`CONTEXT-MAP.md`** at the repo root if it exists: it points at one `CONTEXT.md` per context. Read each one relevant to the topic.
- **`docs/adr/`**: read current ADRs that touch the area you're about to work in. Deprecated or superseded ADRs are historical context, not active constraints. In multi-context repos, also check `src/<context>/docs/adr/` for context-scoped decisions.

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. Call the Skill tool with "domain-modeling" when a domain term is resolved or a genuinely durable project constraint is established. Task-local implementation choices do not trigger ADR creation.

## File structure

Single-context repo (most repos):

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

Multi-context repo (presence of `CONTEXT-MAP.md` at the root):

```
/
├── CONTEXT-MAP.md
├── docs/adr/                          ← system-wide decisions
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/                  ← context-specific decisions
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (call the Skill tool with "domain-modeling" to close it).

## Flag current ADR conflicts

If your output contradicts a current ADR, surface it explicitly rather than silently overriding:

> _Conflicts with ADR-0007 (event-sourced orders); this would require revisiting that constraint because…_

ADRs are mutable current-state documents. If the durable decision changes, update the ADR in place; deprecate or delete it when it is no longer active; supersede it only when keeping the old and new decisions distinct is useful. Do not preserve stale constraints merely for auditability — Git history is the historical record.
