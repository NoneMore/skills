# Review Capability Boundary

> Status: draft boundary note for the capability-oriented refactor.

## Core idea

`review` is a broad capability over many kinds of existing results.

Its center of gravity is:

> **Independently evaluate an existing result against the expectations that matter for that result, and surface substantiated findings.**

The object boundary should be broad. The evaluation methods should be object-specific.

---

## Purpose

Independently evaluate an existing result and identify material problems, mismatches, omissions, or risks relative to the expectations that matter for it.

## Accepts

Any sufficiently concrete existing result, including for example:

- code, a diff, branch, or PR/MR;
- a running implementation or current system behavior;
- a design or architecture proposal;
- a specification;
- a plan;
- a ticket decomposition;
- a prototype or other concrete artifact.

The reviewed object does not need to have been produced by another project skill.

## Owns

Evidence-backed findings about where the reviewed result does or does not meet the expectations relevant to the requested review.

The primary outcome is an **independent evaluation**, not a lifecycle transition and not necessarily a persisted review artifact.

## Outcome-specific invariants

These responsibilities belong in core because they follow directly from review as an evaluation capability:

1. **Use criteria appropriate to the object and review intent.** Do not force every result through one universal checklist or fixed pair of axes.
2. **Distinguish findings from preference and speculation.** A reviewer preference is not automatically a defect; a plausible concern is not automatically a substantiated finding.
3. **Verify material claims independently.** Do not treat the producer's explanation, implementation intent, or claim of correctness as proof that the result is correct.
4. **Do not require producing the replacement result.** Review can suggest fixes, redesigns, or rewrites, but its own outcome is complete when the material evaluation is established.

## Done when

The material concerns within the requested review scope have been evaluated and the findings are explicit enough for the user to act on or accept the result.

An explicit lack of findings is also a valid outcome when the requested review has been performed sufficiently to support that conclusion.

## Persistence

When the review surface is naturally durable, such as a PR/MR review, findings may be persisted there.

Otherwise conversation context is a valid default result. `review` does not require a canonical review-result schema.

---

## Object-specific guidance belongs below the core

Different reviewed objects need different evaluation dimensions and evidence-gathering methods. Those differences are useful, but they do not belong in one universal review procedure.

### Code / diff / PR

Potential object-specific concerns include correctness, requested behavior, regressions, verification, maintainability, repository conventions, and architecture effects.

Possible methods include reading surrounding code, tracing callers, running relevant tests, inspecting history, and comparing against a request or spec.

### Design / architecture

Potential concerns include assumptions, missing scenarios, conceptual consistency, module/interface shape, coupling, failure modes, and relevant future constraints.

Possible methods include scenario stress-testing, counterexamples, comparing alternatives, and inspecting the existing architecture and domain model.

### Specification

Potential concerns include ambiguity, missing decisions, contradictions, unverifiable requirements, scope gaps, hidden assumptions, and accidental implementation commitments.

### Decomposition / tickets

Potential concerns include coverage, slice independence, dependency correctness, missing integration work, granularity, and actionability.

These are examples, not a closed taxonomy. They are candidates for optional references such as `references/code.md`, `references/design.md`, `references/spec.md`, or `references/decomposition.md` if the guidance proves worth preserving.

The core skill should not enumerate all of their methods.

---

## Boundary with neighboring capabilities

The distinction is based on the primary outcome, not on which actions are allowed.

```text
"How should this architecture work?"        -> design
"Here is the architecture; find problems." -> review

"Write this spec."                          -> specify
"Find problems in this spec."              -> review

"Break this work into tickets."            -> decompose
"Check whether these tickets are good."    -> review

"Implement this change."                   -> implement
"Check whether this implementation is good." -> review
```

Another capability may evaluate its own work locally. Independent `review` remains useful when evaluation itself is the user's requested outcome.

---

## What should disappear from the current `code-review`

The current implementation should not define the abstraction around:

- code as the only reviewable object;
- a mandatory diff/fixed-point model;
- a fixed Standards + Spec pair of axes;
- a fixed code-smell checklist as core capability semantics;
- tracker configuration as a prerequisite;
- mandatory sub-agent structure;
- generic evidence-gathering steps repeated in core merely because review may use them.

Some specialized techniques may survive as optional object-specific reference guidance.

The core rule is:

> **Review has a broad object boundary, but only outcome-specific evaluation responsibilities belong in core.**
