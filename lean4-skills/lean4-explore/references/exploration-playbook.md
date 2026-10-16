# Exploration playbook

Use this reference when a Lean/mathlib task is genuinely open-ended: the hard part is deciding which object, abstraction, API, hypothesis boundary, generalization, or implementation path deserves commitment.

## Maintain a branch ledger

Keep the active search tree small and explicit. For each branch, record:

- the hypothesis or design idea;
- what evidence would distinguish it from alternatives;
- the cheapest useful experiment;
- current status: viable, rejected, deferred, or selected.

Do not preserve branches merely because they were mentioned. Preserve them when the reason for rejection may later become invalid or when they expose a meaningful tradeoff.

## Re-identify the local concept

Before adding a new predicate, wrapper, or helper theorem, ask what the object is in more general mathematical language. A domain-specific “stabilizes here” predicate may be ordinary fixed-point membership; an intersection of iterates may already be a canonical greatest fixed point; a custom equivalence may be an existing characterization.

Search the namespace of the general structure, not only the vocabulary of the application.

## Generalize where the proof actually lives

When the essential proof uses only generic structure, consider whether the reusable result belongs at that structural layer. A good generalization should reduce application-specific machinery and have a clear statement independent of accidental local notation.

Do not generalize merely to maximize abstraction. Prefer a generic lemma when it clarifies the application, exposes a canonical API, or has credible reuse.

## Check symmetry and duality

When a useful result appears on one side of a paired construction, inspect the corresponding dual or symmetric side. Common signals include least/greatest fixed points, order duals, additive/multiplicative forms, left/right actions, converse relations, complements, and opposite categories.

The goal is not to double the API automatically. Determine whether the paired theorem is natural, cheap, and useful enough to keep the library coherent.

## Pressure-test assumptions

For each nontrivial hypothesis, ask what breaks without it. Use cheap concrete examples, standard counterexamples, finite instances, or scratch Lean declarations. A failed proof is not evidence that a hypothesis is necessary; a candidate counterexample is not a certified refutation until Lean checks the relevant claim.

This mode is exploratory. If the requested outcome becomes a certified disproof, hand off to `lean4-refute`.

## Revisit discarded designs when constraints change

Old implementations are evidence. Recover the reason they were abandoned: universe mismatch, performance, API awkwardness, missing theorem, import cost, or maintenance burden. If a new library feature changes that reason, reopen the branch and test the changed constraint instead of assuming the old verdict still holds.

## Look for upstream leverage

Sometimes the shortest path to a clean application is a small general-purpose lemma in a lower-level module. Compare:

- local workaround cost;
- general theorem statement and natural home;
- downstream simplification;
- API coherence and dual/symmetric consequences;
- whether the general change is appropriate for the current project or should be a separate upstream task.

A useful exploration may conclude that the current feature should wait on or be split from a more general dependency.

## Use disposable Lean experiments

Useful discriminators include `#check`, `#synth`, `#print`, `example`, a minimal scratch theorem, a temporary import, or a tiny isolated file. Keep them disposable unless a later outcome-specific task explicitly promotes them into production source.

Report the verification strength honestly. A scratch elaboration answers a local question; it does not by itself prove project integration.

## Converge deliberately

Prefer a branch when the evidence is stronger on the dimensions that matter for the task: canonicality, faithfulness, generality, reuse, proof simplicity, import cost, trust, performance, and project conventions.

Stop exploring when one branch dominates, when a small set of options remains with a real user-facing tradeoff, or when the next uncertainty is no longer exploratory. Carry forward rejected branches only when their rejection rationale is useful context.
