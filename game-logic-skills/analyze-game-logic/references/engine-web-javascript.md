# Web / JavaScript Game Adapter

Use this adapter when the gameplay implementation boundary is JavaScript or
TypeScript delivered as browser bundles/chunks, an Electron/NW.js-style web
runtime, or locally supplied Node.js game/server code. This adapter focuses on
recovering readable modules and logic from bundled, transpiled, minified, or
obfuscated JavaScript while preserving evidence provenance.

## 1. Applicability and detection

Apply this adapter when at least two supporting indicators point to a Web/JS
implementation boundary, for example:

- HTML/bootstrap files load `.js`, `.mjs`, chunk manifests, service workers, or
  hashed bundle names;
- JavaScript syntax or source-map markers are present in the material target;
- webpack/browserify/Vite/Rollup/esbuild/Bun/SystemJS/AMD/UMD runtime scaffolding
  or module registries are visible;
- browser APIs (`window`, `document`, `fetch`, `WebSocket`, workers, IndexedDB,
  localStorage) or Node.js module/runtime APIs are used by gameplay code;
- source maps, `sourcesContent`, TypeScript paths, package names, or original
  module paths corroborate the boundary.

Distinguish these nearby cases before tracing logic:

- **Readable source:** use the core source-available fast path directly. Do not
  decompile already-readable source merely for ceremony.
- **Bundled/minified JS:** recover modules/readability before semantic tracing.
- **Obfuscated JS:** deobfuscate first or in parallel with bundle recovery; do
  not assume a formatter can restore semantics.
- **JS shell + WebAssembly:** route JavaScript glue here, but treat material
  gameplay logic inside `.wasm` as a separate WebAssembly/native boundary.
- **Remote server-authoritative gameplay:** client code can establish protocol
  use and local prediction/UI behavior, but it cannot by itself prove the
  server's internal logic. Analyze server-side JS only when the relevant source
  or authorized local artifact is supplied; do not replace missing server code
  with active probing of a live service.

A single `.js` filename is not enough to prove that the mechanic itself is
implemented in JavaScript.

## 2. Implementation model

Typical logic-bearing artifacts include:

- entry bundles and lazy chunks;
- unpacked module bodies and recovered original source from source maps;
- Web Workers / Shared Workers and service-worker code when they own state or
  scheduling relevant to the mechanic;
- JSON/config tables, generated registries, level/event tables, and state-store
  definitions referenced by code;
- locally supplied Node.js modules for authoritative simulation or game-server
  logic.

### Gameplay semantic mapping

Use these Web/JS mappings as runtime anchors:

- **Simulation/time:** `requestAnimationFrame`, fixed-step accumulators,
  browser timers, engine callbacks, worker loops, or local server ticks; render
  cadence does not prove simulation cadence.
- **State/lifecycle:** objects/classes, ECS, reducer/store, scene/world
  singletons, workers, or local server modules and their creation/update/teardown
  paths.
- **Events/dispatch:** DOM/device input, engine abstractions, event buses,
  actions/reducers, worker messages, timers, direct calls, and queued ordering.
- **Persistence/authority:** localStorage/IndexedDB/files/config/save modules;
  local simulation, prediction, serialized outbound values, received state, and
  remote authority. Client artifacts cannot prove unavailable server internals.
- **Presentation/physics:** React/UI state, DOM/canvas, Pixi/Phaser/Cocos draw
  paths, animation/audio/effects, interpolation, and engine/custom physics may
  expose a mechanic without owning its gameplay mutation.

### Electron / NW.js container discovery

Before bundle analysis, identify the application container/bootstrap layer. For
Electron targets, inspect `resources/app/`, `resources/app.asar`, any
`app.asar.unpacked` tree, and the relevant `package.json` entry point. Separate
the Electron main process, preload scripts, and renderer entry points before
following gameplay code. For NW.js, likewise identify the package/bootstrap
entry and renderer-facing scripts before treating a renderer bundle as the whole
application.

