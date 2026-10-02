# Issue model

This is the authoritative semantic contract for the tracker v2 prototype. Storage backends define representation and operations; they must preserve these meanings rather than redefine them.

## 1. Intake and managed work

An issue is either external intake or managed work.

### External intake

External intake reports an observation, asks for support, requests a feature, starts a discussion, or otherwise supplies project input.

External intake remains untyped. Preserve the reporter's identity, wording, evidence, and discussion instead of converting the issue into managed work.

Triage may gather missing information and produce a recommendation. A maintainer then decides whether the project will act. If action is accepted, create or attach a separate managed issue and record the intake issue as a direct source.

### Managed work

Managed work is internally created project work whose proposer has already decided what the project should own.

Every managed issue has exactly one managed-work type and an issue-specific completion condition when it is created. Managed work does not pass through intake triage.

The presence of exactly one managed-work type is sufficient to identify an issue as managed work. There is no separate `managed` field.

## 2. Managed-work types

Exactly two types exist.

### `investigation`

Completion means that a material uncertainty has been resolved enough to stop investigating.

Examples:

- determine why login fails on Windows;
- determine whether an API can satisfy a requirement;
- determine what offline behavior the product should support;
- determine which migration approach should be adopted.

The result may be a finding, clarification, recommendation, or decision. Research, prototyping, discussion, experimentation, and code reading are methods, not types.

An investigation may produce zero, one, or many new issues. When it produces a change, create a new `change` issue with the investigation as a direct source. Never mutate the investigation into a change.

### `change`

Completion means that an observable state has been made different and the issue's own completion condition is satisfied.

Examples:

- fix a regression;
- add a feature;
- change configuration or infrastructure;
- update documentation;
- migrate data;
- remove deprecated behavior.

`change` is broader than code change.

## 3. Type invariants

- Type describes the required outcome, not the method used to reach it.
- There are no container issue types.
- Any managed issue may be decomposed into child issues of either type.
- Bug, feature, enhancement, docs, refactor, security, and similar classifications are optional repository taxonomy, not managed-work types.
- External classification never determines managed-work type.
- If external intake requires project work, create or attach it to a separate managed issue instead of retyping the intake issue.

## 4. Status

Status is orthogonal to type, but some statuses apply only to intake or only to managed work.

### Intake-only statuses

- `needs-triage` — external intake still needs maintainer evaluation or re-evaluation.
- `needs-info` — external intake cannot be evaluated because information is missing from the reporter or another source.

Managed work never uses `needs-triage` or `needs-info`: its proposer must resolve those questions before creating it.

### Managed-work statuses

- `ready` — managed work is decided, sufficiently defined, and can be claimed now.
- `in-progress` — managed work is actively being worked.
- `blocked` — managed work cannot proceed until an explicit prerequisite is completed or cleared.

Use `blocked` when there is a concrete prerequisite that must be acted on or completed, such as another issue. Use `waiting` instead when no work should happen until an external event or decision arrives.

### Shared lifecycle statuses

- `waiting` — no active work is needed now; the issue is waiting for an external event or human decision.
- `done` — the issue's own completion condition has been satisfied, or external intake has been fully addressed.
- `cancelled` — the issue will not be completed or acted on as defined.

For external intake, `waiting` may mean triage has produced a recommendation and is waiting for a maintainer decision, or that accepted downstream work is still in progress.

Typical intake paths:

```text
needs-triage -> needs-info -> needs-triage
needs-triage -> waiting
waiting -> needs-triage
waiting -> done
waiting -> cancelled
```

Typical managed-work paths:

```text
ready -> in-progress
ready -> blocked|waiting
in-progress -> blocked|waiting
blocked|waiting -> ready|in-progress
in-progress -> done
ready|in-progress|blocked|waiting -> cancelled
```

These are normal paths, not a reason to invent more statuses. Unusual transitions must still preserve the status meanings above.

Terminal statuses are `done` and `cancelled`.

## 5. Sources

`Sources` is direct provenance: the issues whose information or demand was used to define the current issue.

Example:

```text
#101 external report ----\
#117 external report -----+--> #150 investigation --> #166 change
#129 external report ----/
```

Rules:

- Sources are issue references, not workflow names.
- Record direct sources only. Do not copy transitive sources forward.
- Sources may be many-to-many.
- A maintainer-initiated issue may have no sources.
- Multiple external reports may source one investigation.
- One investigation may source many changes.
- A later external report may be added as another direct source when it supplies evidence for the same managed issue.
- Source relationships do not imply hierarchy or blocking.

## 6. Hierarchy

Parent/child means decomposition.

A child is a constituent part of completing its parent. Any managed issue type may parent either managed issue type.

Do not use parent/child merely to group related issues. Use ordinary links, labels, milestones, or projects for grouping.

Child completion does not imply parent completion. The parent closes only when its own completion condition is satisfied.

## 7. Dependencies

`Blocked by` means scheduling dependency: the blocker must reach an acceptable terminal condition before the blocked issue can proceed.

Dependencies are independent from hierarchy and provenance. Never infer one relation from another.

## 8. Claiming

Assignee represents the active claim.

Do not create a second claim lifecycle field. A `ready` managed issue with no active assignee is executable frontier work.

Claiming normally moves `ready` to `in-progress`. Releasing or suspending work must leave a truthful status such as `ready`, `blocked`, or `waiting`.

## 9. Closing and reconciliation

A managed issue reaches `done` only when its own completion condition is satisfied. Completing all children is evidence, not proof.

External source issues are reconciled independently. A completed managed issue may justify closing a source issue, but closure is not automatic: the source issue's report or request must actually be addressed.

## 10. Model summary

```text
Issue
├── Type?          investigation | change
├── Status         lifecycle
├── Sources[]      direct provenance
├── Parent?        decomposition
├── BlockedBy[]    scheduling dependency
├── Assignee?      active claim
└── Body/comments  contract, evidence, outcome
```

An issue without a type is external intake. Managed work has exactly one type.
