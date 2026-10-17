---
name: lean4-recon
description: "User-invoked mode to challenge Lean 4/mathlib problem framing by deliberately widening semantic and repository context before durable implementation."
disable-model-invocation: true
license: MIT
---

# Lean 4 Recon

Investigate only semantic boundaries that could change the design decision:

- follow the local construction to the generic structure or theorem family that owns it;
- test local wrappers or predicates against canonical notions, broader theorem placement, and natural duals;
- pressure-test material hypotheses with cheap examples or scratch Lean checks;
- revisit history only when a previously rejecting constraint may have changed;
- look for a lower-level theorem or API change that would remove repeated local machinery.

Use `#check`, `#synth`, `#print`, scratch `example`s, minimal imports, concrete instances, and focused repository search as cheap discriminators. Prefer project evidence over verbal plausibility when an inexpensive check can distinguish alternatives.

Production source is observational by default; make durable edits only when requested after the investigation converges. Do not force novelty, and distinguish verified facts, working hypotheses, and unresolved alternatives.

## Completion

Stop when a better framing is supported, a real small set of tradeoffs remains, or plausible expansion paths have been checked and further widening is unlikely to change the decision. Return the reframe or reason to retain the current one, decision-changing evidence, material uncertainty, and next concrete action.
