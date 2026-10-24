---
name: specify
description: Turn sufficiently settled intent into a precise, task-scoped implementation and verification contract. Use when the user explicitly wants a specification, requirements contract, or task-specific acceptance criteria.
disable-model-invocation: true
---

# Specify

## Purpose

Turn sufficiently settled intent into a precise contract for the work at hand, so implementation and verification do not need to invent material choices.

## Accepts

Conversation decisions, an issue or request, an existing design, project context, or any combination that is concrete enough to specify without inventing material product or design choices.

## Owns

- the specific problem or outcome being addressed;
- intended observable behavior and scope at the level the task needs;
- material settled decisions and constraints that the work must honor;
- non-goals or boundaries whose omission would create material scope ambiguity;
- acceptance conditions that distinguish a satisfying result from a non-satisfying one;
- explicit material unresolved questions when the source material is not yet decision-complete.

Treat established product and design decisions as constraints, not as choices to silently reopen. If material sources conflict or a product or design choice remains unresolved, do not silently settle it as part of specification. If the user delegates the choice, resolve it explicitly before treating the specification as implementation-ready; otherwise identify what remains undecided.

## Approach

Identify the intent and constraints settled by the request, applicable project evidence, and existing design. Translate them into concrete behavior, boundaries, and acceptance conditions at the granularity needed for the task. Derive necessary consequences of settled requirements without introducing discretionary product or design choices.

Use representative scenarios and edge cases to expose material ambiguity, contradictions, or missing decisions. If a material choice is not established or delegated, keep it explicit rather than supplying a plausible default.

Include detail when its absence could materially change implementation or verification, not merely to make the specification appear complete.

## Result

Present a task-scoped specification with the material outcome, expected behavior, scope, constraints, and acceptance conditions. Clearly distinguish settled requirements from unresolved decisions. Prefer observable acceptance criteria over implementation instructions unless the implementation choice is itself a requirement.

Use the structure that best communicates the contract rather than a mandatory template.

## Project conventions and default

Follow applicable project conventions for specification form, placement, and change handling. Inspect relevant project instructions and sources of truth when needed to determine whether they apply.

Use a project-prescribed destination when authorized; otherwise return the specification in conversation unless the user requests and authorizes another destination. If a specification file is produced without an applicable project change convention, keep its necessary revision guidance in that file: edit it in place, treat its current body as the requirements for the task, and update materially affected behavior, scope, and acceptance conditions together.

Do not create a separate specification governance document, approval workflow, revision log, or archival process merely to define how the file changes.

## Done when

The specification is precise enough for the current work to be implemented and verified without silently inventing material choices. If that is not yet possible, capture the settled scope and explicitly identify the decisions that still block a reliable contract.
