---
name: engineering-initiative-shaping
description: "Explicit Large-workload orchestration for discussing and brainstorming an initiative, stabilizing macro requirements and governing design, then splitting it into Medium-sized requirements. Never infer Large from complexity, architecture scope, file count, risk, or apparent effort."
disable-model-invocation: true
metadata:
  version: "v5-rc.1"
  invocation: "user"
---

# Engineering Initiative Shaping

Shape a user-declared **Large** engineering initiative into a trustworthy macro direction and a set of Medium-sized requirements that can be handled independently by downstream orchestration.

The objective is not to solve the whole initiative in one context. The objective is to make the initiative **decomposable without accidental product or architecture decisions**.

## Invocation contract

This is an **explicit orchestration mode**. It may be selected directly by the user or by an upstream Meta-Agent acting under user-selected/configured workload policy, normally because that upstream layer has already classified the work as Large.

Never infer Large or invoke this mode merely because:

- the task looks difficult;
- many files/modules are involved;
- the repository is large;
- architecture is relevant;
- risk or uncertainty is high;
- one executor would personally prefer more planning.

Large is a user-specific capacity envelope, not a complexity score. This Skill must not reclassify the request.

Invocation does not grant code/VCS/deployment/publication/credential authority.

## Large is not bootstrap

A Large initiative may occur in a mature system whose foundations remain valid. Do not enter `engineering-foundation-design` merely because this mode is active.

Bootstrap is appropriate only when foundational architecture itself is explicitly being established or materially reset. Large shaping and bootstrap may compose when both are explicitly selected, but neither implies the other.

## Start from destination, not tasks

Establish at macro granularity:

- the destination/outcome and why it matters;
- material non-goals;
- important existing constraints and invariants;
- compatibility, migration, data, safety, security, operational, or organizational boundaries;
- what must remain stable during the initiative;
- what success would look like across phases.

Inspect repository evidence before asking the user for facts. Ask about consequential intent and trade-offs that evidence cannot settle.

## Discuss and brainstorm before fixing the route

Large work often contains decision fog. Explore enough alternatives to expose consequential branches before locking the macro design.

Useful discussion may include:

- alternative target architectures or migration shapes;
- major seam/ownership choices;
- compatibility strategies;
- sequencing strategies that change risk or reversibility;
- research/prototype questions whose answers materially affect the route;
- operational cutover or coexistence models;
- constraints that could invalidate an attractive direction.

Do not brainstorm indefinitely. Distinguish:

- **accepted governing decisions**;
- **rejected alternatives worth remembering only if they prevent repeat debate**;
- **open consequential decisions** that need evidence or decision-owner input.

For empirical questions, use `engineering-investigation` when available; otherwise run bounded, safe probes with falsifiable hypotheses and report evidence and limitations. Investigation grants no persistent implementation authority.

## Macro specification

Once enough direction is accepted, establish a written macro specification at the level needed to constrain downstream Medium requirements. Use `engineering-specification` when available and useful; otherwise use the macro contract below directly.

The macro specification should capture only initiative-wide truths such as:

- target outcome and non-goals;
- governing architecture/design direction;
- cross-phase invariants and contracts;
- compatibility/migration policy;
- phase boundaries or stable seams;
- acceptance principles and important negative constraints;
- unresolved decisions that intentionally remain for later phases.

Do not pre-design every Medium requirement. Leave bounded phase-local decisions to the later specification workflow.

## Split by Medium capacity, not by architecture layer

The output of Large shaping is a set of requirements that the upstream system can treat as **Medium** according to the user's capacity policy.

Prefer boundaries that:

- produce independently meaningful progress or de-risk a later phase;
- have explicit outcomes and acceptance behaviour;
- minimize unnecessary shared mutable scope;
- expose real dependency edges;
- preserve a safe intermediate system state;
- keep initiative-wide Fixed decisions explicit;
- leave phase-local design questions resolvable inside the Medium workflow.

Do not claim a unit is Medium based on LOC, file count, or model intuition. Use the supplied upstream capacity policy to propose boundaries; the upstream user/Meta-Agent owns classification and acceptance. If that policy is absent, produce candidate units with explicit outcomes/dependencies, mark capacity acceptance pending, and request the missing capacity decision before claiming shaping complete. Continue useful macro-design work while that decision is pending.

## Research and decision tickets

Some Large initiatives are blocked by unknowns rather than implementation volume. It is valid to emit a Medium-sized investigation or design-resolution requirement instead of pretending the implementation route is known.

A phase may therefore be:

- an implementation requirement;
- a migration/coexistence requirement;
- an investigation/prototype requirement;
- a compatibility or operational decision requirement;
- a validation/cutover requirement.

The key is that each output has a bounded outcome and enough governing context to enter the Medium workflow.

## Persistence and knowledge governance

Large shaping commonly creates initiative-wide durable design decisions. Persist only accepted knowledge that future phases need, in canonical locations. Keep brainstorm transcripts and superseded route sketches transient unless they have lasting explanatory value.

For concrete lifecycle decisions, use `engineering-knowledge-governance` when available; otherwise update the existing canonical home within task authority, distinguish accepted target state from current state, and reconcile obsolete claims.

Phase plans remain downstream coordination artifacts; do not create one giant permanent master-plan narrative that future truth must be synchronized against.

## Handoffs

At an actual shaping handoff, use `engineering-handoff` when available; otherwise carry governing decisions, current state, remaining questions/work, evidence/gaps, canonical sources, and the next action. The existence of many future phases is not itself a handoff.

## Exit condition

Large shaping is complete when:

- the macro destination and initiative-wide constraints are explicit;
- enough governing design is accepted to prevent phases from independently inventing incompatible foundations;
- remaining consequential unknowns are explicit and assigned to bounded future requirements rather than hidden;
- the initiative is divided into units the upstream user/Meta-Agent accepts as Medium-sized;
- each unit has a meaningful outcome, key dependencies, governing sources/decisions, and acceptance intent sufficient to begin the Medium specification workflow;
- there is no need to create a giant detailed execution plan for the entire initiative.

**Stop here.** Downstream Medium workflows own detailed specification, planning, handoff, execution, and acceptance for each unit.
