# Unity Mono Engine Adapter

This adapter covers Unity gameplay logic implemented in managed assemblies under
the Mono scripting backend. Apply the core workflow from `SKILL.md`; this file
adds only Unity/Mono-specific boundaries, evidence relationships, tracing pivots,
and locator guidance.

Treat Unity IL2CPP and unmanaged/native code as separate implementation
boundaries. When a material path crosses into a native plugin, Unity engine-native
code, or another unmanaged boundary, preserve the managed-side transition evidence
and continue with the core compiled/native workflow. Do not extend Mono assembly,
IL, metadata-token, JIT, or runtime assumptions across that boundary.

## 1. Applicability and detection

Use mutually supporting indicators before classifying a material boundary as
Unity Mono, such as:

- a Unity player data directory with managed assemblies under `Managed`;
- game-specific managed assemblies such as `Assembly-CSharp.dll` or equivalent
  project assemblies;
- Mono runtime artifacts consistent with the player platform and build;
- Unity engine managed assemblies and metadata consistent with the same target.

Do not classify the mechanic as Mono from one managed-looking artifact alone.
Corroborate both the shipped backend and the implementation path responsible for
the mechanic.

## 2. Implementation model

A Unity Mono mechanic can span three evidence surfaces:

- **managed implementation:** managed types/members, explicit calls,
  delegates/events, generated implementations, and decisive reads/writes;
- **serialized configuration/object state:** values, object references,
  composition/instance configuration, prefab/scene overrides, and configured
  callbacks;
- **engine dispatch:** Unity lifecycle/messages and other callbacks whose runtime
  edge may not appear as an ordinary managed call site.

Inspect only the surfaces needed to close the claim.

### Gameplay semantic mapping

Use Unity constructs as search and evidence anchors, not automatic proof of
ownership or causality:

- **Lifecycle/update:** `Awake`, `OnEnable`, `Start`, `Update`, `FixedUpdate`,
  `LateUpdate`, disable/destroy callbacks, and coroutines.
- **Triggers:** collision/trigger callbacks, input handling, serialized callbacks,
  delegates/events, animation callbacks, coroutines, timers/invocation helpers,
  and explicit managed calls.
- **State owners:** `MonoBehaviour`/`Component` instances, `ScriptableObject`
  assets/instances, ordinary managed objects, static fields, managers, and
  serialized references.
- **Timing:** frame/fixed callbacks, coroutine waits, animation/physics callbacks,
  custom accumulators, and explicit time APIs may use different time domains.
- **Persistence:** static lifetime, scene survival, and `DontDestroyOnLoad` do not
  prove save persistence.
- **Presentation:** UI, animation, audio, particles, and rendering may observe
  gameplay or feed callbacks back into it.

## 3. Semantic anchors

For managed implementation identity, prefer:

- exact relevant assembly hash;
- assembly name + namespace/type + member/full managed signature;
- field/property names and declaring types;
- strongly typed call sites, delegate/event subscriptions, and diagnostic strings;
- generated state-machine/closure relationships when they contain decisive logic.

Scope findings to the target build and relevant assembly hash. Use the managed
signature as the primary reusable locator; metadata tokens and IL offsets are
supporting locators for that exact assembly only.

When serialized configuration is material, retain the smallest evidence that
closes the relation: serialized field/member identity, relevant scene/prefab/asset
or local object identity, object references/overrides, configured callback target,
and provenance from declaration default through serialized/runtime assignment to
the material read or copy.

A serialized declaration proves only that a value/reference can participate in
serialization; it does not prove which value or object the shipped mechanic
consumes.

For engine dispatch, absence of a conventional managed xref does not prove a Unity
message or serialized-configured callback is unreachable. Conversely, a
lifecycle-shaped method name does not prove scenario-specific dispatch. Distinguish
ordinary managed calls, engine-dispatched messages, and serialized-configured
callbacks when the invocation source matters.

## 4. Managed fidelity and Unity object model

Stay at managed metadata, IL, and Unity object semantics while they close the
question. Do not invent Mono object headers, GC layouts, JIT code addresses, or
private Unity native layouts when managed evidence is sufficient.

