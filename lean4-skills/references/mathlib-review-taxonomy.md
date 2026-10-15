# Mathlib Review Taxonomy

Use this vocabulary when reviewing work intended for upstream mathlib. The review workflow decides whether a finding is material; this file only names common review surfaces.

## Surface style and naming

Check local formatting, line width, tactic idiom, declaration naming, namespace placement, and whether dot notation is natural. Use [mathlib-style.md](mathlib-style.md) for concrete conventions.

## Documentation

Public API should have appropriate declaration/module documentation, while private proof scaffolding should not accumulate unnecessary docstrings. Check that comments explain mathematical or design intent rather than development history.

For Verso-specific inline documentation, load [verso-docs.md](verso-docs.md).

## Existing results, placement, and imports

Ask whether an equivalent or more general result already exists. If the result is new, check whether it lives in the lowest sensible module and whether imports expose only what the API needs.

## API and generality

Review the weakest reasonable hypotheses, representation choices, public-vs-private surface, argument order, and whether a declaration is substantive rather than vacuous scaffolding.

Do not generalize merely because a more abstract statement is imaginable; the generalization should improve real reuse or library coherence.

## Attributes and simplification

Check `@[simp]`, `@[ext]`, reducibility, coercions, and other attributes as global API decisions. A locally useful rewrite is not automatically a good global simp lemma. Load [simp-reference.md](simp-reference.md) for simp-normal-form decisions.

## Instances

Look for instance diamonds, loops, accidental local-instance selection, unnecessary global instances, and API designs that make typeclass inference fragile. Load [instance-pollution.md](instance-pollution.md) when multiple same-class instances are involved.

## Module-system and generated-file obligations

Check current repository requirements for module headers, public visibility/imports, and generated root/import files. Recover these requirements from the repository rather than assuming a cached command or layout.

## Findings

A review finding should name the concrete impact: correctness, API quality, integration, maintainability, performance, or upstream acceptance. Do not invent style nits when there is no material issue.
