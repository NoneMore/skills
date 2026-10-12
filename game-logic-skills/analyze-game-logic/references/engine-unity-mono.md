# Unity Mono Engine Adapter

This adapter covers Unity gameplay logic implemented in managed assemblies running
under the Mono scripting backend. Apply the core workflow from `SKILL.md` and its
specialized references only when material; this file adds Unity/Mono-specific
boundaries, evidence relationships, tracing pivots, and locator guidance.

Treat Unity IL2CPP as a separate implementation boundary. When a material path
crosses into a native plugin, Unity engine-native code, or another unmanaged
boundary, preserve the managed-side transition evidence and continue with the
core compiled/native workflow for the unresolved relation. Do not extend Mono
assembly, IL, metadata-token, JIT, or runtime assumptions across that boundary.

## 1. Applicability and detection

Use multiple mutually supporting indicators before classifying the material
boundary as Unity Mono, for example:

- a Unity player data directory with managed assemblies under a `Managed`
  directory;
- game-specific managed assemblies such as `Assembly-CSharp.dll` or equivalent
  project assemblies;
- Mono runtime artifacts consistent with the player platform and recovered build;
- Unity engine managed assemblies and metadata consistent with the same target;
- no stronger evidence that the material gameplay path is IL2CPP/native.

Do not classify a target as Mono from one managed-looking artifact alone. An
installed package may contain tooling, editor, server, debug, or leftover files,
and a Mono title may still route a material relation through native code.
Corroborate both the shipped backend and the implementation path responsible for
the mechanic.

## 2. Implementation model

Reason across three related evidence graphs when they are material:

```text
managed implementation graph
serialized configuration / object graph
engine-dispatch graph
```

- The **managed implementation graph** contains managed types and members,
  explicit calls, delegate/C# event relationships, generated implementations,
  and decisive managed reads/writes.
- The **serialized configuration/object graph** can define values, object
  references, object composition/instance configuration, and configured
  invocation edges. It can therefore change effective values, referenced object
  identity, sharing, and callback wiring.
- The **engine-dispatch graph** contains Unity lifecycle/messages and other
  callbacks whose runtime edge may be established by the engine rather than an
  ordinary managed call site.

Join only the portions material to the claim. Do not require complete graph
recovery or persist the three graphs as a schema merely because they were useful
during reasoning.

### Gameplay semantic mapping

Use Unity constructs as search and evidence anchors, not automatic proof of
ownership or causality:

- **Lifecycle/update:** `Awake`, `OnEnable`, `Start`, `Update`, `FixedUpdate`,
  `LateUpdate`, disable/destroy callbacks, and coroutines can identify execution
  opportunities.
- **Triggers:** collision/trigger callbacks, input handling, serialized callbacks,
  delegates/events, animation callbacks, coroutines, timers/invocation helpers,
  and explicit managed calls can identify invocation paths.
- **State owners:** `MonoBehaviour`/`Component` instances, `ScriptableObject`
  instances/assets, ordinary managed objects, static fields, managers, and
  serialized references are candidates whose actual sharing/lifetime must come
  from instancing and data flow.
- **Timing:** frame/fixed callbacks, coroutine waits, animation/physics callbacks,
  custom accumulators, and explicit time APIs may use different time domains.
- **Persistence:** static lifetime, scene survival, and `DontDestroyOnLoad` do not
  by themselves prove save persistence.
- **Presentation:** UI, animation, audio, particles, and rendering may be observers
  or may feed callbacks back into gameplay; follow the material relation.

## 3. Semantic anchors

### Managed implementation anchors

Prefer exact relevant assembly identity/hash plus semantic member identity:

- assembly name + namespace/type + member/full managed signature;
- field/property names and declaring types;
- strongly typed call sites, delegate/C# event subscriptions, and diagnostic
  strings;
- generated state-machine/closure relationships when they contain the decisive
  implementation;
- metadata tokens and IL offsets as exact-assembly supporting locators.

