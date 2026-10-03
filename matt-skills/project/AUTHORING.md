# Authoring capability-oriented project skills

This note captures how the body of a capability-oriented `SKILL.md` should be written.

The goal is to keep a skill useful and behavior-shaping without turning it into either a generic methodology handbook or a workflow engine.

## Core rule

A `SKILL.md` should contain the guidance that remains true across multiple concrete methods of completing the capability.

Prefer a small core made of:

1. **Capability contract** — what user-facing outcome the skill owns, what natural inputs it accepts, and when that local outcome is complete.
2. **Capability invariants** — properties that should remain true regardless of which concrete method is chosen.
3. **Decision heuristics** — cues for choosing among possible techniques based on the shape, uncertainty, risk, and evidence needs of the current task.

Move specialized expert methods into optional reference material when they are useful enough to preserve.

```text
SKILL.md
  = capability contract
  + capability-specific invariants
  + decision heuristics

references/
  = specialized expert methods

conversation + repository
  = actual task state
```

The skill body should not attempt to enumerate every possible task subtype or artifact shape.

---

## Capability contract

The contract says what the skill owns, not how every instance must proceed.

A useful contract normally includes:

- `Purpose`
- `Accepts`
- `Owns`
- `May also`
- `Done when`
- `Does not require`

Example shape for implementation:

```text
Purpose:
Turn a concrete requested change into working production behavior.

Owns:
- making the production changes necessary for the requested outcome
- preserving relevant existing behavior
- obtaining proportionate evidence that the requested outcome works

Done when:
The requested behavior exists and there is enough evidence, relative to the
risk and scope of the change, that it works without unacceptable regressions.
```

This does not imply a sequence such as diagnose -> TDD -> review -> reconcile.

---

## Capability invariants

Invariants are the highest-value part of the core skill body. They should shape behavior across many task shapes without prescribing one method.

Possible implementation invariants include:

- understand the requested outcome before committing to a solution;
- use the existing system as the primary source of constraints;
- avoid unrelated change unless broader change is justified by the requested outcome;
- verify behavior at the level where failure would matter;
- do not confuse a preferred test command passing with evidence that every material surface of the requested behavior has been verified.

Possible design invariants include:

- make material design decisions explicit rather than leaving them implicit in downstream implementation;
- distinguish durable project decisions from temporary exploration;
- preserve room for multiple techniques such as inspection, comparison, experimentation, prototyping, or direct reasoning.

Possible review invariants include:

- derive evaluation criteria from the object and user intent rather than forcing one universal checklist;
- distinguish findings from speculative concerns;
- support material findings with evidence proportionate to the claim.

An invariant belongs in core `SKILL.md` only when it remains useful across multiple concrete methods.

---

## Decision heuristics

Heuristics tell the agent when a technique is likely useful without turning that technique into a required stage.

Example implementation heuristics:

```text
If the failure mechanism is unclear, investigate before changing code.

If behavior can be checked cheaply with an automated test, prefer that over
manual confidence alone.

If the change crosses a risky integration boundary, verify at that boundary.

If the existing architecture makes the requested behavior awkward, make the
smallest design decision necessary rather than blindly patching around it.

If uncertainty can be reduced more cheaply with a spike or prototype, use one.
```

These heuristics may naturally invoke behaviors associated with debugging, testing, prototyping, research, or design. None of those behaviors becomes a required cross-skill transition.

---

## References hold specialized methods

A reference is appropriate when a problem shape has reusable expert technique that materially improves execution but does not define a separate user-facing capability.

Possible examples:

```text
implement/
  SKILL.md
  references/
    debugging.md
    testing-strategies.md
    refactoring.md
    migrations.md
    performance-work.md

review/
  SKILL.md
  references/
    code.md
    design.md
    spec.md
    decomposition.md

design/
  SKILL.md
  references/
    domain-modeling.md
    architecture.md
    interface-design.md
    decision-techniques.md
```

These names are illustrative, not a required taxonomy.

The reference split should follow the natural specialization of the capability:

- review guidance often varies by **object being evaluated**;
- implementation guidance often varies by **problem shape or technique**;
- design guidance may vary by **decision domain or modeling method**.

Do not force every capability into the same reference structure.

---

## Do not replace horizontal workflow with vertical workflow

Removing a lifecycle pipeline is not enough if the replacement merely creates many implementation subflows.

Avoid replacing:

```text
design -> tdd -> review -> reconcile
```

with:

```text
implement-feature
implement-bug
implement-refactor
implement-migration
```

or a single large `implement` skill that internally encodes those as mandatory named branches with their own rigid phases.

The task subtype may affect technique selection. It should not automatically create another workflow protocol.

---

## Test for core-vs-reference placement

For each instruction, ask:

> Does this remain true across multiple materially different ways of completing the capability?

If yes, it probably belongs in `SKILL.md`.

If it is specific to one technique, problem shape, artifact type, or expert discipline, it probably belongs in optional reference material.

Examples:

```text
Always write a failing test first.
```

This is technique-specific and does not belong in the core implementation skill.

```text
Obtain evidence proportionate to the risk and behavior changed.
```

This remains true across many implementation methods and is a good core invariant.

Similarly:

```text
Always create three alternatives.
```

is a design technique, while:

```text
Do not silently leave material design decisions for downstream implementation
when those decisions are part of the user's current concern.
```

is a capability-level invariant.

---

## References are not hidden required stages

Moving instructions into references must not recreate sequencing indirectly.

A reference should be available when useful, not required merely because a task was classified into a category.

Bad:

```text
This is a bug. Load debugging.md and execute phases 1-8 before any code change.
```

Preferred:

```text
Use debugging guidance when the uncertainty and failure shape make it useful.
```

The capability remains responsible for its own outcome either way.

---

## Authoring target

A healthy capability should tend toward:

```text
small, outcome-oriented SKILL.md
+ a few high-value invariants
+ conditional decision heuristics
+ optional deep references
+ no fixed project-wide sequence
```

The skill body is not a textbook. It is the smallest set of instructions that reliably improves ownership of the capability's outcome across varied tasks.
