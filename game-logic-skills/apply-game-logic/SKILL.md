---
name: apply-game-logic
description: Apply recovered, version-scoped gameplay knowledge to an authorized offline/single-player target. Use for calculators, simulators, instrumentation, mods, tests, and scoped local gameplay changes when a finding, mechanic record, or existing handoff already contains the facts material to the application. Use $analyze-game-logic only when mechanic knowledge is missing or stale. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v1.5.0"
---

# Apply Game Logic

Consume recovered mechanic knowledge without redoing reverse engineering. Accept a sufficiently complete finding, mechanic record, architecture note, or existing game-logic-mechanic-handoff/v1. Do not require a format conversion when the material facts are already present. Architecture notes from other builds are rediscovery clues, not automatically confirmed facts for the current target.

If the request starts without verified mechanic knowledge, or the installed target has drifted from the evidence, ask $analyze-game-logic for only the missing relation.

## 1. Bound the application

Work only on authorized offline/local targets.

Supported work includes derived calculators/simulators/tests, observation around a known mechanic, supported mods/configuration, reversible local runtime changes, and explicitly authorized destructive local patches.

Do not manipulate multiplayer or service state, accounts, credentials, DRM/payment/licensing enforcement, anti-cheat, leaderboards, matchmaking, or another player's experience.

Installed game files remain read-only unless the user explicitly authorizes a destructive version-specific modification. User intent establishes behavioral scope; actual write permission, confirmation, and irreversible-action enforcement must still come from the runtime or tool boundary.

## 2. Check only facts material to the requested result

Before implementation, establish the facts that can change correctness or scope. Depending on the task these may include:

- target version/build/hash;
- confidence and validation state;
- formula order, units, clamps, rounding, RNG, or timing;
- trigger/caller and authoritative mutation;
- owner, lifetime, persistence, reset, and fan-out;
- authority/serialization;
- stable source/function or module + RVA locators.

A confirmed fact can be consumed within its recorded scope. A working hypothesis may support a labeled experiment or validation harness, but it must not be the sole basis for a retained or destructive gameplay change whose correctness or scope depends on that hypothesis. A material unknown is a stop condition for the affected application path.

If a supplied finding explicitly marks itself as superseded or replaced, do not consume it as the current fact even when its contents are otherwise complete. Use the identified successor when available, or revalidate only the affected relation. Do not require lifecycle metadata when the input does not provide it.

Do not demand unrelated fields merely because another representation contains them.

## 3. Choose the smallest adequate application

For calculators, simulators, reference implementations, and tests, preserve the recovered operation order and state semantics exactly. Separate recovered facts from assumptions introduced by the derived tool.

For observation-only instrumentation, use the smallest stable boundary and avoid changing the state transition being observed.

For gameplay changes, load [references/change-design.md](references/change-design.md). Establish behavioral scope before choosing the mechanism; reversibility alone does not prove narrow scope.

For retained native runtime mechanisms that write process memory or install/replace executable code, load [references/native-runtime-delivery.md](references/native-runtime-delivery.md). If the deliverable is a Cheat Engine table/Auto Assembler script or CE is the retained runtime surface, also load [references/cheat-engine-delivery.md](references/cheat-engine-delivery.md).

## 4. Bind implementation to evidence

Every application should state which mechanic record/finding and target version it consumes.

For source/script/config targets, prefer semantic locators plus a target hash when material. For native work, persist and hand off target identity + module + RVA. Tool-local preferred/runtime VAs are transient and adapters own conversion. Retained implementations may use symbolic, site-relative, or other tool-native forms when they map unambiguously to the canonical site; derive absolute addresses from module + RVA when needed. Validate the exact emitted implementation before writing or hooking.

If the installed version/hash no longer matches the evidence, stop and revalidate only the material relation with $analyze-game-logic.

## 5. Validate the application result

Validate the application, not the mechanic discovery process.

- Derived tools: compare boundary and representative cases against the recovered rule.
- Instrumentation: verify observation does not materially change the relevant behavior.
- Gameplay changes: compare control and modified behavior and test only edge cases that can expose scope leakage.

A successful result in one scenario proves only that scenario unless broader ownership/fan-out is already evidenced.

If validation contradicts the recovered mechanic rather than the implementation, return that discrepancy to $analyze-game-logic instead of patching around it.

## 6. Preserve provenance and rollback when needed

For a one-off explanation or calculation, provenance in the answer is enough.

For retained or deployed outputs, load [references/application-artifacts.md](references/application-artifacts.md). Keep the authoritative implementation, target identity, consumed mechanic knowledge, validation result, and rollback/control state together in a self-contained working location. Do not require a project-level store, artifact registration, or an Analyze call solely for bookkeeping.

Before a destructive change, capture the original bytes/content or an integrity-verifiable backup. If the original state cannot be captured and verified well enough to restore, stop before modifying the installed target.

## Completion

Before finishing, verify that all material mechanic dependencies are present, uncertainty was not promoted silently, the target still matches the evidence, the application preserves or intentionally changes the mechanic as requested, validation covers the claimed scope, and any retained/deployed change can be traced and rolled back without conversational memory.
