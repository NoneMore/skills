# Upstream Mathlib Branch

Load when the repository is mathlib or the user explicitly says the work is intended for an upstream mathlib contribution. Do not impose this branch merely because mathlib is a dependency.

## Authoritative contribution policy

Treat the current Lean Community contribution documentation as authoritative instead of caching a local copy of its rules.

Normative pages:

- [Library Style Guidelines](https://leanprover-community.github.io/contribute/style.html)
- [Mathlib naming conventions](https://leanprover-community.github.io/contribute/naming.html)
- [Documentation style](https://leanprover-community.github.io/contribute/doc.html)

Source Markdown in the Lean Community website repository:

- [style.md](https://github.com/leanprover-community/leanprover-community.github.io/blob/lean4/templates/contribute/style.md)
- [naming.md](https://github.com/leanprover-community/leanprover-community.github.io/blob/lean4/templates/contribute/naming.md)
- [doc.md](https://github.com/leanprover-community/leanprover-community.github.io/blob/lean4/templates/contribute/doc.md)

When a style, naming, module/import, or documentation decision matters, consult the current source rather than relying on remembered or vendored rules. If the authoritative source is unavailable, inspect nearby current mathlib code and keep any material uncertainty explicit rather than claiming normative compliance.

## Additional expectations

- Search for an existing or more general result before adding a new public declaration.
- Review API generality, file placement, imports, attributes, instances, and documentation using `references/mathlib-review-taxonomy.md`.
- For new files, respect the repository's current module/root-file generation requirements rather than caching assumptions about them.
- Treat mathlib-specific review findings as blockers only when the task is actually targeting upstream mathlib; otherwise they are advisory.

Local Lean projects may intentionally choose different style or API tradeoffs. The common skill follows the local project unless this branch is active.
