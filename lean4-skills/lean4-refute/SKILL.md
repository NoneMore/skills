---
name: lean4-refute
description: "Use for formal mathematics in Lean 4/mathlib when the requested outcome is to show a proposition is false or to find and Lean-certify a counterexample or proof of its negation. Do not treat failed proof search or exploratory counterexample probing alone as certified falsity."
license: MIT
---

# Lean 4 Refute

## Purpose

Produce a Lean-certified logical refutation of a target proposition while preserving the original target.

## Invariants

- Preserve the original declaration; encode witnesses or negations as separate checked results.
- Failure to prove a proposition is not evidence that it is false.
- Do not weaken the trust basis with new axioms, `sorry`, or `admit` to manufacture a refutation.
- A refutation is not certified if it relies on the target declaration itself as a premise or on unresolved `sorry`/`admit` or other assumptions forbidden by the agreed trust policy.

## Workflow

1. Resolve the exact proposition and inspect its logical shape.
2. Choose the cheapest promising bounded route: a concrete witness, a small decidable/finite search, contradiction with existing accepted facts, or a direct proof of the negation.
3. Search local declarations and active imports before widening to mathlib. Search by meaning/type rather than guessed names and validate candidates in the actual project context.
4. Encode the candidate witness or negation as a separate result without invoking the target declaration itself as evidence, then ask Lean to certify it.
5. Verify that result in the actual project context. When the target or surrounding environment contains `sorry`/`admit`, custom axioms, or otherwise uncertain trust dependencies, inspect the refutation's trust basis with `#print axioms` or an equivalent environment check and reject certification if it depends on `sorryAx`, the target as an assumption, or another dependency forbidden by the agreed policy. If changed imports or project integration matter, use a gate that rebuilds or exercises that boundary rather than relying on possibly stale file-local artifacts, and report the gate that actually ran.

Keep search bounded. If the proposition instead needs redesign, use `lean4-formalize`; if the user wants to keep proving the fixed target, use `lean4-prove`. If the requested work is to investigate whether an assumption is genuinely necessary, probe examples and counterexamples, or challenge the surrounding framing without yet requiring certified falsity, use `lean4-recon`. Once a Lean-certified disproof itself becomes the requested outcome, use this Skill.

## Outcomes

- **REFUTED:** Lean typechecks a logically independent result that refutes the target under the agreed trust basis; the result does not use the target declaration as a premise, and any required trust inspection shows no forbidden dependency.
- **WITNESS_UNCERTIFIED:** a plausible witness or argument exists but Lean certification or the required trust check did not complete.
- **INCONCLUSIVE:** bounded search produced no certified refutation.

Only `REFUTED` is a certified disproof.
