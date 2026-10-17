---
name: lean4-recon
description: "User-invoked mode for open-ended formal-mathematics investigation in Lean 4/mathlib when the user wants to challenge or improve the current problem framing before committing to a durable implementation. Deliberately widen semantic and repository context to look for canonical abstractions, broader theorems, dual formulations, assumption boundaries, historical constraints, or lower-level design leverage."
disable-model-invocation: true
license: MIT
---

# Lean 4 Recon

Deliberately widen context around a Lean/mathlib problem before committing to a durable design. The purpose is to test whether the local framing is really an instance of a more canonical abstraction, theorem, characterization, duality, or weaker assumption boundary.

This mode is user-invoked because it spends context divergently rather than merely finishing the local artifact.

## Investigation

Start from the local declaration and cross only semantic boundaries that could change the design decision:

- follow the implementation to the generic structure or theorem family that owns it;
- test whether local predicates, wrappers, aggregates, or helpers are canonical existing notions;
- check whether the essential theorem belongs at a more general layer or has a natural dual;
- pressure-test material hypotheses with cheap examples or scratch Lean checks;
- revisit history only when a previously rejecting constraint may have changed;
- look for a small lower-level theorem or API change that would remove repeated local machinery.

Use `#check`, `#synth`, `#print`, scratch `example`s, minimal imports, concrete instances, and focused repository search as cheap discriminators. Prefer project evidence over verbal plausibility when an inexpensive check can distinguish the alternatives.

Production source is observational by default. Experiments are allowed, but do not silently promote them into durable edits. If implementation is also requested, make only the changes the user authorized after the investigation has converged.

Do not force novelty: retaining the current framing is a valid outcome. Distinguish verified facts, working hypotheses, and unresolved alternatives.

## Stop and completion

Stop when a better framing is supported well enough to proceed, a real small set of tradeoffs remains, or the plausible expansion paths have been checked and further widening is unlikely to change the decision.

Return the material reframe or reason to retain the current one, the evidence that changes the decision, any remaining uncertainty that could still matter, and the next concrete action.
