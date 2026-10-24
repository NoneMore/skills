# Leanblueprint Basics

This reference follows the public `PatrickMassot/leanblueprint` README/package behavior and the bundled mechanical tool's intentionally narrow projection contract.

## Standard Layout

The stock `leanblueprint` scaffold keeps blueprint sources under `blueprint/src`:

- `content.tex` — main mathematical content, possibly importing more files;
- `web.tex` — plasTeX/web entry point;
- `print.tex` — PDF/LaTeX entry point;
- `macros/common.tex` — macros shared by web and print;
- `macros/web.tex` / `macros/print.tex` — target-specific macros.

Projects may use a custom layout. Follow the project rather than forcing the scaffold.

## Core Macros

### `\lean{Decl.Name}`

Associates the surrounding definition/theorem-like environment with one or more Lean declarations.
Use fully qualified names when needed.

Current upstream stores one declaration list on the surrounding environment while separately collecting names for declaration checking. Repeated `\lean{...}` occurrences do not merge reliably at the node level. Use one complete occurrence per owner.

### `\leanok`

Claims that the surrounding environment is formalized. It may appear on a statement/definition or on its proof.

For synchronization:

- statement-level `\leanok` should correspond to a Lean declaration whose type/meaning matches the blueprint statement;
- proof-level `\leanok` should correspond to an implemented proof/definition, not merely a declaration name that resolves.

The marker is a claim in blueprint metadata. Neither the bundled mechanical checker nor `checkdecls` proves that the claim is semantically correct.

### `\uses{label1,label2}`

Records dependencies for the surrounding environment and drives the dependency graph.

- On a theorem/definition: list what is needed to state/define it.
- On a proof: list results used only in the proof route.

Current `plastexdepgraph` stores a single dependency list on each owner; repeated `\uses` occurrences overwrite rather than merge. Use one complete occurrence per statement/proof.
Prefer direct mathematical dependencies rather than transitive closure.

### `\notready`

Marks a statement/definition whose mathematical blueprint is not ready to formalize.
Do not use it merely because the Lean implementation is unfinished.
A node that is simultaneously `\notready` and node-level `\leanok`/`\mathlibok` has mechanically conflicting status.

### `\mathlibok`

Marks a node already supplied by Mathlib. Upstream also sets the containing node's `leanok` status.
Use it for the node itself, not because its proof happens to use Mathlib.

### `\proves{label}`

Associates a proof with a statement when the proof does not immediately follow that statement.
Use it when reordering/separating proofs would otherwise make the association unclear.
The target must resolve to a tracked dependency-graph node.

### `\discussion{issue}`

Links the surrounding statement/definition to a GitHub issue.
Preserve it unless the task changes that discussion link.

## Dependency-Graph Semantics

Leanblueprint delegates dependency graphs to `plastexdepgraph`.
The parsed graph keeps statement dependencies and proof dependencies separately (`edges` and `proof_edges`) even though later readiness/display processing may combine dependency information.
When obtaining a normalized machine view, treat the graph edge sets as authoritative for statement/proof separation rather than re-reading postprocessed node `userdata['uses']`.

The dependency graph is expected to be acyclic for upstream ancestor/readiness computation. A cycle is therefore a mechanical graph error, not merely a style warning.

Leanblueprint can configure the tracked theorem-environment set through the `thms` option. Do not hard-code only the default theorem environment names when analyzing an existing project.

## Nodes and Granularity

Create a separate node when it represents a meaningful formalization obligation, such as:

- a definition/structure/construction used later;
- a key lemma or proof bottleneck;
- a result reused by several later nodes;
- a cited external theorem that must be tracked explicitly;
- the final target.

Keep routine algebra, rewriting, unfolding, `simp`-level facts, and one-use observations inside proof prose when practical.
Node granularity is a mathematical/editorial decision, not a mechanical checker rule.

## Bundled Mechanical Projection

`scripts/blueprint.py` provides three read-only JSON operations:

```sh
python3 <skill-path>/scripts/blueprint.py check --project-root PROJECT
python3 <skill-path>/scripts/blueprint.py inspect --project-root PROJECT
python3 <skill-path>/scripts/blueprint.py diff BEFORE.json AFTER.json
```

The parser adapter drives the project's real plasTeX/leanblueprint configuration only far enough to resolve labels, proof associations, and dependency graphs. It deliberately stops before upstream status postprocessing that writes `blueprint/lean_decls`, mutates combined dependency state, and computes readiness/ancestor-derived display fields.

`check` is intentionally limited to projection/graph invariants where mechanical failure would make the normalized state ambiguous or misleading. Current diagnostics include repeated single-value macros, unresolved/invalid dependency targets, invalid macro owners, proof-association problems, duplicate labels across objects, self-dependencies/cycles, conflicting raw status, and disagreement between raw macro occurrences and the upstream graph projection.

`inspect` emits normalized facts only after `check` passes. The v1 state contains:

- node primary label (or `null` when no explicit tracked label is available), kind/title, and source file/line;
- statement `uses`, `lean`, `leanok`, `mathlibok`, and `notready`;
- associated proof source, proof-only `uses`, and proof `leanok`.

It intentionally omits prose, readiness/frontier/priority metrics, semantic equivalence judgments, and inferred formalization conclusions.

Exit codes:

- `0` — operation succeeded;
- `1` — the project was mechanically projected but invariant violations were found;
- `2` — a reliable projection could not be established with the installed/project runtime.

Exit `2` is a stop boundary for this automation layer. Do not silently substitute a regex parser and claim equivalent coverage.

## Project Conventions

Existing projects may define custom theorem environments, macros, labels, source organization, generated files, validation commands, and project-specific status/planning tools.
Use project-native tooling when it clearly provides a more authoritative factual view, but do not import project-specific ranking/planning policy into the generic Skill.

## CLI Validation

The stock leanblueprint CLI provides:

- `leanblueprint web` — build the web blueprint;
- `leanblueprint pdf` — build the PDF;
- `leanblueprint checkdecls` — check that Lean declaration names referenced by the generated declaration list exist in the Lean environment;
- `leanblueprint all` — run the main builds/checks;
- `leanblueprint serve` — serve generated web output locally.

`checkdecls` is deliberately narrow: it verifies declaration-name existence. It does not compare the Lean type to blueprint prose, establish proof completeness, or guarantee absence of placeholders such as `sorry`.
When mappings/status change, build Lean as needed, rebuild the web blueprint so `blueprint/lean_decls` is current, then run the declaration check.

plasTeX does not run BibTeX itself. In projects using the stock bibliography workflow, a PDF/bibliography build may need to precede the web build when references change.