Keep these concepts separate in retained findings:

```text
target scope
  = game/player build identity

managed implementation identity
  = exact relevant managed assembly hash

semantic locator
  = assembly name + namespace/type + member/full managed signature

exact-assembly supporting locator
  = metadata token / IL offset
```

Target scope records where the claim was established; assembly hash identifies
the managed implementation bytes. Prefer the semantic locator for reuse and use
tokens/IL offsets only as supporting locators for that exact assembly.

### Serialized configuration anchors

When material, retain the smallest evidence that closes the serialized relation:

- serialized field/member identity;
- recovered scene/prefab/asset/local object identity when useful;
- object references or prefab/scene overrides;
- configured callback target/member relationships;
- provenance from declaration default through serialized/runtime assignment to
  the material read or copy.

Do not require a universal serialized-object locator schema. Persist semantic
managed identity and the value/reference/wiring provenance needed by the claim.
A serialized declaration proves that a value or reference can participate in
serialization; it does not prove which value or object the shipped mechanic
actually consumes.

### Engine-dispatch anchors

Absence of a conventional managed xref does not prove a Unity message is dead or
unreachable. Conversely, a lifecycle-shaped method name does not prove that a
particular runtime instance receives it in the requested scenario.

Distinguish **dispatch eligibility** from **observed dispatch**. Also distinguish
managed calls, engine-dispatched messages, and serialized-configured callbacks;
absence from one invocation graph is not evidence that an edge in another graph
does not exist.

## 4. Managed fidelity and Unity object model

Managed metadata, IL, and Unity object semantics are the default analysis surface.
Do not invent Mono object headers, GC layouts, JIT code addresses, or private
Unity native layouts while managed evidence closes the question.

Decompiler output is reconstructed source. Use it for semantic orientation and
inspect decisive IL, or use independent runtime evidence, when a material claim
depends on exact conversion, evaluation/order, branching, dispatch, exception
flow, or compiler transformation.

Generated state machines, closures, iterators, async methods, and backing members
can separate a source-level concept from the member that performs the material
behavior. Preserve that relation when it affects the locator or claim.

For object identity and scope:

- `GameObject`/`Component` containment is not automatically gameplay ownership;
- a `ScriptableObject` reference may resolve to a shared asset, clone, or
  runtime-created instance;
- `static` indicates managed sharing, not save persistence or intended global
  gameplay ownership;
- `DontDestroyOnLoad` describes scene/session lifetime, not disk persistence;
- serialized values/references may be overridden or replaced before material
  consumption.

Runtime object identifiers and JIT/native addresses are observation context, not
durable managed locators.

## 5. Recommended tracing workflow

Use the shortest Unity-specific progression that closes the unresolved relation:

```text
managed semantic anchor
  -> material serialized relation only when it can change the claim
  -> material invocation relation
  -> runtime object identity/sharing only when ownership or scope depends on it
  -> decisive managed relation
  -> unmanaged boundary only when the unresolved fact crosses it
```

### Material-driven serialized recovery

Recover serialized configuration only when an unresolved relation could change:

- the effective value consumed by the mechanic;
- referenced object/asset identity;
- sharing or instance scope;
- object composition relevant to ownership;
- configured invocation wiring relevant to trigger/caller scope.

A serialized field or Unity object reference is not by itself a reason to recover
the surrounding prefab, scene, or asset graph. Traverse by unresolved relation,
not by containment, and stop when that relation is closed.

Stay at managed evidence when a later deterministic assignment settles the
material value, the claim is insensitive to serialized variation, managed
construction/lookup already settles the relevant identity, or plausible
serialized alternatives are equivalent for the requested conclusion.

### Common pivots

- **Field-backed:** resolve the effective value at material consumption and the
  actual instance only when ownership/fan-out matters.
- **Event/lifecycle-backed:** identify the invocation-edge class; resolve the
  emitter/source or receiving instances only when caller/scope matters.
- **`ScriptableObject`-backed:** distinguish shared asset from clone/runtime
  instance only when that identity can change the conclusion.

