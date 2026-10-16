# Mathlib Search and Integration

Use when an existing declaration may avoid re-proving, re-defining, or over-specializing something.

## Search from meaning and type

Before guessing a theorem name:

1. State what the needed result does mathematically.
2. Identify its important input/output types and structures.
3. Search the project's active imports and local declarations.
4. Broaden to mathlib by names, natural-language/semantic search, or type-pattern search when those capabilities are available.
5. Inspect candidate signatures and nearby declarations before using them.
6. Validate the candidate in the actual project context with `#check`, live hover/goal information, or a compiled use site.

Do not assume mathematical notation maps directly to Lean API names.

## Use proof-search tactics as discovery, not opaque dependencies

When appropriate, tools/tactics such as `exact?`, `apply?`, `rw?`, or `simp?` can reveal candidate declarations. Treat suggestions as search results: inspect what they use and prefer an explicit stable result when that improves readability or predictability.

## Search nearby abstractions

If the exact lemma is absent, look for:

- a more general theorem with weaker assumptions;
- an iff or characterization that turns the goal into a standard form;
- a congruence/extensionality theorem instead of manual unfolding;
- a theorem in the namespace of the main structure or property;
- an equivalent formulation using canonical library types.

This often produces a better proof than searching only by surface words from the goal.

## Imports

Add the narrowest import consistent with local project style. Do not copy an import from a search result without checking that it is appropriate for the target project.

For upstream mathlib work, load [upstream mathlib guidance](branches/mathlib-upstream.md) for the current contribution policy and review bar.

## Stop condition

Search is complete when a candidate has been validated or additional search is no longer likely to change the strategy. "Search before prove" does not mean exhaustive unbounded searching.
