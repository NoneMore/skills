# Issue model

Backends represent this model; they do not redefine it.

Contract version: `2`.

Issue origin is not tracker state. Uncontrolled/native issues remain outside the tracker; workflows may create tracked work with those issues recorded in `Sources`.

## Work

Every tracked issue has one immutable `Type`:

- `investigation` — its completion condition establishes an answer, evidence, or decision that resolves uncertainty;
- `change` — its completion condition establishes an observable state change. Analysis or discovery performed to make that change does not make the work an investigation.

Choose `Type` from what satisfying the completion condition produces, not from how much uncertainty exists while doing the work. Do not change `Type`. When a completed investigation implies implementation work, finish it and create a new `change` with the investigation in `Sources`.

Every tracked issue has one `Status`:

- `ready` — no issue-local condition prevents the work from proceeding;
- `waiting` — no project-local action can advance the work until a named external event or decision occurs;
- `done` — the issue-specific completion condition has been satisfied;
- `cancelled` — the work has been intentionally terminated without satisfying its completion condition.

`done` and `cancelled` are terminal. Later project work is a new tracked issue; when a terminal issue directly motivates that work, record it in `Sources`.

Every tracked issue has an issue-specific, checkable completion condition. A `waiting` issue also records `Waiting for` (the named external event or decision) and `Resume when` (a condition that can be checked directly as true or false). Do not use `waiting` merely because the next step is uncertain or requires more analysis.

Skills may add sections they own, but must preserve unrelated content.

## Relations

- `Sources` is required direct provenance. It may reference tracked issues or durable external/native sources; referencing a source does not make it tracked. `Sources` must not self-reference and does not imply hierarchy or dependency. Empty provenance is explicit.
- `Parent` is optional decomposition between tracked issues. Each issue has at most one parent; self-reference and cycles are forbidden. Completing all children does not complete the parent. An issue with any tracked child is not an execution leaf; after decomposition, any remaining directly executable work must be represented by a child.
- `BlockedBy` is a scheduling dependency between tracked issues. Self-reference and cycles are forbidden. A `ready` issue with any unresolved blocker is blocked and not actionable; blocking does not change `Status`. A blocker is resolved for scheduling only when it is `done`; `cancelled` does not satisfy dependents.

Repository taxonomy, source-specific ingestion and triage, execution coordination, migration, delivery policy, and issue-template UX are outside the tracker model. Contract versioning and upgrade gating belong to setup; migrations themselves remain outside the tracker model.
