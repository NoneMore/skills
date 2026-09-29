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
