# Game Logic Composition Evals

These scenarios validate the useful boundary between analysis and application without enforcing a bespoke RPC protocol.

## 1. Cold-start change recovers knowledge before applying it

The user asks to change a local/offline mechanic and no verified mechanic knowledge exists.

Required assertions:
- analyze-game-logic recovers the material mechanic facts first
- application does not guess patch sites, units, or ownership from intent
- apply-game-logic consumes the recovered version-scoped mechanic knowledge
- analysis does not design the downstream change
- application does not repeat broad reverse engineering

## 2. Existing knowledge avoids unnecessary composition

The user supplies a sufficiently complete finding, mechanic record, or legacy game-logic-mechanic-handoff/v1 and asks for a derived tool or retained local change.

Required assertions:
- apply-game-logic validates only facts material to the requested result
- no normalization-only analyze round-trip occurs
- durable provenance does not require another Skill solely for bookkeeping
- a genuinely missing or stale mechanic relation still returns narrowly to analyze-game-logic

## 3. Analysis database refinement stays on the analysis side

A focused native investigation uses an established project-scoped writable disassembler/decompiler workspace. The current workflow treats its working database as editable analysis state, even if the user did not separately request each rename, type, or comment.

Required assertions:
- analyze-game-logic may rename, type, comment, or reconstruct the material analysis slice when evidence supports it
- an established project-scoped working database does not require a separate per-edit opt-in unless the user or workflow marks it read-only or archival
- existing stronger analyst-authored semantic state is preserved unless material new evidence justifies revision
- clean reconstructed pseudocode remains an explanatory projection; short snippets may be stored as comments without becoming another canonical semantic store
- writable analysis-database changes are not treated as downstream gameplay application by themselves
- apply-game-logic is invoked only if the user also requests a calculator, simulator, instrumentation, mod, test, or gameplay change
- installed game files remain read-only during analysis
