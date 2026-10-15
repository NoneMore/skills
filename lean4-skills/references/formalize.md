# Formalization Workflow

Use when translating an informal claim into Lean or when statement design is explicitly in scope.

## Contract

1. Resolve the mathematical claim and intended level of generality. If a source contains several claims, make the selected claim or selection rule explicit.
2. Search mathlib for canonical types, definitions, theorem shapes, and existing results before choosing an encoding.
3. Draft the weakest faithful statement with explicit hypotheses and no hidden axioms.
4. Check that the declaration itself elaborates. A draft may contain an explicitly reported proof hole.
5. If proving exposes a statement mismatch, revise only declarations created for the task or explicitly authorized for statement work; otherwise report the mismatch rather than changing the statement.

When a checked proof is required, use `references/prove.md` for the generated declaration.

## Completion

- **Draft:** the intended claim is represented in Lean and the declaration skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** the generated declaration satisfies the checked-proof completion rule in `references/prove.md`.
- Any unresolved item makes the result partial; surface it explicitly and do not present the result as checked.
