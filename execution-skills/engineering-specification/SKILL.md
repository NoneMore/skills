---
name: engineering-specification
description: "Create an explicitly requested engineering specification or RFC draft, distinguishing proposed decisions from accepted design and implementation readiness. Also use when upstream orchestration requests specification before execution; never infer it from task size alone."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Specification

Turn an engineering request into a written, reviewable account of **what should change, what must remain true, and the proposed or accepted approach**, according to the requested deliverable.

This is a reusable discipline, not a workload classifier and not a mandatory stage for every task.

## Invocation boundary

Invoke when either:

- the user explicitly asks to define requirements, write a specification, or settle an engineering design; or
- an upstream user/Meta-Agent orchestration mode explicitly requests a specification, such as the bundle's Medium workflow or the macro-design portion of Large initiative shaping.

Do **not** invoke merely because a task is large, risky, multi-file, architectural, ambiguous-looking, or likely to benefit from planning. Leaf Skills must never infer Small/Medium/Large.

This skill does not grant repository mutation or external-effect authority. If writing the specification into the repository is part of the active workflow, that document mutation must already be authorized by the underlying task or orchestration mode.

## Objective

A useful specification reduces consequential ambiguity without prescribing every reversible implementation detail.

It should let a capable executor answer:

- What observable outcome should become true?
- Why is this change being made?
- What is in scope and out of scope?
- What important current behaviour or constraints must remain true?
- What engineering approach has been accepted?
- Which decisions are fixed, which remain open, and which details are local implementation choices?
- What evidence will demonstrate success?

The specification should not become a transcript of the discussion.

## Discover before deciding

Inspect available repository evidence before asking the user for facts:

- current code and tests;
- maintained specifications, ADRs, architecture documents, schemas, contracts, and runbooks;
- relevant configuration and build/runtime constraints;
- current behaviour and reproducible evidence when it matters;
- existing terminology and canonical documentation locations.

Separate **facts** from **decisions**. Repository evidence can often settle current-state facts. Ask the decision owner only for unresolved product intent, compatibility, scope, UX, risk tolerance, or consequential design choices that evidence cannot decide.

If evidence contradicts an assumption in the request, surface the contradiction before encoding it as a requirement.

## Written specification contract

Use the repository's existing conventions rather than forcing a template. At minimum, preserve the following semantic roles when they are material:

1. **Problem / outcome** — the observable state that should become true and the reason it matters.
2. **Scope and non-goals** — what the change owns and what it deliberately does not solve.
3. **Relevant current state** — only facts needed to understand the change, with canonical references where possible.
4. **Requirements / acceptance behaviour** — externally or operationally meaningful behaviour that must hold.
5. **Constraints and invariants** — compatibility, security, data, performance, operational, architectural, or authority boundaries that must remain true.
6. **Approach / design status** — distinguish proposals and alternatives from accepted governing decisions. For an implementation-ready specification, identify the chosen direction sufficiently to prevent accidental redesign.
7. **Affected boundaries / contracts** — modules, APIs, schemas, data flows, integrations, or ownership seams whose behaviour matters.
8. **Decision budget** — consequential decisions that are Fixed, reversible implementation choices that are Local, and unresolved consequential choices that are Open.
9. **Verification intent** — the classes of evidence that will prove the requirements and important invariants.
10. **Open questions** — only unresolved consequential questions; blocking ones mean the specification is not execution-ready.

Do not create sections merely to fill a template. Omit roles that truly do not matter for the change.

## What belongs in "How"

The accepted engineering approach should prevent implementation from making consequential product or architecture decisions by accident, regardless of capacity label.

Specify consequential structure such as:

- the seam or module that should own the behaviour;
- contract or data-model changes;
- compatibility or migration strategy;
- failure semantics and important edge handling;
- dependency direction or integration strategy;
- important observability or operational behaviour.

Do not specify reversible local mechanics that a bounded executor can safely decide while preserving the accepted outcome and constraints.

## Brainstorming versus accepted specification

Exploration may produce alternatives. A specification must make the accepted direction distinguishable from rejected or still-open options.

Do not silently convert an attractive brainstorm option into a fixed design. When a consequential choice is unresolved, either resolve it with the decision owner or mark it Open and keep the specification not-ready for bounded execution.

## Relationship to planning

Specification and execution plan are different artifacts:

- **Specification:** what / why / constraints / accepted engineering approach.
- **Execution plan:** sequence, dependency, coordination, concrete work units, verification points, and handoffs for getting from current state to the specified state.

Do not mix implementation task checklists into the governing specification merely because they were discussed together. After the specification is accepted, use `engineering-execution-planning` when available and an execution plan is explicitly required. Otherwise provide the requested sequence, dependencies, and verification points directly; specification work alone does not start planning.

## Knowledge lifecycle

A specification may become durable engineering knowledge when it owns maintained behaviour, contracts, architecture, or constraints. A change-local specification may instead be a coordination artifact whose useful content should later be merged into canonical sources and whose stale shell should be retired.

For a concrete lifecycle decision, use `engineering-knowledge-governance` when available. Otherwise keep accepted/current state distinct, update the existing canonical source within task authority, and retire obsolete coordination state when appropriate.

Prefer links to canonical sources over copied background. Avoid creating a second source of truth.

## Completion and readiness

Distinguish three claims: the requested artifact is complete, its governing design is accepted, and implementation is ready. Writing a document establishes neither acceptance nor implementation readiness.

For a requested draft/RFC with intentionally deferred decisions, finish when the requested scope is represented, proposals and accepted constraints are distinguishable, and material Open questions and their implications are explicit. Mark acceptance/readiness as pending where appropriate. Do not prolong the task with decision-seeking questions, choose an alternative, or start planning/implementation merely to make the draft execution-ready. Ask only if missing information prevents producing the requested draft at all.

For a requested implementation-ready specification, readiness requires:

- the intended outcome and material non-goals are explicit;
- consequential governing constraints are discoverable and reconciled;
- the accepted engineering approach is clear enough to prevent accidental redesign;
- blocking Open decisions are resolved;
- acceptance and important negative constraints can be verified;
- another capable agent can distinguish Fixed, Local, and Open decisions without reconstructing the original conversation.

If readiness is the requested outcome and these conditions are not met, resolve or report its blockers rather than hiding them inside implementation tasks. A complete draft with deferred decisions can still satisfy a draft-only request.
