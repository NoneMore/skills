# Static Analysis Refinement

Load this reference only when a compiled/native investigation is already using a writable disassembler/decompiler project (or equivalent structured analysis workspace) and semantic write-back would materially reduce later re-analysis.

Do not create or expand a database-refinement workflow for narrow triage merely because the workspace is writable. These changes improve the analysis workspace; they are not downstream gameplay application and do not by themselves require `$apply-game-logic`.

## Prefer the analysis database for code-local semantics

When an established analysis project can store names, types, comments, structures, and branch/decompiler annotations directly, treat that database as the primary home for code-local semantic refinement.

Keep three layers distinct:

- **Evidence:** instructions, original tool output, symbols/RTTI, strings, xrefs, source artifacts, and runtime observations.
- **Workspace-local interpretation:** names, types, structures, comments, branch annotations, and other code-local semantics attached to the analysis project.
- **Portable mechanic finding:** the version-scoped claim, confidence, locators, material mechanic details, validation state, and unknowns that should survive outside one analysis database.

The analysis database owns the middle layer. It does not replace a reusable finding when the normal persistence triggers in [project-knowledge.md](project-knowledge.md) apply.

Do not export or retain an annotated binary dump or pseudocode file merely to preserve information that can live in the structured analysis database. This avoids duplicating the same semantic state and reduces large dump artifacts.

Raw/generated dumps still have value when they independently serve as evidence—for example when regeneration is expensive or lossy, exact tool output must be audited, coverage of a large/partial analysis must be demonstrated, or the user explicitly wants the dump retained. In those cases keep the raw rendering as evidence and keep code-local analyst interpretation in the database rather than producing a second annotated copy. Portable findings still follow the normal persistence rules.

Preserving the evidence boundary does not require preserving every textual rendering. Stable locators, the target binary/build identity, the analysis project, and selectively retained raw evidence should be sufficient to reproduce or audit material conclusions.

## Refine the material slice

Useful derived outputs include:

- concise function purpose and side effects;
- meaningful names for material functions, parameters, locals, globals, and fields;
- recovered calling conventions, signatures, enums, partial structures/classes, and field offsets;
- annotations for decisive guards, state transitions, resets, source discrimination, RNG/timer branches, and authoritative mutations.

When useful for explanation, generate the smallest clean C++-like reconstruction needed to express the recovered mechanic. Treat it as a derived explanatory projection rather than another canonical semantic store.

Apply only the subset that helps navigate or continue the current mechanic analysis. Do not broadly rename or propagate types through unrelated code.

## Preserve the evidence boundary

Instructions, original decompiler output, symbols/RTTI, strings, xrefs, source artifacts, and runtime observations are evidence whether observed directly or selectively retained under the normal persistence rules.

Renames, comments, reconstructed types, inferred field meanings, and clean pseudocode are derived interpretations. A rename or reconstructed type cannot become an independent confirmation of the claim that motivated it.

Keep stable source/function or module + RVA locators and enough reproducible or retained evidence to audit or reverse each material annotation.

## Keep uncertainty visible

Use the strongest name or type justified by the evidence, not the most specific plausible interpretation.

- Keep uncertain members neutral or offset-based instead of inventing semantics.
- Recover structures incrementally; unknown `field_xxx` members may remain unknown.
- Do not invent ownership, inheritance, padding meaning, or field purpose to make a model look complete.
- Keep build-sensitive signatures and layouts scoped to the analyzed version.
- Record uncertainty in comments/findings when a precise name would overstate confidence.

## Clean reconstruction

Semantic pseudocode should express the recovered mechanic, not reproduce compiler scaffolding.

Collapse redundant temporaries, generated lifetime machinery, and other noise only when no material side effect is lost. Preserve or call out material casts, ownership/lifetime behavior, exception behavior, or unknowns that were intentionally abstracted.

Never present reconstructed pseudocode as original source. Prefer structured database state for durable code-local semantics. Short reconstructed snippets may live in comments when they clarify local behavior, but do not maintain rewritten pseudocode as another canonical semantic store. Generate only the smallest useful reconstruction for explanation or handoff.

## Write-back discipline

An established, project-scoped analysis database is mutable working state by default when write-back tooling is available. Do not require a separate per-rename/type/comment opt-in merely because refinement mutates that workspace. A merely writable arbitrary file is not enough; the database must already be part of the active analysis project.

Prefer a working database or backup under the analysis/project directory rather than an original or sidecar copy in the installed binary/source directory. This matters especially when the binary is large or the analysis database is expensive to reconstruct: preserve a recoverable project copy, then refine that copy rather than withholding useful write-back.

Preserve existing analyst-authored names, types, comments, structures, and other curated semantic state by default. Do not silently replace stronger or user-authored annotations with another merely plausible interpretation. Revise existing semantic state only when material new evidence justifies the change; otherwise add a non-destructive note or report the proposed alternative inline.

Honor explicit read-only or archival instructions and any workflow state that marks the project as immutable. Treat installed game files and source binaries as read-only during analysis. Database annotations must not silently become binary patches, runtime hooks, or gameplay changes.

If the workspace is read-only or write-back tooling is unavailable, report the useful proposed names/types/comments or refinement set inline when that helps the user's next step. Do not create a durable artifact solely to satisfy this reference; use the normal persistence rules when retention is independently warranted.
