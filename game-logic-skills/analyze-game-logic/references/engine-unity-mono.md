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

Classify a material boundary as Unity Mono from mutually supporting indicators,
such as:

- a Unity player data directory with managed assemblies under `Managed`;
- game-specific assemblies such as `Assembly-CSharp.dll` or equivalent project
  assemblies;
- Mono runtime artifacts consistent with the player platform and build;
- Unity engine managed assemblies and metadata consistent with the same target.

Corroborate both the shipped backend and the implementation path responsible for
the mechanic; one managed-looking artifact is insufficient.

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

Use Unity constructs as search/evidence anchors, not automatic proof of ownership
or causality:

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

Prefer exact relevant assembly hash plus semantic managed identity:

- assembly name + namespace/type + member/full managed signature;
- field/property names and declaring types;
- strongly typed call sites, delegate/event subscriptions, and diagnostic strings;
- generated state-machine/closure relationships when they contain decisive logic.

Scope findings to the target build and relevant assembly hash. Use the managed
signature as the primary reusable locator; metadata tokens and IL offsets support
only that exact assembly.

When serialization matters, retain the smallest relevant field/member,
scene/prefab/asset or local-object identity, reference/override, configured
callback target, and assignment-to-consumption provenance.

For invocation, distinguish ordinary managed calls, engine-dispatched messages,
and serialized-configured callbacks. Absence of a conventional managed xref does
not make the latter two unreachable, and a lifecycle-shaped name alone does not
prove scenario-specific dispatch.

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

For serialized fields and Unity object references, recover only what can change
the claim: effective value, referenced object/asset identity, sharing/instance
scope, ownership-relevant composition, or configured callback wiring. A serialized
declaration alone does not establish the consumed value/object, and a whole
scene/prefab/asset graph is unnecessary when a smaller relation closes the claim.

Common pivots:

- **Field-backed:** resolve the value at material consumption and the actual
  instance only when ownership/fan-out matters.
- **Event/lifecycle-backed:** resolve invocation class and emitter/source or
  receiving instances only when caller/scope matters.
- **`ScriptableObject`-backed:** distinguish shared asset from clone/runtime
  instance only when identity changes the conclusion.

## 6. Static-analysis guidance

Inspect game-specific managed assemblies and metadata before escalating to native
analysis. Prefer targeted type/member/data-flow relationships over broad
assembly-wide decompilation. Treat ordinary managed call graphs as partial where
engine dispatch, reflection, serialized callbacks, delegates, or native bridges
can supply material edges.

## 7. Runtime-observation guidance

Apply the core runtime-validation gate. When live Unity realization remains
material, useful observation points include lifecycle/message or event entry,
values around the decisive mutation, coroutine progression, object
creation/clone/pooling/replacement, and scene/lifetime transitions. Record enough
context to distinguish material runtime instances.

## 9. Version-sensitive assumptions

Revalidate only Unity/Mono details used by the claim, including:

- Mono/runtime packaging and managed assembly layout;
- assembly splitting/code generation when it affects identity or recovery;
- material serialization behavior;
- lifecycle, scene, domain/reload, or activation behavior when it affects
  dispatch, lifetime, or reset;
- generated shapes, metadata tokens, stripping, or optimization when used as
  evidence;
- managed-to-native transition details when the unresolved relation crosses that
  boundary.

## 10. Common failure modes

- Classifying the material path as Mono from one managed-looking artifact.
- Treating reconstructed C# as exact source when compiler behavior is material.
- Treating managed xrefs as a complete invocation graph.
- Reading a declaration default while missing a material serialized/runtime
  override.
- Inferring per-instance ownership from containment or a `ScriptableObject` field.
- Extending Mono assumptions across IL2CPP or an unmanaged boundary.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- exact relevant managed assembly hash and semantic locator;
- optional token/IL-offset support scoped to that assembly;
- serialized value/reference/wiring provenance at material consumption;
- invocation class/source when it affects the claim;
- generated implementation relation when it carries decisive behavior;
- managed-to-unmanaged transition evidence when the claim crosses it.

## 12. Bundled tools

No Unity Mono helper is bundled.
