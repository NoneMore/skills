# Durable Application Artifacts

Use the existing game-logic project store as the authoritative durable store for
application work. Do **not** create a second application manifest.

The store defined by
`../../analyze-game-logic/references/project-knowledge.md` remains authoritative:
`artifacts/manifest.json` inventories retained outputs and
`notes/findings/` holds the recovered mechanic evidence that the application
consumes.

## When this record is required

Create a durable application record whenever the output must survive the current
session, including a deployed mod/patch/hook/instrumentation file, a reusable
calculator/simulator, or any change whose rollback/provenance must be recoverable
later.

A throwaway explanation or non-retained calculation does not require a durable
application record.

## Storage convention

Use:

```text
artifacts/applications/<application-id>/record.md
artifacts/applications/<application-id>/<authoritative source/config/tool files>
artifacts/applications/<application-id>/<validation logs when retained>
```

Register the record itself in the existing manifest with kind
`gameplay-application-record`. Register every authoritative generated source,
configuration, patch description, backup, or validation artifact that is required
to reproduce or undo the application. Link those manifest entries to the finding
IDs consumed by the application through `finding_refs`.

The installed/deployed copy inside the game tree is never the authoritative
source.

## Application record

Use this exact minimum structure:

```markdown
# <Application title>

- ID: `<stable-id>`
- Status: `active | superseded`
- Target: `<game version/build, material hashes>`
- Handoff schema: `game-logic-mechanic-handoff/v1`
- Consumes findings: `<finding IDs or none>`
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

For destructive changes, persist the original bytes/content or an integrity-
verified backup artifact **before** modifying the installed target.

## Later-session recovery check

A later session must be able to:

1. run `project_store.py verify`;
2. locate the active `gameplay-application-record`;
3. identify the exact mechanic finding/handoff and target build it consumed;
4. locate the authoritative implementation and original/control artifacts; and
5. execute the documented rollback without relying on conversational memory.

If any of these cannot be reconstructed from the project store, provenance and
rollback are incomplete.
