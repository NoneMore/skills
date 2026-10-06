# Godot GDScript Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Godot
GDScript/scene/resource mechanic to an authorized local/offline gameplay change.
Select the mechanism class first with [change-design.md](change-design.md); this
guide only refines Godot-specific implementation within that class.

## Refine a Godot intervention from recovered scope

Choose the narrowest point supported by the recovered ownership, fan-out, and
consumption-time facts:

- For configuration or supported mod changes, use the specific project, scene,
  resource, or mod-interface value that uniquely controls the requested behavior.
- For script changes, use the recovered callback, signal/caller edge, or
  base/override implementation whose fan-out matches the requested scope.
- For reversible runtime changes, use a live Node/Resource/autoload value only
  when the finding establishes its identity, sharing, lifetime/reset behavior,
  and effective type.

Consume analysis facts rather than re-deriving them here. In particular, target
the recovered consumption-time owner for exported properties, preserve recovered
base/derived ownership, and do not treat a shared `Resource` mutation as
per-instance unless the finding establishes locality or duplication. Apply the
same recovered distinction between autoload session lifetime and save persistence.

## Scene/resource and pack changes

A scene/resource override can be narrower than a code change only when the
recovered graph establishes the consuming instances and scope. Preserve any
material inherited-scene, shared-resource, or duplication relation from the
finding.

PCK creation or patch tooling does not make an installed-pack edit preferable.
Destructive pack/executable modification remains the last mechanism class in
[change-design.md](change-design.md) and still requires the core authorization
and rollback preconditions.

## Runtime guards and restoration

For runtime changes, guard on the strongest available combination of exact
target hash/version, `res://` locator, expected original value/state,
scene/resource identity, and the caller/emitter relation establishing scope.

Restoring one property may not undo side effects already emitted through
signals, scene transitions, saves, or spawned objects; make restoration behavior
explicit for the selected mechanism.

## Validation

Compare control and modified behavior at the material instances and event
sources, exercising only recovered scope edges that can reveal leakage or stale
ownership. If validation exposes a missing ownership, timing, sharing, or
C#/.NET/GDExtension/native relation, return only that relation to
`$analyze-game-logic` rather than reconstructing it in the application guide.
