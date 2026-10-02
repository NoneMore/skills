# Project tracker v2 prototype

This directory is an isolated prototype for replacing the current project tracker model.

It intentionally does **not** port the existing downstream workflows. The prototype starts at setup and defines one semantic issue model plus two storage backends:

- GitHub Issues — the reference implementation when all required native capabilities are available.
- Local Markdown — the degraded fallback.

The authoritative tracker semantics live in [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md). Backend documents define representation and operations only.

## Model at a glance

Issues are either external intake or internally owned managed work.

Managed work has exactly one of two types:

- `investigation` — resolve uncertainty.
- `change` — make observable state different.

External intake remains separate from managed work so reporter identity, evidence, and discussion are preserved.

## Non-goals

This prototype does not:

- port or preserve the current `request`, `spec`, `implementation-ticket`, `decision-map`, or `decision-ticket` roles;
- define special container/tracking issue types;
- model research, prototype, grilling, or task as issue types;
- support GitLab, Jira, Linear, or a generic "other tracker" contract;
- migrate existing issues;
- define downstream workflow behavior yet.
