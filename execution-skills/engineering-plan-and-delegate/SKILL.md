---
name: engineering-plan-and-delegate
description: "Explicit orchestration mode for turning accepted engineering intent into a concrete execution plan and, when real handoffs occur, delegated work packages. May choose direct execution without decomposition or delegation. Never auto-invoke from task size, workload class, complexity, or multi-file scope."
disable-model-invocation: true
metadata:
  version: "v5-rc.1"
  invocation: "user"
---

# Engineering Plan and Delegate

Deliberately enter planning/decomposition/delegation mode while keeping reusable planning and handoff disciplines separate.

## Invocation contract

This is an **explicit orchestration skill**. It may be selected directly by the user or by an upstream Meta-Agent acting under user-selected/configured policy.

Preserve upstream capacity labels; neither a label nor apparent complexity or potential parallelism authorizes this mode. Require an explicit orchestration choice.

This skill grants no repository mutation, VCS, deployment, publication, credential, or other external-effect authority.

## Orchestration responsibilities

This Skill owns only three decisions:

1. Is the accepted intent ready for execution planning, or does consequential ambiguity still belong in specification/design?
2. What planning/decomposition strategy is appropriate for the requested orchestration mode?
3. Where is an **actual** execution handoff occurring?

Use the reusable disciplines for the details:

- when available, use `engineering-execution-planning` to create/revise the concrete plan;
- when available, use `engineering-handoff` at actual cross-agent/model/session/context/executor handoffs;
- use `engineering-knowledge-governance` when available and persisted state creates a concrete lifecycle decision.

Load a named skill through the runtime's supported skill mechanism only when its trigger holds. If a companion is unavailable, use the bounded fallback here: plan observable units, real dependencies, fixed constraints, and verification; at an actual handoff add current state, remaining work, observed evidence/gaps, and the next action. Persist only for continuity in an existing canonical home. Missing companions do not require installation or an extra approval step.

## Readiness gate

Planning assumes accepted intent and enough governing design to bound execution.

If material product, architecture, compatibility, data, security, operational, or risk choices remain Open, return them to the appropriate decision owner or `engineering-specification`/explicit design mode. Do not convert unresolved design into implementation tickets.

A bounded investigation can instead be explicitly assigned to gather evidence for an Open question. Fix its scope, permitted probes, evidence deliverable, and decision owner; research readiness does not authorize choosing or implementing the resulting design.

A valid outcome of explicit planning/delegation mode can still be **direct execution with no decomposition** if one executor can safely complete and verify the accepted work. Manual invocation is permission to evaluate decomposition, not a requirement to manufacture ceremony.

## Decomposition intent

Prefer independently verifiable outcomes with real dependencies and minimal shared mutable scope. Preserve fixed decisions and bound the receiver's remaining choices. Do not delegate merely to maximize parallelism.

## Capability selection

Choose executor capability by **remaining decision burden and consequence**, not by workload class or file count.

A cheaper/weaker executor is appropriate when Fixed decisions, scope, governing sources, verification, and escalation triggers are explicit and remaining choices are mostly reversible Local mechanics.

Use stronger reasoning where consequential ambiguity remains. Do not make a work package longer merely to conceal unresolved architecture from a weak executor.

## Capacity adjustments

On an executor's capacity report, compare observed progress and remaining implementation/verification with the supplied capacity policy. Decide whether to continue, adjust budget/topology, split/defer, or pause only within explicitly delegated authority; otherwise present evidence, uncertainty, and a recommendation to the user. A workload label alone is not delegated budget authority. Preserve valid progress and communicate the decision and limits to affected receivers. Do not treat a forecast mismatch as permission to change scope/acceptance or start another explicit mode. Awaiting an answer does not extend existing limits.

## Persistence

A plan is coordination state, not automatically durable engineering knowledge.

Persist a plan when continuity requires it or the upstream layer explicitly selects the Medium profile and assigns this mode responsibility for that artifact. A capacity label alone creates no artifact requirement. Use the repository's existing convention and reference the specification supplied by its owner.

Retire/archive stale plan state when its coordination value ends. Preserve long-lived truths in their canonical specification/design/contract sources rather than synchronizing them forever through a master plan.

## Completion criterion

This orchestration mode is complete when either:

- execution is demonstrably bounded enough to proceed directly; or
- a concrete plan exists and every real receiver has a bounded handoff contract sufficient to begin or resume without reconstructing consequential intent or accidentally redesigning the system, whether supplied by the companion skill or the local fallback.

The remaining work should be execution and verification, not unresolved foundational decisions disguised as tasks.
