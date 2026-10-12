# Unity Mono Engine Adapter

This adapter covers Unity gameplay logic implemented in managed assemblies running
under the Mono scripting backend. Apply the core evidence, gameplay-semantics,
runtime-validation, and project-knowledge rules from `SKILL.md`; this file adds
Unity/Mono-specific boundaries, evidence relationships, tracing pivots, and
locator guidance.

Treat Unity IL2CPP as a separate implementation boundary. Do not carry Mono
assembly, IL, metadata-token, JIT, or runtime assumptions into an IL2CPP target.
When the material path crosses into a native plugin, Unity engine-native code, or
another unmanaged boundary, preserve the managed-side transition evidence and
continue with the core compiled/native workflow for the unresolved relation.

## 1. Applicability and detection

Use multiple mutually supporting indicators before classifying the material
boundary as Unity Mono. Useful indicators include:

- a Unity player data directory together with managed assemblies under a
  `Managed` directory;
- game-specific managed assemblies such as `Assembly-CSharp.dll` or equivalent
  project assemblies;
- Mono runtime artifacts consistent with the player platform and recovered build;
- Unity engine managed assemblies and metadata consistent with the same target;
- absence of stronger evidence that the material gameplay path is IL2CPP/native.

Do not classify a target as Mono from `Assembly-CSharp.dll`, a Unity executable,
or a `Managed` directory alone when the installed package may contain tooling,
editor, server, debug, or leftover artifacts. Corroborate the shipped backend and
the implementation path actually responsible for the mechanic.

A Unity title may mix managed gameplay code with native plugins or engine-native
behavior. The presence of a Mono backend does not imply that every material state
transition remains in managed code.

## 2. Implementation model

Reason across three related evidence graphs when they are material:

```text
managed implementation graph
serialized configuration / object graph
engine-dispatch graph
```

The **managed implementation graph** contains managed types and members, explicit
calls, delegate/C# event relationships, generated state-machine or closure
relationships, and decisive managed reads/writes.

The **serialized configuration/object graph** can define values, object
references, object composition and instance configuration, and configured
invocation edges such as serialized callbacks. It can therefore change not only
a field value but also which object is referenced, whether state is shared, and
which managed target can be invoked.

The **engine-dispatch graph** contains Unity lifecycle/messages and other callbacks
whose runtime edge may be established by the engine rather than an ordinary
managed call site.

Join only the graph portions material to the claim. Do not require complete graph
recovery, and do not persist graph structure merely because it was useful during
reasoning.

### Gameplay semantic mapping

Validate material mappings against the recovered target rather than assuming that
a familiar Unity construct proves gameplay ownership:

- **Lifecycle/update:** `Awake`, `OnEnable`, `Start`, `Update`, `FixedUpdate`,
  `LateUpdate`, disable/destroy callbacks, and coroutines are useful dispatch
  anchors when present. Their presence identifies an execution opportunity, not
  authoritative gameplay ownership.
- **Triggers:** collision/trigger callbacks, input handling, serialized callbacks,
  delegates/events, animation callbacks, coroutines, timers/invocation helpers,
  and explicit managed calls are useful source/caller anchors. Distinguish
  managed, engine-dispatched, and serialized-configured invocation edges.
- **State owners:** `MonoBehaviour`/`Component` instances, `ScriptableObject`
  instances/assets, ordinary managed objects, static fields, manager/singleton
  objects, and serialized references are candidates. Determine actual ownership,
  sharing, lifetime, and reset from construction/instancing and data flow.
- **Timing:** per-frame callbacks, fixed-step callbacks, coroutine waits,
  animation/physics callbacks, custom accumulators, and explicit time APIs can
  use different time domains. Do not infer seconds or fixed-step behavior from a
  counter or method name alone.
- **Persistence:** scene survival, static lifetime, or `DontDestroyOnLoad` is not
  proof of save persistence. Resolve concrete save/load/checkpoint/reset behavior
  only when persistence can change the claim.
- **Presentation:** UI, animation, audio, particles, and rendering code are often
  observers, but callbacks and event wiring can cross back into gameplay. Follow
  the material relation before classifying a path as presentation-only.

## 3. Semantic anchors

Prefer anchors that preserve semantic identity and the relationship between the
three evidence graphs.

### Managed implementation anchors

Useful managed anchors include:

- exact relevant assembly identity/hash;
- namespace + type + member + full managed signature;
- field/property names and declaring types;
- strongly typed call sites and diagnostic strings;
- delegate/C# event subscription sites;
- generated state-machine/closure relationships when they contain the decisive
  implementation;
- metadata tokens and IL offsets as same-assembly supporting locators.

Keep four concepts separate for retained findings:

```text
target scope
  = game/player build identity

managed implementation identity
  = exact relevant managed assembly hash

semantic locator
  = assembly name + namespace/type + member/full managed signature

same-build supporting locator
  = metadata token / IL offset
```

Target/build identity scopes where the finding was established. Assembly hash
identifies the managed implementation bytes. A semantic managed locator should
remain the primary implementation locator; metadata tokens and IL offsets are
useful supporting locators for the exact assembly rather than durable cross-build
identities.

