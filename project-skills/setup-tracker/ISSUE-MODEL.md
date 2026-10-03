# Issue model

Backends represent this model; they do not redefine it.

## Classification

Only explicitly classified issues participate in the tracker. Unclassified repository issues remain outside it.

Every tracked issue has one kind:

- `intake` — external input such as a report, request, question, or discussion;
- `managed` — work the project has decided to own.

Every managed issue also has one type: `investigation` (resolve uncertainty) or `change` (change observable state). Intake has no managed-work type. Repository taxonomy such as bug, feature, docs, or security is independent.

Preserve intake reporter, wording, evidence, and discussion. Accepted intake may source separate managed work rather than being rewritten into managed work.

## Status and content

| Kind | Allowed status |
| --- | --- |
| intake | `needs-triage`, `waiting`, `done` |
| managed | `ready`, `waiting`, `done` |

Status is explicit tracker state; backend open/closed state does not define it.

Every managed issue has an issue-specific, checkable completion condition.

A `waiting` issue records both `Waiting for` (the external event or decision) and `Resume when` (a checkable condition for becoming actionable again).

Skills may add sections they own, but must preserve unrelated content.

## Relations

- `Sources` is direct provenance. It may reference existing intake or managed work, must not self-reference, and does not imply hierarchy or dependency.
- `Parent` is optional managed-work decomposition. Only managed work participates; each issue has at most one parent; self-reference and cycles are forbidden. Completing all children does not automatically complete the parent.
- `BlockedBy` is a managed-work scheduling dependency. Both endpoints must be existing managed work; self-reference and cycles are forbidden.

## Scope

Assignment, claiming, concurrency, execution ownership, frontier selection, orchestration, migration/versioning, delivery policy, and issue-template UX are outside the tracker model.
