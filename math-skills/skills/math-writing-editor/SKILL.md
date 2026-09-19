---
name: math-writing-editor
description: Create, restructure, rewrite, or polish mathematical `.tex` and `.md` notes. Use when the user asks to edit a math file, generate a new math note, extract or refill an outline/framework, or revise mathematical content with user-granted autonomy; do not use for chat-only prose unless the output should become a file.
---

# Math Writing Editor

Use this skill to edit or generate mathematical notes in `.tex` and `.md`.
It should improve prose, structure, and presentation while respecting the
user's requested level of mathematical autonomy.

## Scope

Supported output files:

- `.tex`
- `.md`

The user may provide an existing file, pasted note material, a framework, or
reference materials. If there is no existing target file, create a new output
file when the user asks for one or when the task naturally requires a file. If
the output path is unspecified, choose a conservative name near the source when
possible, such as `note.md`, `source.outline.md`, `source.rewritten.md`,
`paper.edited.tex`, or `paper.rewritten.tex`, and report it.

Do not deliver substantial edited mathematical prose only in chat unless the
user explicitly asks for chat-only output.

## Output Rules

- By default, preserve the original and write a sibling revision file:
  - `paper.tex` -> `paper.edited.tex`
  - `section.md` -> `section.edited.md`
- If the user explicitly asks to edit directly or in place, edit the original
  file.
- If the user asks for an outline, framework, rewritten note, or newly generated
  note, create the requested file rather than treating it as a diagnostic note.
- Do not create extra reports or commentary files unless requested.
- If the user's instructions grant autonomy over a mathematical choice, make the
  choice within that scope and summarize important assumptions in the final
  response. Ask only when the choice would exceed the granted scope, contradict
  references, or determine a core theorem/definition the user has not delegated.

## Autonomy Levels

Infer the narrowest level that satisfies the request.

- **Copyedit**: preserve mathematical content; improve grammar, clarity, flow,
  and formatting.
- **Structural edit**: reorganize sections, paragraphs, proof exposition, and
  dependency order while preserving intended mathematical meaning.
- **Mathematical rewrite**: when explicitly requested, add, remove, or change
  mathematical exposition, examples, proof sketches, definitions, theorem
  packaging, or connective tissue to fit the user's goal.
- **Autonomous fill**: when the user gives permission to freely fill gaps,
  generate missing prose or mathematical explanation in a style consistent with
  the note, using provided references where available and clear internal
  reasoning elsewhere.

Do not stop for every local mathematical judgment once the user has granted
autonomy. Stay within the stated topic, level, notation, and style.

## Framework Workflow

For outline-based note restructuring:

1. Extract a concise `.outline.md` or framework file from the source note when
   requested. Include section hierarchy, theorem/proof slots, dependency order,
   and placeholders for material to be rewritten or added.
2. After the user edits the framework, rebuild the note from the framework, the
   original note, and any provided references.
3. Preserve useful labels, citations, notation, theorem names, and proof
   dependencies where they still fit.
4. When filling from mixed sources, keep reference-backed material consistent
   with the references and make autonomous material stylistically compatible
   with the surrounding note.

## Allowed Edits

- Grammar, spelling, punctuation, capitalization, and typography.
- Sentence-level rewriting for clarity, concision, and flow.
- Paragraph splitting, merging, reordering, and transition improvement.
- Section and proof-prose restructuring.
- Rewording titles, captions, explanatory prose, introductions, and motivation.
- Conservative LaTeX and Markdown cleanup, including spacing, line breaks,
  formatting consistency, and obvious non-mathematical typos.
- Mathematical additions, deletions, or rewrites when requested or covered by
  user-granted autonomy.

## Mathematical Safety

By default, do not independently change:

- Theorems, lemmas, propositions, definitions, hypotheses, conclusions, or
  proof obligations.
- Quantifiers, domains, dependencies, assumptions, equality or inequality
  directions, formula contents, or reference targets.
- Mathematical examples, applications, interpretations, claims, proof steps, or
  unstated assumptions.

These items may be changed when the user asks for mathematical rewriting or
grants autonomy. In that case:

- Keep notation, terminology, and proof style consistent with the note.
- Make new content fit the existing structure and local dependencies.
- Do not silently contradict supplied references or earlier assumptions.
- Do not present speculative or invented external facts as sourced.
- Ask before changing core goals, definitions, theorem statements, or global
  assumptions unless the user has clearly delegated those choices.

Treat mathematical-looking typos as user decisions in copyedit mode. In rewrite
or autonomous-fill mode, fix them only when the intended correction is clear
from context or references; otherwise ask or leave a visible TODO if the user
allowed placeholders.

## LaTeX and Markdown Safety

- Preserve formulas, theorem environments, labels, citations, cross-references,
  reference keys, and citation keys unless the requested edit requires changing
  them.
- Preserve leanblueprint commands such as `\uses`, `\lean`, `\leanok`, and
  `\mathlibok` unless the user asks to update blueprint dependencies or the
  rewrite requires it.
- Do not add packages or rewrite macro definitions unless needed for the
  requested output. Preserve `\newcommand`, `\renewcommand`,
  `\DeclareMathOperator`, theorem-style declarations, and similar definitions
  by default.
- Preserve comments unless the user asks to edit or resolve them.
- Copy `verbatim`, `lstlisting`, `minted`, fenced code blocks, indented code
  blocks, and inline code exactly unless the user explicitly asks to edit them.
- In alignment-sensitive environments such as `align`, `aligned`, `array`,
  `matrix`, `cases`, `split`, and diagrams, preserve alignment markers, line
  breaks, and row structure unless the requested mathematical or presentational
  rewrite requires a change.
- Move formulas, theorem-like environments, definitions, or proof blocks only
  when the move fits the requested structure and preserves or intentionally
  updates dependency order.

## Style

Use restrained, clear, research-style mathematical prose unless the source note
uses a different style.

- Match the note's language, notation, register, and density.
- Prefer precise short sentences over ornate phrasing.
- Keep terminology stable.
- Make references and pronouns explicit when needed.
- In proofs, improve readability and local justification; add missing
  connective explanation when requested or covered by autonomy.
- In introductions or motivation sections, organize and polish existing
  material; add new claims only when requested or delegated.

If the target language is ambiguous and the user asks for newly written prose,
choose the dominant language of the source materials. Ask only when no dominant
language is available.

## Workflow

1. Determine the requested mode: copyedit, structural edit, mathematical
   rewrite, outline extraction, rebuilt note, or autonomous fill.
2. Identify the source file, pasted material, framework, references, and output
   path. If no output path is provided, choose a conservative file name.
3. Read the relevant files and infer the note's style, notation, structure, and
   mathematical dependencies.
4. Perform the requested edit or generation, staying within the user's granted
   autonomy.
5. Review the final diff or generated file before responding. Check formulas,
   theorem statements, assumptions, proof obligations, labels, citations,
   references, `\uses`, `\lean`, cross-references, and dependency order.
6. Briefly report the output file path, the mode used, and any material
   assumptions or unresolved decisions.
