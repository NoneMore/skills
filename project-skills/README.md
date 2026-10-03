# Project tracker prototype

An isolated prototype for replacing the current project tracker model.

It defines:

- one semantic issue model;
- explicit tracker classification so unclassified repository issues remain outside the tracker;
- GitHub Issues as the intended backend when the repository uses GitHub and required native relations are usable;
- Local Markdown as an explicit alternative, not an automatic fallback for missing GitHub capability;
- a versioned repository-local tracker contract (`Contract-Version: 1`).

See [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md) for the semantic contract. Backend documents define representation and operations only.

Every tracked issue is explicitly classified as either intake or managed work. Setup never adopts, repairs, migrates, or reinterprets pre-existing unclassified issues; that belongs to a separate migration/takeover workflow.

Managed work has exactly one of two types:

- `investigation` — resolve uncertainty;
- `change` — make observable state different.

Every managed issue has a checkable completion condition. Managed work in `waiting` must also say what it is waiting for and the checkable condition for becoming actionable again. Skills that create or execute managed work may add structured sections they own, such as execution notes, implementation results, conclusions, or evidence, while preserving unrelated sections.

Lifecycle status is explicit. `done` and `cancelled` are terminal: ordinary tracker operations cannot move a terminal issue back to a live status or change one terminal outcome into another. Reopening requires a separate migration/repair workflow.

External intake remains separate from managed work so reporter identity, evidence, and discussion are preserved. Intake can source managed work but does not participate in managed-work hierarchy or dependency graphs. Hierarchy and dependency relations are managed-work-only, self-reference is forbidden, and both graphs must remain acyclic.

For managed work, assignee is the current execution claim rather than long-lived ownership. The execution model does not permit concurrent top-level execution of the same managed issue; subagents operate inside the claiming execution rather than claiming the issue independently. Executable frontier work is `ready`, unclaimed, and has no live blocker.

GitHub tracker labels are namespaced as `tracker:kind:*`, `tracker:type:*`, and `tracker:status:*` so ordinary repository taxonomy such as `bug`, `feature`, or `documentation` remains independent. GitHub setup can install intake-only forms for common entry points while keeping blank issues available. Shipped forms explicitly classify their issues as intake.

For blank issues, a GitHub contract persists an immutable `Intake-Cutover-Number` captured when the first contract is published. Unclassified issues at or below that repository issue/PR number remain historical and outside the tracker; later unclassified issues may be classified by downstream intake/triage workflows. This makes the setup boundary recoverable from a fresh checkout rather than depending on session memory.

When GitHub is the intended backend, setup requires usable Issues, labels, assignees, native sub-issues, and native issue dependencies. Global invariant checks must be able to enumerate complete paginated result sets, and claim operations must be able to verify that the resolved GitHub login is assignable. Archived or otherwise unusable canonical tracker labels are setup conflicts rather than objects setup silently repairs. If a required capability is unavailable, setup stops rather than silently switching the repository to Local Markdown or using textual relation fallbacks.

Local Markdown keeps monotonically increasing positive numeric issue IDs with canonical rendering `0001` through `9999`, then `10000` and upward. Creation uses create-only semantics with collision retry; runtimes that cannot provide that guarantee must serialize concurrent creators.

`Contract-Version: 1` is a frozen normative protocol snapshot once published. Normative semantic or backend-contract changes require a new contract version rather than silently changing the meaning of version 1.

## Non-goals

This prototype does not port downstream workflows, migrate or take over existing issues, support other tracker vendors, or modify the current Matt skills.
