---
name: agents-md-wizard
description: Create, refresh, or audit AGENTS.md or equivalent workspace instructions by deciding what agents need, what belongs elsewhere, and how to write it.
disable-model-invocation: true
---

# AGENTS.md Wizard

Treat `AGENTS.md` as an agent-facing supplement to shared project documentation, not a second README. Aim for the smallest set of durable instructions that meaningfully changes agent behavior.

## 1. What belongs in AGENTS.md?

Inspect existing agent instructions and only the project evidence relevant to the request. Look for information an agent needs but cannot reliably infer or find in ordinary project documentation:

- Agent-specific instructions: non-obvious tool usage, operational constraints, or task workflows intended for agents.
- External context: relevant tools, services, or adjacent workspaces, including how and when the agent should locate or use them.
- Task-triggered pointers to authoritative shared documents that an agent might otherwise overlook.

Prefer stable relationships and discovery methods over hard-coded environment details. Keep personal or machine-specific non-secret settings in local/user-level configuration rather than committed agent instructions. Do not read secret values merely to author instructions, and do not embed credentials or secrets in instruction files; use appropriate secret-management tools instead.

Ground instructions in the user's intent or maintained project authority. Do not turn directory names, plausible conventions, or current runtime restrictions into permanent project policy.

## 2. What does not belong?

- Knowledge all contributors should share—architecture, business rules, APIs, development conventions—belongs in README, docs, ADRs, or another shared source of truth.
- Readily discoverable facts—dependency versions, script inventories, directory trees, and generated state—usually need no repetition.
- Generic exhortations, speculative prohibitions, and copies of existing rules add maintenance cost without useful guidance.

When a shared rule matters to an agent, point to its authoritative document at the relevant task boundary instead of restating it. If important shared knowledge is undocumented, identify the documentation gap; do not make `AGENTS.md` its only home.

Preserve valid existing human-authored rules. A proposed relocation or removal of a meaningful guardrail is a policy change, not a cosmetic cleanup.

## 3. How should it be written?

Use the repository's [Writing for Agents](../../WRITING-FOR-AGENTS.md) guide for additional wording guidance when available. These core rules apply even when that file is absent: write concrete actions and constraints, name conditions when they change applicability, and say when and why a referenced resource should be read.

Each line should justify its context and maintenance cost by preventing a plausible mistake, avoiding repeated reasoning, or improving verification.

## Apply

- For create or refresh requests, inspect the relevant scope, keep the useful agent-only content, and make the smallest effective edit. Respect how the active environment loads instruction files; do not assume nested files compose automatically.
- For audits, report misplaced, missing, duplicated, stale, or unclear instructions without editing files.
- Do not write on a bare Skill invocation without a requested outcome. An explicit create/update request authorizes the corresponding edit; do not add a routine approval gate.
- Ask only when an unresolved decision changes the instruction, its scope, or an existing human guardrail. Do not invent a rule to avoid asking.
- After editing, check the intended file and referenced paths, then summarize what changed and any material gaps.
