# Game Logic Composition Evals

These scenarios validate the useful boundary between analysis and application without enforcing a bespoke RPC protocol.

## 1. Cold-start change recovers knowledge before applying it

The user asks to change a local/offline mechanic and no verified mechanic knowledge exists.

Required assertions:
- the user's desired behavior is preserved as an analysis scope constraint
- analyze-game-logic recovers only the mechanic facts material to that behavior
- application does not guess patch sites, units, or ownership from intent
- analysis stops at the smallest mechanic slice material to that behavior and does not select the change mechanism
- apply-game-logic consumes the recovered version-scoped mechanic knowledge
- application does not repeat broad reverse engineering

## 2. Existing knowledge avoids unnecessary composition

The user supplies a sufficiently complete finding, mechanic record, or legacy game-logic-mechanic-handoff/v1 and asks for a derived tool or retained local change.

Required assertions:
- apply-game-logic validates only facts material to the requested result
- no normalization-only analyze round-trip occurs
- durable provenance does not require another Skill solely for bookkeeping
- a genuinely missing or stale mechanic relation still returns narrowly to analyze-game-logic

## 3. Analysis database refinement stays on the analysis side

A focused native investigation refines an established project-scoped disassembler/decompiler workspace.

Required assertions:
- analyze-game-logic owns code-local workspace refinement needed to support the recovered mechanic
- workspace refinement does not invoke apply-game-logic by itself
- apply-game-logic is invoked only when the user also requests a downstream tool, instrumentation, test, mod, or gameplay change

## 4. Engine adapters pass facts without forcing application adapters

A cold-start gameplay-change request reaches a GameMaker YYC or Web/JavaScript implementation boundary and analysis loads the matching engine adapter.

Required assertions:
- analyze-game-logic records engine-specific ownership, caller/source, type/lifetime, authority, provenance, and version facts only when material
- the analysis adapter does not rank or select a write, hook, wrapper, config, or patch mechanism
- apply-game-logic consumes the recovered engine-specific facts without re-deriving them
- a GameMaker YYC application does not require a separate YYC application guide; retained native runtime mutations use the shared native-runtime-delivery contract, while other mechanism classes remain governed by the shared core/change-design rules
- Web/JavaScript application guidance is loaded only after the material mechanic, behavioral scope, and mechanism class make that guide relevant
- mechanism selection remains on the application side and is bound to the recovered version-scoped evidence
- change-design remains authoritative across mechanism classes; any remaining engine-specific application guide only refines a selected class

## 5. Continuity uses architecture notes, not shared infrastructure

A user asks for either one-off triage or a retained application, with no pre-existing project store.

Required assertions:
- neither Skill bootstraps a project-level store, manifest, ID registry, or schema migration for one-off or continuity work; helper-local provenance is allowed
- one-off Analyze creates no mandatory notes; continuity retains only useful knowledge, requested material, or valuable evidence
- Apply keeps retained output and rollback materials self-contained without calling Analyze for bookkeeping

## 6. New builds verify old knowledge before application

A later game build is available alongside a useful architecture note and possibly a legacy schema-3 store.

Required assertions:
- structural recognition clues help locate the current behavior without treating old addresses as authoritative
- material mechanic and version-sensitive claims are revalidated before Apply consumes them
- useful legacy files can be consulted as historical evidence but are not automatically rewritten or migrated
- the current result records changed understanding and remaining uncertainty; historical notes/snapshots stay unchanged unless an overview is actively maintained, without a historical artifact graph

## 7. Verified note-only knowledge routes directly to Apply

The user supplies a sufficiently verified architecture note scoped to the current build and requests an offline derived tool. No separate finding, mechanic record, or handoff exists.

Required assertions:
- discovery metadata routes the application task to apply-game-logic with the architecture note as a valid input
- Apply consumes material verified facts from the note without a normalization-only Analyze call or a new schema
- Apply identifies the source note and target build in its output
- only a genuinely missing or stale material relation returns narrowly to analyze-game-logic
