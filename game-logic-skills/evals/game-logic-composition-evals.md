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

A focused native investigation refines an established project-scoped disassembler/decompiler workspace.

Required assertions:
- analyze-game-logic owns code-local workspace refinement needed to support the recovered mechanic
- workspace refinement does not invoke apply-game-logic by itself
- apply-game-logic is invoked only when the user also requests a downstream tool, instrumentation, test, mod, or gameplay change

## 4. Validation tooling does not dictate deployment tooling

A native offline mechanic is recovered and Frida is used during analysis to discriminate callers and confirm causal control. The user then requests a reusable local gameplay change.

Required assertions:
- analyze-game-logic returns the validated version-scoped mechanic and scope facts without prescribing the final deployment surface
- apply-game-logic chooses the delivery mechanism independently from the analysis instrumentation
- a lower-mediation guarded write or patch may be selected when it preserves the required scope and lifecycle behavior
- dynamic instrumentation remains valid when context-sensitive filtering or lifecycle logic materially requires it
