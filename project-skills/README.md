# Project tracker prototype

An isolated prototype for replacing the current project tracker model.

It defines:

- one semantic issue model;
- GitHub Issues as the reference backend when required native relations are usable;
- Local Markdown as the fallback;
- a versioned repository-local tracker contract (`Contract-Version: 1`).

See [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md) for the semantic contract. Backend documents define representation and operations only.

Managed work has exactly one of two types:

- `investigation` — resolve uncertainty;
- `change` — make observable state different.

Every managed issue has a checkable completion condition. Managed work in `waiting` must also say what it is waiting for and the checkable condition for becoming actionable again. Skills that create or execute managed work may add structured sections they own, such as execution notes, implementation results, conclusions, or evidence, while preserving unrelated sections.

External intake remains separate from managed work so reporter identity, evidence, and discussion are preserved. Intake can source managed work but does not participate in managed-work hierarchy or dependency graphs. Hierarchy and dependency relations are managed-work-only, self-reference is forbidden, and both graphs must remain acyclic.

For managed work, assignee is the current execution claim rather than long-lived ownership. Managed work has at most one assignee; executable frontier work is `ready`, unclaimed, and has no live blocker. Claims are coordination rather than a distributed lock, so execution workflows re-check claim ownership before consequential mutations or external effects.

GitHub tracker labels are namespaced as `tracker:type:*` and `tracker:status:*` so ordinary repository taxonomy such as `bug`, `feature`, or `documentation` remains independent. GitHub setup can install intake-only forms for common entry points while keeping blank issues available; reporters never choose the internal managed-work type or lifecycle state.

Local Markdown keeps monotonically increasing numeric issue IDs, but creation must use create-only semantics with collision retry; runtimes that cannot provide that guarantee must serialize concurrent creators.

## Non-goals

This prototype does not port downstream workflows, migrate existing issues, support other tracker vendors, or modify the current project skills.
