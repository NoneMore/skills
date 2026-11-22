---
name: agents-md
description: Create, refresh, or audit AGENTS.md and similar agent instruction files. Use when deciding what agent-specific context and instructions belong in them, what belongs in shared documentation, or how to write concise, effective guidance.
---

# AGENTS.md

Treat `AGENTS.md` as an agent-facing supplement, not a second README. Keep only durable agent-specific context and instructions that meaningfully improve agent understanding or behavior.

## What belongs

- **Context:** non-obvious agent-specific facts, dependencies, and constraints that inform decisions.
- **Instructions:** agent-specific actions, constraints, tool use, and task-triggered pointers to authoritative resources.

## What belongs elsewhere

- Keep architecture, business rules, APIs, and conventions shared by all contributors in maintained project documentation. Point to them only when an agent needs a task-specific reading trigger.
- Omit readily discoverable facts, duplicated rules, and generic advice.
- Keep machine-specific configuration and secrets out of committed agent instructions.
- When important shared knowledge is undocumented, flag the gap rather than making `AGENTS.md` its only source.

## How to write it

- Ground content in user intent or authoritative project sources; do not invent project policy.
- State context as precise facts and instructions as concrete actions or constraints.
- For a reference, say when to consult it and what it provides.
- Keep entries that prevent plausible mistakes, avoid meaningful repeated reasoning, or improve verification.

## Apply

- Create or refresh when requested, making the smallest effective change.
- Audit without editing files.
- Preserve existing valid constraints unless the user authorizes changing them.
- Ask only when an unresolved decision materially affects the result.
- Verify added or changed references.
