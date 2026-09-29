# Gameplay Semantic Model

Use this reference for gameplay behavior and causality questions. The semantic unit is the mechanic, not a function, address, script, bundle, or decompiler view.

## Bound the mechanic

Prefer a player-observable behavior and reproduction path when one exists. Hidden/background systems are also valid when bounded by a controlled state transition or other evidence-backed condition.

A mechanic normally needs only the material part of this causal shape:

Source / Trigger
  -> Eligibility / Gate
  -> Rule / Transition
  -> Authoritative state mutation

Inputs, modifiers, RNG, scheduling, and secondary effects attach where evidence shows they belong. Do not impose a generic pipeline.

Resolve cross-cutting dimensions only when they can change the claim:

| Dimension | Material questions |
| --- | --- |
| Time | clock/scheduler, units, pause or time-scale behavior |
| State | owner, sharing/fan-out, creation, reuse, lifetime |
| Ordering | direct vs queued/deferred execution, order-sensitive paths |
| Persistence | death/checkpoint/scene/save/reset behavior |
| Authority | where state is computed, serialized, sent, or received |
| Presentation | UI/render/VFX/SFX/localization versus gameplay ownership |
| Physics/spatial | update domain, collision/query source, units/coordinates |

For formulas include material clamps, quantization, and rounding. For randomness identify the source/stream, range mapping, comparison, rerolls/bias, and skipped or repeated rolls when relevant.

## Close the slice

A mechanic slice is complete enough for a claim when the material trigger reaches the claimed authoritative mutation and every dimension that could change the result is either resolved or explicitly unknown.

Prefer concise gameplay pseudocode plus stable implementation locators over a broad call graph.

## Downstream mechanic record

When another task will consume the result, pass only the facts material to that task. A current reusable finding is sufficient when it already contains them.

A compact record usually contains:

- mechanic/behavior;
- target version/build and material hashes;
- status: confirmed, working hypothesis, or unknown;
- rule/transition pseudocode;
- material trigger/gate and authoritative mutation;
- material units/timing/RNG details;
- material owner/lifetime/fan-out/persistence/authority details;
- stable implementation locators;
- evidence/validation summary;
- material unknowns and version sensitivity.

Do not add empty fields for dimensions that do not matter.

For compatibility, existing records identified as game-logic-mechanic-handoff/v1 remain valid application inputs. Consumers should validate the material facts they need rather than requiring an exact top-level shape or forcing a new normalization pass.
