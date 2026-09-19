# Math Agent Skills

Source repository for installable Codex skills for mathematical reading,
writing, note editing, and Lean-oriented formalization workflows.

Repository slug: `math-agent-skills`.

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

Generates insertion-ready leanblueprint LaTeX for a specified Lean
formalization target from local reference materials. Use it for Lean blueprint
routes, proof routes, dependency routes, and formalization roadmaps.

Default prompt:

```text
Use $lean-blueprint-author to generate a leanblueprint route for the specified theorem from these reference materials.
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
    SKILL.md
    agents/openai.yaml
    references/create-workflow.md
    references/foundations.md
    references/modify-workflow.md
    references/output-contract.md
    references/update-workflow.md
```

There is intentionally no root-level `SKILL.md`; each skill is installed from
its own folder under `skills/`.

## Validation

Validate each skill folder with the skill-creator validator:

```sh
python3 /home/raibunitsu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/math-paper-reader
python3 /home/raibunitsu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/math-writing-editor
python3 /home/raibunitsu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/lean-blueprint-author
```
