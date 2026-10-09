# Upstream Mathlib Branch

Load when the repository is mathlib or the user explicitly says the work is intended for an upstream mathlib contribution. Do not impose this branch merely because mathlib is a dependency.

## Additional expectations

- Apply mathlib's file/header, naming, line-width, documentation, import, and proof-style conventions from `../mathlib-style.md`.
- Search for an existing or more general result before adding a new public declaration.
- Review API generality, file placement, imports, attributes, instances, and documentation using `../mathlib-review-taxonomy.md`.
- For new files, respect the repository's current module/root-file generation requirements rather than caching assumptions about them.
- Treat mathlib-specific review findings as blockers only when the task is actually targeting upstream mathlib; otherwise they are advisory.

Local Lean projects may intentionally choose different style or API tradeoffs. The common skill follows the local project unless this branch is active.