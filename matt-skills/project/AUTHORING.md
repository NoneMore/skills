# Authoring capability-oriented project skills

This note captures how the body of a capability-oriented `SKILL.md` should be written.

The goal is to keep a skill behavior-shaping without turning it into a generic agent handbook, methodology catalog, or workflow engine.

## Core rule

A core instruction belongs in a capability only when it passes **both** of these tests:

1. **Cross-method test** — does this remain true across multiple materially different ways of completing the capability?
2. **Outcome-coupling test** — is this responsibility specifically implied by the outcome this capability owns, rather than being generic advice that would apply almost unchanged to other skills?

A healthy skill therefore tends toward:

```text
SKILL.md
  = capability contract
  + outcome-specific invariants
  + optional outcome-specific heuristics

references/
  = specialized expert methods

general agent behavior
  = omitted from the skill
```

The second filter is important. "Understand the task", "inspect context", "resolve ambiguity", "gather evidence", and "ask when necessary" may all be good agent behavior, but repeating them in every skill does not define a capability.

---

## Capability contract

The contract states the local result the capability owns.

The smallest useful shape is usually:

- `Purpose`
- `Owns`
- `Done when`

Add `Accepts` when describing natural input shapes improves direct entry or discoverability.

Other sections are optional:

- `May also` is useful only when an overlap would otherwise be surprising or confusing. Do not use it to enumerate everything an agent is allowed to do.
- `Does not require` is especially useful during this refactor to make removed predecessor/protocol assumptions explicit. It does not need to remain forever once those assumptions no longer exist.

A capability boundary defines **ownership**, not a permission boundary.

Example implementation contract:

```text
Purpose:
Turn a requested production change into working production behavior.

Owns:
- the production behavior requested
- preservation of relevant behavior outside the intended change
- production artifacts fit to remain in the real system
- evidence that the changed behavior works at the boundary where it matters

Done when:
The requested production behavior works, relevant preservation expectations hold,
and the resulting production artifacts are acceptable to keep.
```

This does not imply a sequence such as diagnose -> TDD -> review -> reconcile.

---

## Outcome-specific invariants

Invariants are the highest-value part of the core skill body, but only when they are coupled to the owned outcome.

Good implementation invariants are specific to changing the production system:

- own the requested production behavior, not merely the textual edit;
- preserve relevant production behavior outside the intended change unless changing it is justified;
- verify the changed behavior at the system boundary where the implementation is expected to matter;
- do not leave exploratory shortcuts, fake dependencies, or temporary scaffolding in the production result unless they are intentionally part of the design.

Good design invariants are specific to resolving design choices:

- make material design choices explicit rather than silently delegating them to later implementation;
- keep the chosen direction coherent with the constraints that motivated it;
- distinguish settled design decisions from genuinely open design questions.

Good review invariants are specific to independent evaluation:

- use criteria appropriate to the reviewed object and review intent rather than a universal checklist;
- distinguish violated expectations and material risks from preferences or speculative concerns;
- independently verify material claims rather than treating the producer's explanation as proof;
- do not require producing the replacement result in order to complete the review.

Compare these with generic instructions such as:

```text
Understand what done means.
Gather enough evidence.
Resolve important uncertainty.
```

Those may be sound general behavior, but they fail the outcome-coupling test because they can be copied almost unchanged into `design`, `review`, `implement`, and other capabilities.

---

## Decision heuristics are optional

A capability does not need a heuristic section merely because useful techniques exist.

A heuristic belongs in core only when it also passes both placement tests:

```text
cross-method = yes
outcome-coupled = yes
```

If a heuristic mainly says when to research, investigate, prototype, test, inspect history, or ask a question, it is probably general agent behavior or specialized method guidance rather than capability core.

Do not make every skill restate the same execution wisdom.

---

## References hold specialized methods

A reference is appropriate when a problem shape, object type, or expert discipline has reusable technique that materially improves execution but does not define a separate user-facing capability.

Illustrative shapes:

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

These names are examples, not a required taxonomy.

The natural split differs by capability:

- review guidance often varies by **object being evaluated**;
- implementation guidance often varies by **problem shape or technique**;
- design guidance may vary by **decision domain or modeling method**.

Do not force every capability into the same reference structure.

---

## General agent behavior is not skill content

Do not use project skills as a place to restate behaviors expected of the agent generally.

Typical examples to omit unless a capability-specific version can be derived from the outcome:

- read the relevant files;
- inspect history when useful;
- research unknown facts;
- clarify material ambiguity;
- form hypotheses;
- gather evidence;
- use tools proportionately;
- tell the user about unresolved uncertainty.

The fact that a capability may perform these actions does not require listing them under `May also` or turning them into named phases.

---

## Do not replace horizontal workflow with vertical workflow

Removing a lifecycle pipeline is not enough if the replacement merely creates task-subtype workflows.

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

or with one large `implement` skill that encodes those categories as mandatory named branches with rigid phases.

Task shape may influence which references or techniques are useful. It should not automatically create another workflow protocol.

---

## Core-vs-reference placement

For every proposed instruction, ask in order:

```text
1. Cross-method test
   Would this still be true if the capability were completed using a very
   different valid method?

2. Outcome-coupling test
   If I replaced this skill with another capability, would the instruction
   still read almost unchanged?
```

Strong core candidates answer:

```text
cross-method = yes
outcome-coupled = yes
```

Technique-specific guidance belongs in references.

Generic guidance that fails outcome coupling usually belongs nowhere in the project skill suite.

This second failure mode is also a useful deletion signal: if a proposed skill has no meaningful instructions left after generic behavior and techniques are removed, it may not justify an independent invocation surface.

---

## References are not hidden required stages

Moving instructions into references must not recreate sequencing indirectly.

Bad:

```text
This is a bug. Load debugging.md and execute phases 1-8 before any code change.
```

Preferred:

```text
Use specialized debugging guidance when it materially helps the current work.
```

The capability remains responsible for its own outcome either way.

---

## Authoring target

A healthy capability should tend toward:

```text
small outcome-oriented SKILL.md
+ a few outcome-specific invariants
+ optional outcome-specific heuristics
+ optional deep references
+ no generic agent handbook
+ no fixed workflow sequence
```

The skill body is the smallest set of instructions that reliably improves ownership of **this particular outcome** across varied tasks.