# Project tracker

A small backend-independent contract for tracked project work, plus portable shaping for deciding what kind of engineering work should happen next.

- [`setup-tracker/ISSUE-MODEL.md`](setup-tracker/ISSUE-MODEL.md) defines tracker semantics.
- [`setup-tracker/github.md`](setup-tracker/github.md) and [`setup-tracker/local-markdown.md`](setup-tracker/local-markdown.md) define backend representation.
- `setup-tracker` configures one backend and publishes the contract without adopting existing work.
- Published contracts are versioned; setup stops on a version mismatch rather than inferring compatibility or migrating tracked work.
- `shape-work` uses existing project evidence to distinguish a direct change, a bounded investigation, explicit execution planning, or a consequential user decision without depending on harness-specific Plan Mode behavior.
- Shaping is read-only by default. Tracker persistence is optional and, when explicitly requested, follows the published tracker contract rather than persisting transient implementation mechanics.

Repository taxonomy, source-specific ingestion and triage, execution coordination, migration, delivery policy, public issue forms, additional tracker vendors, and changes to the current Matt skills remain outside this scope. `shape-work` may hand off to the reusable execution investigation/planning disciplines; it does not redefine them.