### Serialized configuration anchors

When material, useful serialized anchors include:

- serialized field/member identity;
- recovered scene, prefab, asset, or local object identity;
- object references and prefab/scene overrides;
- configured callback target/member relationships;
- the provenance from declaration default through serialized/runtime assignment
  to the material read or copy.

Do not require a universal serialized-object locator schema. Persist semantic
managed identity and the effective value/reference/wiring provenance needed by
the claim. Retain recovered serialized object identifiers when they materially
improve reproducibility or discrimination.

A serialized field declaration proves that a value or reference can participate
in serialization; it does not prove the declaration-time/default value or object
is the one consumed by the shipped mechanic.

### Engine-dispatch anchors

Unity message methods can be invoked by engine dispatch rather than ordinary
managed call sites, so absence of a conventional xref does not prove a method is
dead or unreachable. Conversely, a lifecycle-shaped method name does not by
itself prove scenario-specific dispatch.

Distinguish **dispatch eligibility** from **observed dispatch**. Declaring type,
message name/signature, and target-version semantics may establish that a method
is a valid dispatch candidate; which runtime instance receives it, when, and how
often may remain a dynamic question.

Treat managed calls, engine-dispatched messages, and serialized-configured
callbacks as distinct invocation-edge classes. Do not use absence from one graph
as evidence that an edge in another graph does not exist.

## 4. Managed fidelity and Unity object model

Managed semantic evidence is the default analysis surface. Stay at managed
metadata, IL, and Unity object semantics while they close the question. Do not
invent Mono object headers, GC layouts, JIT code addresses, or private Unity
native layouts when managed evidence is sufficient.

Managed decompiler output is reconstructed source, not guaranteed original C#.
Use it for semantic orientation. Inspect decisive IL, or use an independent
runtime observation, when numeric conversion, arithmetic/evaluation order,
branch behavior, virtual/interface dispatch, exception flow, or a compiler
transformation can change the claim.

Compiler-generated state machines, closures, lambdas, iterators, async methods,
and generated backing fields can separate the source-level concept from the
member that performs the material mutation. Preserve both the semantic source
identity and generated implementation relation when material.

Unity object identity requires particular care:

- a `GameObject`/`Component` containment relation is not automatically gameplay
  state ownership;
- a `ScriptableObject` reference can point to a shared asset, clone, or
  runtime-created instance; establish the material identity before inferring
  per-actor or global scope;
- a static field indicates managed sharing, not save persistence or intended
  global gameplay ownership;
- `DontDestroyOnLoad` indicates a scene/session-lifetime choice, not disk
  persistence;
- prefab or scene serialization can override code defaults before material
  consumption, and runtime code can overwrite or replace those values/references
  afterward.

Runtime object identifiers and JIT/native addresses are observation context, not
durable managed locators. If a material path crosses P/Invoke, a native plugin,
Unity engine-native code, or another unmanaged boundary, retain the managed
caller/argument/transition evidence and continue outside this adapter for the
unresolved relation.

## 5. Recommended tracing workflow

Start from a strong managed semantic anchor, identify the unresolved material
relation, and use the shortest Unity-specific progression that can close it:

```text
managed semantic anchor
  -> material serialized relation only when it can change the claim
  -> managed / engine-dispatch / configured invocation relation when material
  -> runtime object identity or sharing only when ownership/scope is material
  -> decisive managed relation
  -> unmanaged boundary only when the unresolved fact actually crosses it
```

### Material-driven serialized recovery

Recover serialized configuration only when an unresolved serialized relation can
materially change the claim, such as:

- the effective value consumed by the mechanic;
- which object or asset is referenced;
- whether consumers share or clone referenced state;
- object composition relevant to ownership or instance scope;
- configured invocation wiring relevant to trigger/caller scope.

The presence of a serialized field or Unity object reference is not by itself a
reason to recover the surrounding prefab, scene, or asset graph. Traverse the
serialized graph by unresolved relation, not by containment, and stop when that
relation is closed.

It is safe to stop at managed evidence when the material read is deterministically
dominated by a later managed assignment, the claim is insensitive to serialized
variation, managed construction/lookup already determines the relevant identity,
or plausible serialized alternatives are equivalent for the requested outcome.
Keep non-material serialized uncertainty explicit without lowering an otherwise
closed claim.

### Field-backed mechanics

Identify the declaring member and resolve the effective value at material
consumption when serialized/runtime assignment can change it. Resolve the actual
runtime instance only when ownership, sharing, or fan-out affects the claim.

### Event- and lifecycle-backed mechanics

Identify the invocation-edge class first. For events, distinguish subscription or
serialized wiring from the actual emitter/source when fan-out matters. For Unity
messages, distinguish dispatch eligibility from which instances actually receive
the callback in the material scenario.

### `ScriptableObject`-backed mechanics

Distinguish a shared asset reference from a clone or runtime-created instance
before using mutation to infer scope. Do not require that distinction when every
plausible identity produces the same requested conclusion.

