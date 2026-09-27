# Engine Adapter Contract

Engine adapters map the gameplay semantic model and evidence protocol in
`SKILL.md` onto one specific engine, backend, compilation mode, or runtime
boundary. They contribute version-sensitive implementation knowledge and
engine-specific mappings; they inherit core scope, permission, and mechanic
closure rules instead of restating them.

## Contents

1. [Applicability and detection](#1-applicability-and-detection)
2. [Implementation model](#2-implementation-model)
   - [Gameplay semantic mapping](#gameplay-semantic-mapping)
3. [Semantic anchors](#3-semantic-anchors)
4. [ABI, runtime values, and object model](#4-abi-runtime-values-and-object-model)
5. [Recommended tracing workflow](#5-recommended-tracing-workflow)
6. [Static-analysis guidance](#6-static-analysis-guidance)
7. [Runtime-observation guidance](#7-runtime-observation-guidance)
8. [Modification-point selection](#8-modification-point-selection)
9. [Version-sensitive assumptions](#9-version-sensitive-assumptions)
10. [Common failure modes](#10-common-failure-modes)
11. [Evidence checklist](#11-evidence-checklist)
12. [Bundled tools](#12-bundled-tools)

Use the following section contract. Omit a section only when it is genuinely not
applicable; prefer an explicit `Unknown / version-dependent` note over invented
details.

## 1. Applicability and detection

Document:

- the exact boundary the adapter covers;
- mutually supporting detection indicators;
- how to distinguish nearby modes/versions that need different treatment;
- common false positives and insufficient indicators.

Detection rules must not rely on a single filename when stronger corroboration
is available.

## 2. Implementation model

Explain where gameplay logic, resources, metadata, registrations, scripts, and
runtime state live for this boundary. Clarify which files/modules are primary
logic targets and which are only metadata/resource containers.

### Gameplay semantic mapping

Map each applicable primitive in
[gameplay-semantics.md](gameplay-semantics.md) to the concrete engine/runtime
constructs that implement or expose it. For each useful mapping, document:

- the concrete construct or subsystem;
- whether the mapping is a strong convention or only a search heuristic;
- the strongest engine-specific anchors for locating it;
- material version/runtime caveats.

Keep this section engine-specific. Reference the canonical model instead of
restating its generic mechanic stages, cross-cutting dimensions, or workflow.

## 3. Semantic anchors

List the highest-value engine-specific entry points, such as:

- script/event/function names;
- metadata or registration tables;
- symbols, RTTI, reflection data, or generated naming conventions;
- resource identifiers or diagnostic strings;
- engine/runtime helper calls.

Explain what each anchor proves and what it does not prove.

## 4. ABI, runtime values, and object model

Document only evidence-backed conventions for:

- function signatures and calling conventions;
- object/instance representation;
- runtime value/tagged-value representation;
- field lookup/metadata layout;
- ownership, lifetime, or reference-counting behavior.

Mark conventions as version-sensitive unless they are guaranteed by a stable
public ABI. Include how to validate them before applying types or writes.

## 5. Recommended tracing workflow

Describe the shortest engine-specific progression from a strong anchor to the
state-changing implementation and any engine-specific ownership, lifetime, or
validation pivots. Do not restate the canonical semantic stages or generic scope
rules.

## 6. Static-analysis guidance

Document engine-specific tactics for IDA/Ghidra/metadata tools, including noisy
patterns to collapse, decisive instruction/data-flow evidence, engine-specific
false positives, and when broad scanning is counterproductive.

## 7. Runtime-observation guidance

Document engine-specific observation points, guards, value/type and version
checks, detach/restore limitations, and claims for which runtime observation
materially changes confidence. Runtime-action permissions come from `SKILL.md`.

## 8. Modification-point selection

Describe engine-specific choices for the narrowest reversible intervention:
configuration, data/value source, one call site, shared function, or other
engine-supported mechanism. Call out shared-state and lifetime hazards.

## 9. Version-sensitive assumptions

Maintain a compact list of layouts, offsets, kind values, registration formats,
helper names, or other details that must be revalidated per runner/runtime/game
version. Do not present observed layouts as universal.

## 10. Common failure modes

List mistakes specific to this engine boundary, especially false semantic
anchors, misleading xrefs, generated-code noise, unsafe type assumptions, and
shared behavior that can cause overly broad changes.

## 11. Evidence checklist

Specify only the engine-specific evidence that supplements the core mechanic
record, evidence states, and independence rules.

## 12. Bundled tools

If helper scripts exist, describe:

- where they run;
- whether they are read-only;
- their deterministic outputs;
- runtime/Python requirements;
- version/heuristic assumptions;
- what results still require manual validation.

Keep scripts mechanical. Do not bury critical interpretation rules only in code.
