---
name: agents-md-wizard
description: Create, refresh, or audit AGENTS.md or equivalent workspace instructions by deciding what agents need, what belongs elsewhere, and how to write it.
disable-model-invocation: true
---

# AGENTS.md Wizard

Treat `AGENTS.md` as an agent-facing supplement to shared project documentation, not a second README. Aim for the smallest set of durable agent-specific context and instructions that meaningfully improve agent understanding, decisions, or behavior.

## 1. What belongs in AGENTS.md?

Inspect existing agent instructions and only the project evidence relevant to the request. Include information agents specifically need and might otherwise miss or misinterpret during relevant tasks:

- **Context:** non-obvious agent-specific facts, dependencies, and constraints that inform decisions but cannot be reliably inferred from the project alone.
- **Instructions:** actionable agent-specific rules, tool usage, task workflows, and task-triggered pointers to authoritative shared documentation.

Prefer stable relationships and discovery methods over hard-coded environment details. Keep personal or machine-specific settings in local/user-level configuration, and credentials or secrets out of agent instruction files.

Ground context and instructions in the user's intent or maintained project authority. Do not turn directory names, plausible conventions, or current runtime restrictions into permanent project policy.

## 2. What does not belong?

- Knowledge all contributors should share—architecture, business rules, APIs, development conventions—belongs in README, docs, ADRs, or another shared source of truth.
- Readily discoverable facts—dependency versions, script inventories, directory trees, and generated state—usually need no repetition.
- Generic exhortations, speculative prohibitions, and copies of existing rules add maintenance cost without useful guidance.

When a shared rule matters to an agent, point to its authoritative document at the relevant task boundary instead of restating it. If important shared knowledge is undocumented, identify the documentation gap; do not make `AGENTS.md` its only home.

## 3. How should it be written?

Use the repository's [Writing for Agents](../../WRITING-FOR-AGENTS.md) guide for additional wording guidance when available. These core rules apply even when that file is absent: state context as precise facts, express instructions as concrete actions or constraints, name conditions when they change applicability, and say when and why a referenced resource should be read.

Each entry should justify its context and maintenance cost by preventing a plausible mistake, avoiding repeated reasoning, or improving verification.

## Apply

- For create or refresh requests, inspect the relevant project evidence, keep useful agent-facing content, and make the smallest effective edit.
- For audits, report misplaced, missing, duplicated, stale, or unclear context and instructions without editing files.
- Preserve valid existing human-authored rules. Treat relocation or removal of a meaningful guardrail as a policy change, not a cosmetic cleanup.
- Do not write on a bare Skill invocation without a requested outcome. An explicit create/update request authorizes the corresponding edit; do not add a routine approval gate.
- Ask only when an unresolved decision changes the instruction, its scope, or an existing human guardrail. Do not invent a rule to avoid asking.
- After editing, check referenced paths, then summarize what changed and any material gaps.
