# Static Analysis Refinement

Load this reference only when a compiled/native investigation is already using a writable disassembler/decompiler project (or equivalent structured analysis workspace) and semantic write-back would materially reduce later re-analysis.

Do not create or expand a database-refinement workflow for narrow triage merely because the workspace is writable. These changes improve the analysis workspace; they are not downstream gameplay application and do not by themselves require `$apply-game-logic`.

## Prefer the analysis database over annotated dumps

When the workspace can store names, types, comments, structures, and decompiler annotations directly, treat that database as the primary home for derived static-analysis semantics.

Do not export or retain an annotated binary dump or pseudocode file merely to preserve information that can live in the structured analysis database. This avoids duplicating the same semantic state and reduces large dump artifacts.

Raw/generated dumps still have value when they independently serve as evidence—for example when regeneration is expensive or lossy, exact tool output must be audited, coverage of a large/partial analysis must be demonstrated, or the user explicitly wants the dump retained. In those cases keep the raw rendering as evidence and keep analyst interpretation in the database rather than producing a second annotated copy.

Preserving the evidence boundary does not require preserving every textual rendering. Stable locators, the target binary/build identity, the analysis project, and selectively retained raw evidence should be sufficient to reproduce or audit material conclusions.

## Refine the material slice

Useful derived outputs include:

- concise function purpose and side effects;
- meaningful names for material functions, parameters, locals, globals, and fields;
- recovered calling conventions, signatures, enums, partial structures/classes, and field offsets;
- annotations for decisive guards, state transitions, resets, source discrimination, RNG/timer branches, and authoritative mutations;
- clean C++-like semantic pseudocode that removes decompiler/runtime noise without hiding material behavior.

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

Never present reconstructed pseudocode as original source. Prefer database comments/types/names and the smallest useful reconstructed snippet over maintaining a separate fully annotated pseudocode dump.

## Write-back discipline

When write-back tooling is available, update the existing analysis workspace in the same bounded scope as the investigation.

Treat installed game files as read-only during analysis. Database annotations must not silently become binary patches, runtime hooks, or gameplay changes.

If the workspace is read-only or write-back tooling is unavailable, report the useful proposed names/types/comments or refinement set inline when that helps the user's next step. Do not create a durable artifact solely to satisfy this reference; use the normal persistence rules when retention is independently warranted.
