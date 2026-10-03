# Issue model

Authoritative semantics for the tracker. Backend documents define representation only.

## Tracked issues

Only explicitly classified issues participate in this tracker. Unclassified repository issues are outside it; do not infer tracker meaning from missing metadata, open/closed state, author, age, or historical usage.

Every tracked issue has exactly one kind:

- `intake` — external project input such as a report, request, question, or discussion;
- `managed` — work the project has decided to own.

Intake preserves the original reporter, wording, evidence, and discussion. Accepted intake may source separate managed work rather than being rewritten into managed work.

## Managed-work type

Every managed issue has exactly one type:

- `investigation` — resolve a material uncertainty;
- `change` — make observable state different.

Intake has no managed-work type. Repository taxonomy such as bug, feature, docs, or security is independent from tracker type.

## Status

Every tracked issue has one explicit lifecycle status.

Intake statuses:

- `needs-triage`
- `waiting`
- `done`

Managed statuses:

- `ready`
- `waiting`
- `done`

Status is semantic tracker state. A backend's own open/closed state may mirror it but does not define it.

When a tracked issue is `waiting`, record both:

- `Waiting for` — the external event or decision;
- `Resume when` — a checkable condition for becoming actionable again.

## Managed-work content

Every managed issue must state an issue-specific, checkable completion condition.

Skills may add sections they own, such as notes, conclusions, results, or evidence. When updating one of those sections, preserve unrelated content.

## Sources

`Sources` records direct provenance: tracked issues used to define the current issue.

- Sources may be empty or many-to-many.
- Record direct sources only, not transitive closure.
- A source must exist and must not reference the current issue itself.
- Sources do not imply hierarchy or dependency.

## Hierarchy

Parent/child means decomposition: a child is part of completing its parent.

- Only managed work participates in hierarchy.
- Each managed issue has at most one parent.
- Parent relations must reference existing managed work, must not self-reference, and must not form cycles.
- Completing all children does not automatically complete the parent.

## Dependencies

`BlockedBy` records scheduling dependencies.

- Only managed work participates in dependencies.
- Both endpoints must be existing managed work.
- Dependencies must not self-reference or form cycles.
- Dependencies are independent from hierarchy and sources.

## Execution metadata

Assignment, claiming, concurrency, execution ownership, frontier selection, and orchestration are not tracker semantics. A downstream workflow may use backend metadata for those purposes, but this contract does not prescribe how.
