---
name: orchestrate
description: Coordinate engineering execution through appropriate delegation, verified handoffs, evidence-backed stage decisions, and integration. Use when the user explicitly asks to orchestrate a request or existing plan.
disable-model-invocation: true
---

# Orchestrate

## Purpose

Take engineering work from a request or existing plan through appropriately coordinated execution to a verified outcome or an explicit blocked or incomplete result.

## Accepts

An engineering request, issue, specification, or existing plan. Prior decomposition is not required.

## Owns

- choosing direct execution or delegation, with actionable assignments and preserved task constraints;
- coordinating real prerequisites, handoffs, and shared-resource conflicts;
- deciding when consequential stages can start or continue from relevant evidence;
- revising affected execution decisions when material evidence changes;
- integrating delivered work and verifying the requested outcome.

## Approach

Execute directly when delegation adds no material benefit. Otherwise identify executable work and real prerequisites from the task or plan; use separate decomposition only when it helps. Preserve established scope and completion conditions without inventing product or design decisions.

Before dispatch, establish that the unit is actionable with the current dependencies, shared resources, and recipient's available tools and authority. Convey its intended outcome, relevant constraints, artifact or interface boundary, and verifiable completion conditions. Keep decisions requiring parent or user authority with the parent.

For a dependent assignment, establish that the upstream artifact or interface is available to its consumer and sufficiently verified for the dependent work. A producer's interface declaration or completion claim alone is not evidence of a cleared handoff. Obtain a relevant consumer check or other concrete availability evidence before releasing the dependency.

Before a consequential or costly stage, assess evidence for the task's actual failure risks, including checks of the affected execution path and any established independent review conditions. Validate or hold the affected stage when necessary evidence is missing; do not invent a universal approval gate.

When new evidence undermines a material assumption behind a launch or continuation decision, promptly reassess the affected scope. Stop or revise unsafe work while preserving independently useful progress.

Make consequential decisions reviewable in the ordinary execution record: what triggered the decision, who owned it, the evidence relied on, what was decided, and what would require reconsideration. Use detail proportionate to the risk; do not impose a fixed schema, permanent decision log, or ceremony on routine work.

Integrate delivered artifacts against the original requested outcome and cross-task constraints. Verify material completion claims independently where appropriate rather than treating subagent reports as proof.

## Boundaries

Execution roles own their assigned outputs within their actual tools and permissions. Return material scope or product decisions and unavailable parent-control operations to the parent; skill instructions do not grant tool authority.

Do not require a `decompose → orchestrate → implement` pipeline, introduce a tracker workflow, or add runtime scheduling or permission mechanisms.

## Result

Report verified outcomes, material evidence supporting completion, and any blocked, failed, or incomplete work without presenting unverified results as done.

## Done when

The requested outcome is integrated and verified to the task's relevant conditions, or remaining work and the evidence needed to proceed are explicitly identified as blocked or incomplete.
