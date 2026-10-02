# Issue model

Authoritative semantics for tracker v2. Backend documents define representation only.

## Intake and managed work

An issue is either external intake or managed work.

**External intake** is project input from outside the managed-work flow: reports, requests, support questions, or discussion. Keep it untyped and preserve the original reporter, wording, evidence, and discussion.

Triage may gather missing information and make a recommendation. A maintainer decides whether the project will act. Accepted work is represented by a separate managed issue that records the intake issue as a direct source.

**Managed work** is internally created work whose proposer has already decided what the project should own. It is created with exactly one type and an issue-specific completion condition. It does not pass through intake triage.

An issue with exactly one managed-work type is managed work. An issue without one is intake.

## Types

Exactly two managed-work types exist:

- `investigation` — complete when a material uncertainty is resolved enough to stop investigating;
- `change` — complete when an observable state has changed and the issue's completion condition is satisfied.

Type describes the required outcome, not the method. Research, prototyping, discussion, experimentation, and code reading are methods.

An investigation never becomes a change. If investigation produces work that changes state, create a new `change` issue sourced from the investigation.

Repository taxonomy such as bug, feature, docs, refactor, or security is independent from managed-work type.

## Status

Status is lifecycle only. Claiming and dependencies are separate dimensions.

Intake may use:

- `needs-triage` — maintainer evaluation is still needed;
- `needs-info` — evaluation is waiting on missing information;
- `waiting` — no action is needed until an external event or human decision;
- `done` — the intake has been addressed;
- `cancelled` — the project will not act on it as defined.

Managed work may use:

- `ready` — the work is defined and remains live;
- `waiting` — no action is needed until an external event or human decision;
- `done` — its completion condition is satisfied;
- `cancelled` — it will not be completed as defined.

`done` and `cancelled` are terminal.

Whether a `ready` issue is executable is derived from its assignee and blockers, not from status.

## Sources

`Sources` is direct provenance: issues whose information or demand was used to define the current issue.

- Record direct sources only, not transitive sources.
- Sources may be many-to-many or empty.
- Sources do not imply hierarchy or dependency.

## Hierarchy

Parent/child means decomposition: a child is part of completing its parent.

Do not use hierarchy merely to group related issues. Completing all children does not itself complete the parent.

## Dependencies

`BlockedBy` records scheduling dependencies. An issue is executable only when none of its blockers is non-terminal.

Dependencies are independent from hierarchy and provenance.

## Claim

Assignee is the claim mechanism. Do not add another execution-state field.

A claimed issue may still have blockers; claim and dependency are independent.

## Reconciliation

External intake is closed independently from managed work. Completing managed work may justify closing a source issue, but only when that source has actually been addressed.
