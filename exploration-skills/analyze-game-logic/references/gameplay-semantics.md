# Gameplay Semantic Model

Use this reference as the canonical semantic model when the core workflow calls
for gameplay-mechanic reconstruction. The unit of analysis is the **mechanic**,
not an individual function, address, script, bundle, or decompiler view. Engine
adapters map concrete runtime constructs onto this model.

## 1. Bound the mechanic

Prefer a player-observable behavior and reproduction path when one exists.
Hidden/background systems are equally valid when bounded by a reproducible or
controlled scenario, system event, state transition, or other evidence-backed
condition.

Record the behavior or scenario, trigger/source, and relevant state conditions.
A name such as `Update`, `Tick`, or `Step` is an implementation locator, not
a mechanic definition.

Do not force every mechanic through every field. Omit genuinely irrelevant
elements; mark an unresolved element `unknown` when it could change the
interpretation.

## 2. Semantic model

This is a coverage/decomposition model, not a presumed execution order. Real
mechanics may branch, interleave, repeat, short-circuit, or run asynchronously.

Recover the material causal core:

```text
Source / Trigger
  -> Eligibility / Gate
  -> Rule / Transition
  -> Authoritative state mutation
```

Inputs, modifiers, and RNG may feed the rule/transition. Recover their actual
data flow and operation order from evidence; do not impose a generic modifier or
RNG pipeline. Secondary gameplay effects and presentation are consumers or
branches unless data flow shows they also own authoritative mutation.

Resolve cross-cutting dimensions only when they can change the claim:

| Dimension | Resolve when material |
| --- | --- |
| Time / scheduling | clock or scheduler, units, pause/time-scale/loading behavior |
| State / lifecycle | owner, sharing/fan-out, creation/init, activation, pooling/reuse, death/despawn/destruction |
| Ordering / dispatch | direct vs queued/deferred events and order-sensitive execution |
| Persistence / reset | what survives death, checkpoint, scene/room transition, save/reload, reset/migration |
| Authority / serialization | where the value is computed; prediction, sent/received, serialized, authoritative state |
| Presentation | UI/HUD, render, VFX/SFX, animation, localization, telemetry vs gameplay ownership |
| Physics / spatial | update domain, collision/query source, units/coordinates, integration step |

For state machines, include material transition predicates, entry/exit effects,
interrupts, and reset conditions. For formulas, include material clamping,
quantization, and rounding. For randomness, identify the source/stream, roll
site, range mapping, comparison, rerolls/bias, and skipped/repeated-roll
conditions.

A UI read, animation, sound, log entry, or localization string may expose a
mechanic without owning its state. Likewise, a low-level state write is not
enough when trigger, ownership, lifetime, or authority is material and unresolved.

## 3. Trace and close

1. Select only the semantic parts material to the question.
2. Find the trigger/source and likely state owner, then trace the material path
   to the authoritative mutation; audit distinct callers/sources when needed.
3. Resolve cross-cutting dimensions only where they can alter the result or
   interpretation.
4. Express the result as concise gameplay pseudocode plus implementation
   locators, then apply the evidence/validation protocol from `SKILL.md`.

A mechanic slice is complete enough for a claim when the material trigger
reaches the claimed authoritative mutation and every material branch, unit,
timing rule, owner/lifetime, persistence/reset rule, authority boundary, and
observer boundary is either resolved or explicitly unknown. Supporting locators
and evidence must remain version-scoped and reproducible.

Prefer a small complete slice over a broad call graph that does not explain the
behavior.

## 4. Compact mechanic record

Use only the applicable fields:

```text
Mechanic:
Reproduction / controlled scenario:
Source / trigger:
Eligibility / gate:
Inputs / modifiers / RNG:
Rule / transition:
Authoritative mutation:
Secondary effects / consumers:
Time / scheduling:
Entity/state owner, lifetime, and fan-out:
Persistence / reset:
Authority / serialization:
Presentation:
Implementation locators:
Validation:
Unknowns / version sensitivity:
```

Do not silently omit an unresolved field that could change the interpretation.
This model complements, rather than replaces, the core evidence/provenance,
independent-validation, and version/hash rules.
