# Engine Adapter Contract

Engine adapters map the generic analysis protocol in `SKILL.md` onto one
specific engine, backend, compilation mode, or runtime boundary. They should
contain version-sensitive implementation knowledge, not duplicate the core
workflow.

## Contents

1. [Applicability and detection](#1-applicability-and-detection)
2. [Implementation model](#2-implementation-model)
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

Translate the core trace procedure into the most efficient engine-specific
progression from semantic anchor to implementation and validation. Prefer a
short ordered flow over a second generic reverse-engineering tutorial.

## 6. Static-analysis guidance

Document engine-specific tactics for IDA/Ghidra/metadata tools, including noisy
patterns to collapse, decisive instruction/data-flow evidence, and when broad
scanning is counterproductive.

## 7. Runtime-observation guidance

Document useful engine/runtime observation points, safe guards, value/type
checks, and version checks. Distinguish read-only observation from behavior
changes and call out detach/restore limitations where relevant. Identify any
engine-specific claims for which runtime observation should normally precede a
Confirmed conclusion, especially timing/unit behavior, source discrimination,
state lifetime, causality, or intervention scope.

Do not weaken the core runtime-action boundary in `SKILL.md`: adapter guidance
may recommend what to observe, but it must not imply permission to launch,
attach, instrument, or write memory outside the user's established scope.

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

Specify the minimum engine-specific evidence to record before a mechanic is
considered understood. The checklist supplements, rather than replaces, the
core evidence states and the evidence-independence definition in `SKILL.md` §5.

## 12. Bundled tools

If helper scripts exist, describe:

- where they run;
- whether they are read-only;
- their deterministic outputs;
- runtime/Python requirements;
- version/heuristic assumptions;
- what results still require manual validation.

Keep scripts mechanical. Do not bury critical interpretation rules only in code.
