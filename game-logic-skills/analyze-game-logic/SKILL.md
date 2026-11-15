---
name: analyze-game-logic
description: Recover and verify authorized offline/single-player game logic with reproducible evidence. Use when a mechanic, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale, including cold-start requests that later feed $apply-game-logic. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v5.6.0"
---

# Analyze Game Logic

Answer the user's question with the smallest evidence-backed, build-scoped implementation slice. A location lookup does not require a full mechanic reconstruction; add tools, validation, and retained artifacts only when they resolve a material uncertainty.

This skill recovers mechanic knowledge. It does not choose a change or delivery mechanism.

## Boundaries

- Work only on authorized offline/local targets. When online impact or authorization is unclear, stay with non-invasive static inspection until the distinction matters.
- Do not interfere with multiplayer, server-authoritative state, other players, accounts, credentials, DRM, payments, licensing, or anti-cheat.
- Keep installed game files read-only during analysis; observation-only instrumentation must be reversible.
- Names, cross-references, constants, and presentation code are search clues, not proof of units, probability, state ownership, lifetime, authority, or causality.

## Workflow

### 1. Scope

Identify the mechanic or implementation locator, the target build/files, and the exact claim to establish. Let the question and unresolved facts determine depth: find an identity, explain one causal path, or reconstruct a larger system only as needed.

If the user ultimately wants a change, use that outcome to bound the facts to recover, not to select a patch method.

### 2. Locate

Start with readable source/configuration, scripts, resources, strings, symbols, metadata, reflection, and existing analysis projects. Prefer targeted functions and data-flow slices to broad decompilation.

Escalate to a less-readable layer only when the relevant path demonstrably crosses it or a bounded search shows the readable layers cannot resolve a material fact. Truncated output or partial inspection cannot prove exhaustive coverage.

When engine-specific interpretation matters, identify the actual gameplay boundary from corroborating project/data markers and load its adapter directly:

| Boundary | Adapter |
| --- | --- |
| GameMaker YYC | [engine-gamemaker-yyc.md](references/engine-gamemaker-yyc.md) |
| Godot GDScript / scenes / resources | [engine-godot-gdscript.md](references/engine-godot-gdscript.md) |
| Unity Mono | [engine-unity-mono.md](references/engine-unity-mono.md) |
| RPG Maker MV/MZ | [engine-rpgmaker-mv-mz.md](references/engine-rpgmaker-mv-mz.md) |
| Web / JavaScript | [engine-web-javascript.md](references/engine-web-javascript.md) |
| LÖVE / Love2D Lua | [engine-love2d-lua.md](references/engine-love2d-lua.md) |

Prefer a confirmed game-engine adapter over a generic JavaScript/runtime adapter for engine-owned gameplay. Use a generic adapter additionally only for a distinct material boundary; ambiguous or unsupported backends (including Unity IL2CPP, Unreal native, and GameMaker VM) follow this core workflow without invented engine rules. Do not load unrelated adapters.

### 3. Understand

For behavior questions, follow the smallest material causal chain:

**Trigger/source → Eligibility/gate → Rule/transition → Authoritative state mutation**

Resolve only facts that affect the answer: formula order, clamping/rounding, units and RNG; event source and scheduler; state owner, sharing, lifetime, persistence and reset; and gameplay authority versus presentation. For complex cross-cutting behavior, consult [gameplay-semantics.md](references/gameplay-semantics.md).

A narrow location/identity claim can stop at an evidence-backed, distinguishable locator. For compiled/native code, prefer a verified module + RVA for the inspected build over an unscoped absolute address; do not reuse it as proof for another build.

### 4. Verify and report

Check each material claim against semantic evidence. Different views of the same code are not independent corroboration; cross-references establish association, not behavior.

Label conclusions **Confirmed** (material checks satisfied), **Working hypothesis** (plausible but missing a material check), or **Unknown** (an unresolved fact could change the result).

Runtime validation is not required for an identity-only lookup or a statically decisive rule. When actual timing, causality, caller, state lifetime, authority, or effective randomness cannot be established statically, consult [runtime-validation.md](references/runtime-validation.md). If practical validation is not performed, leave the affected claim a working hypothesis and say what remains to test.

Report only what the task needs: build/version/hash scope, conclusion and concise mechanic pseudocode when relevant, stable locators, supporting evidence, validation status, and material unknowns. Distinguish observation from inference.

**Stop when the requested identity or mechanic is sufficiently supported, remaining material uncertainty is explicit, and the result is usable for the next step.**

## Optional follow-through

- **Analysis workspace:** For substantive compiled/native work already using a project-scoped editable disassembler/decompiler database, consult [static-analysis-refinement.md](references/static-analysis-refinement.md) for bounded, evidence-backed, non-destructive annotations. Do not create this work for a narrow lookup.
- **Retention:** For an explicit save request, multi-session work, or costly/lossy evidence worth reusing, consult [project-knowledge.md](references/project-knowledge.md). One-off lookups need no storage. Saved snapshots are build-scoped and need no ongoing maintenance; old notes guide rediscovery, not proof of a new build.
- **Downstream application:** Pass only the material, version-scoped mechanic facts to $apply-game-logic. A sufficiently complete finding is already a valid handoff; no extra protocol or format conversion is needed.
