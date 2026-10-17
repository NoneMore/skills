---
name: lean4-mathlib-contribute
description: "Use when a concrete Lean 4 artifact already exists and the requested outcome is to assess or adapt it specifically for upstream mathlib contribution readiness. Own current contribution-policy compliance, nearby mathlib conventions, canonical API and generality fit, naming/docs/import discipline, proof robustness, simp/global-attribute concerns, and integration evidence needed for an upstream-ready result. Do not use merely because a task imports, searches, or proves with mathlib, and do not use when the primary outcome is still initial statement formalization, ordinary proof completion, a concrete diagnostic, trust audit, certified refutation, generic review, or local optimization."
license: MIT
---

# Lean 4 Mathlib Contribute

## Purpose

Assess or adapt an existing Lean artifact so its suitability for upstream mathlib contribution is supported by current upstream policy, nearby current code, and the verification evidence appropriate to the affected scope.

## Preconditions and invariants

- A concrete Lean artifact already exists: a declaration, proof, file, diff, or PR-sized change that can be inspected against upstream expectations.
- The requested outcome is explicitly upstream mathlib contribution readiness, not merely using mathlib as a dependency or theorem library.
- Treat mathlib contribution policy as live external state. Consult current authoritative upstream guidance at execution time rather than relying on cached policy text in this Skill.
- Inspect nearby current mathlib code when local conventions, API shape, placement, naming, imports, attributes, or proof style materially affect the readiness decision.
- Review-only requests are read-only. When adaptation is requested, make bounded changes justified by an upstream-readiness finding.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the accepted trust basis to satisfy an upstream convention.

## Workflow

1. Establish the concrete artifact, intended upstream destination or neighborhood when known, and whether the user wants readiness findings only or actual adaptation.
2. Retrieve the current authoritative mathlib contribution guidance relevant to the artifact. If live policy cannot be consulted, continue only with independently verifiable code evidence and state that policy compliance remains unverified.
3. Inspect the nearest relevant current mathlib declarations/files and evaluate the artifact against material upstream concerns: canonical abstractions and APIs, theorem generality and hypothesis boundary, namespace and naming, declaration placement, docstrings, imports, attributes and simp behavior, proof robustness, duplication, and maintenance cost.
4. If adaptation is requested, apply the smallest coherent changes that address substantiated readiness gaps. Search, small experiments, proof repairs, and local diagnostics may remain internal substeps when they are bounded means to the upstream-readiness outcome; do not silently turn the task into unrelated refactoring.
5. Run the repository-configured Lean/mathlib gates that establish the affected correctness and integration scope, and report exactly what ran. Re-check any policy or nearby-code criterion materially affected by the edits.

## Boundaries

Ordinary Lean work that happens to use mathlib stays with its direct outcome owner. Creating a declaration from mathematical intent is `lean4-formalize`; completing a fixed proof is `lean4-prove`; resolving a concrete Lean/Lake failure is `lean4-diagnose`; trust-basis work is `lean4-trust`; generic review and local proof improvement remain `lean4-review` and `lean4-optimize`.

An eventual plan to submit upstream does not by itself move the current task here. Select this Skill when upstream suitability or adaptation is itself the requested result for an existing artifact.

Upstream readiness may justify changes to API shape, generality, naming, imports, documentation, or proof structure that a narrower Skill would normally preserve. Make those changes only when the upstream-readiness request authorizes them, and surface any material semantic or public-API change explicitly rather than treating it as style cleanup.

## Completion

Claim upstream readiness only when the applicable current contribution guidance was consulted, relevant nearby current code was inspected where it affects the decision, the artifact passes the required verification/integration gate, and no known material upstream blocker remains.

For review-only work, return prioritized readiness findings with evidence and concrete acceptance criteria without editing. If live policy, nearby source, or a required verification gate could not be checked, report the strongest verified result and the remaining readiness uncertainty rather than calling the artifact upstream-ready.
