# Project tracker prototype

An isolated prototype for replacing the current project tracker model.

It defines:

- one semantic issue model;
- GitHub Issues as the reference backend when required native relations are usable;
- Local Markdown as the fallback.

See [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md) for the semantic contract. Backend documents define representation and operations only.

Managed work has exactly one of two types:

- `investigation` — resolve uncertainty;
- `change` — make observable state different.

Every managed issue has a checkable completion condition. Skills that create or execute managed work may add structured sections they own, such as execution notes, implementation results, conclusions, or evidence, while preserving unrelated sections.

External intake remains separate from managed work so reporter identity, evidence, and discussion are preserved. GitHub setup can install intake-only forms for common entry points while keeping blank issues available; reporters never choose the internal managed-work type or lifecycle state.

## Non-goals

This prototype does not port downstream workflows, migrate existing issues, support other tracker vendors, or modify the current project skills.
