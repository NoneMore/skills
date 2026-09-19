# Web / JavaScript Game Adapter

Use this adapter when the gameplay implementation boundary is JavaScript or
TypeScript delivered as browser bundles/chunks, an Electron/NW.js-style web
runtime, or locally supplied Node.js game/server code. This adapter focuses on
recovering readable modules and logic from bundled, transpiled, minified, or
obfuscated JavaScript while preserving evidence provenance.

## Contents

1. [Applicability and detection](#1-applicability-and-detection)
2. [Implementation model](#2-implementation-model)
   - [Electron / NW.js container discovery](#electron--nwjs-container-discovery)
3. [Semantic anchors](#3-semantic-anchors)
4. [ABI, runtime values, and object model](#4-abi-runtime-values-and-object-model)
5. [Recommended tracing workflow](#5-recommended-tracing-workflow)
   - [Tool roles and ordering](#tool-roles-and-ordering)
6. [Static-analysis guidance](#6-static-analysis-guidance)
   - [Source maps first](#source-maps-first)
   - [webcrack](#webcrack)
   - [Wakaru](#wakaru)
   - [Prettier](#prettier)
7. [Runtime-observation guidance](#7-runtime-observation-guidance)
8. [Modification-point selection](#8-modification-point-selection)
9. [Version-sensitive assumptions](#9-version-sensitive-assumptions)
10. [Common failure modes](#10-common-failure-modes)
11. [Evidence checklist](#11-evidence-checklist)
12. [Bundled tools](#12-bundled-tools)

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

1. Hash the exact HTML/bootstrap, bundle/chunk, source-map, worker, and config
   files material to the claim.
2. Look for a usable source map before transforming code. If original source is
   recoverable, prefer it and retain the bundle/map hashes as provenance.
3. Inventory entries, lazy chunks, workers/service workers, source maps,
   WebAssembly/config boundaries, and bundler signatures. For Electron/NW.js,
   perform the container/bootstrap discovery above first. Record the detected
   bundler/runtime when evidence supports it.
4. For unreadable production JavaScript, generate and compare webcrack and
   Wakaru views as needed in temporary staging rather than overwriting the source;
   after comparison, choose one canonical readable view for durable retention.
   - run **Wakaru** on the original bundle for bundle-aware unpacking and
     production-JS recovery, preferably `--unpack=inspect` during reverse
     engineering;
   - run **webcrack** when obfuscation/deobfuscation value is evident, or when an
     explicit tool comparison is requested;
   - use **Prettier** only on generated output selected for readable retention;
     formatting alone does not justify a second durable copy.
5. When both webcrack and Wakaru views were generated, compare them before
   deciding whether the alternative view preserves materially distinct value.
   Treat agreement on module boundaries, strings, constants, and call/data-flow
   as corroboration, not as independent semantic proof when both derive from the
   same input relation.
6. Batch semantic searches across the recovered tree, then trace the smallest
   module cluster that owns the state transition.
7. Reconstruct concise pseudocode in terms of original/recovered module path,
   function or stable structural locator, input state, mutation, output, and
   network boundary if any.
8. Validate dynamically only when required by the core workflow and within the
   authorized local/offline scope.

### Tool roles and ordering

The three tools are complementary, not interchangeable:

- **webcrack** is the first-choice additional pass when obfuscator-style
  transforms or other clear deobfuscation needs are present. It can deobfuscate,
  unminify, transpile, and unpack webpack/Browserify bundles; ordinary production
  minification alone does not require durable parallel retention.
- **Wakaru** is production-JS recovery and bundle decomposition. It supports
  multiple bundler families and explicitly is not a general-purpose
  deobfuscator, so heavily obfuscated input may need webcrack first. Running
  Wakaru separately on the original bundle is often more useful than feeding it
  only a rewritten output because bundle structure may be easier to detect
  before another tool changes it. These are parallel views of the same evidence,
  not independent semantic evidence.
- **Prettier** is a formatter, not a reverse-engineering engine. Use it last on
  generated copies; formatting does not validate semantics.

Do not force a single linear pipeline when one transform destroys information
needed by another. Preserve parallel outputs only until their information value
has been compared. Retain the clearest view by default; keep alternatives only
when they preserve materially distinct structure or evidence.

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

### webcrack

Current webcrack releases provide a CLI/API that parses to AST, prepares,
deobfuscates, unminifies/transpiles, optionally reconstructs JSX, unpacks
supported bundles, and regenerates code. Use output directories outside the
original game tree. Its current package line requires a supported even-numbered
Node.js release; record the actual Node and webcrack versions used.

Useful patterns:

```bash
webcrack bundle.js -o <artifacts>/webcrack
webcrack input.js > <artifacts>/webcrack.js
```

Run bundle/chunk inputs into distinct output directories and preserve the entry /
lazy-chunk / worker relation separately; do not assume one unpack invocation
reconstructs an application's entire dynamic chunk graph. Do not pre-create a
webcrack `-o` leaf directory unless the invocation also deliberately uses the
tool's overwrite semantics.

Do not treat generated variable names as recovered originals unless separately
supported. If processing untrusted code, run transformation tooling in a
constrained analysis environment with no secrets and preferably no network
access; deobfuscation can involve code-evaluation mechanisms depending on tool
and pattern.

### Wakaru

Wakaru can decompile a file or unpack detected bundles/chunks. For reverse
engineering, `--unpack=inspect` is useful when finer module boundaries matter;
`--unpack=strict` is useful when heuristic fallback would create ambiguous
splits. `--source-map` can improve name recovery, and `wakaru extract <map>` can
recover `sourcesContent` when present.

**Important:** `--unpack=inspect` is an inspection-oriented decomposition. Its
module output may not preserve the bundle's executable initialization order, so
do not use an inspect tree as a drop-in rebuilt application or as proof of
runtime ordering. Trace initialization/order claims back to the original bundle
or another order-preserving representation.

Useful patterns:

```bash
wakaru bundle.js --unpack=inspect -o <artifacts>/wakaru
wakaru input.js --source-map input.js.map -o <artifacts>/wakaru-source-aware.js
wakaru extract input.js.map -o <artifacts>/sourcemap-sources
```

Start at the standard rewrite level. Use aggressive/speculative rewrites only
when needed and record that choice because readability can improve while
semantic confidence decreases.

### Prettier

Prettier parses and reprints code for consistent formatting. Never run
`prettier --write` against original evidence. Format a generated copy, ideally
with project configuration disabled when reproducibility matters:

```bash
prettier --write --no-config --no-editorconfig <generated-copy>
```

Record the formatter version when line-based locators depend on its output.
Prefer module/function/AST-structural locators over formatted line numbers for
long-lived findings.

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

Browser DevTools, local instrumentation, or a harness may be appropriate only
within the authorized scope established by the core workflow. Do not use this
adapter as permission to tamper with live multiplayer services, authentication,
leaderboards, or other users.

## 8. Modification-point selection

For authorized offline/local analysis, prefer:

1. existing config/data tables;
2. a local source-level value or pure function;
3. a narrow local module wrapper or call site;
4. a broader shared state/update function only after side effects are mapped.

Preserve original bundles. Make modifications in a copied analysis/build tree
or through a reversible local override. If the mechanic is server-authoritative
and the server artifact is not supplied, do not propose client-side changes as
if they changed the authoritative rule.

## 9. Version-sensitive assumptions

Revalidate per target/tool version:

- bundler signatures and chunk/runtime layouts;
- webcrack unpack/deobfuscation coverage;
- Wakaru-supported bundler forms and rewrite rules;
- Node.js version compatibility for webcrack and its native isolation
  dependency;
- formatter output and parser behavior;
- source-map completeness and whether paths/names correspond to the shipped
  bundle;
- framework/engine-generated lifecycle patterns.

As of the adapter refresh on 2026-09-07, the documentation consulted described
`webcrack` 2.16.0, `@wakaru/cli` 1.10.0, and Prettier 3.9.6. These are reference
points, not hard-coded requirements; record and validate the versions actually
used for each analysis.

## 10. Common failure modes

- Running Prettier on the original bundle and losing byte/hash provenance.
- Treating beautification as deobfuscation or semantic recovery.
- Feeding only a rewritten webcrack output to Wakaru and losing a bundler
  signature Wakaru could have recognized in the original, or vice versa.
- Assuming two decompiler outputs are independent proof of a gameplay formula.
- Treating Wakaru `--unpack=inspect` output as an executable reconstruction or
  trusting its file order as original initialization order.
- Trusting generated variable names as original names without source-map
  support.
- Searching one giant bundle repeatedly instead of unpacking and narrowing to a
  module cluster.
- Mistaking UI rendering or client prediction for authoritative state mutation.
- Ignoring worker code, lazy chunks, or a WebAssembly boundary.
- Assuming a failed unpack means the file is not bundled; wrappers and new
  bundler variants can defeat detection.
- Running third-party deobfuscation tooling over untrusted input in an analysis
  environment that contains credentials or unrestricted network access.

## 11. Evidence checklist

Before considering a Web/JS mechanic understood, record:

- exact bundle/chunk/map/config hashes material to the claim;
- detected JS/bundler/runtime boundary and supporting indicators;
- original source-map provenance and bundle/map association status when used;
- tool names, versions, commands/options, and which generated tree supplied the
  cited locator;
- module path/ID and function/structural locator for the state-changing logic;
- relevant callers/consumers and data-flow into/out of the mutation;
- whether the value is local, predicted, persisted, sent, received, or
  server-authoritative;
- an independent consistency check required by the core workflow;
- runtime validation status when timing, causality, lifetime, randomness, or a
  modification point makes it material.

## 12. Bundled tools

`scripts/web_js_triage.py` is a read-only-to-source orchestration helper. It:

- accepts one or more JS/TS files or directories, inventories Web-relevant files,
  and gives each code input a stable isolated analysis ID;
- hashes material input inventory, explicit/auto-discovered source maps, and all
  retained generated artifacts;
- records source-map association strength rather than silently assuming a map
  belongs to a bundle;
- resolves installed `webcrack`, `wakaru`, and `prettier` commands, or can use
  pinned `npx` package versions when explicitly enabled;
- defaults to `--retention lean`: tool output is generated in temporary staging,
  Wakaru is the default canonical recovery view, and webcrack runs/is retained
  only when a lightweight heuristic detects obvious obfuscation or
  `--force-webcrack` explicitly requests it;
- supports `--retention all` for difficult deobfuscation/tool comparison, keeping
  the prior parallel raw webcrack/Wakaru trees plus formatted copies;
- optionally extracts source-map sources through Wakaru and records the
  inspection-mode initialization-order caveat;
- in lean mode formats promoted canonical output in place, verifies successful
  Prettier formatting with `--check`, removes verified raw staging copies after
  success, and keeps raw staging on transformation/verification failure;
- in lean mode summarizes successful tool steps in the manifest without retaining
  their log files; failed/timeout logs remain available for diagnosis;
- when `--force` is used, removes only helper-managed output trees before the new
  run, preventing stale generated evidence while preserving unknown user files;
  if managed-looking paths already exist without a recognizable prior triage
  manifest, cleanup is refused rather than guessing ownership;
- returns a non-zero status when no analyzer step can run, rather than reporting
  an empty triage as success;
- writes schema-2 `triage-manifest.json` with overall status, commands, tool/Node
  versions, input and output hashes, provenance, map associations, outcomes, and
  generated paths.

The helper never edits the input bundle/map. It does not execute the game or
contact a service. Directory inventory detects Electron `app.asar` as a
container indicator but does not extract it; expose authorized ASAR contents
first. Third-party transformation tools still process untrusted syntax, so run
them in a constrained analysis environment when input is not trusted.

Examples:

```bash
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py game.bundle.js --source-map game.bundle.js.map \
  --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py dist/ --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py main.js lazy-1.js worker.js \
  --source-map main.js.map --source-map lazy-1.js.map --source-map worker.js.map \
  --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage \
  --allow-npx
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage \
  --force-webcrack
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage \
  --retention all
python scripts/web_js_triage.py --self-test
```

The helper is mechanical only. A successful transform does not establish which
module owns the mechanic, whether a network value is authoritative, or whether
a recovered rewrite is semantically exact.
