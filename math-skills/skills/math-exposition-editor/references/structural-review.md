# Structural exposition review

Read this when the author asks about section order, introduction design, proof presentation across sections, or whole-manuscript organization. Do not use this procedure to audit mathematical validity.

## First map the reader's route

Using the *available manuscript*, record for each relevant section:

1. Its stated purpose or question.
2. The definitions and named results it presents.
3. Where the author says those results are used or discussed next.
4. The burden on a new reader: missing orientation, abrupt transition, redundant setup, or delayed explanation.

For whole-paper work, include the abstract, introduction, main statements, section openings and endings, and conclusion where present. Do not reconstruct missing mathematics or invent a dependency graph from plausibility. If only excerpts are supplied, label the map as partial.

## Diagnose organization

- **Motivation:** Does the introduction explain the problem, the paper's explicitly stated contribution, and the route through the sections without unsupported novelty claims?
- **Placement:** Can the reader find a definition or result near its first sustained discussion? Distinguish a genuinely awkward introduction from a necessary earlier statement.
- **Flow:** Do transitions say why the next section is relevant according to the author's text, instead of merely announcing its presence?
- **Proof presentation:** Would a roadmap, paragraph split, or descriptive heading make a supplied proof easier to navigate without inserting a mathematical step?
- **Repetition:** Is a repeated explanation unnecessary, or does it orient the reader after a long detour? Keep the latter.
- **Deferred material:** If moving a proof or technical discussion to an appendix might help, identify the necessary pointers and reader costs; do not make that move unilaterally.

## Structural proposals requiring author decisions

For a proposed move, split, merge, demotion, or deletion of a theorem/lemma/proof/definition; a change to the hierarchy of main results; or a shift between body and appendix, identify the affected material, existing pointers, and reader-facing tradeoffs. Apply the author-approval requirement in `SKILL.md` before making such edits. Do not decide equivalence, sufficiency, or dispensability of mathematical claims.

Suggested review format:

| Location | Reader-facing issue | Proposed presentation change | Needs author decision? |
| --- | --- | --- | --- |
| Section / paragraph | Observable exposition friction | Smallest helpful change | Yes/No and why |

Rank findings by likely reader impact and keep a distinction between an observed writing problem and an optional stylistic preference. When proposing multiple feasible structures, explain their reader-facing tradeoffs; do not select an unapproved mathematical emphasis.

## After an authorized restructure

After approval, check prose at both old and new locations for broken antecedents, missing transitions, and redundant introductions. Track the moved items and the pointers readers need to find them; apply the preservation and LaTeX artifact checks in `SKILL.md`.
