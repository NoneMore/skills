---
name: apply-game-logic
description: Apply an already-recovered, version-scoped gameplay mechanic to an authorized offline/single-player target. Use when a canonical mechanic handoff already exists; route cold-start or finding-only requests through companion $analyze-game-logic first. Supports derived tooling, instrumentation, mods, and scoped local changes while preserving confidence, version, ownership/fan-out, provenance, and rollback. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v1.0.0"
---

# Apply Game Logic

Consume recovered gameplay knowledge instead of rediscovering it. This skill
activates on an existing version-scoped `game-logic-mechanic-handoff/v1`.
A cold-start request, or a request that supplies only reusable findings, routes
through companion `$analyze-game-logic` first so that one canonical handoff is
emitted before application begins.

This is an explicit Skill-level composition dependency, not a filesystem
dependency. Invoke the companion by canonical skill name; never read, shell out
to, or otherwise depend on a sibling skill's directory layout. If the companion
is unavailable when normalization, missing mechanic knowledge, or durable
project-store registration is required, report that dependency instead of
emulating it from sibling files.

## 1. Establish the application boundary

Expected input is an authorized offline/local target, a concrete downstream goal,
and an existing canonical `game-logic-mechanic-handoff/v1`. A reusable finding
is upstream evidence, not direct application input: ask `$analyze-game-logic`
to normalize the active finding(s) and emit the handoff before entering this
workflow.

Supported application classes include:

- deriving calculators, tables, simulators, reference implementations, or test
  harnesses from recovered formulas and transitions;
- adding reversible observation or instrumentation around a known mechanic;
- designing, applying, or validating a local gameplay change or mod;
- converting stable locators and mechanic knowledge into version-guarded tooling.

Do not manipulate multiplayer state, matchmaking, leaderboards,
server-authoritative state, another player's experience, accounts, credentials,
or online-service enforcement. Do not bypass DRM, payments, licensing, or
anti-cheat. Installed game files remain read-only unless the user explicitly
authorizes a destructive, version-specific local modification.

## 2. Validate the mechanic input before use

Before implementing anything, require the supplied input to identify itself as
`game-logic-mechanic-handoff/v1` and identify which fields are material to the
requested result. Unknown or unsupported schema versions return to the companion
producer rather than being guessed or locally migrated. Check the handoff for:

- target game/content version, build identity, and material file/module hashes;
- claim status and evidence/validation state;
- source/trigger and authoritative mutation when causality matters;
- formula order, clamps, rounding, RNG mapping, units, and timing when numeric
  behavior matters;
- state owner, lifetime, persistence/reset rules, and fan-out when scope matters;
- authority/serialization when local versus external control matters;
- stable source/function or `module + RVA` locators when code/data will be
  addressed directly.

A **Confirmed** fact may be consumed as established within its recorded scope.
A **Working hypothesis** may support a clearly labeled experiment, prototype, or
validation harness, but must not be silently treated as a safe production
assumption. An **Unknown** that can change correctness, target scope, or safety is
a stop condition for that application path.

A reusable finding marked **superseded** is never direct input to this skill.
When a finding-only request is received, companion `$analyze-game-logic` owns
successor resolution and handoff emission. Apply never maps finding lifecycle
states into handoff status itself.

When a material fact is missing, invoke or hand back to `$analyze-game-logic`
with the narrow unresolved question. Do not restart broad reverse engineering and
do not infer the missing fact from names, raw addresses, or convenience.

## 3. Choose the smallest application that satisfies the goal

Preserve the recovered mechanic semantics exactly before optimizing convenience.

### Derived logic and tooling

For calculators, simulators, reference implementations, tables, or tests:

1. Preserve operation order, units, clamps, quantization/rounding, RNG range
   mapping, skipped/repeated-roll conditions, and state preconditions.
2. Separate facts recovered from the target from assumptions introduced by the
   derived tool.
3. Prefer a small pure function/state-transition model when it can represent the
   requested behavior.
4. Include version/source provenance so the derived result is not mistaken for a
   version-independent rule.

### Runtime observation

For logging, tracing, or instrumentation that does not intentionally change the
gameplay outcome:

1. Observe the smallest stable boundary that answers the question.
2. Avoid introducing alternate timing, mutation, or fan-out that changes the
   mechanic being observed.
3. Keep setup and cleanup explicit and reversible.
4. Record exactly which recovered locator or finding the instrumentation relies
   on.

