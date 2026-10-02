# Project tracker v2 prototype

An isolated prototype for replacing the current project tracker model.

It defines:

- one semantic issue model;
- GitHub Issues as the reference backend when required native relations are usable;
- Local Markdown as the fallback.

See [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md) for the semantic contract. Backend documents define representation and operations only.

Managed work has exactly one of two types:

- `investigation` — resolve uncertainty;
- `change` — make observable state different.

External intake remains separate from managed work so reporter identity, evidence, and discussion are preserved.

## Non-goals

This prototype does not port downstream workflows, migrate existing issues, support other tracker vendors, or modify the current project skills.
