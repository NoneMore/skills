# LaTeX Research Note Curator

Conservatively integrate scattered research material into a **user-selected, long-lived mathematical `.tex` note** while preserving its argument flow, source attribution, and the distinction between established and tentative claims.

Use this Skill for **ongoing note curation** (fragment integration, overlap review, cross-references, or localized reorganization). For broad copyediting, independent note creation, Markdown editing, or user-authorized mathematical rewriting, use [`math-writing-editor`](../math-writing-editor/SKILL.md). Reading a paper without editing the note is the job of [`math-paper-reader`](../math-paper-reader/SKILL.md).

## Contents

- `SKILL.md`: canonical instructions and behavioral contract.
- `agents/openai.yaml`: optional runtime-specific discovery metadata.
- `examples/Working-Notes.tex`: a self-contained sample about compact operators, weak convergence, and an incomplete research thread. **It is not a default editing target.**
- `evals/cases.md`: focused, inspectable acceptance scenarios; not a claim that automated evals have been run.

No generated PDF is checked in: compile the example locally if needed. No external service, database, extra Skill, or script is required to curate a `.tex` note.

## Install

Copy this **Skill folder** to the runtime's skills directory (for Codex, `${CODEX_HOME:-$HOME/.codex}/skills/`), or configure the runtime to discover it from its repository path.

## Example tasks

- “Integrate this handwritten proof attempt into `notes/Working-Notes.tex`. Preserve the missing step and show a diff.”
- “Find possible duplicates of the compactness argument in my canonical note, but don't merge statements with different hypotheses.”
- “Suggest up to three useful cross-references between this week's additions and older sections, explaining any uncertainty.”
- “Incorporate this paper's Lemma 2.1 as an attributed fact; don't assert that you checked the proof or that it resolves my conjecture.”

## Build the illustrative document (optional)

From this directory, with `latexmk` and the LaTeX packages used in the example installed:

```sh
cd examples
latexmk -pdf -interaction=nonstopmode -halt-on-error -no-shell-escape Working-Notes.tex
```

The PDF demonstrates renderability, **not** mathematical correctness. This step is optional for using the Skill on a different note.
