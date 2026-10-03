# Issue model

Authoritative semantics for the tracker. Backend documents define representation only.

<!-- repository-contract:start -->

## Tracked issues and classification

Only issues that a backend explicitly classifies as tracker issues participate in this contract. An unclassified repository issue is outside the tracker: do not infer tracker meaning from missing labels, missing fields, open/closed state, author, age, or historical usage.

Setup never classifies, adopts, or migrates pre-existing unclassified issues. Bringing existing work under this contract is a separate migration or takeover workflow.

Every tracked issue has exactly one kind:

- **intake** — project input from outside the managed-work flow: reports, requests, support questions, or discussion;
- **managed** — internally created work whose proposer has already decided what the project should own.

External intake preserves the original reporter, wording, evidence, and discussion. Triage may gather missing information and make a recommendation. A maintainer decides whether the project will act. Accepted work is represented by a separate managed issue that records the intake issue as a direct source.

Managed work is created with exactly one managed-work type and an issue-specific completion condition. It does not pass through intake triage.

Kind is independent from type, status, sources, hierarchy, dependencies, and claim. Missing or contradictory classification metadata is invalid tracker state; never reinterpret it as another kind.

## Types

Exactly two managed-work types exist:

- `investigation` — complete when a material uncertainty is resolved enough to stop investigating;
- `change` — complete when an observable state has changed and the issue's completion condition is satisfied.

Only managed work has a managed-work type, and it has exactly one. Intake has no managed-work type.

Type describes the required outcome, not the method. Research, prototyping, discussion, experimentation, and code reading are methods.

An investigation never becomes a change. If investigation produces work that changes state, create a new `change` issue sourced from the investigation.

Repository taxonomy such as bug, feature, docs, refactor, or security is independent from managed-work type.

## Managed-work content

Every managed issue must state an issue-specific, checkable completion condition.

The issue body should contain only context that helps define or execute the work. Do not duplicate tracker metadata such as kind, type, status, sources, hierarchy, dependencies, or claim in the body when the backend has a canonical representation for those dimensions.

Skills that create or execute managed work may add structured sections for information they own. Examples include execution notes, implementation results, investigation conclusions, evidence, experiments, or handoff material.

Skill-owned sections are extensions of the managed issue, not tracker dimensions. A skill may create and update the sections it owns, but must preserve unrelated sections and content owned by other skills. The tracker contract does not require every managed issue to contain every extension section.

Extension sections must not redefine the issue's kind, type, lifecycle status, provenance, hierarchy, dependencies, claim, or completion condition.

## Status

Status is lifecycle only. Claiming and dependencies are separate dimensions.

Every tracked issue has exactly one explicit lifecycle status. Backends must store it explicitly; open/closed state or missing metadata must not be used to derive lifecycle status.

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

`done` and `cancelled` are terminal. Once an issue reaches either terminal status, it must not transition to any different lifecycle status under this contract. Reopening or changing a terminal outcome requires an explicit migration or repair workflow outside ordinary tracker operations; repeating the same terminal status is idempotent.

### Waiting contract

Managed work in `waiting` must record both what it is waiting for and a checkable resume condition. Backends define the representation, but the semantic content is:

- **Waiting for:** the external event or human decision that currently requires no project action;
- **Resume when:** the condition whose satisfaction makes the issue actionable again.

This waiting metadata is required managed-work content, not a tracker dimension. When the resume condition becomes true, move the issue to `ready` unless it has instead become `done` or `cancelled`. Managed work that is not `waiting` must not retain active waiting metadata.

## Sources

`Sources` is direct provenance: issues whose information or demand was used to define the current issue.

- Record direct sources only, not transitive sources.
- Sources may be many-to-many or empty.
- A source must reference an existing tracked issue and must not reference the current issue itself.
- Sources do not imply hierarchy or dependency.

## Hierarchy

Parent/child means decomposition: a child is part of completing its parent.

Only managed work participates in hierarchy. Intake may be a source of managed work but cannot be a parent or child.

Each managed issue has at most one parent. Parent relationships must reference existing managed issues, must not self-reference, and must not form cycles.

Do not use hierarchy merely to group related issues. Completing all children does not itself complete the parent.

## Dependencies

`BlockedBy` records scheduling dependencies. A blocker is live while its referenced issue is non-terminal.

Only managed work participates in dependency relationships. A blocker and blocked issue must both be managed work. Dependencies must reference existing issues, must not self-reference, and must not form cycles.

Dependencies are independent from hierarchy and provenance.

## Claim

For managed work, assignee is the execution claim. It means "this actor is currently executing this issue", not long-lived ownership. Do not add another execution-state field.

Managed work has at most one assignee. Intake assignees, when a backend permits them, are ordinary repository metadata and are not tracker claims.

The execution model does not permit concurrent top-level execution of the same managed issue. A runtime must serialize attempts to execute the same issue. Subagents operate inside the claiming execution and do not acquire independent claims on that issue.

A managed issue may be claimed only when it is `ready` and has no live blocker. Claim acquisition is coordination rather than a distributed lock: after acquiring a claim, re-read the issue and begin or continue consequential execution only while the current actor remains the sole assignee and the issue remains `ready` with no live blocker. If a conflicting claimant is observed, do not continue execution and release only the current actor's claim when possible.

Release the claim when execution stops, when handing work off, or before moving the issue out of `ready`. Claim is independent from hierarchy and provenance.

## Frontier

Executable frontier work is managed work that is `ready`, unclaimed, and has no live blocker.

Frontier is derived, not stored.

## Reconciliation

External intake is closed independently from managed work. Completing managed work may justify closing a source issue, but only when that source has actually been addressed.

<!-- repository-contract:end -->
