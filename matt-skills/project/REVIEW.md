# Review Capability Boundary

> Status: draft boundary note for the capability-oriented refactor.

## Core idea

`review` is a broad capability over many kinds of existing work products.

Its center of gravity is not code review specifically. It is:

> **Independently evaluate an existing result against the expectations that matter for that result, and surface evidence-backed findings.**

The object boundary should be broad. The evaluation methods should be object-specific.

---

## Purpose

Evaluate an existing result independently enough to identify material problems, omissions, mismatches, risks, or quality concerns.

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

- identify the relevant expectations for the review;
- examine the existing result against those expectations;
- gather enough evidence to support material findings;
- report findings clearly enough for the user to decide what to do next.

The primary outcome is an **independent evaluation**, not a lifecycle transition and not necessarily a persisted review artifact.

## May also

When useful, `review` may:

- inspect surrounding code, history, docs, issues, specs, ADRs, or domain material;
- run tests or experiments;
- reproduce behavior;
- compare alternatives or prior versions;
- verify claims against the current system;
- suggest concrete fixes or alternative designs;
- make small temporary changes to test a concern.

These are evidence-gathering techniques, not separate required capabilities.

## Done when

The concerns relevant to the requested review have been examined and the material findings are explicit, with enough evidence to distinguish substantiated concerns from speculation.

An explicit lack of findings is also a valid outcome when the review has been sufficiently thorough for the requested scope.

## Does not require

- a diff;
- a PR/MR;
- a spec;
- a previous `implement` run;
- a fixed Standards/Spec two-axis model;
- a canonical review-result schema;
- tracker setup;
- persistence outside the conversation.

When the natural review surface is durable, such as a PR/MR review, findings may be persisted there. Otherwise conversation context is a valid default result.

---

## Broad capability, object-specific methods

The capability boundary should not force every object through one generic checklist.

Different review objects need different evaluation dimensions and evidence-gathering techniques.

### Code / diff / PR

Likely concerns include:

- correctness;
- behavior requested vs behavior delivered;
- regressions;
- tests and verification;
- maintainability and unnecessary complexity;
- repository conventions;
- architecture effects.

Useful methods may include reading the diff and surrounding code, running tests, tracing callers, inspecting history, and comparing against a request/spec.

### Design / architecture

Likely concerns include:

- assumptions;
- missing or contradictory scenarios;
- conceptual consistency;
- module/interface/seam shape;
- coupling and locality;
- failure modes;
- relevant future constraints.

Useful methods may include scenario stress-testing, counterexamples, comparing alternatives, inspecting the existing architecture, and challenging domain terminology.

### Specification

Likely concerns include:

- ambiguity;
- missing decisions;
- contradictions;
- unverifiable requirements;
- scope gaps;
- hidden assumptions or accidental implementation commitments.

### Decomposition / tickets

Likely concerns include:

- coverage of the intended work;
- slice independence;
- dependency correctness;
- missing integration work;
- useful granularity and actionability.

These categories are examples, not a closed taxonomy. Object-specific guidance can live as optional reference material rather than separate project skills.

---

## Boundary with neighboring capabilities

The distinction is based on the primary outcome, not on which actions are allowed.

```text
"How should this architecture work?"       -> design
"Here is the architecture; find problems." -> review

"Write this spec."                          -> specify
"Find problems in this spec."              -> review

"Break this work into tickets."             -> decompose
"Check whether these tickets are good."     -> review

"Implement this change."                    -> implement
"Check whether this implementation is good."-> review
```

`review` may suggest redesigns, rewrites, or fixes, but it does not need to take ownership of producing the replacement result in order to complete its own outcome.

Likewise, another capability may review its own work locally. Independent `review` remains useful when the user's primary intent is evaluation.

---

## What should disappear from the current `code-review`

The current implementation should not define the abstraction around:

- code as the only reviewable object;
- a mandatory diff/fixed-point model;
- a fixed Standards + Spec pair of axes;
- a fixed code-smell checklist as core capability semantics;
- tracker configuration as a prerequisite;
- mandatory sub-agent structure.

Some of those techniques may remain useful for code review and can survive as optional reference guidance.

The core rule is:

> **Review has a broad object boundary, but object-specific evaluation techniques.**