### Gameplay changes

When the requested result intentionally changes local gameplay behavior, load
[references/change-design.md](references/change-design.md). Establish behavioral
scope before choosing an implementation mechanism, then prefer the least invasive
acceptable mechanism.

## 4. Bind implementation to recovered evidence

Every generated application must state what recovered knowledge it consumes.

For source/script/config targets, prefer semantic locators such as module,
function, key, or definition plus a target hash when material. For native
targets, prefer stable `module + RVA` locators and independently verify
VA/RVA/file-offset/runtime-address conversions before writing or hooking.

Do not rely on a raw runtime address across launches or builds. If a signature or
pattern is used for relocation, verify that it resolves uniquely and still maps
to the recovered semantic site.

If the target version/hash differs from the mechanic record, treat the record as
stale until the material relation is revalidated by `$analyze-game-logic`.
Version similarity alone is not sufficient.

## 5. Validate the application result

Validation answers a different question from mechanic recovery: not "is this how
the game works?" but "did this application preserve or change the recovered
mechanic exactly as intended?"

Use the smallest comparison that can expose failure:

- for calculators/simulators, compare known boundary cases and representative
  states against the recovered formula or controlled target observations;
- for instrumentation, verify that observation does not alter the relevant
  state-transition result or timing beyond documented limits;
- for gameplay changes, compare control and modified behavior and test only edge
  cases that can reveal scope leakage, such as other actors/sides, alternate
  event sources, pause/death/loading, scene transitions, save/reload, or
  difficulty/state variants.

A successful result in one scenario proves only that scenario unless the claimed
scope is independently evidenced. If validation exposes a mismatch in the
underlying mechanic model, stop application work on that assumption and return
the discrepancy to `$analyze-game-logic`.

## 6. Preserve provenance and rollback

For non-retained explanations or calculations, report provenance in the answer.
For any reusable or deployed output whose provenance/rollback must survive the
session, load
[references/application-artifacts.md](references/application-artifacts.md) and
reuse the existing game-logic project store. Do not create a second application
manifest.

Persist the exact normalized handoff first as a registered immutable
`gameplay-mechanic-handoff` artifact, then persist a registered
`gameplay-application-record` derived from that snapshot plus every
authoritative source/config/backup/validation artifact required to reproduce or
undo the application.

Project-store mutation is a companion capability owned by
`$analyze-game-logic`. Ask that skill to perform the mechanical registration in
the existing game-logic store, including one-way consumed-finding dependencies;
do not locate or invoke its helper by sibling filesystem path.

For runtime hooks, writes, injected instrumentation, mods, or patches, the record
must capture:

- exact target version/build/hash and stable locator;
- the exact handoff artifact ID/hash consumed;
- authoritative source for the generated change or instrumentation;
- original/control value, bytes, file content, behavior, or registered backup;
- applied value, bytes, file content, or behavior;
- expected scope and known shared-use risks;
- validation results;
- cleanup, disable, or restoration procedure.

Reversibility is necessary for many local interventions but does not establish
narrow scope or correctness by itself. The installed/deployed copy is never the
authoritative source.

## 7. Deliver the application

Report:

- the mechanic finding/handoff consumed and its confidence state;
- the chosen application mechanism and why it is the smallest adequate one;
- generated code/config/patch/tooling or exact implementation steps;
- version and locator guards;
- validation performed and observed result;
- assumptions, unresolved dependencies, scope limitations, and rollback path.

Do not bury a newly discovered mechanic uncertainty inside implementation detail.
Surface it as an analysis dependency.

## 8. Completion criteria

Before finishing, verify that:

- every material mechanic dependency is present and confidence-scoped;
- no working hypothesis or unknown was silently promoted to confirmed;
- the target build/version matches the evidence consumed by the application;
- derived numeric/state logic preserves material order, units, rounding, RNG, and
  lifecycle semantics;
- gameplay changes have evidence for the claimed ownership/fan-out scope;
- native writes/hooks use verified stable locators rather than raw launch-specific
  addresses;
- destructive local modification occurred only with explicit authorization;
- reusable/deployed changes or tools retain the exact normalized handoff as an
  immutable verified artifact plus a durable application record, authoritative
  retained source, and documented cleanup/restoration path;
- validation tests the claimed application scope rather than only the happy path;
- any contradiction in the underlying mechanic model is returned to
  `$analyze-game-logic` instead of patched around by guesswork.
