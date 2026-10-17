# Local Proof Cleanup

Use when an already-correct proof should keep the same mathematical/library strategy but its local term or tactic shape can become clearer, more direct, or less brittle.

## Prefer direct local forms

Prefer a direct term, rewrite, or small explicit normalization set when it expresses the same argument more clearly than broader automation. Do not replace a working `exact`, `rfl`, or explicit rewrite with broad `simp` or another search-heavy tactic merely to save syntax. Compact forms such as `rwa` or a well-scoped `simpa` are fine when they make the local argument clearer without materially increasing hidden search or brittleness.

Keep intermediate names when they expose mathematical intent, create a useful checking boundary, or make diagnostics easier to understand. Inline a `have` or `let` only when doing so does not create meaningful repetition, nesting, or inference burden.

A local cleanup is not a reason by itself to add imports, promote a theorem into the global simp set, or widen a proof-specific helper into public API. If the best change requires a new reusable abstraction or a different proof approach, treat it as strategy simplification instead.

## Respect elaboration context

Small-looking rewrites can change elaboration behavior across tactic/term boundaries, `calc` steps, coercions, subtypes, casts, or implicit arguments. Validate the candidate in its actual source context rather than assuming two surface forms are interchangeable.

When simplifier policy is material, follow [simp and simp-lemma design](simplification.md). Repository-specific style and simplification policy take precedence over generic preferences.

## Verification

Apply one coherent cleanup at a time and rerun the same semantic verification gate used for the baseline. Reject candidates that introduce new diagnostics, unresolved `sorry`/`admit`, trust changes, or a less maintainable proof merely for token or line savings.

If a proposed cleanup changes imports, global simp behavior, or reusable API surface, expand verification to the affected integration boundary rather than treating it as theorem-local.
