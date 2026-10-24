---
name: decompose
description: Plan bounded engineering work into actionable steps, truthful dependencies, decision gates, and verification checkpoints; split into tasks or tickets when useful. Use when the user explicitly wants an execution plan, migration or investigation plan, phased work, or task breakdown.
disable-model-invocation: true
---

# Decompose

## Purpose

Turn an engineering goal into a credible plan for reaching it, rather than requiring every plan to be a set of tickets.

## Accepts

A request, goal, issue, specification, design, existing plan, or investigation problem with enough context to identify meaningful next work. Uncertainty may remain if the plan can show how to resolve it.

## Owns

- an actionable path covering the intended outcome;
- real sequencing constraints and opportunities for independent work;
- work boundaries and deliverables at the granularity the goal warrants;
- material assumptions, risks, and decisions that gate dependent work;
- checkpoints and completion signals that make progress verifiable.

Respect settled product and design choices. Do not invent material decisions or present blocked work as ready. Where a choice is unresolved, identify the investigation or decision needed and what depends on it. Planning does not perform or continuously coordinate the subsequent work.

## Approach

Establish the target outcome, current state, and constraints that affect execution. Choose a proportionate approach, ordering work by real prerequisites, integration needs, and meaningful risk rather than arbitrary stages.

Expose uncertainties early enough that later work need not rely on guesses. Plan investigation, validation, and transition or recovery checks when they materially affect a safe path. If splitting work into items helps, prefer independently verifiable end-to-end slices where feasible; mechanical changes or migrations may require ordered cross-cutting work.

## Result

Present an execution plan in the form that fits the request: a concise path, phased rollout, investigation sequence, or work-item breakdown. Make deliverables, dependencies, decision gates, and verification checkpoints explicit where omission could change execution. Avoid invented schedules, ownership, or a mandatory template.

Use [tracer-bullets.md](references/tracer-bullets.md) when work-item boundaries or dependency edges need specialized guidance.

Publish tasks to a tracker only when requested and authorized, following the project's existing conventions rather than creating workflow states or coordination rules.

## Done when

The next actor can tell what work can proceed, what must wait for a real prerequisite or decision, and how to verify the intended outcome, without material work or dependencies being left implicit.
