# Lean Custom Syntax

Use when defining notation, macros, syntax categories, elaborators, tactic syntax, or an embedded DSL. Lean metaprogramming APIs are version-sensitive; verify uncertain names against the active toolchain.

## Choose the shallowest mechanism

- simple operator -> `infix` / `infixl` / `infixr`;
- fixed notation -> `notation`;
- syntax-to-syntax transformation -> `syntax` + `macro_rules`;
- type/environment-aware interpretation -> an elaborator;
- genuinely new grammar -> `declare_syntax_cat` plus a bridge into terms/commands/tactics.

Do not write an elaborator when a hygienic macro is sufficient.

## Precedence and associativity

Treat precedence as part of the language interface. Test nested expressions and combinations with surrounding Lean syntax, not just the isolated happy path.

## Hygiene and errors

Macros are hygienic by default. Preserve user source locations and attach errors to the smallest invalid syntax node when validating a DSL. Break hygiene only when the language design genuinely requires user-visible names.

## Escalating to elaboration

Use elaboration only when expansion needs type information, local context, environment declarations, or controlled unification. Keep parsing/validation separate from semantic elaboration when that improves error quality.

## Pretty printing

If a DSL is meant for humans to read in goals/errors, consider an unexpander/delaborator so printed output preserves the user-facing abstraction. Test both elaboration and rendering.

## Verification

Add minimal examples for precedence, hygiene, invalid input, elaboration, and expected expansion/pretty-print behavior. Prefer current Lean reference/source over cached MetaM/TacticM API names when a call is uncertain.
