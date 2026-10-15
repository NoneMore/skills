# Changelog

## Unreleased

- Added a bundled read-only `scripts/blueprint.py` mechanical layer with `check`, `inspect`, and normalized-state `diff` commands.
- Reused the project's real plasTeX/leanblueprint dependency graph instead of reintroducing a regex/static parser emulator.
- Added deterministic checks for projection failures such as repeated single-value `\uses`/`\lean`/`\proves`, unresolved or invalid dependency targets, proof-association conflicts, duplicate labels across objects, dependency cycles, conflicting status, and raw/upstream projection mismatch.
- Added source file/line capture and a small normalized JSON state that keeps statement/proof dependencies separate without copying mathematical prose or adding planning/readiness heuristics.
- Added ordinary unit tests for the mechanical layer plus an integration test that runs when a leanblueprint runtime is installed.
- Refocused `SKILL.md` and workflows so the model owns mathematical/semantic judgment while repeatable project-state collection and structural verification are delegated to deterministic tooling.
- Tightened Update scope: synchronization no longer silently rewrites mathematical content merely to make metadata fit.

## v4.1

- Kept the `v4.0-slim` information architecture: a short operational `SKILL.md` plus focused basics/workflow references.
- Tightened declaration-check validation: after `\lean{...}` changes, build Lean as needed, rebuild the web blueprint to refresh `blueprint/lean_decls`, then run `leanblueprint checkdecls`.
- Documented the upstream `\lean{...}` storage behavior and retained the rule to use one complete mapping per environment rather than relying on repeated-command merging.
- Clarified that build/checkdecls success does not establish semantic equivalence, proof completeness, or absence of placeholders such as `sorry`.
- Restored a compact anti-overengineering guardrail without reintroducing runtime auditors, CI simulators, parser emulators, evidence taxonomies, or helper-script frameworks.

## v4.0-slim

- Re-centered the Skill on leanblueprint's documented model: `content.tex`, dependency nodes, `\lean`, `\leanok`, `\uses`, and a small set of CLI checks.
- Collapsed shared foundations, output rules, runtime semantics, and validation policy into two short references.
- Removed runtime pin/CI-consumption analysis, confidence levels, evidence-level taxonomy, static parser emulation, and helper scripts/tests.
- Simplified Modify from four authorization levels to a direct minimal-edit workflow.
- Simplified Update to declaration mapping, semantic status synchronization, and targeted validation.
- Kept only practical safeguards: preserve unrelated project content, avoid invented Lean names/status, and validate the surface actually changed.
