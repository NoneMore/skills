# Durable Application Artifacts

Use the existing game-logic project store for durable application work. The store
capability is owned by companion `$analyze-game-logic`; this skill defines the
application-side records and asks the companion to perform mechanical
registration/verification by canonical Skill invocation.

Do not locate, read, or invoke a helper through a sibling filesystem path.

The store layout remains:

- `artifacts/manifest.json`: integrity/provenance inventory;
- `notes/findings/`: reusable mechanic findings when available;
- `reports/analysis.md`: optional analysis/report navigation.

Application artifacts live under the same project root. The installed/deployed
copy inside the game tree is never authoritative.

## When this record is required

Create a durable application record whenever the output must survive the current
session, including a deployed mod/patch/hook/instrumentation file, a reusable
calculator/simulator, or any change whose rollback/provenance must be recoverable
later.

A throwaway explanation or non-retained calculation does not require a durable
application record.

If the companion store capability is unavailable when durable retention is
required, report that dependency and do not claim durable provenance/rollback.

## Storage convention

Use:

```text
artifacts/applications/<application-id>/mechanic-handoff-v1.yaml
artifacts/applications/<application-id>/record.md
artifacts/applications/<application-id>/<authoritative source/config/tool files>
artifacts/applications/<application-id>/<validation or backup artifacts>
```

### 1. Persist the normalized handoff snapshot first

Persist the exact `game-logic-mechanic-handoff/v1` input as
`mechanic-handoff-v1.yaml` before producing durable application outputs.

Ask companion `$analyze-game-logic` to register that file in the existing
project store as kind `gameplay-mechanic-handoff`. The manifested SHA-256 is
the immutable input snapshot even when the handoff came from outside the project
and has no reusable finding.

Treat a finding ID as local only when provenance establishes that the handoff
was emitted from the current project store, for example by the current
`$analyze-game-logic` flow or by an explicitly retained same-store handoff
artifact. Do not infer locality merely because the same ID string resolves in the
current store.

For an externally supplied handoff, keep its `evidence.finding_ids` inside the
immutable hashed handoff snapshot by default. Materialize a one-way
`consumes_finding_refs` edge only when same-store origin is established.
External finding IDs must not block durable registration, even when an unrelated
same-named finding exists in the current store.

For locally proven consumed findings, ask the companion to record
`consumes_finding_refs`. This must not populate `finding_refs` or modify any
finding's `## Evidence` section.

`finding_refs` means an artifact/source is evidence *for* a finding.
`consumes_finding_refs` means an artifact was derived *from* a finding whose
current-store origin is established. These relations must never be conflated.

### 2. Persist the application record and implementation

Ask companion `$analyze-game-logic` to register `record.md` as kind
`gameplay-application-record`, derived from the handoff artifact. Register every
authoritative generated source, configuration, patch description, backup, or
validation artifact required to reproduce or undo the application.

Provide the companion enough metadata to perform the operation without
reconstructing application intent:

- artifact path and stable ID;
- artifact kind and description;
- target version/build/module/hash/range metadata;
- producer/tool metadata;
- `derived_from` artifact IDs;
- source references when applicable;
- one-way consumed finding IDs only when same-store origin is established;
  keep external or origin-unknown finding IDs solely in the handoff snapshot.

Do not request reciprocal `finding_refs` merely because an application consumed
a finding.

## Application record

Use this exact minimum structure:

```markdown
# <Application title>

- ID: `<stable-id>`
- Status: `active | superseded`
- Target: `<game version/build, material hashes>`
- Input handoff: `artifact:<handoff-artifact-id>`
- Mechanism: `<config | runtime-data | hook | patch | derived-tool | other>`

## Intent and scope

<Requested outcome, actors/event sources/contexts in scope, and known exclusions.>

## Authoritative implementation

- `artifact:<artifact-id>`: <source/config/tool/patch definition and role>

## Control / original state

<Original value, bytes, file content reference, or observable behavior sufficient
to restore/control the target. For large originals, reference a registered
artifact instead of copying it here.>

## Applied / derived state

<Applied value/bytes/configuration or generated behavior, including stable
locators and version guards.>

## Validation

<Control-vs-application checks, scope checks, observed result, limitations.>

## Rollback / cleanup

<Exact disable, restore, or cleanup procedure using the authoritative artifacts
above.>

## Assumptions and unknowns

<Any remaining non-material assumptions or limitations.>
```

For destructive changes, persist the original bytes/content or an
integrity-verified backup artifact **before** modifying the installed target.

## Integrity rules

Before later reuse or rollback, ask companion `$analyze-game-logic` to perform
the project store's integrity verification and evidence/dependency link checks.

The companion store must enforce:

- `finding_refs`: reciprocal evidence relation;
- `consumes_finding_refs`: one-way dependency whose finding exists and whose
  consuming artifact does not appear in that finding's Evidence section;
- registered file size/hash and provenance references;
- artifact/source/supersession references.

## Later-session recovery check

A later session must be able to:

1. verify the project store through the companion capability;
2. locate the active `gameplay-application-record`;
3. resolve its exact immutable `gameplay-mechanic-handoff` artifact and SHA-256;
4. follow one-way `consumes_finding_refs` without treating application artifacts
   as mechanic evidence;
5. identify the exact target build plus authoritative implementation and
   original/control artifacts; and
6. execute the documented rollback without relying on conversational memory.

If any of these cannot be reconstructed from the project store, provenance and
rollback are incomplete.
