---
name: lean-blueprint-author
description: Create, edit, and synchronize Lean blueprints with a Lean project using leanblueprint conventions.
disable-model-invocation: true
---

# Lean Blueprint Author

Version: **v4.1**

Use this Skill for three tasks:

- **Create** a dependency/proof route for a target theorem, definition, or other tracked node.
- **Modify** existing blueprint content, structure, dependencies, or proof routes.
- **Update** `\lean`, `\leanok`, `\mathlibok`, and related metadata from the current Lean project.

The goal is a useful mathematical blueprint, not a framework around the blueprint.
Prefer the project's existing conventions and leanblueprint's documented workflow over custom machinery.

## Core Rules

1. **Keep the route minimal.** Include nodes that are needed to state or prove the target, reused later, or worth tracking as independent formalization work. Keep routine steps in proof prose.
2. **Separate statement and proof dependencies.** Put statement dependencies in the theorem/definition environment and proof-only dependencies in the proof environment.
3. **Treat metadata as factual.** Add or change Lean names/status only when the local project supports the claim. Do not invent declaration names or citations.
4. **Preserve project style.** Reuse the project's theorem environments, labels, macros, citation style, and proof layout. Avoid normalizing unrelated content.
5. **Edit the smallest useful region.** For an existing blueprint, preserve surrounding prose and metadata unless the requested change requires touching them.
6. **Validate what changed.** Prefer one relevant build/check over broad defensive audits.

For leanblueprint macro meanings and standard project layout, see `references/leanblueprint-basics.md`.
For operation-specific steps, see `references/workflows.md`.

## Project Discovery

For work on a real project, locate:

- the Lean project root containing `lakefile.lean` or `lakefile.toml`;
- the blueprint source, usually `blueprint/src/content.tex` in the stock layout;
- `blueprint/src/web.tex` when building the web blueprint;
- `blueprint/src/print.tex` when building the PDF.

Do not require the stock layout when the repository already uses a custom build command or file organization.
For standalone LaTeX snippets or pasted blueprint fragments, a project checkout is not required.

Do not run `leanblueprint new` unless the user asks to initialize a blueprint. The command is an opinionated convenience for Lake/Git/GitHub projects, not a prerequisite for using leanblueprint.

## Operation Dispatch

Choose the operation from the user's goal:

- **Create** — author a new route or set of nodes for a target.
- **Modify** — change an existing blueprint's mathematical content, proof route, structure, labels, or dependencies.
- **Update** — synchronize an existing blueprint with current Lean declarations and formalization status without redesigning the mathematics.

If a request mixes operations, do the smallest combination that directly satisfies it. For example, a synchronization that exposes a genuinely missing mathematical lemma may become a small Modify task.

## Validation

When editing a real project, use the narrowest relevant checks:

- Run the project's web build, normally `leanblueprint web`, after structural, dependency, or `\lean{...}` mapping edits. The web build regenerates `blueprint/lean_decls` in the stock workflow.
- If Lean mappings/status changed, ensure the Lean project is built (`lake build` as needed), rebuild the web blueprint, then run `leanblueprint checkdecls` (or the project's equivalent declaration check). Do not rely on `checkdecls` against a stale `blueprint/lean_decls`.
- Use `leanblueprint all` when a broad final validation is appropriate.
- Run `leanblueprint pdf` when the user requests PDF validation, print-specific content changed, or the project's bibliography workflow requires it before the web build.
- Inspect the resulting diff and fix errors caused by the edit.

A successful build or `checkdecls` confirms syntax/declaration availability, not mathematical equivalence, proof completeness, or absence of placeholders such as `sorry`. Use the Lean source/types and implementation when deciding whether a blueprint statement or proof is actually formalized.

## Avoid Overengineering

Keep the Skill focused on blueprint authoring and synchronization:

- do not add runtime-pin auditors, CI simulators, parser emulators, evidence taxonomies, or safety-gate frameworks unless a concrete project problem requires them;
- do not scan unrelated workflows, lockfiles, or repository history merely to establish a theoretical runtime contract;
- prefer the project's real Lean/leanblueprint commands over bespoke static-analysis machinery;
- when version-specific behavior actually matters, inspect that installed/upstream behavior directly and address only the concrete issue.

## Output

Prefer concrete edits over long process reports.

- For **Create**, provide insertion-ready blueprint LaTeX and a short dependency summary.
- For **Modify**, show/apply the changed region and summarize structural/dependency effects.
- For **Update**, summarize Lean-name/status changes and unresolved mappings.
- When commands were run, report only the relevant results and remaining issues.