## 6. Static-analysis guidance

Inspect game-specific managed assemblies and metadata before escalating to native
analysis. Prefer targeted type/member/data-flow relationships over broad
assembly-wide decompilation.

Use decompiled C# for semantic orientation and decisive IL when reconstructed
source can hide a material detail. Collapse compiler-generated boilerplate only
after preserving its relation to the source-level mechanic; coroutine/iterator
state machines can move timing and mutation logic out of the apparent user-facing
method body.

Treat ordinary managed call graphs as partial evidence. Unity message dispatch,
reflection, serialized callbacks, delegates, and engine/native bridges can create
material runtime edges that are incomplete or absent in a conventional static
xref graph.

Do not recover serialized artifacts merely because recovery is possible. Recover
the smallest value/reference/wiring relation needed to resolve a material
uncertainty.

## 7. Runtime-observation guidance

Apply the core runtime-validation gate to unresolved Unity-specific relations;
runtime validation is not a mandatory second phase.

Static plus serialized evidence can confirm a claim when every relation material
to that exact claim is closed without runtime-dependent uncertainty. Require
runtime closure only when the claim depends on unresolved live realization of a
value, invocation edge, runtime object identity, sharing/lifetime relation,
timing/order behavior, or causal effect.

Useful Unity-specific observation points include:

- lifecycle/message entry for the material instance;
- serialized/event/delegate invocation when caller/source is unresolved;
- relevant values before and after the decisive managed mutation;
- coroutine progression when timing/order is material;
- object construction, clone, pooling, replacement, enable/disable, or destruction
  when identity/lifetime is material;
- scene/lifetime transitions when they can change the claim.

Record enough runtime identity context to distinguish material instances, but
treat runtime instance identifiers and JIT/native addresses as session-scoped
observation evidence rather than durable semantic locators.

Do not require runtime validation merely because the same relation could also be
observed dynamically. Tool-specific debugger, logging, hook, or instrumentation
procedures belong in focused support references when they become material.

## 9. Version-sensitive assumptions

Treat version-sensitive categories as revalidation prompts, not cached
compatibility claims. Revalidate only the categories material to the target and
claim, including:

- Mono/runtime packaging and managed assembly layout;
- assembly splitting and code-generation details when they affect identity or
  recovery;
- serialization behavior relevant to the material field/reference/wiring;
- lifecycle, scene, domain/reload, or activation behavior when it affects
  dispatch, lifetime, or reset;
- compiler-generated shapes and metadata tokens when used as evidence;
- stripping/optimization behavior when presence or absence is itself material;
- managed-to-native transition details when the unresolved relation crosses that
  boundary.

Record Unity/version lineage when it materially scopes one of these relations,
resolves ambiguity, or improves reproducibility. Do not maintain a compatibility
matrix in this adapter.

## 10. Common failure modes

- Treating managed-looking Unity artifacts as proof that the material gameplay
  path is Mono without corroborating the shipped backend.
- Treating decompiled C# as exact original source when IL/compiler transforms are
  material to the claim.
- Treating absence from the managed xref graph as proof that an engine-dispatched
  or serialized-configured callback is unreachable.
- Treating a lifecycle-shaped method name as proof of scenario-specific dispatch.
- Reading a field initializer/default while missing a material prefab, scene,
  asset, or runtime override.
- Recovering whole prefab/scene graphs when one serialized value/reference/wiring
  relation would close the claim.
- Treating `GameObject`/`Component` containment or a `ScriptableObject` field as
  proof of gameplay ownership or per-instance scope.
- Treating `static` or `DontDestroyOnLoad` state as save-persistent.
- Persisting runtime instance IDs or JIT/native addresses as durable managed
  locators.
- Extending Mono assumptions across an IL2CPP, native-plugin, or engine-native
  boundary.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- target build scope and exact relevant managed assembly hash;
- managed semantic locator: assembly name + namespace/type + member/full managed
  signature;
- metadata token/IL offset only when useful as exact-assembly supporting evidence;
- material serialized value/reference/wiring provenance at the consumption point;
- invocation-edge class and source/caller/dispatch relation when it affects scope;
- Component/GameObject/ScriptableObject/static ownership, sharing, lifetime,
  reset, or persistence relation only when it changes the claim;
- generated implementation relation when the decisive behavior is compiler
  generated;
- explicit transition evidence into native plugin, Unity engine-native code, or
  another unmanaged boundary;
- remaining runtime-dependent uncertainty when static/serialized evidence cannot
  close a material claim.

Do not persist the three reasoning graphs as a required schema.

## 12. Bundled tools

No Unity Mono helper is bundled in this adapter. Tool support is operational
state, not an adapter invariant: inspect the current tool/runtime capability when
a material recovery or instrumentation path requires it. Keep tool-specific or
volatile compatibility recipes in focused support references when they earn the
extra indirection.

Treat recovery, decompilation, debugging, and instrumentation tools as mechanical
capabilities; successful output is not evidence of gameplay ownership or causal
control by itself.