`app.asar` is a container boundary, not JavaScript source by itself. Extract or
otherwise expose its authorized local contents with an appropriate ASAR-aware
tool before routing the contained `.js`/`.mjs`/chunk files through this adapter.
Record the container hash as provenance. Do not infer that renderer code is the
only authority merely because it is easiest to inspect.

Treat HTML, CSS, localization, telemetry wrappers, storefront SDKs, and asset
loaders as supporting evidence unless data flow shows that they own the target
state or transition.

Do not collapse browser and server code into one trust boundary. Record where a
value is computed, where it is only displayed, and whether a network message is
an input, output, prediction, or authoritative result.

## 3. Semantic anchors

High-value anchors, in descending order when available:

1. **Source maps and original module paths.** A matching map with
   `sourcesContent` can recover source closer to the original than any
   deobfuscation pass. Hash both bundle and map and preserve their relation.
2. **Module/chunk graph.** Entry module, dynamic-import edges, webpack module
   IDs, Browserify requires, Vite/Rollup chunk imports, and worker entry points
   narrow the search much faster than global text reading.
3. **Gameplay vocabulary.** Batch-search names and string literals for state,
   timers, cooldowns, damage, RNG/chance/roll, inventory, progression, spawn,
   score, difficulty, win/loss, save, and mechanic-specific terms.
4. **State mutation APIs.** Stores/reducers/actions, ECS component writes,
   observable setters, persistence calls, and authoritative simulation update
   functions are stronger than UI reads of the same value.
5. **Scheduling and time.** `requestAnimationFrame`, `setTimeout`,
   `setInterval`, engine tick callbacks, delta-time accumulation, worker timers,
   and server tick loops help distinguish wall time from simulation time.
6. **Network boundary.** `fetch`, WebSocket/socket libraries, RPC/event names,
   serializers, message handlers, and validation branches show what crosses the
   client/server boundary. They do not prove remote implementation details not
   present in the artifact.
7. **Framework/engine registrations.** Phaser, Pixi, Cocos Creator, custom ECS,
   React/state libraries, or other framework conventions can lead to lifecycle
   entry points, but framework presence alone does not prove mechanic ownership.

Minified identifier names are weak anchors until supported by data flow,
constants, strings, call structure, or recovered names.

## 4. ABI, runtime values, and object model

JavaScript does not have a stable native ABI comparable to a compiled engine
adapter. Recover semantics at the language/runtime boundary instead:

- distinguish lexical variables, closure-captured state, object properties,
  prototype methods, class fields, module singletons, and imported bindings;
- track mutation through aliases and destructuring rather than relying on a
  pretty-printed local name;
- distinguish JavaScript `number`, `bigint`, strings, typed arrays, and packed
  binary protocol fields where numeric precision or endianness matters;
- treat TypeScript types reconstructed from syntax or source maps as evidence,
  but do not invent static types for dynamically shaped objects without use-site
  support;
- for Node/Electron native addons or `.wasm`, stop at the call boundary and route
  the material lower-level implementation separately.

Renaming by a decompiler/deobfuscator is interpretive output, not original
symbol evidence unless a source map or other independent artifact supports it.

## 5. Recommended tracing workflow

When mechanic reconstruction applies, use this Web/JS-specific progression:

1. Identify the container/bootstrap and the JavaScript, worker, WebAssembly, or
   native boundaries material to the target.
2. Obtain the minimum readable view needed for semantic tracing: prefer matching
   source maps; otherwise unpack or deobfuscate only the relevant bundle/chunk
   set while preserving provenance outside the original game tree.
3. Locate the simulation/state owner, relevant scheduler, and authority boundary
   supported by evidence.
4. Batch-search gameplay vocabulary and mutation APIs, then narrow to the
   smallest module cluster containing the mechanic.
5. Apply the canonical gameplay semantic model to that cluster, following
   materially distinct callers/consumers and lifecycle or persistence paths as
   needed.
6. Reconstruct concise gameplay pseudocode with stable module/function locators,
   then perform the independent consistency check and dynamic validation required
   by the core workflow.

