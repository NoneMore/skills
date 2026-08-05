---
schema: unity-modding-analysis/v1
analysis_revision: 1
status: partial
game: <name>
build_id: <version-or-hash-id>
backend: <Mono-or-IL2CPP>
architecture: <architecture>
loader: <name-and-version-or-none>
interop_generator: <name-and-version-or-not-applicable>
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

# <Target or question>

## Scope and stop boundary

- Question: <what this analysis must answer>
- In scope: <targets and behaviors>
- Out of scope: <implementation, deployment, unrelated systems>

## Fingerprint

| Component | Version/hash | Evidence |
| --- | --- | --- |
| Game/build |  |  |
| Native module or Mono assembly |  |  |
| IL2CPP metadata |  |  |
| Loader |  |  |
| Interop/generator |  |  |
| Ghidra project/program |  |  |

## Tool ledger

| Tool | Version | Invocation/configuration | Inputs | Output/reference | Limitation |
| --- | --- | --- | --- | --- | --- |

For Agent-driven Ghidra work, include the Headless/PyGhidra/MCP implementation and version, transport and endpoint scope, project persistence, allowed mutations, and mutation log location.

## Target facts

| Assembly/module | Declaring type | Signature | Token/RVA/locator | Static/instance | Evidence |
| --- | --- | --- | --- | --- | --- |

## Evidence ledger

| ID | Status | Claim | Evidence/premises | Confidence or next action |
| --- | --- | --- | --- | --- |
| E1 | Observed |  |  |  |
| I1 | Inferred |  |  |  |
| P1 | Pending |  |  |  |

## Call timing and behavior

<Lifecycle, caller/callee observations, expected counts, thread, and representative positive/negative paths.>

## Candidate seams

| Seam | Evidence | Expected effect | Risk | Decision |
| --- | --- | --- | --- | --- |

## Rejected or superseded hypotheses

| Hypothesis | Disproving evidence | Build/tool version |
| --- | --- | --- |

## Compatibility and reuse

- Reusable while: <matching fingerprint facts>
- Recheck after: <game, loader, generator, platform, or tool changes>
- Persistent analysis root: <user-scoped path outside the mod repository or none>
- Proprietary/generated artifacts remain at: <fingerprinted paths under that root or none>
- Disposable scratch used: <temporary paths and whether any useful result was promoted, or none>

## Pending work

- <Concrete next action, required asset/decision, and expected proof>
