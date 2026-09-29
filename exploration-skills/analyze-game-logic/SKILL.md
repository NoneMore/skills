---
name: analyze-game-logic
description: Recover and verify authorized offline/single-player game logic with reproducible static or dynamic reverse engineering. Use for mechanic analysis and for cold-start gameplay change/tooling requests when no version-scoped mechanic handoff or complete finding already exists. Produces verified mechanic knowledge for downstream $apply-game-logic use. Excludes multiplayer or online-service interference, credential theft, DRM or payment bypass, piracy, and copyrighted-asset distribution.
metadata:
  version: "v5.0.0"
---

# Analyze Game Logic

Treat the gameplay mechanic as the primary semantic unit for behavior or causality
questions. Keep narrow identity/location questions narrow. Use the smallest
analysis path that can close the user's actual question with version-scoped,
reproducible evidence.

This skill **produces mechanic knowledge**. It may use reversible instrumentation
when required to validate a claim, but it does not design gameplay modifications
or downstream tools. When the user wants to consume recovered logic, finish the
material recovery work and hand the result to `$apply-game-logic`.

## 1. Establish the task boundary

Expected input is an authorized offline/local target plus a concrete analysis
question when one is known. Reproduction steps, saves, binaries, source, existing
analysis databases, symbols, source maps, or prior findings are useful inputs but
are not all required before static triage begins.

- Infer authorization from the request and available context when it is already
  clear; do not ask for redundant confirmation.
- If authorization or online impact is genuinely unclear, limit work to safe,
  non-invasive static triage. Ask before launching, attaching to, instrumenting,
  or otherwise interfering with a process when the answer changes whether that
  action is permitted.
- Do not manipulate multiplayer state, matchmaking, leaderboards,
  server-authoritative state, another player's experience, accounts,
  credentials, or online-service enforcement.
- Incidental storefront APIs, achievements, cloud saves, telemetry, or crash
  reporting do not by themselves make local gameplay analysis out of scope.
- If instrumentation would require bypassing DRM or anti-cheat, use permitted
  static or observational analysis instead.
- Treat installed game files as read-only. Gameplay changes belong to
  `$apply-game-logic`; analysis-only instrumentation must be reversible and
  provenance-preserving.
- Do not infer units, probabilities, ownership, lifetime, authority, or causal
  control from names, xrefs, constants, or presentation evidence alone.

## 2. Choose analysis depth

Match overhead to the requested result:

- **Triage:** answer a narrow location/identity question. Avoid project-store
  ceremony unless retained evidence or a reusable finding is actually produced.
- **Focused analysis:** close the evidence loop for one mechanic, function,
  formula, field, or call path and retain reusable evidence/findings.
- **Full reproducible analysis:** maintain the complete baseline, durable
  knowledge stores, dynamic validation record when material, and per-game report.

Promote triage when conclusions will be reused, large artifacts are generated,
multiple sessions are likely, or downstream application will depend on the
finding.

For focused/full work—and before persisting retained evidence or a reusable
finding from triage—follow
[references/project-knowledge.md](references/project-knowledge.md) for durable
project-store and reporting rules. Before repeating work, search retained
findings/evidence for the target version, module, function, type, or behavior and
verify it before reuse. Keep durable analysis outputs outside the installed game
tree. Distinguish runner/file versions from actual game-content versions and
preserve conflicting indicators instead of silently choosing one.

## 3. Discover the material implementation path

Triage imports, strings, RTTI, symbols, resources, file layout, metadata, and
loaded modules before decompiling large functions. Map only the implementation
layers material to the question, for example declarative data, readable scripts,
managed/VM/generated/native code, engine or middleware APIs, and runtime state or
event dispatch.

Do not infer an engine from one filename alone; require mutually supporting
indicators when practical.

Treat layers as a search progression, not parallel defaults. Before escalating
from readable/configuration layers into a more opaque or expensive boundary,
name the **material unknown** and establish either:

- positive transition evidence, such as readable logic terminating at an opaque
  API/call; or
- bounded negative evidence showing that the relevant readable layers and
  semantic anchors were searched sufficiently for the opaque boundary to become
  the next material place to investigate.

Competing hypotheses that cannot otherwise be distinguished also justify
escalation. Preserve a user-requested starting layer/order until it has been
characterized enough to justify moving on.

### Source-available fast path

When the material implementation is directly readable source or scripts, stay at
source level while it can close the question:

- establish entry points and state-owning modules;
- batch related semantic anchors before iterative reads;
- map the relevant callers/callees or data dependencies as a compact cluster;
- use source/module/function locators as primary evidence.

Do not manufacture binary-style artifacts or copy readable source into the
analysis root merely to satisfy the evidence store.

### Tooling economy

Use the lowest-cost evidence-preserving path. Reuse existing analysis projects,
structured integrations, helpers, or bounded one-shot queries; build
task-specific infrastructure only when those cannot close the material unknown.

After mapping the material path, consult
[references/engine-registry.md](references/engine-registry.md) and load only the
adapter or adapters needed for the unresolved boundary. If no adapter is bundled,
continue with this core workflow and record version-sensitive conventions from
evidence.

