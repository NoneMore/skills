# Gameplay Semantic Model

Use this reference for focused/full analysis of a gameplay mechanic. The unit of
analysis is the **mechanic**, not an individual function, address, script, bundle,
or decompiler view. Engine adapters map their concrete lifecycle and runtime
conventions onto this model.

Do not force every mechanic through every stage. Mark a stage `not applicable`
when evidence shows it is absent, and `unknown` when it has not yet been
resolved.

## 1. Define the mechanic in player-observable terms

Start from the behavior the player can reproduce or observe, for example:

- taking damage grants temporary invulnerability;
- an attack sometimes becomes a critical hit;
- a cooldown advances while playing but stops while paused;
- an item modifies a derived stat until unequipped;
- a checkpoint preserves some state but resets other state.

Record the reproduction path and the observable outcome before collapsing the
question into implementation details. A function name such as `Update`,
`Tick`, or `Step` is not a mechanic definition.

## 2. Reconstruct the semantic chain

Use this chain as the default mechanic skeleton:

```text
Trigger
  -> Eligibility / Preconditions
  -> Input state
  -> Computation / Rule
  -> Randomness (when applicable)
  -> Authoritative state mutation
  -> Secondary gameplay effects
  -> Presentation
  -> Persistence / Reset / Lifetime
```

For each material stage, record:

- the owning object/module/system;
- the event, function, script, table, or call path that implements it;
- the important inputs and outputs;
- the relevant time domain;
- the authority boundary;
- the lifetime/reset conditions;
- the evidence that supports the interpretation.

A UI read, animation, sound, combat-log entry, or localization string may expose
a mechanic without owning the authoritative state mutation. Conversely, a low-
level state write is not understood until its trigger, eligibility, and lifetime
are known.

## 3. Cross-engine gameplay primitives

Use these primitives to decide what evidence matters. They are gameplay
semantics, not engine-specific ABI rules.

### Time and scheduling

Determine which clock advances the mechanic:

- render frames;
- simulation/fixed ticks;
- variable delta time;
- wall clock / monotonic time;
- alarms/timers/coroutines/tasks;
- animation frames or event counts.

Establish pause, slow-motion/time-scale, loading, cutscene, background-tab, and
scene/room-transition behavior before converting counters to seconds.

### State machines and transitions

Identify states, transition predicates, entry/exit effects, interrupt paths,
fallback/default states, and reset conditions. Trace both the transition that
enters a state and the path that leaves or expires it.

### Stats, formulas, and modifiers

Recover the order of operations, not only the final constant:

```text
base
  -> additive modifiers
  -> multiplicative modifiers
  -> conditional modifiers
  -> clamp / quantization / rounding
  -> derived value
```

Audit difficulty, equipment, skills/perks, buffs/debuffs, level scaling, global
modifiers, and source-specific overrides when they can share the same formula.

### Randomness

Identify the RNG source/stream, seed or state when available, range mapping,
roll site, comparison, rerolls, luck/bias modifiers, and the conditions under
which a roll is skipped or repeated. A displayed percentage does not by itself
establish the effective runtime probability.

### Entity and object lifecycle

Map creation/spawn, initialization, activation, update, disable/death/despawn,
pooling/reuse, and destruction. Determine whether state belongs to an entity,
component, world/scene, singleton/global store, or transient event object.

### Events, input, and dispatch

Trace the path from input/event source to gameplay handler and any secondary
events. Distinguish direct calls from queued/deferred events and identify
ordering when it changes semantics.

### Persistence and reset

Determine what survives checkpoint, death, room/scene change, save/reload,
new-game/reset, and version migration. Separate runtime state from serialized
state and from defaults reconstructed during load.

### Authority and prediction

Record where the authoritative value is computed. For local/offline games this
may simply be the local simulation owner. For network-capable code, distinguish
local prediction, presentation, serialization, received state, and authoritative
simulation. Do not infer unavailable server logic from a client prediction path.

### Presentation separation

Separate state-changing logic from UI, HUD, draw/render, VFX, SFX, animation,
localization, and telemetry. Presentation can be a useful semantic anchor but is
not evidence of mechanic ownership unless data flow shows that it mutates the
authoritative state.

### Physics and spatial rules

When material, identify the physics/update domain, collision/query source,
coordinate/unit conventions, integration step, and whether the mechanic is
implemented in engine physics callbacks or custom simulation code.

## 4. Mechanic-first tracing procedure

1. State the mechanic and reproduction path in gameplay terms.
2. Select the relevant primitives above; do not investigate unrelated engine
   subsystems.
3. Find the trigger and likely state owner. Trace forward toward authoritative
   mutation and backward from observed state consumers when that is faster.
4. Recover eligibility, inputs, formula/transition/RNG, and the exact mutation.
5. Audit secondary sources and shared paths so one caller or event is not
   mistaken for the whole mechanic.
6. Resolve lifetime, reset, time-domain, and persistence behavior that can change
   the player's observed result.
7. Separate presentation from state ownership and record the authority boundary.
8. Express the result as concise gameplay pseudocode plus implementation
   locators, then apply the evidence protocol from `SKILL.md`.

Prefer a small complete mechanic slice over a broad call graph that does not
explain the behavior.

## 5. Compact mechanic record

A focused finding or report can use this shape:

```text
Mechanic:
Reproduction:
Trigger:
Eligibility:
Inputs:
Computation / transition:
RNG:
Authoritative mutation:
Secondary gameplay effects:
Presentation:
Time domain:
Entity/state owner:
Persistence / reset:
Authority:
Implementation locators:
Validation:
Unknowns / version sensitivity:
```

Omit genuinely irrelevant fields, but do not silently omit unresolved fields
that could change the interpretation.

## 6. Completion criteria

Before calling a mechanic understood, verify as applicable that:

- the trigger reaches the claimed authoritative mutation;
- eligibility and source-specific branches are accounted for;
- units, update rates, and time scaling are established;
- formulas include modifier order, clamping, and rounding that affect outcomes;
- RNG claims include the roll source and effective conditions;
- state ownership and entity/object lifetime are known;
- death, pause, loading, scene/room change, and save/reload behavior are resolved
  when they can affect the mechanic;
- presentation-only paths are not mistaken for state-changing paths;
- authority/prediction boundaries are explicit;
- the implementation locators and evidence are version-scoped and reproducible.

The mechanic model complements the generic evidence/provenance rules. It does
not replace independent validation, version/hash binding, or engine-specific
runtime knowledge.
