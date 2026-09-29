---
name: apply-game-logic
description: Apply previously recovered, version-scoped gameplay logic to authorized offline/single-player targets. Use to design or validate local gameplay changes, mods, runtime instrumentation, calculators, simulators, reference implementations, or other tooling that consumes known mechanic logic. Requires explicit handling of confidence, ownership/fan-out, units, authority, version guards, and rollback. Use $analyze-game-logic when material mechanic facts are missing. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v1.0.0"
---

# Apply Game Logic

Consume recovered gameplay knowledge instead of rediscovering it. Treat a
version-scoped mechanic record or reusable finding as the input contract and the
requested application as the output. Re-enter `$analyze-game-logic` only for a
specific material fact that the application cannot safely or correctly proceed
without.

## 1. Establish the application boundary

Expected input is an authorized offline/local target, a concrete downstream goal,
and either a mechanic handoff record, reusable finding, or enough verified
implementation detail to construct one.

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

Before implementing anything, identify which mechanic facts are material to the
requested result. Check the supplied record/finding for:

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

For generated tools or derived models, record the mechanic finding/version they
were derived from and the assumptions added by the application.

For runtime hooks, writes, injected instrumentation, mods, or patches, record:

- exact target version/build/hash and stable locator;
- authoritative source for the generated change or instrumentation;
- original/control value, bytes, file content, or behavior when applicable;
- applied value, bytes, file content, or behavior;
- expected scope and known shared-use risks;
- cleanup, disable, or restoration procedure.

Reversibility is necessary for many local interventions but does not establish
narrow scope or correctness by itself.

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
- deployed changes/instrumentation have authoritative provenance and a documented
  cleanup/restoration path;
- validation tests the claimed application scope rather than only the happy path;
- any contradiction in the underlying mechanic model is returned to
  `$analyze-game-logic` instead of patched around by guesswork.
