# Gameplay Semantic Model

Use this reference as the canonical semantic model for focused/full analysis of a
gameplay mechanic. The unit of analysis is the **mechanic**, not an individual
function, address, script, bundle, or decompiler view. Engine adapters map
concrete runtime constructs onto this model.

Do not force every mechanic through every field. Omit elements that are genuinely
irrelevant, and mark unresolved elements `unknown` when they could change the
interpretation.

## 1. Define the mechanic

Prefer a player-observable behavior and reproduction path when one exists. Hidden
or background systems are still mechanics when they can be bounded by a
reproducible or controlled scenario, system event, state transition, or other
evidence-backed condition.

Useful definitions include:

- taking damage grants temporary invulnerability;
- a cooldown advances during play but stops while paused;
- an AI director changes spawn pressure after a hidden threshold;
- a checkpoint preserves some state but resets other state.

Record the observable behavior when available; otherwise record the controlled
scenario, trigger/source, relevant state conditions, and expected evidence. A
function name such as `Update`, `Tick`, or `Step` is not a mechanic
definition.

## 2. Canonical mechanic model

Treat this as a coverage/decomposition model, not a fixed execution pipeline.
Real mechanics may branch, interleave, repeat, short-circuit, or run
asynchronously.

Recover the material causal core:

```text
Source / Trigger
  -> Eligibility / Gate
  -> Rule / Transition
  -> Authoritative state mutation
```

Inputs, modifiers, and RNG may feed the rule/transition. Secondary gameplay
effects and presentation are usually consumers or branches of the resulting
state rather than fixed terminal stages.

Resolve these cross-cutting dimensions when they can change the interpretation:

- time domain and scheduling;
- entity/state ownership and lifecycle;
- event ordering and deferred dispatch;
- persistence, reset, and reload behavior;
- authority, prediction, and serialization boundaries;
- presentation and other observers/consumers;
- physics/spatial rules when material.

For each material part, retain the implementation locator and evidence supporting
the interpretation. A UI read, animation, sound, combat-log entry, or
localization string may expose a mechanic without owning its authoritative state.
Likewise, a low-level state write is not fully understood when its trigger,
ownership, or lifetime remains material and unresolved.

## 3. Cross-engine primitives

### Time and scheduling

Determine which clock advances the mechanic: render frames, simulation/fixed
ticks, variable delta time, wall/monotonic time, alarms/timers/coroutines/tasks,
animation frames, event counts, or another scheduler. Establish pause,
time-scale, loading, cutscene, background, and scene/room-transition behavior
before converting counters to seconds.

### State, formulas, and randomness

For state machines, identify transition predicates, entry/exit effects,
interrupt paths, and reset conditions.

For formulas, recover the evidence-backed order of operations, including
material modifiers, clamping, quantization, and rounding. Do not infer a generic
modifier order.

For randomness, identify the RNG source/stream, roll site, range mapping,
comparison, rerolls or bias modifiers, and conditions under which a roll is
skipped or repeated. A displayed percentage does not establish the effective
runtime probability by itself.

### Ownership, lifecycle, and dispatch

Determine whether state belongs to an entity/component, world/scene,
singleton/global store, transient event object, worker, local server, or another
owner. Map creation/spawn, initialization, activation, update,
disable/death/despawn, pooling/reuse, and destruction when they affect lifetime.

Trace material input/events to their gameplay handlers. Distinguish direct calls
from queued/deferred dispatch and establish ordering when it changes semantics.

### Persistence, authority, and presentation

Separate runtime state from serialized state and defaults reconstructed during
load. Determine what survives death, checkpoint, scene/room transitions,
save/reload, new-game/reset, or version migration when material.

Record where the authoritative value is computed. For network-capable code,
distinguish local prediction, presentation, serialization, received state, and
authoritative simulation; do not infer unavailable server implementation from a
client prediction path.

Separate gameplay state changes from UI/HUD, draw/render, VFX, SFX, animation,
localization, and telemetry unless data flow proves those paths also own the
mutation.

### Physics and spatial rules

When material, identify the physics/update domain, collision/query source,
coordinate/unit conventions, integration step, and whether the mechanic is
implemented in engine callbacks or custom simulation code.

## 4. Trace and close the mechanic

1. Define the observable behavior or controlled scenario.
2. Select only the semantic primitives material to the question.
3. Find the trigger/source and likely state owner; trace forward toward the
   authoritative mutation and backward from consumers when useful.
4. Recover the relevant gate, inputs/modifiers/RNG, rule/transition, and exact
   mutation.
5. Audit materially distinct callers/sources so one event is not mistaken for
   the whole mechanic.
6. Resolve time, lifetime, reset/persistence, authority, event ordering, and
   presentation only where they can change the result or the interpretation.
7. Express the result as concise gameplay pseudocode plus implementation
   locators, then apply the evidence and validation protocol from `SKILL.md`.

A mechanic is complete enough for the claim when the material trigger reaches
the claimed authoritative mutation; relevant source-specific branches, units,
timing, state ownership/lifetime, persistence/reset, authority, and presentation
boundaries are either resolved or explicitly unknown; and the supporting
locators/evidence are version-scoped and reproducible.

Prefer a small complete mechanic slice over a broad call graph that does not
explain the behavior.

## 5. Compact mechanic record

A focused finding or report can use this shape:

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
Entity/state owner and lifetime:
Persistence / reset:
Authority / serialization:
Presentation:
Implementation locators:
Validation:
Unknowns / version sensitivity:
```

Omit genuinely irrelevant fields, but do not silently omit unresolved fields
that could change the interpretation.

This model complements the generic evidence/provenance rules. It does not replace
independent validation, version/hash binding, or engine-specific runtime
knowledge.
