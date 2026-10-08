# Reference Map

Use this map to load the minimum sufficient context. `SKILL.md` is the canonical shared behavioral contract; workflow files below are canonical for their task-specific behavior.

## Primary workflows

- `workflows/prove.md` — proving, sorry filling, and compiler-error repair
- `workflows/formalize.md` — drafting and formalization from informal claims
- `workflows/disprove.md` — counterexample search and certified refutation
- `workflows/review.md` — read-only code review
- `workflows/optimize.md` — strategy refactoring, golfing, and performance cleanup
- `workflows/learn.md` — teaching and exploration

Load one primary workflow for a task. Do not preload all six.

## Conditional branches

- `branches/deep-mode.md` — escalation after a bounded proof path fails
- `branches/persistence.md` — explicit run-history persistence
- `branches/runtime-fallbacks.md` — missing LSP/helper/runtime capabilities
- `branches/mathlib-upstream.md` — upstream mathlib conventions and review bar

These files are not part of the normal path unless their condition is active.

## Knowledge by need

- **Search:** `mathlib-guide.md`, `lean-phrasebook.md`, `lean-lsp-server.md`, `lean-lsp-tools-api.md`
- **Diagnostics:** `compilation-errors.md`, `compiler-guided-repair.md`, `instance-pollution.md`
- **Proof construction:** `sorry-filling.md`, `tactics-reference.md`, `tactic-patterns.md`, `calc-patterns.md`, `simp-reference.md`, `grind-tactic.md`, `proof-templates.md`
- **Optimization:** `proof-simplification.md`, `proof-refactoring.md`, `proof-golfing.md`, `proof-golfing-patterns.md`, `performance-optimization.md`, `profiling-workflows.md`
- **Style/review:** `mathlib-style.md`, `mathlib-review-taxonomy.md`, `verso-docs.md`, `linter-authoring.md`
- **Domains:** `domain-patterns.md`, `measure-theory.md`, `axiom-elimination.md`
- **Advanced Lean:** `lean4-custom-syntax.md`, `metaprogramming-patterns.md`, `compiler-internals.md`, `ffi-interop.md`, `json-patterns.md`, `scaffold-dsl.md`

## Upstream implementation notes

The imported package also retains upstream documents such as `cycle-engine.md`, `disprove-engine.md`, `agent-workflows.md`, `subagent-workflows.md`, `command-examples.md`, `learn-pathways.md`, `run-store.md`, and `handoff-contract.md`.

Treat these as specialized implementation/compatibility material, not common-path instructions. Load them only when a selected workflow or conditional branch needs the corresponding detail. This avoids paying the context cost of plugin command parsing, host adapters, persistence protocols, or subagent orchestration during ordinary Lean work.