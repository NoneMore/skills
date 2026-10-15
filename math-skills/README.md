# Math Agent Skills

Installable Agent Skills for mathematical reading, writing, note editing, and
Lean-oriented formalization workflows.

## Skills

### `math-paper-reader`

Path: `skills/math-paper-reader`

Reads mathematical papers and formulas with visual PDF checks, notation
ledgers, theorem/proof interpretation, equation references, and ambiguity
review. Use it when the task is understanding what a paper says.

Default prompt:

```text
Use $math-paper-reader to read this mathematical paper and explain the key formulas with page or equation references.
```

### `math-writing-editor`

Path: `skills/math-writing-editor`

Creates, restructures, rewrites, or polishes mathematical `.tex` and `.md`
notes. Use it for conservative copyediting, structural note rewrites, outline
extraction, rebuilding a note from a framework, or user-authorized
mathematical content edits.

Default prompt:

```text
Use $math-writing-editor to edit, restructure, or rewrite the specified mathematical .tex or .md note according to my requested level of autonomy.
```

### `lean-blueprint-author`

Path: `skills/lean-blueprint-author`

Creates, modifies, and synchronizes leanblueprint blueprints. For real projects
it includes read-only mechanical tooling that projects/checks the upstream
plasTeX dependency model so the model can focus on mathematical routes,
dependency semantics, and Lean/blueprint correspondence.

Default prompt:

```text
Use $lean-blueprint-author to create, modify, or synchronize this Lean project's blueprint.
```

## Installation

Install one or more skill folders under your Codex skills directory.

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/math-paper-reader "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/math-writing-editor "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/lean-blueprint-author "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Install only the skill folders you want to expose.

## Repository Layout

```text
skills/
  math-paper-reader/
    SKILL.md
    agents/openai.yaml
    references/formula-reading-workflow.md
    references/math-paper-reading-checklist.md
  math-writing-editor/
    SKILL.md
    agents/openai.yaml
  lean-blueprint-author/
    CHANGELOG.md
    SKILL.md
    agents/openai.yaml
    references/leanblueprint-basics.md
    references/workflows.md
    scripts/blueprint.py
    scripts/tests/test_blueprint.py
```

There is intentionally no root-level `SKILL.md`; each skill is installed from
its own folder under `skills/`.

## Validation

If your Codex installation includes the `skill-creator` validator, validate each
skill using its local installation path:

```sh
VALIDATOR="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py"
python3 "$VALIDATOR" skills/math-paper-reader
python3 "$VALIDATOR" skills/math-writing-editor
python3 "$VALIDATOR" skills/lean-blueprint-author
```

The deterministic tests for the lean blueprint helper do not require a Lean
project. The parse integration test runs automatically when the leanblueprint /
plasTeX runtime is installed and otherwise skips explicitly:

```sh
python3 -m unittest discover -s skills/lean-blueprint-author/scripts/tests -v
```
