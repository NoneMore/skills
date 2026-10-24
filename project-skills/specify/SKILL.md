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

Establish the intended outcome and applicable project constraints. Translate settled intent into observable behavior, meaningful boundaries, and acceptance conditions at the granularity the work requires.

Use representative normal, edge, and failure scenarios when they expose material ambiguity. Do not invent requirements or implementation steps merely to make the specification appear complete.

## Result

Present a task-scoped specification with the material outcome, expected behavior, scope, constraints, and acceptance conditions. Clearly distinguish settled requirements from unresolved decisions. Prefer observable acceptance criteria over implementation instructions unless the implementation choice is itself a requirement.

Use the structure that best communicates the contract rather than a mandatory template.

## Project conventions and default

Follow applicable project conventions for specification form, placement, and change handling. Inspect relevant project instructions and sources of truth when needed to determine whether they apply.

Return the specification in conversation unless the user requests and authorizes a file or another destination. If a specification file is produced without an applicable project change convention, make its change handling self-contained: include only the local guidance needed to revise the file coherently and recognize its current requirements. A lightweight default is to edit that file directly, updating materially affected behavior, scope, and acceptance conditions together.

Do not create a separate specification governance document, approval workflow, revision log, or archival process merely to define how the file changes.

## Done when

The specification is precise enough for the current work to be implemented and verified without silently inventing material choices. If that is not yet possible, capture the settled scope and explicitly identify the decisions that still block a reliable contract.
