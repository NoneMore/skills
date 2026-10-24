---
name: lean-blueprint-author
description: Create, edit, and synchronize leanblueprint blueprints and their Lean mappings/status.
disable-model-invocation: true
---

# Lean Blueprint Author

## Purpose

Create, modify, or synchronize a useful mathematical blueprint while pushing repeatable project-state work into deterministic tooling.
Use the model for mathematical structure, semantic correspondence, and editing judgment; use Lean/leanblueprint and the bundled script for facts they can determine mechanically.

## Accepts

- a target theorem, definition, construction, or proof route to add;
- an existing blueprint region that needs mathematical or structural editing;
- an existing blueprint whose `\lean`, `\leanok`, `\mathlibok`, or related status needs synchronization with the Lean project;
- standalone blueprint LaTeX when no project checkout is available.

## Core Invariants

1. **Keep the mathematical route minimal.** Track nodes that are needed to state/prove targets, reused later, or worth independent formalization. Keep routine steps in proof prose.
2. **Separate statement and proof dependencies.** Statement prerequisites belong on the statement/definition; proof-only dependencies belong on its proof.
3. **Treat metadata as factual.** Do not invent Lean declarations, citations, or formalization status. Leave ambiguous mappings/status unresolved.
4. **Preserve project style and scope.** Reuse existing theorem environments, labels, macros, citations, proof layout, and build conventions. Edit the smallest useful region.
5. **Do not change mathematics merely to make metadata fit.** A pure Update reports a blueprint/Lean semantic mismatch and leaves the disputed metadata unchanged unless the requested outcome also includes repairing blueprint content.
6. **Prefer mechanical projection over manual reconstruction.** When working in a project, obtain graph/mapping/status facts from project-native tooling or the bundled read-only tooling rather than manually re-parsing source when a reliable mechanical view is available.

For macro meanings and upstream behavior, see `references/leanblueprint-basics.md`.
For Create/Modify/Update workflows and validation, see `references/workflows.md`.

## Bundled Mechanical Tool

`scripts/blueprint.py` is a read-only helper for standard leanblueprint projects. It deliberately reuses plasTeX/leanblueprint's parsed model instead of implementing a second TeX parser.

Use it from a real project when its standard projection is supported:

```sh
python3 <skill-path>/scripts/blueprint.py check --project-root <project-root>
python3 <skill-path>/scripts/blueprint.py inspect --project-root <project-root> > /tmp/blueprint-state.json
python3 <skill-path>/scripts/blueprint.py diff BEFORE.json AFTER.json
```

- `check` verifies deterministic projection/graph invariants such as unresolved dependencies, silent single-value macro overwrite, invalid proof association, cycles, and conflicting mechanical status.
- `inspect` emits normalized JSON only after those invariants pass. It exposes node identity/location, statement/proof dependencies, Lean mappings, and raw status markers; it does not copy mathematical prose or infer readiness/priority.
- `diff` compares two saved normalized states without parsing TeX.
- exit `0` means the requested mechanical operation succeeded; exit `1` means a valid projection was obtained but `check` found violations; exit `2` means the tool could not establish a reliable projection.

If the project already provides a clearly authoritative read-only blueprint status/graph tool, use it for facts it computes reliably. Do not build a provider framework around project-specific tools.
If the bundled tool exits `2`, do not silently fall back to a regex parser or claim equivalent mechanical coverage. Continue with the real project source/upstream commands as needed and bound the missing automation explicitly.

The bundled tool is not semantic validation and does not replace `leanblueprint web`, Lean builds, `checkdecls`, or project-native validation.

## Operation Dispatch

Choose the smallest operation matching the user's outcome:

- **Create** — add a new mathematical dependency/proof route or tracked node set.
- **Modify** — change existing blueprint mathematics, structure, labels, dependencies, proof placement, or prose.
- **Update** — synchronize existing blueprint mappings/status with the current Lean project while keeping the mathematical route unchanged.

Mixed requests may combine operations, but do not silently broaden a pure synchronization request into mathematical rewriting.

## Done When

- **Create:** the target and sufficient mathematical route are expressed; statement/proof dependencies are placed correctly; metadata is evidence-backed; project validation relevant to the edit passes or remaining failures are explicit.
- **Modify:** the requested mathematical/structural change is reflected; directly affected labels/dependencies/proof associations are coherent; unrelated content is preserved; relevant validation passes or remaining failures are explicit.
- **Update:** every changed mapping/status is supported by the project; ambiguous or semantically mismatched cases remain unresolved rather than guessed; relevant declaration/build checks use current generated state.

For project work, finish by inspecting the actual diff and reporting only material changes, validation results, and unresolved issues.

## Boundaries

Do not turn the Skill into a second leanblueprint implementation. Avoid parser emulation, runtime compatibility matrices, CI simulators, confidence/evidence taxonomies, priority planners, or broad repository audits unless a concrete project failure makes one necessary.
Deterministic helper code should project/check existing upstream semantics; mathematical interpretation remains with the model and the project's authoritative sources.