## 4. Reconstruct the smallest material mechanic slice

For gameplay behavior or causality questions, or when a function, formula, field,
or call path supports such a claim, load
[references/gameplay-semantics.md](references/gameplay-semantics.md). Use its
canonical mechanic model and the selected engine adapter for concrete runtime
mappings.

Trace from strong semantic anchors toward authoritative state mutation:

1. Separate presentation/localization references from state-changing logic.
2. Follow xrefs/data dependencies into candidate functions or source modules.
3. Recover material types, calling conventions, object layouts, value formats,
   callers, callees, field accesses, constants, branches, and return values.
4. Stop when the smallest slice needed for the claim can be expressed as concise
   gameplay pseudocode and material unknowns are explicit.

Prefer targeted function/basic-block analysis over broad decompilation of large
runtime dispatchers. If a generated artifact is too large for context, retain it
on disk as authoritative working evidence: record producer and target
version/hash, verify coverage, use explicit non-overlapping ranges when chunking,
and preserve enough raw output to distinguish tool output from later annotation.
Use indexes, targeted searches, and bounded reads rather than loading it
wholesale; register retained artifacts when the project-store branch applies.

## 5. Close the evidence loop

Classify conclusions consistently:

- **Confirmed:** demonstrated by relevant semantic instruction/data flow or
  repeatable runtime observation, with an independent consistency check when
  material.
- **Working hypothesis:** plausible interpretation still missing a genuinely
  independent consistency check or required dynamic validation.
- **Unknown:** a material version, unit, type, field, owner, lifetime, authority,
  runtime condition, or other fact remains unresolved.

An independent check must constrain the claim through a distinct evidence
relation, not another rendering of the same relation. The same instructions,
registration, or table/data-flow remain one relation; a distinct caller/use path
or controlled runtime observation can qualify.

For compiled/native boundaries, record ASLR-stable `module + RVA` locators.
When converting database VAs, RVAs, file offsets, or runtime addresses, record
the image/module base and independently verify any locator against the original
binary or loaded module before relying on it.

Cross-references establish association/reachability, not gameplay semantics. Do
not convert values into seconds, percentages, world units, or probabilities until
units and update rates are established.

## 6. Apply validation only when it is material

Dynamic validation is optional for narrow identity/location claims when static
semantic evidence is sufficient. When runtime observation is practical, it
should normally be performed before treating runtime-sensitive claims as settled,
including timing/units, causal control, caller/source discrimination, state
lifetime, persistence/reset behavior, authority, and effective random
distributions.

For those categories, if runtime observation is practical but has not been
performed, keep the affected claim as **Working hypothesis**. Whenever dynamic
validation is material to the claim, load
[references/runtime-validation.md](references/runtime-validation.md). Use
authorization and tool availability only to decide whether to execute runtime
actions or instead provide the validation procedure, state why it was not run,
and leave the dynamically material claim unconfirmed.

Analysis-only runtime instrumentation must remain reversible, narrowly scoped to
the observation, and traceable to its authoritative source/provenance.

## 7. Deliver a reusable mechanic handoff

Match the output to analysis depth. A triage answer may be concise. Focused/full
analysis should give the user a navigable synthesis of the concrete question and
reproduction path when known, relevant implementation layers, conclusion and
compact pseudocode, stable source/function or `module + RVA` locators, and
links to reusable findings/evidence where the project-store branch applies.

When another task will consume the recovered logic, emit the exact
`game-logic-mechanic-handoff/v1` record defined in
[references/gameplay-semantics.md](references/gameplay-semantics.md#4-canonical-mechanic-handoff-v1).
That reference is the only application-facing mechanic schema. Reusable findings
and the semantic reconstruction record are evidence/upstream representations,
not alternate application interfaces.

Do not omit an unresolved field when it could change downstream behavior or
scope. A downstream application must not silently upgrade a working hypothesis
or unknown into a confirmed fact.

If the user's request also asks to modify, instrument for a changed outcome,
simulate, calculate from, or otherwise operationalize this mechanic, stop this
skill after the required mechanic knowledge is closed and continue with
`$apply-game-logic`.

## 8. Completion criteria

Before finishing focused/full analysis, verify that:

- every material claim is scoped to the target version/build/hash that supports
  it;
- gameplay/causality claims satisfy the closure criteria in
  [references/gameplay-semantics.md](references/gameplay-semantics.md), with
  material unknowns explicit;
- every **Confirmed** claim has semantic evidence and the independent check from
  section 5 when material;
- runtime-sensitive claims are not marked **Confirmed** when required practical
  validation was omitted;
- reusable sources/artifacts/findings are registered and integrity-valid when the
  project-store branch applies;
- any deployed analysis-only instrumentation retains authoritative
  source/provenance and a documented cleanup/restoration path;
- the final answer/report states the evidence/confidence state,
  dynamic-validation status, material unknowns, observed-vs-inferred distinction,
  and highest-value next step;
- when downstream use is requested, the mechanic handoff exposes every material
  dependency needed by `$apply-game-logic` without performing the application
  itself.
