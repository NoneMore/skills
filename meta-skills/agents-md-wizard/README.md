# AGENTS.md Wizard

A small, explicitly invoked Meta Skill for creating, refreshing, or auditing `AGENTS.md` and equivalent agent instruction files.

**Core idea:** `AGENTS.md` supplements shared project documentation. It should not become a second README or the only place where project knowledge lives.

## Three questions

1. **What to write?** Agent-specific behavior, external tools or adjacent workspaces, and task-triggered pointers to shared knowledge that agents might miss.
2. **What not to write?** Architecture, business rules, and development conventions that all contributors need belong in shared docs. Do not copy readily recoverable config, directory listings, or generic advice.
3. **How to write it?** Follow [Writing for Agents](../../WRITING-FOR-AGENTS.md): concrete actions, relevant triggers, useful pointers, and minimal duplication.

Personal machine paths, private configuration, and volatile state belong in local/user-level configuration or tools rather than committed instructions. If important shared documentation is missing, report that gap instead of making `AGENTS.md` its only source.

## Usage

Install or copy this Skill into a location recognized by your agent runtime, then invoke it explicitly:

```text
Use $agents-md-wizard to create AGENTS.md for this workspace. Keep only agent-specific information or pointers; flag anything that belongs in shared docs.

Use $agents-md-wizard to refresh AGENTS.md without losing existing human-authored guardrails.

Audit AGENTS.md using $agents-md-wizard, but do not edit files.
```

Creation/update requests authorize the necessary edits once important decisions are grounded; audit is read-only. When the requested file would not be loaded by the active runtime, the Skill should explain the mismatch instead of silently changing the requested target.

## Package

- `SKILL.md` — the three questions and minimal execution rules.
- `agents/openai.yaml` — explicit-invocation metadata.
- `examples/agent-only-AGENTS.md` — an illustrative agent-specific supplement.
- `evals/scenarios.md` — focused behavioral checks.

Runtime-specific loading details are obtained from the active environment when needed, rather than maintained as a second instruction-management framework.
