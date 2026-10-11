# Unity Mono Engine Adapter

This adapter covers Unity gameplay logic implemented in managed assemblies running
under the Mono scripting backend. Apply the core evidence, gameplay-semantics,
and project-knowledge rules from `SKILL.md`; this file supplies Unity/Mono-specific
anchors, lifecycle mappings, managed-code tracing tactics, and locator guidance.

Treat Unity IL2CPP as a separate implementation boundary. Do not carry Mono
assembly, IL, metadata-token, JIT, or runtime assumptions into an IL2CPP target.
When the material path crosses into a native plugin or engine-native code, record
the transition evidence and continue with the core compiled/native workflow.

## 1. Applicability and detection

Use multiple mutually supporting indicators before classifying the material
boundary as Unity Mono. Useful indicators include:

- a Unity player data directory together with managed assemblies under a
  `Managed` directory;
- game-specific managed assemblies such as `Assembly-CSharp.dll` or equivalent
  project assemblies;
- Mono runtime artifacts consistent with the player platform and Unity version;
- Unity engine managed assemblies and metadata consistent with the same build;
- absence of stronger evidence that the relevant gameplay path is IL2CPP/native.

Do not classify a target as Mono from `Assembly-CSharp.dll`, a Unity executable,
or a `Managed` directory alone when the installed package may contain tooling,
editor, server, debug, or leftover artifacts. Corroborate the backend from the
shipped runtime layout and the code path actually responsible for the mechanic.

A Unity title may mix managed gameplay code with native plugins. The presence of
a Mono backend does not imply that every material state transition remains in
managed code.

## 2. Implementation model

A useful Unity Mono gameplay model is:

```text
serialized scene / prefab / asset configuration
        -> instantiated GameObjects / Components / ScriptableObjects
        -> managed type and method identity
        -> Unity lifecycle/message dispatch, events, delegates, or explicit calls
        -> managed state read/write or native boundary transition
        -> authoritative gameplay mutation
```

Managed assemblies usually provide the clearest semantic view of project code,
but scene, prefab, and asset serialization can select objects, references, and
values that differ from declaration defaults. Treat serialized configuration and
managed code as one material object graph when the mechanic depends on both.

### Gameplay semantic mapping

Validate these mappings against the target Unity version and recovered build:

- **Lifecycle/update:** `Awake`, `OnEnable`, `Start`, `Update`, `FixedUpdate`,
  `LateUpdate`, disable/destroy callbacks, and coroutines are strong lifecycle
  anchors when present. Their presence identifies an execution opportunity, not
  authoritative gameplay ownership.
- **Triggers:** collision/trigger callbacks, input handling, UnityEvents,
  delegates/events, animation callbacks, coroutines, timers/invocation helpers,
  and explicit managed calls are useful caller/event anchors. Establish the
  actual source and fan-out when scope depends on it.
- **State owners:** `MonoBehaviour`/`Component` instances, `ScriptableObject`
  instances/assets, ordinary managed objects, static fields, manager/singleton
  objects, and serialized references are candidates. Determine actual owner,
  sharing, lifetime, and reset from construction/instancing and data flow rather
  than class or field names.
- **Timing:** per-frame callbacks, fixed-step callbacks, coroutine waits,
  animation/physics callbacks, custom accumulators, and explicit time APIs can
  use different time domains. Do not infer seconds or fixed-step behavior from a
  counter or method name alone.
- **Persistence:** scene survival, static lifetime, or `DontDestroyOnLoad` is not
  proof of save persistence. Trace the concrete save/load/checkpoint/reset path
  when persistence is material.
- **Presentation:** UI, animation, audio, particles, and rendering code are often
  observers, but callbacks and event wiring can cross back into gameplay. Follow
  the data flow before classifying a path as presentation-only.

## 3. Semantic anchors

Prefer anchors that preserve managed type and object relationships:

- assembly identity and hash;
- namespace + type + method + full managed signature;
- field/property names and their declaring types;
- Unity lifecycle/message method names;
- serialized field/property names, object references, and asset identities;
- event/delegate subscription sites and UnityEvent-style callback wiring;
- diagnostic strings and strongly typed call sites;
- metadata tokens and IL offsets as version-scoped supporting locators.

For retained findings, prefer a semantic managed locator such as assembly +
namespace/type + method signature, bound to the exact assembly/build hash. Treat
metadata tokens and IL offsets as useful same-build locators rather than durable
cross-build identities.

Unity message methods can be invoked by engine dispatch rather than ordinary
managed call sites, so the absence of a conventional xref does not prove a
method is dead or unreachable. Conversely, a lifecycle-shaped method name does
not by itself prove Unity dispatch; verify the declaring type, signature, build,
and runtime behavior when material.

A serialized field declaration proves that a value can participate in Unity
serialization; it does not prove the declaration-time/default value is the one
consumed by the shipped mechanic. Distinguish code defaults, prefab values,
scene/instance overrides, runtime assignments, and the value at the material
read or copy.

## 4. ABI, runtime values, and object model

Stay at managed metadata, IL, and Unity object semantics while they close the
question. Do not invent Mono object headers, GC layouts, JIT code addresses, or
private Unity native layouts when managed evidence is sufficient.

Managed decompiler output is reconstructed source, not guaranteed original C#.
When exact branch conditions, arithmetic order, exception behavior, or compiler
transformations can change the claim, verify the decisive relation in IL or
through an independent runtime observation.

Compiler-generated state machines, closures, lambdas, iterators, async methods,
and generated backing fields can separate the user-facing source concept from
the method or field that actually performs the mutation. Preserve both the
semantic identity and the generated implementation relation when material.

Unity object identity requires particular care:

