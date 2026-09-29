# Project Knowledge Stores

Use these stores for focused/full analysis, whenever triage produces retained
evidence or a conclusion worth reusing, and for durable downstream application
artifacts derived from those findings. Do not create them merely to answer a
throwaway location/identity question with no durable output.

## Contents

1. [Store layout](#store-layout)
2. [Complete baseline](#complete-baseline)
3. [Sources and artifacts](#sources-and-artifacts)
4. [Manifest schema](#manifest-schema)
5. [Reusable finding records](#reusable-finding-records)
6. [Deterministic project-store helper](#deterministic-project-store-helper)
7. [Persistence cadence](#persistence-cadence)
8. [Durable evidence chain](#durable-evidence-chain)

## Store layout

Use linked stores for durable analysis knowledge:

- `artifacts/manifest.json`: inventory, integrity, provenance, and lifecycle of
  registered original sources and retained generated artifacts.
- `notes/findings/<finding-id>.md`: reusable interpretations derived from that
  evidence.
- `reports/analysis.md`: concise synthesis and navigation entry point.

The writable analysis project root must be separate from, and must never be
inside, the installed game directory. Artifact paths are confined to the
analysis root. Original sources may remain outside it and are treated as
read-only references. Use lowercase, filesystem-safe stable IDs. Do not encode a
mutable confidence state in an ID.

`project_store.py init` creates all three directories, a schema-v2 manifest, and
a starter `reports/analysis.md`. It does not overwrite an existing report.

## Complete baseline

For focused/full analysis, record the baseline information material to the
conclusion so the target can be identified and the evidence can be reproduced:

- game/content version, storefront, and build identifier;
- executable or source path, relevant modules/files, architecture when
  applicable, and material file metadata;
- SHA-256 of every analyzed binary, source, or data file material to the claim;
- detected engine, scripting backend, and relevant implementation layers or
  compilation boundaries;
- existing analysis databases/projects, symbols, source maps, structured tool
  integrations, and prior analysis artifacts when material.

Distinguish runner/file versions from actual game-content versions. Preserve
conflicting version indicators instead of silently choosing one. Use explicit
`unknown` values when a material baseline field genuinely cannot be established.

## Sources and artifacts

Keep these concepts separate:

- **Source:** an original read-only target that analysis is about, such as a game
  executable, DLL, data file, directly readable JavaScript/Python/Lua/C# source,
  or another original file. A source may live outside the analysis root.
- **Artifact:** an analysis- or application-generated retained output, such as a
  decompilation, extracted function set, runtime log, trace, benchmark,
  reconstructed table, derived tool, patch/mod source, application record, or
  script output. Artifacts live under the project root. Deployed copies inside
  the installed game tree are never authoritative artifacts.

Do not copy an original readable source into `artifacts/` merely so findings can
cite it. Register the original source directly with its path, byte size, and
SHA-256. Create an artifact only when the generated output has independent value
for later analysis or is expensive/lossy to reproduce.

## Manifest schema

New projects use schema version 2:

```json
{
  "schema_version": 2,
  "project": "game-id",
  "sources": [],
  "artifacts": []
}
```

The helper still reads and validates v4.1/schema-v1 manifests. Registering the
first source upgrades a v1 manifest to v2 without rewriting existing artifacts.

### Source entry

A registered source uses this shape:

```json
{
  "id": "offline-index",
  "path": "C:/absolute/path/to/offline/index.html",
  "kind": "source-code",
  "description": "Original offline game page",
  "size": 456789,
  "sha256": "UPPERCASE_HEX_SHA256",
  "target": {
    "game_version": "unknown",
    "build_id": "unknown",
    "module": "offline/index.html",
    "module_sha256": "UPPERCASE_HEX_SHA256",
    "rva_or_range": "not-applicable"
  },
  "finding_refs": ["decision-roll-mechanic"],
  "status": "active"
}
```

Source paths are stored as absolute references because they are intentionally
outside the analysis root and may include parent-directory traversal relative to
the workspace. `verify` re-reads the source but never writes it. Valid source
states are `active` and `missing`.

### Artifact entry

Each retained artifact uses this shape:

```json
{
  "id": "decompile-player-update-1a2b3c",
  "path": "artifacts/v1.2_player_update_game+0x12340.json",
  "kind": "ida-decompilation",
  "description": "Complete decompilation of Player::Update",
  "size": 123456,
  "sha256": "UPPERCASE_HEX_SHA256",
  "producer": {
    "tool": "IDA Pro/Hex-Rays",
    "version": "9.x"
  },
  "target": {
    "game_version": "1.2",
    "build_id": "store-build-id-or-unknown",
    "module": "Game.exe",
    "module_sha256": "UPPERCASE_HEX_SHA256",
    "rva_or_range": "0x12340"
  },
  "derived_from": [],
  "source_refs": ["game-exe"],
  "finding_refs": ["player-update-contract"],
  "status": "active",
  "superseded_by": null
}
```

`derived_from` contains artifact IDs. `source_refs` contains registered source
IDs. Use explicit `unknown` or `not-applicable` values when metadata genuinely
cannot be established. Do not omit uncertainty. Valid artifact lifecycle states
are `active`, `superseded`, and `missing`.

Before reuse, recompute size and SHA-256. On mismatch, stop using the source or
artifact as evidence until intentional regeneration/change is distinguished from
corruption or version drift. If intentional artifact regeneration changes the
bytes, create a new artifact ID, mark the old entry `superseded`, and link it
through `superseded_by`. Reuse the existing entry only when regenerated bytes
have the same hash.

## Reusable finding records

Create one focused Markdown file per independently reusable result. Prefer
`scripts/project_store.py add-finding` and `link` over hand-maintaining reciprocal
references.

Use this template:

```markdown
# <Finding title>

- ID: `<stable-id>`
- Status: `confirmed | working-hypothesis | unknown | superseded`
- Target: `<game version/build, module/source SHA-256>`
- Scope: `<function/type/behavior, source locator, or module + RVA>`
- Supersedes: `<finding IDs or none>`
- Superseded by: `<finding ID or none>`

## Claim

<The reusable result, with units and applicability constraints.>

## Evidence

- `source:<source-id>`: `<function, line/range, key, or source locator>`
- `artifact:<artifact-id>`: `<function, label, line, instruction range, or JSON field>`
- Independent check: `<the distinct evidence relation or controlled runtime test
  required by SKILL.md §5>`

## Reusable detail

<Recovered types, field offsets, function contract, formula, pseudocode, table,
signature, or observation needed by future analyses.>

## Dependencies

<Finding IDs and assumptions this result depends on.>

## Validation and limitations

<What was tested, what remains unverified, version sensitivity, and failure
conditions.>
```

For compatibility, `check-links` still interprets an unprefixed evidence token
such as `` `old-artifact-id` `` as an artifact reference from v4.1. New or
updated findings should use explicit `source:` and `artifact:` prefixes.

Keep findings atomic enough to reuse without reading an entire topic report, but
large enough to preserve the reasoning and evidence needed to assess them. A
finding is not a chronological diary or a copy of raw decompiler output.

A reusable finding is durable upstream evidence, not a second application
interface. When downstream use is requested, adapt the material finding content
into the canonical `game-logic-mechanic-handoff/v1` defined by
`gameplay-semantics.md`. Preserve the finding's status and version scope during
that normalization; never silently promote a working hypothesis or unknown to
confirmed. If ownership/fan-out, units, authority, lifecycle, or another
application-critical relation is missing, recover that relation before the
handoff is emitted.

Durable application outputs reuse this same manifest/store rather than creating a
parallel application store. Register the authoritative application record and its
source/config/backup/validation artifacts under `artifacts/applications/` with
finding links. The companion `apply-game-logic` reference
`references/application-artifacts.md` defines the application-record content
and later-session rollback requirements; the existing schema-v2 manifest remains
the inventory and integrity authority.

## Deterministic project-store helper

Use `scripts/project_store.py` for mechanical store authoring and integrity
checks instead of hand-editing JSON/reciprocal links when practical. It requires
only Python 3.8+ and never modifies registered source files.

Typical operations:

```text
python scripts/project_store.py init --root <analysis-root> --project <game-id>

python scripts/project_store.py register-source --root <analysis-root> \
  --id <source-id> --path <original-file> --description <description> ...

python scripts/project_store.py add-artifact --root <analysis-root> \
  --id <artifact-id> --path artifacts/<file> --kind <kind> \
  --description <description> --tool <tool> --source-ref <source-id> ...

python scripts/project_store.py add-finding --root <analysis-root> \
  --id <finding-id> --title <title> --status confirmed --claim <claim> \
  --source-ref '<source-id>=<locator>' \
  --artifact-ref '<artifact-id>=<locator>' ...

python scripts/project_store.py link --root <analysis-root> \
  --finding-id <finding-id> --source-id <source-id> --locator <locator>

python scripts/project_store.py link --root <analysis-root> \
  --finding-id <finding-id> --artifact-id <artifact-id> --locator <locator>

python scripts/project_store.py verify --root <analysis-root>
python scripts/project_store.py check-links --root <analysis-root>
python scripts/project_store.py supersede --root <analysis-root> \
  --old-id <artifact-id> --new-id <artifact-id>
python scripts/project_store.py --self-test
```

`add-finding` can create the finding and reciprocal source/artifact links in one
operation. `link` updates both the manifest entry's `finding_refs` and the
finding's Evidence section, so the model does not need to hand-maintain both
sides. `register-source` hashes the original file in place and stores an absolute
read-only reference. `add-artifact` only accepts paths confined to the analysis
root.

`verify` checks schema shape, stable IDs, unique paths, source/artifact file
existence, byte size, SHA-256, lifecycle values, artifact provenance references,
and supersession targets. `check-links` checks reciprocal references between
sources/artifacts and finding Evidence sections. These are mechanical integrity
checks; they do not decide whether a gameplay interpretation is semantically
correct.

## Persistence cadence

Persist according to reconstruction cost:

- Preserve expensive, lossy, externally produced, large, or difficult-to-recreate
  evidence promptly.
- For directly readable source and cheap deterministic searches, first close the
  relevant evidence loop, then persist the coherent finding and its evidence
  links together.
- Do not create an artifact for every grep/read result. A source locator in a
  finding is sufficient when the original registered source remains authoritative.
- Do not defer evidence that would be costly to regenerate until the final report.

This keeps short source-level investigations from becoming bookkeeping-heavy
without weakening long-running binary-analysis reproducibility.

## Durable evidence chain

Reports cite finding IDs and summarize their consequences. Findings cite
registered original sources and/or manifested generated artifacts. Manifest
entries link back through `finding_refs`.

Typical source-level chain:

```text
report conclusion -> finding -> registered source -> target path/hash
```

Typical generated-evidence chain:

```text
report conclusion -> finding -> manifested artifact -> source/target version/hash
```
