# Issue model

Backends represent this model; they do not redefine it.

Contract version: `2`.

## Membership and validity

Each backend defines tracker membership. Membership and validity are separate: malformed or incomplete tracked work remains tracked but invalid until repaired or removed.

Issue origin is not tracker state. Uncontrolled/native issues remain outside the tracker; workflows may create tracked work with those issues recorded in `Sources`.

## Work

Every valid tracked issue has one immutable `Type`:

- `investigation` — resolve uncertainty;
- `change` — change observable state.

Do not change `Type`. When a completed investigation implies implementation work, finish it and create a new `change` with the investigation in `Sources`.

Every valid tracked issue has one `Status`:

- `ready` — no issue-local condition prevents the work from proceeding;
- `waiting` — continuation depends on an external event or decision;
- `done` — the issue-specific completion condition has been satisfied;
- `cancelled` — the work has been intentionally terminated without satisfying its completion condition.

`done` and `cancelled` are terminal. Later project work is represented by a new tracked issue; when a terminal issue directly motivates that work, record it in `Sources`.

Every valid tracked issue has an issue-specific, checkable completion condition. A valid `waiting` issue also records `Waiting for` (the external event or decision) and `Resume when` (a checkable condition for becoming ready again).

Skills may add sections they own, but must preserve unrelated content.

## Relations

- `Sources` is required direct provenance for every valid tracked issue. It may reference tracked issues or durable external/native sources; referencing a source does not make it tracked. `Sources` must not self-reference and does not imply hierarchy or dependency. Empty provenance is explicit.
- `Parent` is optional decomposition between tracked issues. Each issue has at most one parent; self-reference and cycles are forbidden. Completing all children does not complete the parent.
- `BlockedBy` is a scheduling dependency between tracked issues. Self-reference and cycles are forbidden. A `ready` issue with any unresolved blocker is blocked and not actionable; blocking is derived from `BlockedBy` and does not change the issue's `Status`. A blocker is resolved for scheduling only when it is `done`; `cancelled` does not satisfy dependents.

Repository taxonomy, source-specific ingestion and triage, execution coordination, migration, delivery policy, and issue-template UX are outside the tracker model. Contract versioning and upgrade gating belong to setup; migrations themselves remain outside the tracker model.