- a `GameObject`/`Component` containment relation is not automatically gameplay
  state ownership;
- a `ScriptableObject` reference can point to a shared asset or to a runtime
  instance/clone; establish actual identity before inferring per-actor scope;
- a static field indicates managed sharing, not save persistence or intended
  global gameplay ownership;
- `DontDestroyOnLoad` indicates a scene-lifetime choice, not disk persistence;
- prefab or scene serialization can override code defaults before the value is
  materially consumed, and runtime code can overwrite it again afterward.

If a material path crosses a P/Invoke/native plugin boundary, Unity engine native
call, or another unmanaged boundary, retain the managed caller/argument evidence
and continue with the compiled/native workflow for the unresolved relation.

## 5. Recommended tracing workflow

For mechanic reconstruction, prefer:

```text
build/backend identification
  -> relevant managed assembly and semantic type/method anchor
  -> serialized object/configuration relation when material
  -> lifecycle/event/explicit caller path
  -> decisive managed state read/write
  -> owner, instance sharing, reset, and persistence paths when material
  -> native boundary transition only when the unresolved relation requires it
  -> controlled runtime validation when timing/ownership/caller scope is material
```

For field-backed mechanics, identify the field's declaring type and then resolve
the actual runtime instance(s) that consume or mutate it. Do not stop at a field
name or a serialized default when prefab/scene/runtime assignment can change the
effective value.

For event-driven mechanics, identify both subscription/wiring and the actual
emitter/caller when fan-out matters. For lifecycle methods, establish which
runtime instances receive the callback and whether the method delegates the
material mutation elsewhere.

For `ScriptableObject`-backed configuration or state, distinguish shared asset
identity from per-instance clones or runtime-created objects before using a
mutation to infer scope.

## 6. Static-analysis guidance

Inspect game-specific managed assemblies and their metadata before escalating to
native analysis. Prefer targeted type/method/field relationships over broad
assembly-wide decompilation.

Use decompiled C# for semantic orientation and inspect IL when reconstructed
source can hide a material detail such as numeric conversion, evaluation order,
state-machine structure, boxing, virtual/interface dispatch, or exception flow.

Collapse compiler-generated boilerplate only after preserving the relation to
the source-level mechanic. In particular, coroutine/iterator state machines can
move timing and mutation logic out of the apparent user-facing method body.

Cross-references and call graphs remain association evidence. Unity lifecycle
message dispatch, reflection, serialized callbacks, delegates, and engine/native
bridges can produce real runtime edges that are incomplete or absent in an
ordinary static managed call graph.

## 7. Runtime-observation guidance

Prefer managed observation points while they are sufficient: method entry/exit,
relevant argument values, before/after a material field/property mutation,
event/delegate invocation, coroutine progression, object construction/enable/
disable/destruction, and scene transitions.

Use the least invasive managed debugger, logging, or instrumentation surface
available for the target. Observation should preserve the behavior being tested;
if instrumentation changes scheduling, object lifetime, exception handling, or
state, treat the affected result as weaker evidence.

When runtime validation depends on a specific instance, record enough identity
context to distinguish duplicated prefabs, pooled objects, shared managers,
shared `ScriptableObject` assets, and replacement objects created across scene
loads or respawns.

JIT/native addresses are runtime observations, not durable locators. Persist the
managed semantic locator and exact build/assembly identity; record a native
module + RVA only when the material mechanic actually crosses into a stable
native implementation boundary.

## 9. Version-sensitive assumptions

Revalidate per target rather than hard-coding:

- Unity major/minor/patch/editor lineage when known;
- Mono/runtime packaging and managed assembly layout;
- assembly names, splitting strategy, and code-generation options;
- serialization behavior relevant to the recovered field/reference;
- lifecycle, domain/reload, and scene-loading behavior material to the mechanic;
- compiler-generated method/type shapes and metadata tokens;
- stripping/optimization effects on unused metadata or code;
- managed-to-native transition details for plugins or Unity engine internals.

## 10. Common failure modes

- Treating every Unity build with managed-looking artifacts as a Mono gameplay
  target without corroborating the shipped backend and material path.
- Treating decompiled C# as exact original source when IL/compiler transforms are
  material to the claim.
- Assuming a Unity lifecycle method must have ordinary managed callers or xrefs.
- Reading a field initializer/default while missing prefab, scene, asset, or
  runtime overrides.
- Treating a `ScriptableObject` field as per-instance state without establishing
  whether consumers share one asset/object.
- Treating `static` or `DontDestroyOnLoad` state as save-persistent.
- Treating UI/animation/event code as presentation-only without following the
  callback path into gameplay.
- Persisting JIT/native addresses as if they were stable managed locators.
- Extending Mono assumptions across an IL2CPP or native-plugin boundary.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- detected Unity/Mono build identity and exact relevant assembly hash;
- managed assembly + namespace/type + method signature locator;
- metadata token/IL offset only when useful as same-build supporting evidence;
- material serialized default/override/runtime assignment relation;
- lifecycle/event/caller path and actual runtime instance identity when relevant;
- Component/GameObject/ScriptableObject/static owner, fan-out, lifetime, reset,
  and save/load behavior when these affect scope;
- generated state-machine/closure relation when the decisive implementation was
  compiler-generated;
- explicit transition evidence into a native plugin, Unity native engine code,
  or another unmanaged boundary.

## 12. Bundled tools

No Unity Mono helper is bundled in this draft. Prefer existing managed metadata,
IL, debugger, and instrumentation capabilities that match the target version and
platform. Treat recovery/decompilation/instrumentation tools as mechanical
capabilities; their successful output is not evidence of gameplay ownership by
itself.
