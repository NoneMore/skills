---
name: lean4-mathlib-contribute
description: "User-invoked mode for assessing or adapting an existing Lean 4 artifact specifically for upstream mathlib contribution readiness using current contribution policy, nearby mathlib conventions, API and generality fit, naming/docs/import discipline, proof robustness, attributes, and integration evidence."
disable-model-invocation: true
license: MIT
---

# Lean 4 Mathlib Contribute

## Purpose

Assess or adapt an existing Lean artifact so its suitability for upstream mathlib contribution is supported by current upstream policy, nearby current code, and the verification evidence appropriate to the affected scope.

## Preconditions and invariants

- A concrete Lean artifact already exists: a declaration, proof, file, diff, or PR-sized change that can be inspected against upstream expectations.
- Treat mathlib contribution policy as live external state. Consult current authoritative upstream guidance at execution time rather than relying on cached policy text in this Skill.
- Inspect nearby current mathlib code when local conventions, API shape, placement, naming, imports, attributes, or proof style materially affect the readiness decision.
- Review-only requests are read-only. When adaptation is requested, make bounded changes justified by an upstream-readiness finding.
- Do not introduce new axioms, `sorry`, `admit`, or otherwise weaken the accepted trust basis to satisfy an upstream convention.

## Workflow

1. Establish the concrete artifact, intended upstream destination or neighborhood when known, and whether the user wants readiness findings only or actual adaptation.
2. Retrieve the current authoritative mathlib contribution guidance relevant to the artifact. If live policy cannot be consulted, continue only with independently verifiable code evidence and state that policy compliance remains unverified.
3. Inspect the nearest relevant current mathlib declarations/files and evaluate the artifact against material upstream concerns: canonical abstractions and APIs, theorem generality and hypothesis boundary, namespace and naming, declaration placement, docstrings, imports, attributes and simp behavior, proof robustness, duplication, and maintenance cost.
4. If adaptation is requested, apply the smallest coherent changes that address substantiated readiness gaps. Search, small experiments, proof repairs, and local diagnostics may be used as bounded supporting work.
5. Run the repository-configured Lean/mathlib gates that establish the affected correctness and integration scope, and report exactly what ran. Re-check any policy or nearby-code criterion materially affected by the edits.

Upstream readiness may justify changes to API shape, generality, naming, imports, documentation, or proof structure that ordinary artifact work would preserve. Make those changes only when the user's explicit invocation and requested adaptation authorize them, and surface any material semantic or public-API change rather than treating it as style cleanup.

## Completion

Claim upstream readiness only when the applicable current contribution guidance was consulted, relevant nearby current code was inspected where it affects the decision, the artifact passes the required verification/integration gate, and no known material upstream blocker remains.

For review-only work, return prioritized readiness findings with evidence and concrete acceptance criteria without editing. If live policy, nearby source, or a required verification gate could not be checked, report the strongest verified result and the remaining readiness uncertainty rather than calling the artifact upstream-ready.