Bundle recovery is a supporting capability; a successful source-map extraction,
Wakaru split, webcrack transform, or formatting pass does not establish mechanic
ownership.

### Recovery tooling

When readable source is not directly available, recover only the minimum view
needed for semantic tracing. Prefer a matching source map; otherwise choose
bundle decomposition, deobfuscation, or formatting according to the artifact.
Generated views of the same bundle are corroborating views, not independent
semantic evidence.

Load [web-recovery-tools.md](web-recovery-tools.md) only when detailed
webcrack/Wakaru/Prettier ordering, CLI recipes, version caveats, or
`scripts/web_js_triage.py` operation is needed.

## 6. Static-analysis guidance

### Source maps first

Check for adjacent `.map` files, inline maps, and `sourceMappingURL`
references. Do not treat a caller-supplied map as matching merely because it can
be parsed. Record an association status such as `linked-by-sourceMappingURL`,
`source-map-file-field-match`, `adjacent-name-match`, or
`manually-supplied-unverified`.

When a map is available:

- verify its relation to the analyzed bundle/version as strongly as the artifacts
  allow, including `sourceMappingURL` and the map's `file` field;
- inspect `sources`, `names`, and `sourcesContent`;
- prefer extracted original sources for semantic analysis when present;
- retain generated decompiled views only when they add useful structure or when
  map coverage is incomplete;
- preserve uncertainty when a manually supplied map cannot be corroborated by a
  bundle reference, filename relation, or map metadata.

Wakaru can consume a source map for name recovery and can extract embedded
original sources from a map. Keep map-derived source separate from tool-rewritten
source so provenance remains obvious. A mismatched map can create highly
plausible but false names and source paths, so source-map association is part of
the evidence, not bookkeeping.

## 7. Runtime-observation guidance

For browser/Electron gameplay, useful read-only observation points include:

- call logging at the recovered state transition or scheduler boundary;
- values entering/leaving a reducer, store action, simulation tick, or worker
  message handler;
- timestamps/delta values around timer and cooldown code;
- locally generated versus network-received values at serialization/handler
  boundaries.

Do not infer server authority from a client-side prediction path. For a local
Node.js backend supplied by the user, prefer a minimal test harness around the
specific pure function/module over starting a complete service stack.

## 9. Version-sensitive assumptions

Revalidate bundler/chunk/runtime layouts, source-map completeness and bundle
association, framework-generated lifecycle patterns, and any transformation-tool
behavior material to the cited recovery view. Record actual tool/runtime
versions in provenance rather than treating documentation snapshots as
requirements.

## 10. Common failure modes

- Treating beautification/deobfuscation or multiple generated views as semantic
  proof.
- Trusting generated names or a source map without establishing provenance and
  bundle association.
- Searching one giant bundle repeatedly instead of narrowing to the relevant
  module/chunk/worker cluster.
- Mistaking UI state or client prediction for authoritative mutation.
- Ignoring lazy chunks, workers, native addons, or a WebAssembly boundary.
- Inferring initialization order from an inspection-oriented decomposition
  rather than an order-preserving representation.

## 11. Evidence checklist

Record Web/JS-specific evidence as applicable:

- exact bundle/chunk/source-map/config hashes material to the cited path;
- runtime/bundler boundary and supporting indicators;
- source-map provenance and bundle/map association status;
- generated-view provenance: tool/version/options plus the tree supplying the
  cited locator;
- stable module path/ID and function/structural locator;
- local/predicted/persisted/sent/received/authoritative role when authority is
  material.

Generic mechanic, validation, and evidence requirements remain in the core.

## 12. Bundled tools

`scripts/web_js_triage.py` is a read-only-to-source recovery orchestrator. It
inventories JS/TS inputs, hashes inputs and retained outputs, records source-map
association strength and tool/runtime provenance, and manages isolated generated
recovery views without editing the input bundle/map or executing the game.

Use [web-recovery-tools.md](web-recovery-tools.md) for retention modes, tool
selection/ordering, CLI examples, version caveats, and operational details.
Generated output remains recovered working evidence, not semantic proof.