Decompiler output is reconstructed source. Verify decisive IL when compiler
reconstruction can change the claim, and preserve generated coroutine/state-machine,
closure, iterator, async, or backing-member relationships when they carry the
material behavior.

For object identity and scope:

- `GameObject`/`Component` containment is not automatically gameplay ownership;
- a `ScriptableObject` reference may resolve to a shared asset, clone, or
  runtime-created instance;
- `static` indicates managed sharing, not save persistence or intended global
  ownership;
- `DontDestroyOnLoad` describes scene/session lifetime, not disk persistence;
- serialized values/references may be overridden or replaced before material
  consumption.

Runtime object identifiers and JIT/native addresses are session-scoped observation
context, not durable managed locators.

## 5. Recommended tracing workflow

Use the shortest Unity-specific progression that closes the unresolved relation:

```text
managed semantic anchor
  -> serialized value/reference/wiring when material
  -> invocation source when material
  -> runtime object identity/sharing when material
  -> decisive managed relation
  -> unmanaged boundary only when the unresolved fact crosses it
```

For serialized fields and Unity object references, recover only the relation that
can change the claim: effective value, referenced object/asset identity, sharing
or instance scope, composition relevant to ownership, or configured callback
wiring. Do not recover an entire scene/prefab/asset graph when a smaller relation
is sufficient.

Common pivots:

- **Field-backed:** resolve the value at material consumption and the actual
  instance only when ownership/fan-out matters.
- **Event/lifecycle-backed:** identify the invocation class and resolve the
  emitter/source or receiving instances only when caller/scope matters.
- **`ScriptableObject`-backed:** distinguish shared asset from clone/runtime
  instance only when identity changes the conclusion.

## 6. Static-analysis guidance

Inspect game-specific managed assemblies and metadata before escalating to native
analysis. Prefer targeted type/member/data-flow relationships over broad
assembly-wide decompilation.

Treat ordinary managed call graphs as partial evidence because engine dispatch,
reflection, serialized callbacks, delegates, and native bridges can create
material edges outside conventional xrefs.

## 7. Runtime-observation guidance

Apply the core runtime-validation gate. When live Unity realization remains
material, useful observation points include lifecycle/message or event entry,
values around the decisive mutation, coroutine progression, object
creation/clone/pooling/replacement, and scene/lifetime transitions.

Record enough context to distinguish material runtime instances, but keep runtime
instance identifiers and JIT/native addresses session-scoped.

## 9. Version-sensitive assumptions

Revalidate only version-sensitive Unity/Mono details used by the claim, including:

- Mono/runtime packaging and managed assembly layout;
- assembly splitting/code generation when it affects identity or recovery;
- serialization behavior relevant to a material field/reference/wiring relation;
- lifecycle, scene, domain/reload, or activation behavior when it affects
  dispatch, lifetime, or reset;
- generated shapes, metadata tokens, stripping, or optimization when used as
  evidence;
- managed-to-native transition details when the unresolved relation crosses that
  boundary.

## 10. Common failure modes

- Classifying the material path as Mono from one managed-looking artifact.
- Treating reconstructed C# as exact source when compiler behavior is material.
- Treating absence from managed xrefs as proof that an engine-dispatched or
  serialized-configured callback is unreachable.
- Reading a declaration default while missing a material serialized/runtime
  override.
- Recovering a whole prefab/scene graph when one serialized relation is enough.
- Inferring per-instance ownership from containment or a `ScriptableObject` field.
- Treating `static` or `DontDestroyOnLoad` state as save-persistent.
- Extending Mono assumptions across IL2CPP or an unmanaged boundary.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- exact relevant managed assembly hash;
- managed semantic locator plus optional same-assembly token/IL-offset support;
- serialized value/reference/wiring provenance at material consumption;
- invocation class/source when it affects the claim;
- generated implementation relation when it carries decisive behavior;
- explicit managed-to-unmanaged transition evidence when the claim crosses it.

## 12. Bundled tools

No Unity Mono helper is bundled. Treat recovery, decompilation, debugging, and
instrumentation tools as mechanical capabilities rather than gameplay-semantic
evidence.
