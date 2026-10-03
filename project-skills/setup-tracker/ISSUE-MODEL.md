# Issue model

Authoritative semantics for the tracker. Backend documents define representation only.

<!-- repository-contract:start -->

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

## Managed-work content

Every managed issue must state an issue-specific, checkable completion condition.

The issue body should contain only context that helps define or execute the work. Do not duplicate tracker metadata such as type, status, sources, hierarchy, dependencies, or claim in the body when the backend has a canonical representation for those dimensions.

Skills that create or execute managed work may add structured sections for information they own. Examples include execution notes, implementation results, investigation conclusions, evidence, experiments, or handoff material.

Skill-owned sections are extensions of the managed issue, not tracker dimensions. A skill may create and update the sections it owns, but must preserve unrelated sections and content owned by other skills. The tracker contract does not require every managed issue to contain every extension section.

Extension sections must not redefine the issue's type, lifecycle status, provenance, hierarchy, dependencies, claim, or completion condition.

## Status

Status is lifecycle only. Claiming and dependencies are separate dimensions.

Every issue has exactly one semantic lifecycle status. A backend may derive a status when its representation makes that status unambiguous; otherwise it must store the status explicitly. Managed work must always store its status explicitly.

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

## Sources

`Sources` is direct provenance: issues whose information or demand was used to define the current issue.

- Record direct sources only, not transitive sources.
- Sources may be many-to-many or empty.
- Sources do not imply hierarchy or dependency.

## Hierarchy

Parent/child means decomposition: a child is part of completing its parent.

Do not use hierarchy merely to group related issues. Completing all children does not itself complete the parent.

## Dependencies

`BlockedBy` records scheduling dependencies. A blocker is live while its referenced issue is non-terminal.

Dependencies are independent from hierarchy and provenance.

## Claim

Assignee is the claim mechanism. Do not add another execution-state field.

Claim is independent from status and dependencies.

## Frontier

Executable frontier work is managed work that is `ready`, unclaimed, and has no live blocker.

Frontier is derived, not stored.

## Reconciliation

External intake is closed independently from managed work. Completing managed work may justify closing a source issue, but only when that source has actually been addressed.

<!-- repository-contract:end -->