## 6. Static-analysis guidance

Inspect game-specific managed assemblies and metadata before escalating to native
analysis. Prefer targeted type/member/data-flow relationships over broad
assembly-wide decompilation.

Collapse generated boilerplate only after preserving its source-level relation.
Treat ordinary managed call graphs as partial evidence because engine dispatch,
reflection, serialized callbacks, delegates, and native bridges can create
material edges outside a conventional xref graph.

Do not recover serialized artifacts merely because recovery is possible; recover
the smallest value/reference/wiring relation needed to close a material unknown.

## 7. Runtime-observation guidance

Apply the core runtime-validation gate; runtime observation is not a mandatory
second phase. Static plus serialized evidence can confirm a claim when every
relation material to that exact claim is closed without runtime-dependent
uncertainty.

Require runtime closure only when the claim depends on unresolved live
realization of a value, invocation edge, runtime object identity, sharing/lifetime
relation, timing/order behavior, or causal effect.

Useful Unity-specific observation points include material lifecycle/message or
event entry, values around the decisive mutation, coroutine progression when
timing matters, object creation/clone/pooling/replacement when identity matters,
and scene/lifetime transitions when they can change the claim.

Record enough context to distinguish material runtime instances, but keep runtime
instance identifiers and JIT/native addresses session-scoped. Do not require
runtime validation merely because a closed static relation could also be observed
dynamically.

## 9. Version-sensitive assumptions

Treat version-sensitive categories as revalidation prompts, not cached
compatibility claims. Revalidate only material categories such as:

- Mono/runtime packaging and managed assembly layout;
- assembly splitting/code generation when it affects identity or recovery;
- serialization behavior relevant to the material field/reference/wiring;
- lifecycle, scene, domain/reload, or activation behavior when it affects
  dispatch, lifetime, or reset;
- generated shapes, metadata tokens, stripping, or optimization when used as
  evidence;
- managed-to-native transition details when the unresolved relation crosses that
  boundary.

Record Unity/version lineage only when it materially scopes one of these
relations, resolves ambiguity, or improves reproducibility. Do not maintain a
compatibility matrix in this adapter.

## 10. Common failure modes

- Classifying the material path as Mono from one managed-looking artifact.
- Treating reconstructed C# as exact source when IL/compiler behavior is material.
- Treating absence from managed xrefs as proof that an engine-dispatched or
  serialized-configured callback is unreachable.
- Treating a lifecycle-shaped method as proof of scenario-specific dispatch.
- Reading a declaration default while missing a material serialized/runtime
  override.
- Recovering a whole prefab/scene graph when one serialized relation would close
  the claim.
- Inferring gameplay ownership from containment or per-instance scope from a
  `ScriptableObject` field alone.
- Treating `static` or `DontDestroyOnLoad` state as save-persistent.
- Persisting runtime instance IDs or JIT/native addresses as durable locators.
- Extending Mono assumptions across IL2CPP or an unmanaged boundary.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- target build scope and exact relevant managed assembly hash;
- managed semantic locator and optional exact-assembly token/IL-offset support;
- serialized value/reference/wiring provenance at the material consumption point;
- invocation-edge class and source/dispatch relation when it affects the claim;
- material ownership/sharing/lifetime/reset/persistence relation;
- generated implementation relation when it affects the decisive behavior;
- explicit managed-to-unmanaged transition evidence when the claim crosses it;
- remaining runtime-dependent uncertainty.

Do not persist the three reasoning graphs as a required schema.

## 12. Bundled tools

No Unity Mono helper is bundled. Tool support is operational state, not an
adapter invariant: inspect current tool/runtime capability only when a material
recovery or instrumentation path requires it. Put lengthy tool-specific or
volatile compatibility guidance in focused support references only when it earns
the extra indirection.

Treat recovery, decompilation, debugging, and instrumentation tools as mechanical
capabilities; successful output is not gameplay-semantic proof by itself.
