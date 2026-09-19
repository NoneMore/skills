# Changelog

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
