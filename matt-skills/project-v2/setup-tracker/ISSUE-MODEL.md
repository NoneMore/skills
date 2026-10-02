# Issue model

This is the semantic contract for the tracker v2 prototype. Storage backends must preserve these meanings.

## 1. Issues and managed work

An issue may be either an intake signal or managed work.

**Intake signal**

An issue that reports an observation, asks for support, requests a feature, starts a discussion, or otherwise supplies project input. Intake issues may be externally authored and do not require a managed-work type.

Do not convert an external intake issue into managed work. External issues preserve reporter identity, wording, evidence, and discussion.

**Managed work**

An issue that maintainers have chosen to own as project work. Every managed-work issue has exactly one type.

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
- If an external issue requires project work, create or attach it to a separate managed issue instead of retyping the external issue.

## 4. Status

Status is orthogonal to type.

Canonical statuses:

- `needs-triage` — intake has not been evaluated yet.
- `needs-info` — progress requires information from a source/reporter.
- `ready` — managed work is sufficiently defined and can be claimed.
- `in-progress` — managed work is actively being worked.
- `blocked` — work cannot proceed until an explicit dependency or condition clears.
- `waiting` — no active work is needed until an external event completes.
- `done` — the issue's own completion condition is satisfied.
- `cancelled` — the issue will not be completed as defined.

Typical intake paths:

```text
needs-triage -> needs-info -> needs-triage
needs-triage -> waiting
needs-triage -> done
needs-triage -> cancelled
```

Typical managed-work paths:

```text
ready -> in-progress
in-progress -> blocked -> in-progress
in-progress -> waiting -> in-progress
in-progress -> done
ready|in-progress|blocked|waiting -> cancelled
```

These are normal paths, not a reason to invent more statuses. A workflow may require explicit human approval for unusual transitions.

Terminal statuses are `done` and `cancelled`.

## 5. Sources

`Sources` is direct provenance: the issues whose information or demand was used to define the current issue.

Examples:

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

A child is a constituent part of completing its parent. Any issue type may parent any issue type.

Do not use parent/child merely to group related issues. Use ordinary links, labels, milestones, or projects for grouping.

Child completion does not imply parent completion. The parent closes only when its own completion condition is satisfied.

## 7. Dependencies

`Blocked by` means scheduling dependency: the blocker must reach an acceptable terminal condition before the blocked issue can proceed.

Dependencies are independent from hierarchy and provenance. Never infer one relation from another.

## 8. Claiming

Assignee represents the active claim.

Do not create a second claim lifecycle field. A ready, unblocked managed issue with no active assignee is executable frontier work.

Status still describes lifecycle: claiming normally moves `ready` to `in-progress`; releasing or suspending work must leave a truthful status such as `ready`, `blocked`, or `waiting`.

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

An issue without a type is not managed work. Managed work has exactly one type.
