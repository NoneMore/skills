# Learning and Exploration Workflow

Use when the user wants to understand Lean, a repository, mathlib, or the formal version of a mathematical idea. This workflow is read-only unless the user explicitly asks to save an exercise or example.

## Contract

1. Resolve the learning target: project code, a mathlib concept, a theorem, a tactic, or a mathematical claim.
2. Inspect/search the relevant Lean material before making concrete claims about APIs or theorem names.
3. Match the explanation to the user's demonstrated level and requested style.
4. Verify key Lean claims when practical. Distinguish verified examples from conceptual or unverified explanations.
5. Adapt based on observable interaction: if the same misunderstanding recurs, change the explanation or example; if the user is succeeding, advance. Do not require an internal multi-role debate ritual to do this.

For repository exploration, build a small map of relevant files and declaration dependencies rather than surveying the whole tree. For mathlib exploration, use local/semantic/type-pattern search and present canonical declarations with minimal examples.

## Teaching styles

Tour, Socratic questioning, exercises, and game-like progression are presentation choices, not separate execution engines. Respect an explicitly requested style; suggest a change rather than silently overriding it.

Completion is user understanding or the requested learning artifact, not a code mutation or commit.