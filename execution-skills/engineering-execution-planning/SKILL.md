---
name: engineering-execution-planning
description: "Create or revise a concrete engineering execution plan from accepted intent and governing design. Use only when planning is explicitly requested or selected by an upstream orchestration mode; never infer planning from task size or complexity alone."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Execution Planning

Turn accepted engineering intent into an executable coordination plan without reopening settled product or architecture decisions.

This is a reusable planning discipline. It does not classify workload size and does not own delegation by itself.

## Invocation boundary

Invoke when:

- the user explicitly asks for an execution plan; or
- an upstream orchestration mode explicitly requests planning after specification/design has been accepted, including the bundle's Medium workflow; or
- `engineering-plan-and-delegate` composes this discipline as part of an explicit delegation workflow.

Do **not** invoke merely because work is large, complex, multi-file, risky, or likely to benefit from planning. Leaf Skills must never infer Small/Medium/Large.

If consequential product, architecture, compatibility, data, security, or operational decisions remain unresolved, return them to specification/shaping rather than hiding them inside execution tasks.

A useful plan makes executable units, real dependencies, verification points, decision budgets, and re-planning conditions clear. Avoid restating the specification.

## Ground the plan

Before decomposing work, inspect the smallest authoritative set of sources needed to understand:

- current implementation seams and ownership;
- accepted specification/design and relevant contracts;
- tests, build/runtime topology, migration constraints, and repository conventions;
- shared mutable areas that affect parallelism;
- dependencies whose ordering is real rather than imagined.

Use repository evidence to settle facts before asking users questions.

## Plan shape

Prefer the lightest plan that preserves safe execution.

Good execution units are usually:

- bounded by an observable outcome or meaningful prerequisite;
- independently verifiable when practical;
- small enough for the intended executor/context boundary;
- explicit about real dependencies;
- narrow in shared mutable scope when parallel execution is intended.

Prefer vertical slices over horizontal layer batches when a vertical result can be verified independently. Mechanical wide refactors may instead use expand–migrate–contract or another repository-appropriate staged shape.

Do not manufacture dependencies merely to make the plan look ordered.

## Decision budget

For each non-trivial unit distinguish, at the lightest useful level:

- **Fixed** — accepted product, architecture, contract, compatibility, scope, or risk decisions that execution must preserve.
- **Local** — reversible implementation mechanics the executor owns.
- **Open** — unresolved consequential decisions that block bounded execution and must escalate.

A plan that depends on an executor silently resolving Open decisions is not ready.

For explicitly assigned research, an Open question may be the work's objective. Bound the probes, evidence, stopping condition, and decision owner; the chosen implementation design need not exist before planning that investigation. Unresolved choices that prevent safe probes still block those probes.

## Verification planning

Attach proof obligations to the behaviour or invariant they support. Plan for both:

- **positive evidence** — the intended behaviour or outcome exists; and
- **negative evidence** — important forbidden states did not appear, such as regression, design/contract violation, accidental scope expansion, weakened invariants, or unnecessary complexity.

Do not substitute broad test commands for direct evidence when they do not exercise the claimed behaviour.

## Written continuity for Medium work

Only when the upstream layer explicitly selects the **Medium profile** and assigns this Skill responsibility for its written plan does that profile require a continuity-capable plan before implementation. Reference the accepted written specification supplied by the specification owner. If that required input is missing, report the missing prerequisite to the upstream owner; do not silently take over specification work.

A Medium capacity label alone creates no artifact requirement. An explicit request to revise a plan with that label does not require creating or rewriting a specification. For ordinary planning, accepted intent/design can be supplied in the conversation; no separate specification file is mandatory.

Use the repository's existing coordination convention. Do not invent a permanent task-document hierarchy. Plans remain transient by default and should be retired, archived, or reconciled when their coordination value ends.

For an ordinary explicit planning request with no Medium orchestration requirement, persistence is based on actual continuity needs rather than task appearance.

## Handoff boundaries

This Skill may identify handoff points. At an actual cross-agent/model/session/context boundary, use `engineering-handoff` when available. Otherwise carry outcome/scope, governing sources, decision budget, dependencies, current state, remaining work, observed evidence/gaps, and the next action in the receiving message.

Do not create work packages for hypothetical delegation. Planning says what could be executed; a work package defines the receiving contract when execution actually crosses the boundary.

## Re-planning

The plan is a coordination hypothesis, not authority over contradictory evidence.

Re-plan or escalate when execution evidence shows that continuation requires:

- changing a Fixed decision;
- materially widening scope;
- changing an unauthorized public/compatibility contract;
- accepting a new consequential risk;
- violating the accepted specification/design;
- adding a prerequisite the current plan fundamentally omitted.

Local mechanics may change without formal re-planning when outcome, scope, fixed decisions, and verification obligations remain intact.

For a reported capacity mismatch, distinguish changed effort estimates from changes to governing design. Present the evidence, remaining work including verification, uncertainty, and options to continue, adjust capacity, split/defer, or pause to the user or authorized upstream owner. Revise only the assigned plan under the owner's decision; reuse valid work and evidence. Neither receiving the report nor its apparent complexity authorizes reclassification, a new orchestration mode, reduced acceptance criteria, or exceeding existing limits. Carry supplied hard limits and pending capacity decisions into actual handoffs.

## Exit condition

Planning is complete when the intended executor(s) can begin without reconstructing consequential intent, the real dependency graph is explicit enough for coordination, verification obligations are clear, and remaining choices are bounded Local decisions rather than hidden product/architecture choices.
