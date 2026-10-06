# Godot GDScript Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Godot
GDScript/scene/resource mechanic to an authorized local/offline gameplay change.
Select the mechanism class first with [change-design.md](change-design.md); this
guide refines Godot-specific implementation points within that class and does
not override the cross-class ordering.

## Refine a Godot intervention from recovered scope

Within the selected mechanism class, choose the narrowest semantic point that is
already supported by the recovered ownership/fan-out facts:

- For configuration or supported mod changes, prefer the specific project,
  scene, resource, or mod-interface value that uniquely controls the requested
  behavior.
- For script changes, prefer the material callback, signal connection, emitter,
  receiver, or explicit call site whose evidenced fan-out matches the requested
  scope.
- For reversible runtime state changes, use a live Node/Resource/autoload value
  only after its owner, instance sharing, reset/lifetime, and effective type are
  established.
- For shared receivers or helpers, narrow at the emitter/connection/caller when
  different sources require different behavior. Use the shared point only when
  the requested change intentionally applies to every evidenced source.

For exported properties, distinguish the script default from serialized scene or
resource overrides and runtime assignments. Modify the effective owner rather
than whichever declaration is easiest to find.

For autoload-owned state, establish whether the requested behavior is intended
to span scene changes and whether save/load logic persists the value. Session
lifetime and save persistence are separate scope dimensions.

## Scene/resource and pack changes

A scene/resource override can be narrower and more semantic than a code change,
but only when the recovered graph proves which instances consume it. Validate
inherited scenes, duplicated resources, and shared subresources when they can
broaden the effect.

The existence of PCK creation/patch tooling does not make an installed-pack edit
the preferred mechanism. A destructive pack/executable change remains the last
mechanism class in [change-design.md](change-design.md) and requires the core
write-authorization and rollback preconditions before modification.

Do not select a destructive patch merely because GDRETools or another pack tool
can mechanically produce it.

## Runtime guards and restoration

For runtime changes, guard on the strongest available combination of exact
target hash/version, effective `res://` locator, expected original value/state,
scene/resource identity, and the caller/emitter relation that establishes scope.

Restoring one property value may not undo side effects already emitted through
signals, scene transitions, saves, or spawned objects. Make restoration behavior
explicit for the selected mechanism.

## Validation

Compare control and modified behavior at the actual scene/resource instances and
event sources that can expose leakage. When material, exercise scene reload,
instance recreation, autoload lifetime, save/load, inherited scenes/resources,
and alternate signal emitters.

If validation shows that the recovered relation actually crosses into C#/.NET,
GDExtension/GDNative, or engine-native logic, return only that missing boundary
relation to `$analyze-game-logic` rather than patching around it.