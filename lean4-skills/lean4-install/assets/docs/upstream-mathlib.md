<!-- lean4-install: managed-guidance -->
# Upstream Mathlib

Use when the repository is mathlib or the user explicitly says the work is intended for an upstream mathlib contribution. Do not impose this guidance merely because mathlib is a dependency.

## Current contribution policy

Consult the current Lean Community documentation for normative decisions instead of treating this installed document as authoritative policy. Start with the repository-wide contribution policy, then use specialized current pages for decisions in their scope:

- [Contributing to mathlib](https://leanprover-community.github.io/contribute/index.html)
- [Library Style Guidelines](https://leanprover-community.github.io/contribute/style.html)
- [Mathlib naming conventions](https://leanprover-community.github.io/contribute/naming.html)
- [Documentation style](https://leanprover-community.github.io/contribute/doc.html)

If the authoritative source is unavailable, inspect nearby current mathlib code and keep material uncertainty explicit rather than claiming normative compliance.

## Review bar

For upstream-targeted work, additionally review:

- **Existing results and API:** equivalent or more general results, weakest useful hypotheses, representation choices, public/private surface, argument order, and whether new API is substantive rather than speculative.
- **Placement, imports, and modules:** the lowest sensible module, narrow imports, public/private visibility, and current generated root/import obligations.
- **Style and documentation:** formatting, naming, namespace placement, natural dot notation, appropriate module/declaration docs, and comments that explain mathematical or design intent rather than development history.
- **Attributes and simplification:** `@[simp]`, `@[ext]`, reducibility, coercions, and similar attributes as global API decisions. A locally useful rewrite is not automatically a good global simp lemma; follow [simplification guidance](simplification.md) when normal-form decisions matter.
- **Instances:** diamonds, loops, unnecessary global instances, accidental instance selection, and fragile inference. When several instances of the same class are relevant, inspect which instance terms were elaborated against.

Treat these expectations as blockers only when the task actually targets upstream mathlib; otherwise local project conventions take precedence.
