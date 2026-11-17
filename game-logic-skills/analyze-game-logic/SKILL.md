---
name: analyze-game-logic
description: Recover and verify authorized offline/single-player game logic with reproducible evidence. Use when a mechanic, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale, including cold-start requests that later feed $apply-game-logic. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v5.6.0"
---

# Analyze Game Logic

Recover the smallest evidence-backed, build-scoped answer. A function lookup needs no full mechanic reconstruction, runtime experiment, or saved project.

## Boundaries

- Work only on authorized offline/local targets. If online impact or authorization is unclear, stay with non-invasive static inspection.
- Do not interfere with multiplayer/server state, other players, accounts, credentials, DRM, payments, licensing, or anti-cheat.
- Treat installed game files as read-only; observation-only instrumentation must be reversible.
- Names, xrefs, constants, and UI/presentation evidence alone do not prove units, probabilities, causality, ownership, lifetime, or authority.

## Workflow

### 1. Scope

Identify the target build/files and the exact mechanic or locator the user needs. Let unresolved facts determine depth: identify a location, explain one causal path, or reconstruct a system only when necessary. A requested future change bounds relevant facts; selecting how to change the game belongs to $apply-game-logic.

### 2. Locate

Start with readable source, scripts, configuration, resources, strings, symbols, metadata, and existing analysis projects. Prefer targeted data-flow slices over broad decompilation. Escalate to an opaque layer only with evidence that the relevant path crosses it, or a bounded search showing readable layers cannot answer the question. Partial or truncated inspection cannot support completeness claims.

When engine-specific knowledge matters, identify the gameplay implementation from corroborating markers and load its adapter directly:

| Boundary | Adapter |
| --- | --- |
| GameMaker YYC | [YYC](references/engine-gamemaker-yyc.md) |
| Godot GDScript / scene-resource graph | [Godot](references/engine-godot-gdscript.md) |
| Unity Mono | [Unity](references/engine-unity-mono.md) |
| RPG Maker MV/MZ | [RPG Maker](references/engine-rpgmaker-mv-mz.md) |
| Web/JavaScript | [Web/JS](references/engine-web-javascript.md) |
| Windows LÖVE/Love2D Lua | [LÖVE](references/engine-love2d-lua.md) |

Prefer the dedicated game-engine adapter for engine-owned logic; use a generic adapter only for a separate material runtime boundary. For unsupported or ambiguous backends (e.g. IL2CPP, Unreal native, GameMaker VM), use the core workflow without inventing engine rules.

### 3. Understand

For behavior questions, trace the material path:

**Trigger/source → Gate → Rule/transition → Authoritative state mutation**

Resolve only consequential formula order, clamps/rounding, units, RNG, event source, timing, state owner/sharing/lifetime, persistence/reset, and gameplay versus presentation authority. For nontrivial cross-cutting semantics, read [gameplay-semantics.md](references/gameplay-semantics.md).

For location-only questions, stop at a distinct, evidence-backed locator. For compiled/native code, verify module + RVA against the inspected build; do not assume addresses survive updates.

### 4. Verify and report

Use semantic evidence and an independent check when material; another rendering of the same code is not independent evidence. Label conclusions **Confirmed** (material checks satisfied), **Working hypothesis** (material validation missing), or **Unknown** (a consequential fact unresolved).

Load [runtime-validation.md](references/runtime-validation.md) only when timing, causality, caller, lifetime, authority, or effective randomness needs runtime evidence. If practical validation is omitted, keep the affected claim a hypothesis.

Report the build/version/hash scope, conclusion and brief pseudocode when relevant, stable implementation locator, evidence, validation state, and material unknowns. Distinguish observations from inferences; scale output to the question.

**Stop once the requested identity or behavior is supported and remaining consequential uncertainty is explicit.**

## Optional follow-through

- For substantive compiled/native work in an existing editable analysis workspace, use [static-analysis-refinement.md](references/static-analysis-refinement.md) for bounded, non-destructive, evidence-backed annotations; not for narrow lookups.
- For explicitly requested retention, multi-session work, or costly/lossy evidence, use [project-knowledge.md](references/project-knowledge.md). One-off lookups need no storage; historical build snapshots guide rediscovery, not current proof, and saving does not imply maintenance.
- Pass material version-scoped findings to $apply-game-logic when application is requested. A sufficient finding needs no extra handoff format.
