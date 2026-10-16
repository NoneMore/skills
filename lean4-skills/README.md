# Lean 4 Skills

A jointly installed family of outcome-oriented capabilities for formal mathematics in Lean 4 and mathlib. These are not stages in a required workflow, and the collection root is not itself a Skill.

Install all eight `lean4-*` Skills together. They are independently discoverable so the runtime can activate the narrow capability whose behavioral contract and references match the requested outcome; they are not intended to be deployed as unrelated standalone products.

Before materially changing this collection, follow the repository-level [Skill Design Principles](../SKILL-DESIGN-PRINCIPLES.md).

## Capabilities

- `lean4-explore` — choose among multiple materially different Lean/mathlib formal directions when that choice is itself the requested outcome.
- `lean4-formalize` — translate mathematical intent into an appropriate Lean declaration when statement design is the requested outcome.
- `lean4-prove` — complete or repair a proof for an existing concrete Lean declaration or goal.
- `lean4-refute` — search for and Lean-certify a counterexample or negation.
- `lean4-diagnose` — diagnose Lean/Lake failures in formal-mathematics work when the primary problem is a concrete diagnostic rather than ordinary proof search.
- `lean4-trust` — inspect and clean up axioms, `sorry`/`admit`, and declaration trust dependencies when the trust basis itself is the requested outcome.
- `lean4-review` — independently review Lean proof code and report evidence-backed findings.
- `lean4-optimize` — improve an already-correct proof for clarity, robustness, maintainability, or measured performance.

## Routing and composition

Choose the primary capability by the requested outcome, not by incidental mechanisms used along the way. Search, theorem lookup, API inspection, small Lean experiments, and explanatory substeps normally remain inside the capability that already owns the task.

`lean4-explore` is not a generic preflight or fallback for every non-editing Lean question. Compose it only when multiple materially different formal directions remain plausible and choosing among them becomes a distinct requested outcome. Different proof strategies for a fixed concrete goal do not by themselves create an exploration outcome. A standalone explanation of existing code with no evaluation request and no open formal-design decision does not require a specialized Lean 4 Skill.

Use the requested deliverable as the commitment test at the `lean4-explore` / `lean4-formalize` boundary. If the task is complete once an evidence-backed formal direction has been chosen, exploration may own that outcome. If the requested deliverable is a Lean declaration, the ordinary choices needed to produce that declaration remain inside `lean4-formalize` unless direction selection is explicitly separated into its own outcome.

An ordinary proof hole remains `lean4-prove` work even when the source currently contains `sorry` or `admit`. Route to `lean4-trust` when inspecting, explaining, or reducing the accepted trust basis is itself the requested outcome.

When capabilities compose, the primary outcome owner also owns the governing invariants. A supporting capability may gather evidence or resolve a bounded subproblem, but it must not broaden the primary owner's mutation permissions, trust basis, scope, or verification claims. In particular, exploratory scratch work does not override a read-only review contract or become a durable edit merely because it informed another capability.

When a real outcome boundary is crossed, hand off explicitly: exploration may settle an encoding for formalization, diagnosis may reduce to ordinary proof search, review may identify a change owned by proof/trust/optimization, and exploration may support an optimization decision without owning the durable edit.

Each capability is directly discoverable from its own metadata. There is no family router or compatibility Skill. Cross-skill composition happens only when the requested outcome genuinely crosses a boundary.

## Family installation and reference locality

The eight `lean4-*` directories form one installation unit and are expected to be installed together. Package-local reference copies exist to make reference loading reliable after a narrow Skill is activated, not to define eight independent deployment units.

For every Skill:

- the directory name matches the `name` in `SKILL.md`;
- only references that the Skill explicitly routes to are carried as shared package-local guidance;
- required provenance and third-party notices stay available locally;
- supporting capabilities do not rely on the collection root being loaded into model context.

The root `references/` directory is the canonical source for reusable material shared by multiple Skills. `scripts/sync-packages.py` vendors the explicit per-Skill reference set and checks it for drift. `SKILL.md` is the authoritative reference-loading map: mentioning another mechanism inside a reference does not implicitly add that mechanism's reference to the Skill. Run `scripts/sync-packages.py --check` to validate package names, vendored-copy drift, and broken or escaping local Markdown links. Skill-specific references remain owned by that Skill.

## Shared source material

- `references/mathlib-guide.md` — search and integration with local declarations and mathlib;
- `references/verification.md` — live, file-local, dependency-aware, and project-level verification gates;
- `references/performance-optimization.md` — measured Lean elaboration/build performance work;
- `references/simp-reference.md` — `simp`, simp-lemma, and simproc design;
- `references/branches/mathlib-upstream.md` — additional policy and review bar for work intended for upstream mathlib.

## Scope

This collection is for formal mathematics in Lean 4 and mathlib. It is not the default for general Lean application development, Lean FFI/programming work, other theorem provers, or ordinary informal mathematics.

Collection-level upstream provenance and licensing are recorded in [UPSTREAM.md](UPSTREAM.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); each Skill carries the required local copies as part of the jointly installed family.
