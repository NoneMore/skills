# Godot GDScript Engine Adapter

This adapter covers Godot gameplay logic implemented in GDScript together with
the scene/resource graph that configures or invokes it. Apply the core evidence
and project-knowledge rules from `SKILL.md`; this file supplies Godot-specific
anchors, lifecycle mappings, and tracing tactics.

Treat C#/.NET assemblies, GDExtension/GDNative libraries, and engine-native code
as separate implementation boundaries. When a material path crosses one of
those boundaries, record the transition and continue with the appropriate core
workflow rather than extending GDScript assumptions across it.

## 1. Applicability and detection

Use multiple mutually supporting indicators, for example:

- `project.godot`, `res://` paths, and Godot project-setting keys;
- `.gd` or compiled `.gdc` scripts;
- `.tscn`/`.scn` scenes and `.tres`/`.res` resources;
- script attachments, `ExtResource`/`SubResource` references, signal
  connections, autoload entries, or input actions;
- Godot runtime/export strings or a PCK/embedded pack consistent with the other
  indicators.

Do not classify the material gameplay boundary as GDScript from a Godot
executable or PCK alone. A Godot title can place the relevant logic in C#,
GDExtension/GDNative, or another native module.

When the readable project is unavailable and the material path is inside an
exported Godot artifact, load [godot-gdretools.md](godot-gdretools.md) for the
smallest necessary GDRETools recovery step. Do not recover the entire project
merely because the tool can do so.

## 2. Implementation model

A useful GDScript-oriented model is:

```text
project settings / autoloads
        +
scene and resource graph
        -> instantiated Nodes / Resources
        -> attached GDScript
        -> inheritance / base-script resolution
        -> callbacks, signals, Callables, explicit calls
        -> authoritative state mutation
```

Scenes and resources are not just containers. They can serialize values that
override script defaults, wire signals, select scripts/resources, and instantiate
the object graph that determines which logic runs.

### Gameplay semantic mapping

Validate these mappings against the target Godot version and recovered project:

- **Lifecycle/update:** `_init`, `_enter_tree`, `_ready`, `_process`,
  `_physics_process`, `_exit_tree`, scene changes, and explicit enable/disable
  state are strong lifecycle anchors when present.
- **Triggers:** signals and their connections, input callbacks/actions, `Timer`
  timeouts, collision/body/area callbacks, animation method calls, Callables,
  and explicit method calls are useful source/caller anchors.
- **State owners:** script members, serialized scene/resource properties,
  `Resource` objects, autoload singletons, project settings, and explicit
  save-state objects are candidates. Establish actual owner, fan-out, and
  lifetime from data flow and instancing rather than from the declaration site.
- **Timing:** callback `delta`, physics ticks, `Timer` configuration/state,
  Tween/Animation progression, custom accumulators, or explicit clock APIs can
  define different time domains. Do not convert counters to seconds without
  evidence for the active domain.
- **Persistence:** autoload lifetime is not proof of save persistence. Trace the
  concrete save/load/checkpoint/reset path when persistence is material.
- **Presentation:** Control/CanvasItem/audio/particles are usually observers, but
  signals, AnimationPlayer method tracks, or script callbacks can cross back
  into gameplay. Follow data flow before classifying them as presentation-only.

## 3. Semantic anchors

Prefer anchors that preserve resource relationships:

- `project.godot` main-scene and autoload entries;
- scene/resource script attachments and `res://` paths;
- `class_name`, `extends`, base-script/global-class relationships, `super`,
  `preload`, `load`, and explicit `PackedScene`/`Resource` paths;
- signal declarations plus scene/code connections;
- exported properties and serialized scene/resource values;
- input-action names, semantic node/resource names, and diagnostic strings.

A script attachment proves association, not authoritative ownership. Resolve
the material GDScript inheritance chain before treating the attached script as
the implementation owner: a declaration or method may live in a base global
class, another script file, or an inner class, and an overriding method may
delegate back to its parent through version-appropriate parent-call semantics.
A signal receiver proves that one receiver exists, not which emitter or
connection caused the observed event.

For an exported property, distinguish the script default, serialized
scene/resource value, and the value at the point where gameplay consumes it.
Saved scene/resource assignments can occur after object initialization, so an
`_init()` read or copy can observe the script default even when the instance
later receives a different serialized value. A property setter can also transform
or react to that assignment. Follow the target-version initialization order,
setters, later runtime assignments, and the first material read/copy before
calling any value authoritative for the mechanic.

If GDRETools was required, treat its recovered paths, scripts, and resources as
reconstructed artifacts. Record the recovery/tool version when material and
corroborate the mechanic relation rather than treating successful recovery as
behavioral proof.

## 4. ABI, runtime values, and object model

Stay at Godot resource/GDScript semantics while they close the question. Treat
`Node`, `Resource`/`RefCounted`, `Object`, `Variant`, `Callable`, `Signal`, and
`NodePath` according to observed project use and the target engine version.

Scene-tree parent/owner relationships are not automatically gameplay-state
ownership. Likewise, reference-counted resource lifetime is not proof that a
value is unique to one actor or scene instance.

