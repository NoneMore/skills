# Math Agent Skills

Installable Agent Skills for mathematical reading, research-note creation and curation, and Lean-oriented formalization workflows.

## Skills

### `math-paper-reader`

Path: `skills/math-paper-reader`

Reads mathematical papers and formulas with visual PDF checks, notation ledgers, theorem/proof interpretation, equation references, and ambiguity review. Use it when the task is understanding what a paper says.

Default prompt:

```text
Use $math-paper-reader to read this mathematical paper and explain the key formulas with page or equation references.
```

### `latex-research-note-curator`

Path: `skills/latex-research-note-curator`

**User-invoked.** Creates, integrates, and curates one thematic mathematical LaTeX research note, with a canonical root `.tex` and one linked PDF. Organizes mathematical arguments, partial proofs, source attribution, and meaningful cross-references.

Example:

```text
Use $latex-research-note-curator to integrate this fragment into my LaTeX research note and connect it to related results.
```

### `lean-blueprint-author`

Path: `skills/lean-blueprint-author`

Generates insertion-ready leanblueprint LaTeX for a specified Lean formalization target from local reference materials. Use it for Lean blueprint routes, proof routes, dependency routes, and formalization roadmaps.

Default prompt:

```text
Use $lean-blueprint-author to generate a leanblueprint route for the specified theorem from these reference materials.
```

## Installation

Install one or more Skill folders under your Codex skills directory.

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/math-paper-reader "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/latex-research-note-curator "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/lean-blueprint-author "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Install only the skills you want. Remove any older local `math-writing-editor` installation separately.

## Repository Layout

```text
skills/
  math-paper-reader/
    SKILL.md
    agents/openai.yaml
    references/formula-reading-workflow.md
    references/math-paper-reading-checklist.md
  latex-research-note-curator/
    SKILL.md
    agents/openai.yaml
  lean-blueprint-author/
    CHANGELOG.md
    SKILL.md
    agents/openai.yaml
    references/leanblueprint-basics.md
    references/workflows.md
```

There is intentionally no root-level `SKILL.md`; each skill is installed from its own folder under `skills/`.

## Validation

If your Codex installation includes the `skill-creator` validator, validate each skill using its local installation path:

```sh
VALIDATOR="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py"
python3 "$VALIDATOR" skills/math-paper-reader
python3 "$VALIDATOR" skills/latex-research-note-curator
python3 "$VALIDATOR" skills/lean-blueprint-author
```

