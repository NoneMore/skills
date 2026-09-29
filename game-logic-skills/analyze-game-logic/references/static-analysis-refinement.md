# Static Analysis Refinement

Use this reference only for focused/full compiled/native analysis already using an established project-scoped disassembler/decompiler workspace where code-local semantic write-back would materially reduce re-analysis. Do not create refinement work for narrow triage. Workspace refinement remains analysis work; it does not by itself require `$apply-game-logic`.

## Keep semantic stores distinct

Keep three layers distinct:

- **Evidence:** reproducible source/tool/runtime observations.
- **Workspace-local interpretation:** names, types, structures, comments, and branch annotations attached to the analysis project.
- **Portable mechanic finding:** the version-scoped claim, confidence, locators, validation state, and material unknowns retained under [project-knowledge.md](project-knowledge.md).

The analysis database is the primary home for workspace-local interpretation. It does not replace a portable finding when normal persistence triggers apply.

Do not retain an annotated dump or rewritten pseudocode solely to duplicate semantics already stored in the database. Retain raw/generated output only when it independently earns persistence, such as for costly/lossy regeneration, audit or coverage needs, or an explicit user request.

## Refine only what the evidence supports

Refine only the material mechanic slice. Useful write-back includes evidence-backed names, signatures, enums, partial structures/fields, function-purpose comments, and annotations for decisive guards, state transitions, resets, caller/source discrimination, timing/RNG branches, and authoritative mutations.

Use the strongest name or type justified by the evidence, not the most specific plausible interpretation. Keep uncertain members neutral or offset-based, recover structures incrementally, and keep build-sensitive layouts version-scoped. A rename, type, or comment cannot independently confirm the interpretation that produced it. Keep stable locators and enough reproducible evidence to audit material refinements.

When explanation benefits from clean pseudocode, generate the smallest useful reconstruction. Treat it as derived explanation, never original source or another canonical semantic store.

## Write back non-destructively

Treat an established project-scoped analysis database as mutable working state when write-back tooling is available; do not require per-annotation confirmation. A merely writable arbitrary file does not qualify, and explicit read-only or archival state wins.

Prefer a recoverable working database or backup under the analysis/project directory over an original or sidecar database in the installed binary/source directory when source boundaries or reconstruction cost matter.

Preserve stronger or analyst-authored semantic state by default. Revise it only when material new evidence justifies the change; otherwise add a non-destructive note or report the proposed alternative inline.

Treat installed game files and source binaries as read-only during analysis. Database refinement must not silently become a binary patch, runtime hook, or gameplay change.

If write-back is unavailable or disallowed, report the useful proposed refinements inline. Do not create a durable artifact solely to satisfy this reference.
