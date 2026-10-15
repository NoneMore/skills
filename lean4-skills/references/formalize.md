# Formalization Workflow

Use when translating an informal claim into Lean or when the user explicitly authorizes statement design. This workflow owns statement shape for declarations it creates or is authorized to revise; it does not silently rewrite pre-existing declarations.

## Contract

1. Resolve the mathematical claim and the intended level of generality. If a source contains several claims, make the selected claim or selection rule explicit.
2. Search mathlib for canonical types, definitions, theorem shapes, and existing results before choosing an encoding.
3. Draft the weakest faithful statement with explicit hypotheses and no hidden axioms.
4. Check that the declaration itself elaborates. A draft may contain an explicitly reported proof hole.
5. When a checked proof is required, hand ownership to `references/prove.md` for the generated declaration.
6. If proving exposes a statement mismatch, revise session-generated declarations or other declarations the user explicitly authorized for statement work. Preserve pre-existing declarations otherwise.

## Completion

- **Draft:** the intended claim is represented in Lean and the declaration skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** after handoff to proving, the generated declaration elaborates with no unresolved proof holes in scope and no unreported trust assumptions.
- **Partial:** every unresolved item is surfaced and the result is not presented as verified.
