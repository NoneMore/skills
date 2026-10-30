# LaTeX Research Note Curator

Conservatively integrate scattered research material into **one user-selected, thematically coherent mathematical LaTeX note project**. The note may span multiple included `.tex` source files, but has one canonical compilation entry point and one unified PDF with meaningful internal cross-references. Its theme bounds relevance, not length or depth. Preserve argument flow, source attribution, and the distinction between established and tentative claims.

Use this Skill for **ongoing note curation** (fragment integration, overlap review, within-note cross-file references, or localized reorganization). For broad copyediting, independent note creation, Markdown editing, or user-authorized mathematical rewriting, use [`math-writing-editor`](../math-writing-editor/SKILL.md). Reading a paper without editing the note is the job of [`math-paper-reader`](../math-paper-reader/SKILL.md).

## Contents

- `SKILL.md`: canonical instructions and behavioral contract.
- `agents/openai.yaml`: optional runtime-specific discovery metadata.
- `evals/cases.md`: focused, inspectable acceptance scenarios; not a claim that automated evals have been run.

No external service, database, extra Skill, or script is required. Source files should be organized along mathematical arguments, not split at arbitrary size thresholds; a single `.tex` file remains a valid note project.

## Install

Copy this **Skill folder** to the runtime's skills directory (for Codex, `${CODEX_HOME:-$HOME/.codex}/skills/`), or configure the runtime to discover it from its repository path.
