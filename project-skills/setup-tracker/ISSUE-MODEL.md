# Issue model

Backends represent this model; they do not redefine it.

## Classification

Only issues with explicit tracker state participate in the tracker. Repository-native issues or other external material may remain untracked until a workflow adopts or triages them.

- `Kind` — optional repository-defined issue category such as bug, feature, docs, or another project taxonomy value. The tracker does not prescribe a universal Kind vocabulary.
- `Type` — workflow semantics: `investigation` (resolve uncertainty), `change` (change observable state), or unset while the work is not yet classified.

Issue origin is not a tracker classification. External and internal input use the same tracked-work model. Do not copy or rewrite a source into a separate tracker issue solely to represent an intake boundary; when durable provenance exists, record it in `Sources`.

## Status and content

Status is explicit tracker state; backend open/closed state does not define it.

- `needs-triage` — the issue has entered the tracker but still needs normalization or classification.
- `ready` — the issue is actionable now. `Type` is required.
- `waiting` — continuation depends on an external event or decision.
- `done` — no further tracker action is required for this issue.

Whenever `Type` is set, the issue has an issue-specific, checkable completion condition. A `waiting` issue records both `Waiting for` (the external event or decision) and `Resume when` (a checkable condition for becoming actionable again).

Skills may add sections they own, but must preserve unrelated content.

## Relations

- `Sources` is required direct provenance for every tracked issue. It may reference tracked issues or durable external/native sources, and referencing a source does not make that source a tracked issue. `Sources` must not self-reference and does not imply hierarchy or dependency. Empty provenance is explicit.
- `Parent` is optional decomposition between typed tracked issues. Each issue has at most one parent; self-reference and cycles are forbidden. Completing all children does not complete the parent.
- `BlockedBy` is a scheduling dependency between typed tracked issues. Self-reference and cycles are forbidden.

Execution coordination (assignment, claiming, concurrency, ownership, frontier selection, orchestration), migration/versioning, delivery policy, source-specific ingestion, and issue-template UX are outside the tracker model.
