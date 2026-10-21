# Proof architecture

Use when a correct proof may follow an unnecessarily indirect or fragile *mathematical mechanism*. This is not general proof cleanup or an invitation to edit.

## Search path

1. Recover the theorem's intended claim, central invariant, and the role of existing lemmas. If correctness is uncertain, record that limit rather than assume a verified baseline.
2. Separate proof mechanisms (induction, transport, universal properties, normal forms, canonical library theorems) from tactic-level syntax.
3. Identify a credible structural alternative: a canonical theorem, stronger induction principle, lower-level law, or explicit invariant replacing repeated conversions.
4. Inspect representative subgoals and material dependencies; avoid speculative broad tactic search or optimizing for line count.
5. Ask if the alternative changes mathematical clarity, stability, or verification cost, and whether it creates new dependencies or hypotheses.

## Discriminating evidence

- Test the pivotal alternative step in scratch Lean against the same statement and trust assumptions; follow one representative path when composition is at issue.
- Compare reliance on definitional accidents, rewrite ordering, coercions, inference, and automation search. Measure performance only when relevant to the decision.
- Probe a plausible countervailing cost: stronger prerequisites, opaque automation, import churn, or harder maintenance.

## Judgment and stop

Distinguish mathematical directness from brevity. Retain the existing proof if an alternative is only cosmetically shorter or its costs outweigh the benefit. Stop with a bounded comparative judgment; verified production edits belong to subsequent authorized execution.

If a proof alternative depends on a reusable invariant or different governing object, follow [abstraction/reuse](abstraction-reuse.md) or [framing](mathematical-framing.md) for that decision, not as automatic parallel assignments.
