---
name: lean4-skills
description: "Legacy explicit entry point for the Lean 4 formal-mathematics skill family. Prefer the outcome-specific lean4-prove, lean4-formalize, lean4-refute, lean4-diagnose, lean4-trust, lean4-review, or lean4-optimize skills."
license: MIT
disable-model-invocation: true
---

# Lean 4 — compatibility entry point

This is a temporary compatibility shim for callers that explicitly invoke `$lean4-skills`. It does not own automatic discovery or model routing; new work should use the outcome-specific skill directly.

Choose the capability that owns the requested outcome:

- [prove](prove/SKILL.md) — complete or repair an already-settled proof target;
- [formalize](formalize/SKILL.md) — design or revise the Lean statement;
- [refute](refute/SKILL.md) — Lean-certify a counterexample or negation;
- [diagnose](diagnose/SKILL.md) — diagnose non-proof Lean/Lake failures in formal-math work;
- [trust](trust/SKILL.md) — inspect or remove unwanted trust dependencies;
- [review](review/SKILL.md) — independently review proof code;
- [optimize](optimize/SKILL.md) — improve an already-correct proof.

Load and follow the selected child skill rather than reproducing its workflow here. If one request genuinely contains multiple outcomes, compose the minimum necessary child skills at their explicit boundaries.

This shim should not become an authoritative second copy of Lean behavior. Remove it once known callers that depend on the legacy `$lean4-skills` name have migrated.