For a material `Resource`, establish runtime identity and fan-out rather than
inferring isolation from the field that references it. Check whether it is an
external or built-in resource, whether path-based loading can return a shared
cached instance, whether `resource_local_to_scene` changes instancing behavior,
and whether `duplicate()`/`duplicate_deep()` or runtime reassignment creates a
distinct object before treating a mutation as per-instance.

Do not invent native `Variant` layouts, object offsets, VM bytecode structures,
or calling conventions. If a material relation crosses into C#/.NET,
GDExtension/GDNative, or engine-native code, preserve the GDScript-side caller
and transition evidence and continue outside this adapter.

## 5. Recommended tracing workflow

For mechanic reconstruction, prefer:

```text
project/autoload/main-scene anchor
  -> relevant scene/resource instance
  -> attached script or configured property
  -> material extends/base-script chain when present
  -> callback, signal connection, Callable, or explicit caller
  -> decisive state read/write
  -> reset, scene-reload, fan-out, and persistence paths when material
  -> controlled runtime validation when material
```

For property-backed mechanics, establish the value at the material consumption
point rather than stopping at either the script declaration or serialized
override. Check initialization order, setters, `_init()`/`_ready()` reads or
copies, material serialized overrides, and later runtime assignments before
concluding which value controls behavior.

For resource-backed mechanics, establish whether consumers share one `Resource`
instance or receive local/duplicated instances before using a resource mutation
to infer scope.

For signal-driven mechanics, identify both emitter and receiver and the actual
connection path. If the receiver is shared, establish which emitters or scene
instances can reach it before claiming scope.

For autoload-owned state, distinguish process/session lifetime from save-file
persistence and determine whether scene instances share the same state.

## 6. Static-analysis guidance

Search readable `.gd`, `.tscn`, `.tres`, and `project.godot` content before
escalating. Prefer resource/script relationships and semantic paths over broad
string scans.

When a relevant scene/resource is binary or GDScript is compiled, use the
smallest GDRETools recovery/conversion path that exposes the unresolved relation.
Recovered GDScript is decompiler output, not guaranteed original source; keep
that provenance visible when exact source form matters.

Collapse boilerplate resource declarations and focus on script references,
`extends`/parent-call relationships, serialized property overrides, signal
connections, autoloads, preload/load targets, resource identity/sharing, and
scene transitions. Do not escalate to native engine analysis while these layers
already close the mechanic.

## 7. Runtime-observation guidance

Useful Godot observation points include material callback entry, signal emission
and receiver entry, `Timer` refresh/timeout, before/after the authoritative
property mutation, scene reload/replacement, and save/load/reset paths.

When a runnable project or supported debugger is available, prefer minimally
invasive logging/debugger-visible state over native hooks for GDScript claims.
A recovered project that runs is still a reconstructed environment; if plugins,
imports, export settings, or engine version differ from the shipped target,
validate any behavior-sensitive claim against the original target when practical.

## 9. Version-sensitive assumptions

Revalidate per target rather than hard-coding:

- Godot major/minor/patch version and GDScript bytecode revision;
- export preset, pack/container layout, and script/resource representation;
- textual versus binary scene/resource serialization;
- exported-property assignment order, setter behavior, and lifecycle semantics;
- GDScript inheritance/parent-call semantics;
- `ResourceLoader` cache behavior, `resource_local_to_scene`, and duplication;
- signal/lifecycle API details and engine-version semantics;
- C#/.NET, GDExtension/GDNative, and engine-native transitions;
- GDRETools recovery/decompilation behavior for the detected target version.

## 10. Common failure modes

- Treating every Godot title as a GDScript target.
- Reading an exported-property default but missing a scene/resource override.
- Treating a serialized override as authoritative without checking whether the
  mechanic consumed or copied the default earlier in initialization.
- Stopping at the attached subclass and missing an inherited declaration,
  override, or parent call that contains the material behavior.
- Treating a `Resource` field as per-instance without checking path-cache sharing,
  `resource_local_to_scene`, duplication, or runtime reassignment.
- Treating a signal receiver as proof of the emitting source or requested scope.
- Assuming an autoload value is save-persistent because it survives scene changes.
- Treating AnimationPlayer or UI code as presentation-only without following
  method calls/signals back into gameplay.
- Treating successful GDRETools recovery as proof of gameplay ownership or exact
  original source.
- Recovering a full project when a file listing, script subset, or one resource
  conversion would close the claim.
- Escalating to native analysis before exhausting the material readable graph.
- Extending GDScript assumptions across a C#/.NET or GDExtension/native boundary.

## 11. Evidence checklist

When material, supplement the core mechanic record with:

- detected Godot version/export form and exact target hash;
- GDRETools version/recovery provenance when recovery was required;
- effective `res://` scene/resource/script locator;
- material GDScript base-script/override/parent-call relation when present;
- script default, serialized/runtime assignment, and material consumption-time
  value relation;
- callback/signal/caller path, including emitter and receiver when relevant;
- Node/Resource/autoload owner, instance fan-out, resource sharing/locality,
  reset, and save/load behavior;
- explicit transition evidence into C#/.NET, GDExtension/GDNative, or native code.

## 12. Bundled tools

No Godot helper is bundled. Use GDRETools as the preferred external recovery and
GDScript decompilation tool only when exported artifacts or binary resources
block the material relation; load [godot-gdretools.md](godot-gdretools.md) for
that path. Treat the tool as a mechanical recovery capability, not as semantic
evidence.