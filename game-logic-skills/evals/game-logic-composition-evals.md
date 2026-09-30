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
