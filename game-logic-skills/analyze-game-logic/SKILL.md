---
name: analyze-game-logic
description: Recover and verify authorized offline/single-player game logic with reproducible evidence. Use when a mechanic, formula, state transition, timing rule, RNG path, ownership boundary, or implementation locator is unknown or stale, including cold-start requests that later feed $apply-game-logic. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v5.2.2"
---

# Analyze Game Logic

Recover the smallest version-scoped mechanic slice that answers the user's question. Keep narrow lookup questions narrow. Do not add persistence, runtime work, or binary analysis unless the question needs them.

This skill produces mechanic knowledge. For downstream requests, use the desired outcome only to determine which mechanic facts are material. Pass the recovered version-scoped facts to $apply-game-logic; do not choose the change mechanism here.

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
- **Full analysis:** preserve enough baseline, evidence, and validation for multi-session or high-cost work.

Promote work when the current task already requires cross-session continuation, the user asks to retain results, evidence is expensive or lossy to reconstruct, or downstream application needs a durable reference. When durable storage applies, use [references/project-knowledge.md](references/project-knowledge.md).

## 3. Find the material implementation path

Start with cheap semantic evidence: readable configuration/source, strings, symbols, RTTI/reflection, imports, resources, file layout, metadata, and existing analysis projects.

Treat implementation layers as a search progression. Before escalating into a more opaque boundary, identify the unresolved fact and establish either:

- positive transition evidence showing the readable path terminates at that boundary; or
- a bounded search showing the relevant readable layers do not contain the required relation.

Stay at source/script level when it can answer the question. Prefer targeted functions and data-flow slices over broad decompilation.

If a tool explicitly reports truncated output or only a partial range was inspected, treat that view as partial. Do not make a conclusion that depends on complete coverage until the required missing range has been checked; expand coverage only when the claim actually needs completeness.

After the material boundary is known, consult [references/engine-registry.md](references/engine-registry.md) and load only the adapter needed for that boundary.

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

For compiled/native boundaries, prefer stable module + RVA locators and verify address conversions against the original binary or loaded module before relying on them.

## 5. Close the evidence loop

Use three states:

- **Confirmed:** semantic evidence supports the claim and any material independent check has been satisfied.
- **Working hypothesis:** plausible, but a material independent check or runtime validation is still missing.
- **Unknown:** a fact that can change the interpretation remains unresolved.

Different renderings of the same relation are not independent evidence. Cross-references show association, not gameplay semantics.

Runtime validation is optional for narrow identity/location claims. When timing, causal control, caller discrimination, state lifetime, authority, or effective randomness materially depends on runtime behavior, load [references/runtime-validation.md](references/runtime-validation.md). If practical validation is omitted, keep the affected claim a working hypothesis.

## 6. Retain only what earns persistence

Do not create a project store for throwaway lookups. Preserve evidence when the user asks to retain it, cross-session continuation is already required, or the evidence is expensive or lossy to reconstruct.

When durable storage applies, [references/project-knowledge.md](references/project-knowledge.md) is authoritative for what to retain. Prefer the bundled helper for mechanical hashing/integrity operations, and use its current --help instead of copying its command surface into this skill.

## 7. Deliver the result

Match output size to the analysis depth. For focused/full analysis, include:

- target version/build/hash scope;
- the conclusion and compact mechanic pseudocode;
- stable source/function or module + RVA locators;
- evidence and validation state;
- material unknowns and observed-versus-inferred distinctions;
- material analysis-workspace refinements written or proposed, when applicable.

When downstream application is requested, provide a compact version-scoped mechanic record containing the facts material to that application. A reusable finding with sufficient facts is valid input to $apply-game-logic; do not normalize it through an extra protocol step solely for ceremony. Existing game-logic-mechanic-handoff/v1 records remain valid compatibility inputs.

## Completion

Before finishing focused/full work, verify that the claimed behavior is version-scoped, material unknowns are explicit, confidence matches the evidence, required practical runtime validation was not silently skipped, and the output contains enough mechanic detail for the user's next step without unrelated workflow machinery. When static-analysis refinement applied, verify that its annotations remain evidence-backed, uncertainty-preserving, and non-destructive.
