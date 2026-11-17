# AGENTS.md Wizard

A small, explicitly invoked Meta Skill for creating, refreshing, or auditing `AGENTS.md` and equivalent agent instruction files.

**Core idea:** `AGENTS.md` supplements shared project documentation. It should not become a second README or the only place where project knowledge lives.

## Three questions

1. **What to write?** Agent-specific behavior, external tools or adjacent workspaces, and task-triggered pointers to shared knowledge that agents might miss.
2. **What not to write?** Architecture, business rules, and development conventions that all contributors need belong in shared docs. Do not copy readily recoverable config, directory listings, or generic advice.
3. **How to write it?** Use concrete actions, relevant triggers, useful pointers, and minimal duplication. The repository's [Writing for Agents](../../WRITING-FOR-AGENTS.md) provides additional guidance when available.

Personal machine paths and non-secret local settings belong in local/user-level configuration rather than committed instructions. Credentials and other secrets belong in appropriate secret-management tools, not agent instruction files. If important shared documentation is missing, report that gap instead of making `AGENTS.md` its only source.

## Usage

Install or copy this Skill into a location recognized by your agent runtime, then invoke it explicitly:

```text
Use $agents-md-wizard to create AGENTS.md for this workspace. Keep only agent-specific information or pointers; flag anything that belongs in shared docs.

Use $agents-md-wizard to refresh AGENTS.md without losing existing human-authored guardrails.

Audit AGENTS.md using $agents-md-wizard, but do not edit files.
```

Creation/update requests authorize the necessary edits once important decisions are grounded; audit is read-only.

## Package

- `SKILL.md` — the three questions and minimal execution rules.
- `agents/openai.yaml` — explicit-invocation metadata.
- `examples/agent-only-AGENTS.md` — an illustrative agent-specific supplement.
- `evals/scenarios.md` — focused behavioral checks.

`SKILL.md` contains the core writing rules, so standalone installations do not require the repository-level writing guide.

