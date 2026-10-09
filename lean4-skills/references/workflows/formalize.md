# Formalization Workflow

Use when translating an informal claim into Lean or when the user explicitly authorizes statement design. This workflow owns statement shaping for declarations it creates; it does not silently rewrite pre-existing user declarations.

## Modes

- **Draft:** produce an elaborating declaration skeleton, normally with a proof hole.
- **Guided:** draft, then prove interactively with the proving workflow.
- **Autonomous:** process a clearly selected claim or bounded claim set without per-cycle prompts; require stop budgets and deterministic claim selection.

These modes are stages of one synthesis workflow rather than separate behavioral contracts.

## Contract

1. Acquire the claim from the user's text or source. If a source contains several claims, select explicitly or by a deterministic user-approved rule.
2. Search mathlib for canonical types, definitions, and existing theorem shapes before choosing an encoding.
3. Draft the weakest faithful statement with explicit hypotheses and no hidden axioms.
4. Check that the declaration elaborates. A proof hole may remain in Draft mode.
5. In Guided or Autonomous mode, invoke the proving workflow on the generated declaration.
6. If proving reveals a statement mismatch, revise only session-generated declarations or create an adjacent corrected/salvaged declaration; preserve pre-existing declarations unless the user explicitly approves rewriting them.

## Rigor

Default to a checked result when the user asks for a completed formalization. If the user requests a sketch, label unresolved proof holes or unverified claims clearly. If explicit assumptions are allowed, list them; never introduce silent global axioms.

## Completion

- **Draft:** the intended statement is represented in Lean and the skeleton elaborates apart from explicitly reported proof holes.
- **Checked:** the generated declaration elaborates with no sorries in scope and no unreported non-standard assumptions.
- **Partial/sketch:** every unresolved item is surfaced and the result is not presented as verified.