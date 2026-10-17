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
- pressure-test material hypotheses with focused examples or scratch Lean checks;
- revisit history only when a previously rejecting constraint may have changed;
- look for a lower-level theorem or API change that would remove repeated local machinery.

Use `#check`, `#synth`, `#print`, scratch `example`s, minimal imports, concrete instances, and focused repository search as discriminators. Prefer the smallest experiment that can distinguish live design alternatives and project evidence over verbal plausibility.

When composition across an abstraction boundary is itself uncertain, follow one representative path until it closes or exposes the lowest-level obstruction. Local proof iteration is justified while its outcome can still change that diagnosis; do not then broaden into parallel cases or production implementation.

Production source is observational by default; make durable edits only when requested after the investigation converges. Do not force novelty, and distinguish verified facts, working hypotheses, and unresolved alternatives.

## Completion

Stop when the design decision is stable: a relevant representative path closes or exposes the lowest-level obstruction, a real small set of tradeoffs remains, or plausible expansion paths have been checked and further investigation is unlikely to change the decision. Return the reframe or reason to retain the current one, decision-changing evidence, material uncertainty, and next concrete action.
