# LaTeX Research Note Curator

Conservatively integrate scattered research material into a **user-selected, long-lived mathematical `.tex` note** while preserving its argument flow, source attribution, and the distinction between established and tentative claims.

Use this Skill for **ongoing note curation** (fragment integration, overlap review, cross-references, or localized reorganization). For broad copyediting, independent note creation, Markdown editing, or user-authorized mathematical rewriting, use [`math-writing-editor`](../math-writing-editor/SKILL.md). Reading a paper without editing the note is the job of [`math-paper-reader`](../math-paper-reader/SKILL.md).

## Contents

- `SKILL.md`: canonical instructions and behavioral contract.
- `agents/openai.yaml`: optional runtime-specific discovery metadata.
- `evals/cases.md`: focused, inspectable acceptance scenarios; not a claim that automated evals have been run.

No external service, database, extra Skill, or script is required to curate a `.tex` note.

## Install

Copy this **Skill folder** to the runtime's skills directory (for Codex, `${CODEX_HOME:-$HOME/.codex}/skills/`), or configure the runtime to discover it from its repository path.
