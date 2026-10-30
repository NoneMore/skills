---
name: latex-research-note-curator
description: Create, integrate, and curate one user-selected mathematical LaTeX research note, organizing arguments, source material, and meaningful cross-references.
disable-model-invocation: true
---

# LaTeX Research Note Curator

A user-invoked Skill for one mathematical research note project, treated as a developing exposition rather than a collection of fragments.

## Note conventions

- Keep material relevant to the chosen investigation. Techniques from other fields belong when they advance its mathematics.
- Maintain one canonical root `.tex` producing one PDF with clickable internal references. Use `\input` or `\include` when it helps organize the argument, not because of file length.
- Organize definitions, statements, dependencies, proofs and attempts, examples, counterexamples, and open questions by mathematical logic. Follow existing notation, macros, writing style, labels, and bibliography conventions.
- Distinguish established results, source-reported claims, conjectures, and incomplete arguments. Preserve source attribution and do not present a proof gap as resolved or invent citations. Compare hypotheses and conclusions before merging similar statements.

## Work

- **Create:** Use the chosen theme, destination, and supplied material to start a minimal, compilable root (such as `main.tex`). Organize known results and questions without inventing missing mathematics.
- **Integrate:** Read the relevant root and included sources. Place new material where it contributes to the argument, compare overlapping claims, and add useful internal references.
- **Curate:** Look across the note for genuine repetition, mathematical connections, and better argument order. Make focused improvements while retaining distinct statements when their equivalence is unclear.

Edit the designated note when asked to modify it; provide suggestions when asked to review. After editing, compile the root using the project's normal LaTeX workflow and briefly report the result.
