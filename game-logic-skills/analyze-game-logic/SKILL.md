---
name: analyze-game-logic
description: Recover and verify authorized offline/single-player game logic with reproducible evidence. Use when a mechanic, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale, including cold-start requests that later feed $apply-game-logic. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v5.5.0"
---

# Analyze Game Logic

Recover the smallest version-scoped mechanic slice that answers the question. Keep narrow lookups narrow; add deeper analysis, runtime work, or retained artifacts only for a task-relevant reason.

This skill produces mechanic knowledge, not a change mechanism. For downstream tasks, use the desired outcome to select material facts and pass version-scoped findings to $apply-game-logic.

## 1. Bound the task

Work only on authorized offline/local targets.

- If online impact or authorization is genuinely unclear, stay with non-invasive static inspection until the distinction matters.
- Do not manipulate multiplayer state, matchmaking, leaderboards, server-authoritative state, accounts, credentials, or another player's experience.
- Do not bypass DRM, payments, licensing, or anti-cheat.
- Treat installed game files as read-only during analysis. Observation-only instrumentation must be reversible.
- Do not infer units, probabilities, ownership, lifetime, authority, or causal control from names, xrefs, constants, or presentation evidence alone.

## 2. Match analysis depth to the question

Use the lightest path that can close the claim:

- **Triage:** locate or identify a function, field, script, table, or call site.
- **Focused analysis:** explain one mechanic or causal path with reusable evidence.
- **Full analysis:** reconstruct a multi-component mechanic or system with the evidence and validation needed to support the requested conclusions.

Choose analysis depth from the question and remaining uncertainty, not from a storage workflow.

## 3. Find the material implementation path

Start with cheap semantic evidence: readable configuration/source, strings, symbols, RTTI/reflection, imports, resources, file layout, metadata, and existing analysis projects.

Escalate from readable code to opaque layers only for a named unresolved fact. Require either evidence that the relevant path crosses that boundary or a bounded search showing the readable layers cannot answer it. Stay with source/scripts when sufficient; prefer targeted functions and data-flow slices over broad decompilation.

Truncated output or a partial inspection cannot support completeness claims. Inspect missing ranges only when material; preserve costly or lossy ranges under [references/project-knowledge.md](references/project-knowledge.md) when useful.

Once the relevant boundary is known, consult [references/engine-registry.md](references/engine-registry.md) and load only its material adapter. Check corroborating project/data markers for a dedicated game-engine adapter before generic language/runtime guidance; use a generic adapter only for a distinct material boundary.

For focused/full compiled/native analysis already using an established project-scoped editable disassembler/decompiler workspace, load [references/static-analysis-refinement.md](references/static-analysis-refinement.md). Do not introduce refinement work for triage.

## 4. Reconstruct the mechanic, not just the address

For behavior or causality questions, load [references/gameplay-semantics.md](references/gameplay-semantics.md).

Trace from a strong semantic anchor to the authoritative state transition. Resolve only dimensions that can change the answer, such as:

- trigger and eligibility;
- formula/order, clamps, rounding, units, and RNG;
- state owner, lifetime, sharing/fan-out, persistence, and reset;
- scheduling, caller/event source, and authority;
- presentation versus gameplay ownership.

Stop when the smallest material slice can be expressed as concise gameplay pseudocode and every remaining material unknown is explicit.

For compiled/native boundaries, prefer module + RVA locators for the inspected build and verify address conversions against the original binary or loaded module before relying on them. Do not assume an RVA remains valid across builds.

## 5. Close the evidence loop

Use three states:

- **Confirmed:** semantic evidence supports the claim and any material independent check has been satisfied.
- **Working hypothesis:** plausible, but a material independent check or runtime validation is still missing.
- **Unknown:** a fact that can change the interpretation remains unresolved.

Different renderings of the same relation are not independent evidence. Cross-references show association, not gameplay semantics.

Runtime validation is optional for narrow identity/location claims. When timing, causal control, caller discrimination, state lifetime, authority, or effective randomness materially depends on runtime behavior, load [references/runtime-validation.md](references/runtime-validation.md). If practical validation is omitted, keep the affected claim a working hypothesis.

## 6. Retain reusable understanding selectively

Unrequested one-off lookups need no storage. For explicit save requests, multi-session work, or materially costly/lossy evidence, follow [references/project-knowledge.md](references/project-knowledge.md). Honor explicit retention even for cheap material; otherwise keep only what has future reading or verification value. Retention does not imply maintenance.

Across builds, old notes guide rediscovery rather than prove current behavior. Revalidate material facts; preserve historical snapshots and update only actively maintained overviews.

## 7. Deliver the result

Match output size to analysis depth. For focused/full work, report:

- target version/build/hash and conclusion with compact mechanic pseudocode;
- stable source/function or module + RVA locators;
- supporting evidence, validation state, material unknowns, and observed versus inferred details;
- material analysis-workspace refinements written or proposed;
- retained note/snapshot paths, build/coverage scope, gaps, and revalidation assumptions, when applicable.

For downstream application, pass only material version-scoped facts to $apply-game-logic. A sufficiently complete finding is already a valid handoff; no extra format conversion is required.

## Completion

For triage, stop when the requested identity/location is version-scoped, evidence-backed, and distinguishable from nearby candidates; do not reconstruct unrelated semantics.

For focused/full work, verify that conclusions are version-scoped; material unknowns are explicit and confidence matches evidence; required practical runtime validation was performed or identified as missing; and next-step facts are present. Any workspace annotations must remain evidence-backed, uncertainty-preserving, and non-destructive.
