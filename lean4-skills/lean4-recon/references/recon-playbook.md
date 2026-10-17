# Recon playbook

Use this reference when a Lean/mathlib task calls for deliberate context expansion before committing to a local design. The goal is not exhaustive browsing; it is to test whether the current framing survives contact with the abstractions and APIs that actually govern it.

## Trace the construction to its owner

Start from the concrete local definition or theorem and follow the implementation one semantic layer at a time. Identify the operators, structures, and generic constructions it depends on, then inspect the namespace and theorem family that owns those abstractions.

A topology-specific definition implemented through an order-theoretic fixed-point approximant should trigger inspection of the fixed-point API, not only more topology search. A local helper built from an existing closure, hull, range, fixed-point, or universal construction may not deserve a new concept at all.

Do not widen mechanically. Cross a boundary when the governing abstraction could change the right statement, API shape, assumptions, placement, or reusable theorem.

## Prefer canonical characterizations over local wrappers

Before adding a predicate, wrapper, or helper theorem, try to state the same fact directly in the language already used by the underlying construction.

Useful questions include:

- Is this ordinary membership in an existing set of fixed points, a range, an order interval, or another canonical object?
- Is the new object already the least or greatest object satisfying a property?
- Is an `iInf`/`iSup`, closure/interior, kernel/hull, or fixed-point expression merely an implementation of an existing semantic construction?
- Would exposing the canonical characterization make downstream proofs shorter and the API more reusable?

If a local wrapper adds no durable semantic distinction, prefer the canonical notion.

## Generalize where the proof actually lives

Inspect which hypotheses and structures the essential argument uses. If a proof written in an application namespace depends only on a generic order, lattice, fixed-point, algebraic, topological, or categorical interface, test whether the reusable theorem belongs at that level.

Generalization is justified when it removes application-specific machinery, exposes an existing abstraction, or has credible reuse. Do not generalize merely to maximize abstraction.

## Check duality and symmetry

Look for least/greatest fixed-point pairs, order duals, converse relations, complements, additive/multiplicative forms, left/right actions, or opposite constructions when one side suggests a natural theorem family.

The goal is not to double the API automatically. A paired theorem matters when its existence changes the natural placement, naming, proof strategy, or reuse of the result under investigation.

## Pressure-test assumptions

For each material hypothesis, ask what fails without it. Use the cheapest useful discriminator: a standard mathematical example, a finite instance, a concrete witness, a scratch theorem, or a small Lean computation.

A failed proof is not evidence that a hypothesis is necessary. A plausible counterexample is not a certified refutation until Lean checks the relevant claim when certification is required.

## Revisit history only when it can change the present

Earlier implementations, abandoned branches, PR discussions, and reviewer feedback can reveal why a design was rejected: universe constraints, missing APIs, performance, import cost, awkward theorem shape, or maintainability.

Reopen a historical direction only when some rejecting constraint may have changed. Do not accumulate development history that no longer affects a live decision.

## Look for downstream leverage

Sometimes the best local design is to add or expose one generic theorem lower in the stack. Compare the cost of a local workaround with the value of a reusable characterization or theorem in the owning abstraction.

Useful leverage signals include repeated local machinery, duplicated proofs across dual constructions, awkward coercions caused by the wrong abstraction boundary, or several downstream declarations becoming immediate consequences of one generic result.

## Use disposable Lean experiments

Useful discriminators include `#check`, `#synth`, `#print`, `example`, minimal imports, tiny isolated files, concrete counterexamples, and temporary local definitions.

Treat these as evidence-gathering tools. A scratch elaboration establishes only the local fact it checks; it does not by itself establish changed-import or project integration behavior.

## Converge without forcing novelty

Stop when one of these holds:

- a materially better framing is supported well enough to hand off to an outcome-specific task;
- a small set of alternatives remains with a real design tradeoff;
- the current framing has survived the plausible semantic expansion paths and further widening is unlikely to change the decision.

A good reconnaissance result can be “keep the current design.” The Skill exists to expose hidden alternatives and canonical structure, not to manufacture change.