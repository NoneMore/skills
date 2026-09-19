---
name: analyze-game-logic
description: Analyze authorized offline/single-player game logic, including Windows PC and Web/JavaScript builds, with reproducible, evidence-backed static and dynamic reverse engineering. Use to identify how gameplay behavior is implemented; trace timers, formulas, state, scripts, and native or managed call paths; inspect binaries or IDA databases; design controlled runtime observations; assess reversible runtime changes; or produce a versioned report. Detect the engine and compilation boundary first, then load matching engine-specific guidance when available. Excludes multiplayer cheating, online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v4.3.2"
---

# Analyze Game Logic

Use a common evidence protocol across engines. Keep engine/runtime conventions in
engine adapters rather than expanding this file with engine-specific details.

## 1. Establish scope

- Establish from the user's request and available evidence whether the task is an
  authorized offline/single-player analysis. Do not ask for redundant
  confirmation when the context already establishes this.
- If authorization or online impact is genuinely unclear, continue only with
  non-invasive static triage that is safe and useful. Ask for clarification
  before launching, attaching to, modifying, or otherwise interfering with a
  process when the answer would change whether that action is permitted.
- Do not manipulate multiplayer state, matchmaking, leaderboards,
  server-authoritative state, another player's experience, accounts,
  credentials, or online-service enforcement.
- Incidental storefront APIs, achievements, cloud saves, telemetry, or crash
  reporting do not by themselves make local gameplay analysis out of scope.
- If instrumentation would require bypassing DRM or anti-cheat, do not bypass
  it; use permitted static or observational analysis instead.
- Treat installed game files as read-only unless the user explicitly authorizes
  a version-specific destructive modification.
- Keep durable analysis outputs outside the installed game tree. If reversible
  instrumentation requires deployment files inside the game directory, retain
  their authoritative source and provenance in the analysis project and
  document cleanup/restoration.
- Record the concrete logic question and in-game reproduction steps when known.
  Do not block useful static triage solely because reproduction steps are not
  yet available.

## 2. Choose analysis depth

Scale project overhead to the task:

- **Triage:** answer a narrow location/identity question. Do not initialize full
  project stores unless retained evidence or reusable findings are produced.
- **Focused analysis:** close the evidence loop for one mechanic, function,
  formula, field, or call path. Persist retained evidence and reusable findings.
- **Full reproducible analysis:** maintain the complete baseline, knowledge
  stores, dynamic validation record, and per-game report.

Promote a triage task to focused/full analysis when conclusions will be reused,
large artifacts are generated, multiple sessions are likely, or a modification
is being designed.

## 3. Build a reproducible baseline

For focused/full analysis, use this layout unless the workspace already defines
an equivalent analysis-only structure:

```text
<analysis-root>/
  artifacts/
    manifest.json
  notes/
    findings/
  reports/
    analysis.md
```

Record the information material to the conclusion:

- game/content version, storefront, and build identifier;
- executable or source path, relevant modules/files, architecture when applicable,
  and material file metadata;
- SHA-256 of every analyzed binary, source, or data file material to the claim;
- detected engine, scripting backend, and compilation boundary;
- existing IDA databases, symbols, source maps, or prior analysis artifacts.

Treat original read-only targets and generated analysis outputs as different
classes of evidence. Register original files that remain outside the analysis
root as **sources**; keep generated/decompiled/extracted outputs under the
analysis root as **artifacts**. Do not copy an original source file merely so a
finding can cite it.

Before repeating work, inspect `artifacts/manifest.json` and search
`notes/findings/` for the target version, module, function, type, or behavior.
Verify retained evidence before reuse. Follow
[references/project-knowledge.md](references/project-knowledge.md) for store
schemas, lifecycle, integrity, cross-linking rules, and the deterministic
`project_store.py` helper.

Distinguish runner/file versions from actual game content versions. Preserve
conflicting version indicators instead of silently choosing one.

## 4. Detect and route the implementation boundary

Triage imports, strings, RTTI, symbols, resources, file layout, metadata, and
loaded modules before decompiling large functions. Determine the actual
implementation boundary, for example:

- native custom code;
- GameMaker VM or YYC;
- Unity Mono or IL2CPP;
- Unreal native code;
- an embedded scripting runtime;
- a Web/JavaScript bundle, browser runtime, or locally supplied Node.js logic;
- another engine or middleware boundary.

Do not infer an engine from one filename alone. Require at least two mutually
supporting indicators when practical.

### Source-available fast path

