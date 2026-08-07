---
schema: native-static-analysis/v1
analysis_revision: 1
status: partial
target_name: <binary-or-component>
build_id: <version-or-stable-hash-id>
binary_sha256: <sha256>
format: <PE-ELF-Mach-O-or-other>
architecture: <architecture-and-endianness>
image_base: <preferred-image-base>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# <Target or analysis question>

## Scope and stop boundary

- Question: <what this analysis must answer>
- In scope: <functions, data, behavior, or comparison>
- Out of scope: <dynamic testing, patching, deployment, unrelated targets>
- Stop boundary: <evidence level sufficient for this task>
- Authorization/target provenance: <user-provided or otherwise authorized scope>

## Fingerprint

| Component | Identity/version | Evidence |
| --- | --- | --- |
| Primary binary | Path, size, SHA-256 |  |
| Format/architecture |  |  |
| Image base |  |  |
| Relevant companion files |  |  |
| Analysis database/project | Path and input identity |  |
| Prior report reused | Path/revision or none |  |

## Tool ledger

| Tool/interface | Version | Invocation/configuration | Input | Output/reference | Limitation |
| --- | --- | --- | --- | --- | --- |

Record automatic analysis state, decompiler/IR availability, relevant loader options, truncation, and whether the analysis database changed.

## Address normalization

| Entity | Tool name/alias | VA | RVA | File offset | Section | Representative bytes/hash |
| --- | --- | --- | --- | --- | --- | --- |

Use RVA and representative bytes to correlate rebased images or another analysis tool. Revalidate function boundaries after switching tools.

## Evidence ledger

| ID | Status | Claim | Evidence or premises | Confidence / disproof condition / next action |
| --- | --- | --- | --- | --- |
| E1 | Observed |  |  |  |
| I1 | Inferred |  |  |  |
| P1 | Pending |  |  |  |

Use only `Observed`, `Inferred`, or `Pending` in the Status column.

## Target facts

### Locators

<Exact symbols, strings, constants, byte patterns, imports, exports, addresses, and xrefs used to locate the target. Distinguish exact matches from families or partial matches.>

### Functions and data

| Target | Boundary/size | Callers/callees/xrefs | Data/state accessed | Evidence |
| --- | --- | --- | --- | --- |

### Calling convention and values

| Parameter/return/state | Candidate role or type | Direct evidence | Confidence |
| --- | --- | --- | --- |

### Behavior summary

<Concise reconstruction tied to evidence IDs. Keep decompiler syntax and business-level interpretation separate.>

## Cross-tool reconciliation

| Finding | Tool A view | Tool B view | Binary-level check | Resolution |
| --- | --- | --- | --- | --- |

Omit this section when only one tool was used. Do not transfer recovered names, types, or function boundaries without checking the exact binary, RVA, section, and bytes.

## Rejected or superseded hypotheses

| Hypothesis | Why it was plausible | Disproving evidence | Build/tool |
| --- | --- | --- | --- |

## Artifacts

| Artifact | Project-relative path | Purpose | Reproducibility/provenance |
| --- | --- | --- | --- |

- Compact report: `<project-root>/analysis/<build-id>/<target-slug>.md`
- Bulk/private assets: `<project-root>/.assets/<build-id>/<tool>/`
- Git ignore status for `.assets/`: <confirmed-or-pending>
- Disposable scratch: <paths and whether useful output was promoted, or none>

Do not commit proprietary binaries, analysis databases, bulk decompiler output, or copied private symbols unless repository policy explicitly permits it.

## Compatibility and reuse

- Reusable without revalidation while: <matching fingerprint and analysis conditions>
- Revalidate after: <binary, architecture, loader, image mapping, tool, or analysis-option changes>
- Stable search leads for other builds: <strings, imports, byte signatures, semantic anchors>
- Build-specific facts that must not be generalized: <addresses, layouts, recovered types, constants>

## Pending work

- <Concrete next action, missing artifact/tool capability, and expected proof>
