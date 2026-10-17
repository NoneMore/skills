# Lean 4 Skills

A jointly installed family of eight capabilities for formal mathematics in Lean 4 and mathlib. The collection root is not itself a Skill.

Six Skills are model-discoverable; two broader modes are explicitly user-invoked. There is no family router and no requirement that exactly one Skill own a request.

The split addresses an observed discovery failure: task-specific guidance hidden behind a broad Skill was not loaded reliably enough, and distinctions available only after activation could not help pre-activation discovery. The family therefore exposes outcome-specific contracts directly while keeping overlap bounded.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Model-discoverable capabilities

- `lean4-formalize` — design or explicitly revise a Lean declaration.
- `lean4-prove` — complete or repair a proof for an existing target.
- `lean4-refute` — find and independently Lean-certify a counterexample or negation.
- `lean4-diagnose` — identify a root cause and migration path for Lean/Lake/build/integration failures.
- `lean4-review` — independently review Lean proof code or audit a declaration's trust dependencies; review-only requests are read-only.
- `lean4-optimize` — improve an already-correct proof from a verified baseline.

Discovery is recall-oriented but still has a context budget. Compatible overlap is acceptable when useful, but blanket activation of most or all Skills defeats the purpose of the split. Collection discovery evals therefore test both required recall and bounded activation.

## User-invoked capabilities

- `lean4-recon` — deliberately widen semantic/repository context to challenge the current framing before committing to implementation.
- `lean4-mathlib-contribute` — assess or adapt an existing artifact for upstream mathlib using current upstream policy and nearby current code.

These set `disable-model-invocation: true`: the user explicitly chooses the larger context spend or upstream-readiness bar.

## Defensive structure

Keep defenses only where they change behavior or completion claims.

Collection-level integrity regressions cover cross-cutting failures such as stale imported artifacts, manufactured success through trust weakening, and verification claims made without the required tooling or gate. Individual Skills state these common constraints tersely and keep detailed doctrine only for Skill-specific risks.

Examples of justified local defenses include independent refutation when the target itself may contain `sorry`, read-only review, optimization from a verified baseline, and live upstream policy for contribution work.

## Knowledge placement

Keep specialized knowledge at the lowest level that earns its cost. Optimization references remain under `lean4-optimize/references/`. Small common behaviors such as local-first mathlib search stay concise in the Skills that use them rather than adding another routing or shared-reference layer.

Collection-level provenance and licensing live once in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Evals

- `evals/routing-evals.md` tests required discovery, bounded compatible overlap, and adjacent-intent exclusion.
- `evals/integrity-evals.md` owns cross-cutting verification/trust regressions.
- Per-Skill behavioral evals test only behavior that materially distinguishes that Skill.

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.
