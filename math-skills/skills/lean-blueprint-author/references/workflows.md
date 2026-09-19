# Workflows

## Create

Use Create when the user wants a new blueprint route for a target theorem, definition, construction, or other tracked node.

1. **Identify the target.** State exactly what the final node should express.
2. **Gather authoritative material.** Use the supplied references, existing blueprint, local Lean code, and reliable library facts that are relevant to the target.
3. **Build the dependency route backward.** Separate prerequisites needed for the statement from lemmas used only in proofs.
4. **Minimize the graph.** Merge routine steps into prose; keep separate nodes for reusable results, substantial bottlenecks, and independent formalization obligations.
5. **Write the LaTeX in project style.** Add `\lean`/status metadata only when the corresponding declarations are actually known in the project.
6. **Validate if working in a project.** Run the web build. If Lean metadata was added or changed, build Lean as needed, rebuild the web blueprint so its declaration list is current, then run the declaration check.

If a necessary bridge is not present in the sources or code, introduce it as a clearly identified proposed local lemma rather than pretending it is an existing theorem.

### Create output

Return insertion-ready LaTeX plus a short summary of the route and any proposed/unresolved nodes.

## Modify

Use Modify for an existing blueprint when the user wants a mathematical or structural change.

1. **Read the affected region and nearby conventions.** Identify the statement/proof/dependencies being changed.
2. **Make the requested change directly.** Preserve unrelated text, labels, citations, custom macros, discussion links, and status markers.
3. **Repair local references.** If labels, node boundaries, or proof placement changed, update affected `\uses`, `\proves`, and ordinary LaTeX references.
4. **Revisit downstream dependencies only where the change matters.** A statement change may affect both statement and proof dependencies; a proof-only change normally affects proof routes, not downstream statements.
5. **Validate the edited surface.** Build the web blueprint. When Lean metadata changed, build Lean as needed, rebuild the web blueprint, then run the declaration check.

Prefer a small patch over reconstructing a whole file. Reordering alone is not a reason to rewrite mathematical dependencies.

### Modify output

Show/apply the changed region and summarize added/removed nodes, changed dependencies, and any mathematical follow-up that remains.

## Update

Use Update to synchronize an existing blueprint with the current Lean project while keeping the mathematical route intact.

1. **Read blueprint mappings.** Collect relevant nodes, their `\lean` declarations, and status markers.
2. **Inspect the Lean project.** Find the corresponding declarations and inspect their types/definitions/proofs when status is being changed.
3. **Synchronize names.** Fix clearly stale declaration names and add obvious missing mappings. Leave ambiguous mappings unresolved rather than guessing.
4. **Synchronize status.**
   - use statement `\leanok` when the mapped Lean declaration matches the blueprint statement;
   - use proof `\leanok` when the corresponding proof/implementation is complete;
   - use `\mathlibok` when the node itself is supplied by Mathlib;
   - keep `\notready` as a mathematical-readiness marker unless the requested update includes changing readiness.
5. **Keep dependencies mathematical.** Do not rewrite `\uses` merely because Lean's implementation imports or calls extra helper declarations. Change blueprint dependencies when the mathematical route changed or the existing graph is wrong.
6. **Validate.** For changed mappings/status, build Lean as needed, rebuild the web blueprint so the generated declaration list is current, then run the project's declaration check.

When an Update reveals that the blueprint statement itself no longer matches the intended theorem, switch to a small Modify operation rather than hiding the mismatch with metadata edits.

### Update output

Summarize:

- Lean names added, removed, or corrected;
- `\leanok` / `\mathlibok` changes;
- unresolved or ambiguous mappings;
- validation results relevant to those changes.

## Shared Editing Notes

- Preserve custom theorem environments and labels.
- Prefer one `\lean{...}` and one `\uses{...}` per environment unless project style says otherwise.
- Keep statement dependencies and proof-only dependencies separate in source, even though the rendered graph may combine information for readiness/display.
- Use `\proves{...}` when a non-adjacent proof needs an explicit target.
- Do not add a new node just to mirror every Lean helper declaration; the blueprint tracks the mathematical plan, not the implementation call graph.
