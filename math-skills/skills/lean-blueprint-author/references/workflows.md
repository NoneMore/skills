# Workflows

## Shared Project Preflight

For work on a real project:

1. Locate the Lean project root and the project's actual blueprint entry/build conventions. The stock layout usually uses `blueprint/src/web.tex`, `blueprint/src/print.tex`, and `blueprint/src/content.tex`, but custom layouts are valid.
2. Prefer a project-native read-only blueprint status/graph tool when it clearly provides the needed factual view. Otherwise use the bundled `scripts/blueprint.py` mechanical tool when supported.
3. Run the mechanical check before relying on a normalized graph view:

   ```sh
   python3 <skill-path>/scripts/blueprint.py check --project-root <project-root>
   ```

   - exit `0`: projection is mechanically coherent;
   - exit `1`: fix/report the structural projection violations before treating the normalized graph as authoritative;
   - exit `2`: the bundled projection is unsupported/unavailable; do not emulate it with a regex parser.
4. For Modify/Update tasks where graph or metadata effects matter, save a pre-edit state when useful:

   ```sh
   python3 <skill-path>/scripts/blueprint.py inspect --project-root <project-root> > /tmp/blueprint-before.json
   ```

The mechanical tool reports project facts; it does not decide mathematical dependency quality, node granularity, or Lean/blueprint semantic equivalence.

For standalone snippets or pasted fragments, work directly from the supplied material and do not claim project-level validation.

## Create

Use Create when the user wants a new route or tracked nodes for a theorem, definition, construction, or other mathematical target.

1. **Identify the target exactly.** State what the final node should express.
2. **Gather authoritative material.** Use the supplied references, nearby blueprint, local Lean declarations/types, and reliable library facts relevant to the target.
3. **Build the route backward.** Separate prerequisites needed to state the target from results used only in its proof.
4. **Minimize the graph.** Keep separate nodes for reusable results, substantial bottlenecks, and independent formalization obligations; keep routine transformations in prose.
5. **Write in project style.** Reuse existing theorem environments, labels, macros, citations, and proof layout. Add Lean metadata only when supported by the project.
6. **Re-run the mechanical check/inspect when project structure changed**, then perform the relevant upstream/project validation described below.

If a necessary bridge is absent from the sources/code, introduce it as a clearly proposed local lemma rather than pretending an existing theorem supplies it.

### Create output

Return/apply insertion-ready LaTeX, summarize the mathematical route, and identify proposed or unresolved nodes.

## Modify

Use Modify when an existing blueprint needs a mathematical or structural change.

1. **Use the mechanical view to localize the edit when available.** Read the affected source region and nearby conventions rather than reconstructing the whole graph manually.
2. **Make the requested change directly.** Preserve unrelated prose, labels, citations, discussion links, custom macros, and status markers.
3. **Repair directly affected references/associations.** Update `\uses`, `\proves`, and ordinary LaTeX references only where the edit requires it.
4. **Use graph impact mechanically; judge consequences mathematically.** Reverse dependencies can identify potentially affected nodes, but whether they require edits is a mathematical decision. A proof-only change normally does not alter downstream statement dependencies.
5. **Re-run `check` and `inspect`.** If a pre-edit state was saved, compare normalized effects:

   ```sh
   python3 <skill-path>/scripts/blueprint.py inspect --project-root <project-root> > /tmp/blueprint-after.json
   python3 <skill-path>/scripts/blueprint.py diff /tmp/blueprint-before.json /tmp/blueprint-after.json
   ```
6. **Validate the edited project surface** with the real project commands below.

Prefer a small patch over reconstructing whole files. Reordering alone is not a reason to rewrite mathematical dependencies.

### Modify output

Summarize the changed region, material node/dependency/mapping effects, and unresolved mathematical follow-up. Prefer mechanically generated structural diff facts over manually counting graph changes.

## Update

Use Update to synchronize an existing blueprint with the current Lean project while keeping the mathematical route intact.

1. **Start from the mechanical mapping/status view when available.** Use `inspect` or a project-native equivalent to collect the relevant nodes and existing metadata.
2. **Inspect authoritative Lean declarations.** Read declaration types/definitions/proofs when changing semantic status; declaration existence alone is insufficient.
3. **Synchronize names.** Fix clearly stale names and add obvious missing mappings. Leave ambiguous candidates unresolved.
4. **Synchronize status.**
   - statement `\leanok`: only when the mapped Lean declaration corresponds to the blueprint statement;
   - proof `\leanok`: only when the corresponding proof/implementation is complete enough to justify the claim;
   - `\mathlibok`: only when the node itself is supplied by Mathlib;
   - `\notready`: keep as a mathematical-readiness marker unless the requested work includes changing readiness.
5. **Keep dependencies mathematical.** Do not rewrite `\uses` merely to mirror Lean imports, helper calls, or implementation details.
6. **Do not repair mathematics just to make synchronization succeed.** If the blueprint statement and intended Lean theorem no longer match, leave disputed metadata unchanged and report the mismatch unless the user's requested outcome includes a Modify operation.
7. **Re-run mechanical check/inspect/diff**, then perform the real Lean/blueprint validation below.

### Update output

Summarize Lean-name/status changes, unresolved or mismatched cases, mechanically observed structural effects, and relevant validation results.

## Real Project Validation

The bundled mechanical tool complements rather than replaces upstream/project validation.
Use the narrowest checks appropriate to what changed:

- After structural/dependency/`\lean{...}` edits, run the project's web build, normally `leanblueprint web`. In the stock workflow this regenerates `blueprint/lean_decls`.
- If Lean mappings/status changed, ensure the Lean project is built as needed, rebuild the web blueprint so declaration data is current, then run `leanblueprint checkdecls` or the project's equivalent.
- Use `leanblueprint all` only when a broad final build is warranted.
- Run `leanblueprint pdf` when PDF/print-specific content changed, the user requests PDF validation, or the project's bibliography workflow requires PDF/BibTeX work before the web build.
- Inspect the repository diff and fix failures introduced by the edit.

A successful web build or declaration check confirms syntax/generation/name availability only. It does not establish mathematical equivalence between blueprint prose and Lean types, proof completeness, or absence of placeholders such as `sorry`.

## Shared Editing Notes

- Preserve custom theorem environments and project label conventions.
- Use one complete `\lean{...}` and one complete `\uses{...}` per owner; current upstream stores these as single values rather than merging repeated occurrences.
- Keep statement and proof dependencies separate in source.
- Use `\proves{...}` for a non-adjacent proof target.
- Do not create blueprint nodes merely to mirror Lean helper declarations.
- Do not treat frontier/priority heuristics as authoring semantics; planning/ranking is outside this Skill's mechanical contract.
