# `simp` and Simp-Lemma Design

Repository-specific simplification policy takes precedence over this generic guidance.

Use when debugging simplification, deciding whether a theorem belongs in the global simp set, or authoring a simproc.

## Choose the mechanism

- one directed local rewrite -> `rw`;
- a known small local normalization set -> `simp only [...]`;
- terminal closure where the project's default simp set is intentionally part of the proof -> `simp` / `simpa`;
- a broadly canonical rewrite -> consider `@[simp]`;
- computed canonical rewriting that cannot be expressed cleanly as ordinary simp lemmas -> consider a simproc.

Do not promote a local convenience into global simp policy without a canonical direction.

## Simp normal form

"Normal form" is relative to the active simp context: lemmas, simprocs, configuration, congruence rules, hypotheses, and discharger.

Before adding `@[simp]`:

1. simplify the proposed left-hand side with the intended context excluding the candidate lemma;
2. if it already rewrites, the candidate LHS is usually not the right global form;
3. check that the RHS moves toward the intended stable representation;
4. check for cycles or competing rewrites;
5. ask whether local `simp only [...]` is sufficient.

Global simp lemmas should encode a stable canonical orientation, not merely an equation that happened to help one proof.

## Debugging

Start with `simp?` or a tiny `simp only [...]` set. If that clarifies the issue, keep the proof explicit. Use simp tracing only after narrowing the problem; raw traces are noisy.

If the current simplifier reaches a fixed point and the goal remains open, inspect the residual goal instead of reflexively adding another global simp lemma. Use an explicit local rewrite, proof step, or solver as appropriate.

## Simprocs

Use a simproc when rewriting genuinely depends on deterministic computation or structured proof construction over the expression being simplified. Keep it narrow, cheap, terminating, and predictable.

A simproc should decline inputs outside its intended domain rather than launching hidden unbounded proof search. Prefer ordinary simp lemmas when they express the same behavior clearly.

For performance-motivated simplification changes, compare against a verified baseline and follow [performance guidance](performance.md) when measurement matters.
