# Matt tracker contract

This document is the authoritative provider-independent contract for tracker semantics used by the Matt engineering skills.

Provider adapters such as `issue-tracker-github.md`, `issue-tracker-gitlab.md`, and `issue-tracker-local.md` define how these capabilities are represented and operated on for a concrete tracker. They must not redefine the provider-independent meaning below.

Workflow skills remain authoritative for workflow-specific payload semantics. For example, this contract requires an Implementation Result capability, while `implement` defines the fields and lifecycle meaning of that result; this contract requires a Reconciliation Result capability, while `reconcile` defines the meaning of its values.

## Design principles

Tracker semantics are orthogonal unless this contract explicitly defines a derivation.

In particular:

- work-item role does not imply triage state, tracker state, execution coordination, provenance, hierarchy, blocking, or Wayfinder lifecycle;
- triage state does not imply tracker open/closed state or execution coordination;
- blocking does not mutate triage state;
- claiming or suspension does not mutate triage state;
- tracker closure does not by itself determine Implementation Result or Reconciliation Result payload semantics;
- Wayfinder ticket type and Wayfinder lifecycle are separate from work-item role and triage state.

Do not collapse these dimensions into one provider-specific status field.

The shared semantic model currently uses the term **work-item role** for `request | decision-map | decision-ticket | spec | implementation-ticket`. Do not globally rename this to `type` in provider storage: local Wayfinder tickets already use `Type:` for `research | prototype | grilling | task`. A future representation migration may change names, but that is separate from this contract extraction.

## Work item capabilities

A configured tracker must provide readable and writable representations for the following capabilities.

### Identity and basic operations

- stable work-item identity within the configured tracker/project;
- create, read, list/search, and comment/note;
- apply and remove configured triage state;
- terminal close/reject operation;
- external-request discovery, or an explicit `unsupported` declaration.

### Work-item role

The tracker must read and write exactly one canonical work-item role when a participating item has one:

- `request`
- `decision-map`
- `decision-ticket`
- `spec`
- `implementation-ticket`

Role is classification, not lifecycle.

### Direct provenance

The tracker must read and write zero or more direct `derived-from` sources on the derived artifact.

A direct source is an artifact used as input to create the current artifact. Do not recursively expand a source's own provenance when reading or writing this relation.

### Hierarchy

The tracker must create and read parent-child relationships.

Hierarchy answers which larger work item a child belongs to. It does not imply blocking, provenance, readiness, or closure.

### Blocking

The tracker must create and read blocking relationships.

An item is **unblocked** when none of its blockers is still semantically open for the relevant workflow. Blocking is a relation; `blocked` is derived and must not be maintained as a second lifecycle status merely to mirror that relation.

### Triage state

The tracker must read and write the configured canonical triage role:

- `needs-triage`
- `needs-info`
- `ready-for-agent`
- `ready-for-human`
- `wontfix`

Repositories may map these roles to different concrete labels/fields through `docs/agents/triage-labels.md`.

Triage state is independent from tracker open/closed state and execution coordination.

### Tracker state

The tracker must expose whether a work item is open or terminal and provide an idempotent terminal operation.

A provider may project several semantic terminal reasons onto one native `closed` state. Consumers must not infer a richer Matt lifecycle meaning from a provider's coarse open/closed field unless the owning workflow defines that inference.

## Implementation execution

These capabilities are consumed primarily by `implement`.

### Execution coordination

The tracker must provide:

- **claim**: acquire the item for the current actor/session;
- **release**: remove the active claim while leaving the item otherwise executable if no other condition excludes it;
- **suspend**: leave the item resumable but outside the execution frontier, and release any active claim;
- **resume ordering**: when resuming suspended work, acquire the claim before removing suspension so another actor cannot enter the frontier in between.

Claim, release, and suspend are coordination state, not triage state.

A claim operation is not considered successful merely because a write command returned success. The configured adapter must define a readback that verifies the persisted owner/claim representation. If another actor owns the item after readback, the claim failed and the workflow must not proceed as owner.

### Execution eligibility and frontier

Execution eligibility and frontier are **derived views**, not independently maintained lifecycle states.

For normal implementation work, an item is eligible only when all of the following are true:

