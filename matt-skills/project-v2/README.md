# Project tracker v2 prototype

This directory is an isolated prototype for replacing the current project tracker model.

It intentionally does **not** port the existing downstream workflows. The prototype starts at setup and defines only the shared issue model plus two storage backends:

- GitHub Issues — the reference implementation.
- Local Markdown — a degraded fallback that mirrors the same semantics.

## Core idea

GitHub issues are signals and work items, but not every issue is managed work.

Managed work has exactly one type:

- `investigation` — resolve uncertainty.
- `change` — make an observable state different.

External reports and requests remain external issues. They are not converted into managed work. Maintainers create separate managed issues and link the external issues as direct sources.

An investigation never changes type into a change. It may produce zero, one, or many change issues, each sourcing the investigation.

## Orthogonal dimensions

- **Type** — what completion means.
- **Status** — where the issue is in its lifecycle.
- **Sources** — which issues directly caused this issue to exist.
- **Parent/children** — decomposition.
- **Blocked by** — scheduling dependency.
- **Assignee** — execution claim.

None of these dimensions may be inferred from another.

## Non-goals

This prototype does not:

- port or preserve the current `request`, `spec`, `implementation-ticket`, `decision-map`, or `decision-ticket` roles;
- define special container/tracking issue types;
- model research, prototype, grilling, or task as issue types;
- support GitLab, Jira, Linear, or a generic "other tracker" contract;
- migrate existing issues;
- define downstream workflow behavior yet.

See `setup-tracker/ISSUE-MODEL.md` for the semantic contract.