When the gameplay implementation is directly readable source (for example
JavaScript/TypeScript, Python, Lua, C#, or unpacked scripts), prefer source-level
dependency analysis over binary-style reverse-engineering ceremony:

- establish the executable/source entry points and state-owning modules;
- batch related semantic anchors before iterative reads (for example RNG/roll/
  chance/odds, success/failure branches, timers, state mutation, and event tables);
- map the relevant callers/callees or data dependencies as a compact cluster;
- use source line/function identifiers as primary locators, adding module + RVA
  only when a compiled/native boundary is actually material.

Do not manufacture binary-style artifacts or copy readable source into the
analysis root merely to satisfy the evidence store. Register the original file
as a source and retain only generated evidence that is useful independently.

After detection, consult
[references/engine-registry.md](references/engine-registry.md). Load only the
adapter matching the confirmed boundary. Do not load unrelated engine adapters.
If no adapter is bundled, continue with this core workflow and document the
version-sensitive conventions you establish from evidence.

Bundled references are directly discoverable here without implying that they
should all be loaded:

- GameMaker YYC: [references/engine-gamemaker-yyc.md](references/engine-gamemaker-yyc.md)
- Web / JavaScript: [references/engine-web-javascript.md](references/engine-web-javascript.md)
- Adapter authoring contract: [references/engine-adapter-contract.md](references/engine-adapter-contract.md)

## 5. Trace the logic

1. Start from strong semantic anchors: internal variable names, script/event
   names, diagnostic text, configuration keys, symbols, registrations, or
   distinctive resources.
2. Separate UI/localization references from state-changing code.
3. Follow cross-references into candidate functions and recover types, calling
   conventions, object layouts, or runtime value formats from evidence.
4. Trace callers, callees, field accesses, constants, and return values until
   the behavior can be expressed as concise pseudocode.
5. Verify material claims with an independent consistency check. Independence
   is about the underlying evidence relation, not the number of tools, views, or
   renderings. A second view of the same instructions or metadata relation is
   corroboration, not an independent check.
   - Decompiler pseudocode and disassembly of the same instructions are one
     underlying relation.
   - A registration entry and a wrapper that merely exposes that same entry are
     one underlying metadata relation.
   - Repeated xrefs that all originate from one table, generated thunk family,
     or shared data-flow chain do not become independent by quantity.
   - A distinct caller/use path can count when it constrains the claim through a
     genuinely separate path; caller and callee views of the same call edge do
     not automatically count as two checks.
   - Controlled runtime observation can provide an independent check when the
     observation tests the claimed behavior rather than merely re-reading the
     same static value.
6. When a compiled/native boundary is material, record ASLR-stable
   `module + RVA` locations and treat raw virtual addresses as supplementary
   evidence. For directly readable source, use source/module/function locators
   instead.

Prefer targeted function/basic-block analysis over broad decompilation of large
runtime dispatchers.

## 6. Handle large analysis artifacts

If decompilation or extraction is too large for a tool response or model
context, write it directly under the analysis project's `artifacts/` directory
and treat the disk-backed file as authoritative.

- Identify module/source, function/range, tool/decompiler, and target
  version/hash in the artifact or its manifest metadata; add `module + RVA`
  when a compiled/native boundary is material.
- Verify coverage and completeness. If chunking is required, use explicit,
  non-overlapping address/basic-block ranges.
- Use indexes, targeted searches, and bounded reads instead of loading the whole
  artifact into context.
- Preserve enough raw output to distinguish tool output from later annotations.
- Treat multiple tool views as analysis-time working state by default, not durable
  deliverables. After comparison, retain the clearest independently useful
  canonical view; keep alternatives only when they preserve materially distinct,
  easy-to-lose, or expensive-to-reconstruct information. Pure formatting copies
  and successful-operation logs normally do not need durable retention.
- Register retained evidence and link it to reusable findings according to
  [references/project-knowledge.md](references/project-knowledge.md).

A displayed fragment is incomplete evidence until expected boundaries and
coverage are confirmed against the retained artifact.

## 7. Classify and persist evidence

Use these states consistently:

- **Confirmed:** demonstrated by relevant instruction/data flow or repeatable
  runtime observation, with the independent consistency check defined in §5
  when material.
- **Working hypothesis:** plausible interpretation that still needs a genuinely
  independent consistency check or a required dynamic validation.
- **Unknown:** missing version, unmapped type/field, unresolved unit, unavailable
  runtime condition, or otherwise insufficient evidence.

Cross-references alone establish association/reachability, not gameplay
semantics. Do not convert values into seconds, percentages, world units, or
probabilities until units and update rates are established.

For focused/full analysis, persist reusable conclusions and retained evidence
according to reconstruction cost rather than mechanically after every small
discovery. Preserve expensive, lossy, externally produced, or difficult-to-
recreate evidence promptly. For cheap source-level observations that can be
re-derived quickly, close the relevant evidence loop first and then persist the
coherent finding/evidence set together. Do not postpone durable evidence until
the final report when loss or rework would be material. Keep lifecycle, IDs,
schemas, integrity checks, authoring operations, and supersession rules in
[references/project-knowledge.md](references/project-knowledge.md), not in this
core workflow.

## 8. Validate dynamically when the claim requires it

Dynamic validation is optional for narrow identity/location claims when static
semantic evidence is already sufficient. When runtime observation is practical,
it should normally be performed before treating the following as settled:

- timer units, update rates, pause/scaling behavior, or conversions to seconds;
- causality claims that a candidate value, field, call, or branch controls the
  observed gameplay behavior rather than merely correlating with it;
- discrimination among multiple callers, event sources, actors, or shared paths;
- state lifetime across pause, death, loading, cutscenes, room/scene changes,
  save/reload, or other transitions material to the claim;
- a runtime write, hook, patch point, or other intervention whose scope and side
  effects depend on the recovered semantics;
- random/probabilistic behavior when a static formula alone does not establish
  the effective runtime distribution or source conditions.

For those categories, if runtime observation is available but has not been
performed, keep the affected conclusion as a Working hypothesis rather than
silently treating static plausibility as dynamic confirmation.

Do not launch or attach to a target merely because dynamic validation would
strengthen a conclusion. Read-only static inspection may proceed autonomously
within the requested scope. Launching, attaching, runtime instrumentation, and
memory writes must be within the user's requested/authorized analysis scope; if
that scope is not established, continue static work and provide the validation
procedure instead of silently performing the runtime action.

When validating source-available logic, use the smallest dependency boundary
that can test the claim. Prefer, in order: static/exhaustive proof, an extracted
pure-function or minimal state-transition harness, subsystem simulation, then
full runtime integration. Do not emulate unrelated UI/runtime subsystems merely
to exercise isolated game logic. If a validation harness repeatedly fails on
unrelated environment dependencies, reduce or redesign the harness rather than
continuing to expand incidental stubs.

When validating dynamically:

- Explain what instrumentation will observe or change before running it.
- Scope attachment to the intended offline process and exact module/version.
- Prefer logging reads, calls, arguments, returns, and state transitions before
  writing memory.
- Use a fixed save/checkpoint and reproduction path when practical. Record
  relevant RNG/seed conditions when randomness can affect the result.
- Compare a control run with the observation run; when a modification is being
  validated, compare control, observation, and modified runs as applicable.
- Change one variable at a time.
- Exercise relevant edge cases such as pause, death, loading, cutscenes,
  difficulty changes, and save/reload when they are material to the claim.
- Record observed values, timestamps or step counts, reproduction steps, and
  limitations.

If runtime tooling is unavailable, unsafe, outside the requested authorization,
or would require a prohibited bypass, provide the validation procedure, state
why it was not run, and mark the result as not dynamically confirmed where
dynamic validation is material.

## 9. Choose the least invasive change

Prefer, in order:

1. an existing game configuration or supported mod interface;
2. a reversible runtime data change with version/value guards;
3. a hook limited to one caller or event source;
4. a hook on shared logic with documented side effects;
5. destructive modification of original installed files only with explicit
   authorization.

Runtime writes, hooks, injected instrumentation, and reversible mod techniques
may be used as scoped analysis techniques when permitted. Document what changes,
where it changes, how it is version-guarded, and how to restore the control
state.

Before any destructive patch, record the exact target hash, original bytes,
replacement bytes/files, file-offset or RVA mapping when applicable, expected
effect, risks, and restoration procedure.

## 10. Maintain the report

For focused/full analysis, keep `reports/analysis.md` as a concise synthesis and
navigation entry point rather than the sole knowledge store. Include:

- baseline metadata and hashes;
- research question and reproduction steps;
- implementation boundary and engine/runtime overview;
- conclusions and concise pseudocode with finding/evidence references;
- dynamic procedure and results when used;
- material functions, types, fields, call paths, signatures, and source-level
  locators or `module + RVA` when applicable;
- confidence labels, unresolved questions, and version sensitivity;
- references to project scripts, reusable findings, and manifested artifacts.

Preserve unrelated workspace changes and keep version-specific findings
separated.

## 11. Final checks

Before finishing a focused/full analysis:

- verify the target version/build/hash supporting each material conclusion;
- ensure every Confirmed claim has semantic evidence and the independent check
  required by §5 when material;
- label unresolved units, fields, types, and version assumptions explicitly;
- verify material original sources and retained artifacts are registered and
  integrity-valid where applicable;
- verify reusable conclusions have finding records and source/artifact cross-links
  are valid;
- confirm no destructive modification occurred without explicit authorization;
- separate observed behavior from inferred behavior;
- state whether dynamic validation was performed, unavailable, outside scope,
  unsafe/prohibited, or unnecessary, and do not mark dynamically material claims
  Confirmed when the required runtime check was available but omitted;
- verify durable outputs live under the analysis root and any deployment files
  inside the game tree have a documented cleanup/restoration path;
- provide the report path when one exists and the highest-value unresolved next
  step.
