# Mathematical framing and representation

Use when the governing mathematical object, predicate, or representation may be unnecessarily specialized. Ask whether another framing changes the statements worth proving, not whether a proof is shorter.

## Search path

1. State the intended object, essential properties, and downstream mathematical use separately from its Lean encoding.
2. Follow local definitions and constructions to their generic mathematical owner (for example, a closure, fixed-point, transport, or universal-property API). Search local and imported mathlib before widening.
3. Compare local wrappers and predicates against canonical notions, equivalent characterizations, broader theorem families, and natural duals. Check if the apparent construction is only a special case.
4. Look for lower-level laws that eliminate repeated local machinery. When an alternative crosses boundaries, follow **one representative composition path** until it closes or exposes the lowest-level obstruction.
5. Revisit a rejected historical option only when a relevant assumption, API, or other blocking constraint may have changed.

## Discriminating evidence

- Probe candidate equivalences and assumptions using focused searches, `#check`, `#print`, `#synth`, concrete cases, or scratch examples.
- Test one representative translation or composition involving the canonical construction; standalone elaboration need not establish compositional fit.
- Test a dual or boundary case only if it could distinguish live alternatives.

## Judgment and stop

Compare conceptual fidelity, generality, assumptions, downstream fit, information preservation, and migration cost. Retain current framing when alternatives lack decision-changing evidence. Stop after the representative path supports or blocks the decision; leave parallel instance proofs to later authorized implementation.

If framing also changes the API or module owner, consult [API expressivity](api-expressivity.md) or [theory organization](theory-organization.md) as a *connected decision*, not automatically a separate parallel investigation.