1. its role is `request`, `spec`, or `implementation-ticket`;
2. its canonical triage state is `ready-for-agent`;
3. its tracker state is open;
4. it has no unresolved blocker;
5. it is not claimed by another actor;
6. it is not suspended;
7. it is an execution leaf.

A `spec` with any `implementation-ticket` child is not an execution leaf. Explicitly named items may still be read for resume or finalization even when they are not currently in the frontier.

The **execution frontier** is the provider's ordered set of items satisfying these predicates. Providers may differ in how they enumerate candidates, but not in the semantic predicates.

Do not persist `eligible`, `frontier`, or `blocked` as duplicate status values when they can be derived from canonical facts.

### Implementation Result storage

The tracker must provide a unique readable/upsertable Implementation Result per participating work item.

The storage representation must support idempotent re-entry: rerunning `implement` updates the canonical result instead of appending ambiguous duplicates.

`implement` owns the result schema and lifecycle meaning, including values such as `awaiting-delivery` or `delivered`.

### Repository delivery policy and evidence

Repository configuration must record:

- delivery mode;
- target branch;
- publication operation when delivery uses a PR/MR-like surface;
- concrete evidence operation proving that the implementation reached the configured target.

`implement` consumes this policy and must not invent provider-specific delivery rules.

Delivery evidence is independent from tracker open/closed state. A workflow may record an Implementation Result before terminal tracker mutation.

### Terminal operation

The tracker must provide an idempotent terminal operation.

For implementation execution this operation must, at minimum, place the tracker item in its provider terminal state and clear execution coordination that would otherwise leave the item claimed or suspended.

The workflow that owns semantic completion decides when to invoke the terminal operation. Provider adapters only define how the operation is realized.

## Upstream reconciliation

These capabilities are consumed primarily by `reconcile`.

### Reconciliation Result storage

The tracker must provide a unique readable/upsertable Reconciliation Result per participating work item.

The storage representation must support idempotent re-entry.

`reconcile` owns the result schema and the semantics of values such as `waiting | satisfied | unsatisfied`.

### Source-keyed upstream notes

For each direct provenance source, the tracker must provide an upsertable note keyed by the reconciling downstream artifact.

Repeating reconciliation for the same source/downstream pair must update the same semantic note rather than append a new ambiguous copy.

## Wayfinder specialization

Wayfinder uses the shared hierarchy, blocking, claim, and verification capabilities, but has its own ticket classification and lifecycle.

A Wayfinder effort consists of:

- one **map**;
- ordered **child tickets** associated with that map;
- ticket type `research | prototype | grilling | task`;
- a Wayfinder lifecycle that can represent open, claimed, resolved, and closed.

Wayfinder ticket type is not the Matt work-item role. Wayfinder lifecycle is not triage state.

The Wayfinder frontier is derived from the map's ordered children: candidates are open children that have no unresolved blocker and are unclaimed; the first candidate in map order wins.

Resolving a ticket persists its answer/result, moves it to the resolved terminal-for-frontier state, and records the required context pointer on the map. Closing a ticket as out of scope is distinct from resolving it with an answer.

Provider adapters define how maps, child ordering, ticket type, lifecycle, blocking, claims, and result/context writes are represented.

## Post-mutation verification

Every mutation used by downstream skills must have a concrete readback/verification path.

After a mutation, the consumer must be able to verify the canonical persisted state that matters to the operation, including as applicable:

- role or triage state;
- provenance or relationship;
- claim/release/suspension state;
- canonical result upsert;
- delivery evidence;
- terminal tracker state;
- source-keyed reconciliation note;
- Wayfinder lifecycle/result.

A command's successful exit is not a substitute for verifying the semantic state when the provider can race, normalize, reject, or partially apply the requested mutation.

## Provider adapter boundary

A provider adapter should primarily answer:

- where each contract capability is stored;
- how to read it;
- how to mutate it;
- how to verify the mutation;
- which provider feature is canonical and what fallback is used when that feature is unavailable.

It should not redefine:

- what a work-item role means;
- whether role implies lifecycle state;
- what makes implementation work eligible;
- what `blocked`, `claimed`, or `suspended` mean semantically;
- the payload semantics owned by `implement` or `reconcile`;
- the provider-independent Wayfinder frontier rule.

When an adapter cannot realize a required capability, configuration must say so explicitly rather than forcing downstream skills to invent behavior.
