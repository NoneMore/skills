# Durable Application Artifacts

Use one game-logic project store for durable application work. This skill ships
its own `scripts/project_store.py`; it must not require a sibling skill directory
at runtime.

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

## Storage convention

Use:

```text
artifacts/applications/<application-id>/mechanic-handoff-v1.yaml
artifacts/applications/<application-id>/record.md
artifacts/applications/<application-id>/<authoritative source/config/tool files>
artifacts/applications/<application-id>/<validation or backup artifacts>
```

### 1. Persist the normalized handoff snapshot first

Persist the exact normalized `game-logic-mechanic-handoff/v1` input as
`mechanic-handoff-v1.yaml` before producing durable application outputs.
Register it with `scripts/project_store.py add-artifact` using kind
`gameplay-mechanic-handoff`. The manifest's SHA-256 makes this the immutable
input snapshot for the application even when the handoff came from outside the
project and has no reusable finding.

If the handoff was normalized from reusable findings, register those as one-way
dependencies with `--consumes-finding-ref <finding-id>`. This populates
`consumes_finding_refs`; it **must not** populate `finding_refs` or modify the
finding's `## Evidence` section.

`finding_refs` keeps its existing meaning: an artifact/source is evidence *for*
a finding and therefore participates in reciprocal Evidence links.
`consumes_finding_refs` means the artifact was derived *from* a finding and is
one-way only.

### 2. Persist the application record and implementation

Register `record.md` as kind `gameplay-application-record` with
`--derived-from <handoff-artifact-id>`. Register every authoritative generated
source, configuration, patch description, backup, or validation artifact required
to reproduce or undo the application. Use `derived_from` to link generated
artifacts to the handoff/application record as appropriate.

Do not use `--finding-ref` merely because an application consumed a finding.

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

## Helper integrity rules

The bundled `scripts/project_store.py` validates file size/hash, artifact/source
references, and the two distinct finding relations:

- `finding_refs`: reciprocal evidence relation;
- `consumes_finding_refs`: one-way dependency whose finding must exist and whose
  artifact must not appear in that finding's Evidence section.

Run both:

```text
python scripts/project_store.py verify --root <project-root>
python scripts/project_store.py check-links --root <project-root>
```

before later reuse or rollback.

## Later-session recovery check

A later session must be able to:

1. verify the project store;
2. locate the active `gameplay-application-record`;
3. resolve its exact immutable `gameplay-mechanic-handoff` artifact and SHA-256;
4. follow any one-way `consumes_finding_refs` without treating application
   artifacts as evidence for those findings;
5. identify the exact target build plus authoritative implementation and
   original/control artifacts; and
6. execute the documented rollback without relying on conversational memory.

If any of these cannot be reconstructed from the project store, provenance and
rollback are incomplete.
