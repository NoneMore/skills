# Issue model

Backends represent this model; they do not redefine it.

## Membership and validity

Each backend defines tracker membership. Membership and validity are separate: malformed or incomplete tracked work remains tracked but invalid until repaired or removed.

Issue origin is not tracker state. Uncontrolled/native issues may remain outside the tracker unless a workflow adopts them.

## Work

Every valid tracked issue has one immutable `Type`:

- `investigation` — resolve uncertainty;
- `change` — change observable state.

Do not change `Type`. When a completed investigation implies implementation work, finish it and create a new `change` with the investigation in `Sources`.

Every valid tracked issue has one `Status`:

- `ready` — actionable now;
- `waiting` — continuation depends on an external event or decision;
- `done` — no further tracker action is required.

Every valid tracked issue has an issue-specific, checkable completion condition. A valid `waiting` issue also records `Waiting for` (the external event or decision) and `Resume when` (a checkable condition for becoming actionable again).

Skills may add sections they own, but must preserve unrelated content.

## Relations

- `Sources` is required direct provenance for every valid tracked issue. It may reference tracked issues or durable external/native sources; referencing a source does not make it tracked. `Sources` must not self-reference and does not imply hierarchy or dependency. Empty provenance is explicit.
- `Parent` is optional decomposition between tracked issues. Each issue has at most one parent; self-reference and cycles are forbidden. Completing all children does not complete the parent.
- `BlockedBy` is a scheduling dependency between tracked issues. Self-reference and cycles are forbidden.

Repository taxonomy, source-specific ingestion and triage, execution coordination, migration/versioning, delivery policy, and issue-template UX are outside the tracker model.
