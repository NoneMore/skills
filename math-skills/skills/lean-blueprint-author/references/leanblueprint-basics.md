# Leanblueprint Basics

This reference follows the public `PatrickMassot/leanblueprint` README and package behavior.

## Standard Layout

The stock `leanblueprint` scaffold keeps blueprint sources under `blueprint/src`:

- `content.tex` — main mathematical content (possibly importing more files);
- `web.tex` — plasTeX/web entry point;
- `print.tex` — PDF/LaTeX entry point;
- `macros/common.tex` — macros shared by web and print;
- `macros/web.tex` / `macros/print.tex` — target-specific macros.

Projects may use a custom layout. Follow the project rather than forcing the scaffold.

## Core Macros

### `\lean{Decl.Name}`

Associates the surrounding definition/theorem-like environment with one or more Lean declarations.
Use fully qualified names when needed.

Prefer one complete `\lean{...}` occurrence per environment unless the project deliberately uses another style. Current upstream stores the declaration list on the surrounding environment while also collecting those names for declaration checking, so do not rely on repeated `\lean{...}` commands to merge metadata.

### `\leanok`

Claims that the surrounding environment is formalized.
It may appear on a statement/definition or on its proof.

For synchronization:

- statement-level `\leanok` should correspond to a Lean declaration whose type/meaning matches the blueprint statement;
- proof-level `\leanok` should correspond to an implemented proof/definition, not merely a declaration name that resolves.

### `\uses{label1,label2}`

Records dependencies for the surrounding environment and drives the dependency graph.

- On a theorem/definition: list what is needed to state or define it.
- On a proof: list results used only in the proof route.

Prefer direct mathematical dependencies rather than transitive closure.

### `\notready`

Marks a statement/definition whose mathematical blueprint is not ready to formalize.
Do not use it merely because the Lean implementation is unfinished.

### `\mathlibok`

Marks a node that is already available in Mathlib. In leanblueprint this also counts as formalized status for the containing environment.
Use it for the node itself, not because its proof happens to use Mathlib.

### `\proves{label}`

Associates a proof with a statement when the proof does not immediately follow that statement.
Use it when reordering or separating proofs would otherwise make the association unclear.

### `\discussion{issue}`

Links the surrounding statement/definition to a GitHub issue.
Preserve it unless the task changes that discussion link.

## Nodes and Granularity

Create a separate node when it represents a meaningful formalization obligation, such as:

- a definition/structure/construction used later;
- a key lemma or proof bottleneck;
- a result reused by several later nodes;
- a cited external theorem that must be tracked explicitly;
- the final target.

Keep routine algebra, rewriting, unfolding, `simp`-level facts, and one-use observations inside proof prose when practical.

## Project Conventions

Leanblueprint's dependency graph can use a custom theorem-environment set through the `thms` option. Existing projects may also define custom macros and label conventions.

When editing an existing project, infer these conventions from its source and keep using them.

## CLI

The stock CLI provides:

- `leanblueprint web` — build the web blueprint;
- `leanblueprint pdf` — build the PDF;
- `leanblueprint checkdecls` — check that Lean declaration names used by the blueprint exist; in the stock workflow, build Lean as needed and rebuild the web blueprint first so `blueprint/lean_decls` is current;
- `leanblueprint all` — run the main checks/builds;
- `leanblueprint serve` — serve the generated web output locally.

`checkdecls` verifies declaration existence; it does not prove that a natural-language blueprint statement matches the Lean type, that the proof is complete, or that the implementation contains no placeholders such as `sorry`.

plasTeX does not run BibTeX itself. In projects using the stock bibliography workflow, a PDF/bibliography build may need to precede the web build when references change.
