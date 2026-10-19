---
name: lean4-abstract
description: >-
  User-invoked Lean 4/mathlib mode for assessing and optionally extracting
  concrete suspected mathematical reuse within one proof or across declarations;
  not routine proving, cleanup, or open-ended reframing.
disable-model-invocation: true
license: MIT
---

# Lean 4 Abstract

Use only when explicitly selected by the user. Investigate a *specific* suspected
mathematical reuse: repeated arguments within one proof, a plausible earlier
declaration, or a library construction. One theorem can suffice; shared tactic
syntax alone cannot.

## Workflow

1. **Bound the question.** Identify the concrete signal, representative sites,
   assessment-only versus implementation authority, and verification gate. If
   no signal can be located, report uncertainty instead of starting speculative
   repository-wide search.
2. **Compare and search.** Check constructions, hypotheses, invariants, and
   conclusions at the smallest relevant sites. Search the active proof and
   nearby code, then local/imported APIs; widen only toward a specific
   construction, theorem family, or plausible owner.
3. **Choose the least costly result.** Apply an existing theorem, factor a
   local/private helper, introduce a justified public declaration, or make no
   change. Distinguish mathematical generality from elaboration convenience;
   length or privacy alone does not justify a new public API.
4. **Validate in Lean.** Check candidate statements and representative uses
   (including repeated uses within one proof) in the actual context: hypotheses,
   universes, coercions, and typeclass inference. Place declarations at the
   appropriate mathematical layer without unnecessary imports or reversing
   dependency direction.
5. **Respect edit and verification scope.** Reading historical consumers does
   not authorize their migration. For authorized edits to already-verified code,
   record a reproducible baseline or report its absence; change only authorized
   sites, preserve public statements, accepted trust and unrelated work, and
   verify affected integration scope. File-local checks against stale imported
   artifacts are not dependency-aware verification.

## Acceptance and stopping

Extract only when checked reuse, clarity, or a stable mathematical boundary
outweighs indirection, parameters, inference/search burden, and maintenance.
A local helper or no change is valid. Reject tactic-only resemblance and
incompatible cases; stop after repeated structural blockers, unproductive
helper chains, or speculative broader search.

This mode tests a bounded reuse hypothesis. User-invoked `lean4-recon` instead
challenges the governing mathematical framing and may explore more broadly.
Report a deeper reframe as a separate option; do not silently switch modes.

Do not add axioms, `sorry`, or `admit` to manufacture success. Behavioral
instructions do not replace runtime/tool authorization controls.

## Completion

- **Assessment:** identify the candidate or reason not to extract, representative
  sites, evidence, tradeoffs, and next action. No production edits on
  assessment-only requests.
- **Implementation:** report the reused/extracted result, authorized consumers
  changed, concrete benefit, verification performed, and limitations. Treat
  unchecked candidate uses or required gates as partial.

Do not commit or push without current-task authorization.
