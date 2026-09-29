# Mechanic Handoff Protocol v1

This file is the standalone application-side copy of the versioned
`game-logic-mechanic-handoff/v1` protocol. It is execution-critical for
`apply-game-logic`; do not require a sibling skill directory to read or validate
this format.

Within this repository, this protocol must remain semantically identical to the
v1 handoff defined by the analysis producer. Any incompatible field or meaning
change requires a new schema identifier rather than silently changing v1.

## Schema

Keep every top-level key. Use `not-applicable` for genuinely irrelevant
dimensions and `unknown` when an unresolved value could affect interpretation
or downstream scope.

```yaml
schema: game-logic-mechanic-handoff/v1
mechanic: <behavior/mechanic name>
target:
  game_version: <version or unknown>
  build_id: <build id or unknown>
  material_hashes: [<path/module=sha256>, ...]
status: confirmed | working-hypothesis | unknown
reproduction_or_scenario: <steps/condition or not-applicable>
source_or_trigger: <source/trigger or unknown>
eligibility_or_gate: <gate or not-applicable>
inputs_modifiers_rng: <ordered inputs/modifiers/RNG detail or not-applicable>
rule_or_transition: <concise mechanic pseudocode / transition>
authoritative_mutation: <state mutation or unknown>
secondary_effects_or_consumers: <effects/consumers or not-applicable>
time_units_scheduling: <units/scheduler/pause behavior or not-applicable>
state_owner_lifetime_fanout: <owner/lifetime/sharing or unknown>
persistence_or_reset: <reset/persistence behavior or not-applicable>
authority_or_serialization: <authority/serialization or not-applicable>
presentation: <presentation-only relation or not-applicable>
implementation_locators: [<source/function or module + RVA>, ...]
evidence:
  finding_ids: [<finding-id>, ...]
  source_or_artifact_refs: [<source/artifact id + locator>, ...]
validation:
  performed: <yes/no/partial>
  summary: <independent check / runtime observation / reason omitted>
unknowns: [<material unknown>, ...]
version_sensitivity: <known sensitivity or unknown>
```

The handoff status is the status of the application-relevant claim. Do not
silently replace a material unknown with `not-applicable`, and do not add
application-specific provenance fields to this mechanic schema.

## Finding normalization

A reusable finding is upstream evidence, not the application interface. Normalize
an active `confirmed`, `working-hypothesis`, or `unknown` finding into the
schema above before application.

A `superseded` finding is never consumable. Follow its `Superseded by`
reference, verify that the successor exists and matches the target/version needed
by the request, and normalize the active successor. If no valid successor is
available, return that narrow dependency to analysis instead of producing a
handoff from stale evidence.
