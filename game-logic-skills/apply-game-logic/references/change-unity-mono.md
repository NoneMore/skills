# Unity Mono Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Unity
Mono mechanic to an authorized local/offline gameplay change. Select the
mechanism class first with [change-design.md](change-design.md); this guide only
refines Unity/Mono-specific implementation within that class.

## Apply the recovered Unity relations

Consume the recovered effective owner, object identity/sharing, lifetime/reset,
invocation, generated-implementation, and managed/native-boundary relations
instead of re-deriving them here. Choose the narrowest application point whose
recovered fan-out matches the requested behavior.

A declaration, serialized value/reference, or later managed state is an
application target only when the finding establishes that it is the state
materially consumed by the mechanic. Do not mutate recovered shared state and
claim an instance-local result. If a relation needed by the selected mechanism is
missing or stale, return only that relation to `$analyze-game-logic`.

Serialized Unity content is application evidence here, not a guaranteed retained
delivery surface. Direct installed-content rewriting remains governed by
[change-design.md](change-design.md) and the main Skill.

## Bind retained managed targets

For a retained managed change, preserve the recovered semantic managed target and
supported target/build. Keep an exact managed assembly hash when that assembly's
binary identity, member shape, or generated implementation is material to the
consumed evidence. Assembly-scoped metadata tokens or IL offsets may support that
semantic target but do not broaden it to another assembly build.

Preserve any recovered generated-implementation or invocation relation that
controls placement; do not retarget to a more convenient surface member merely
because it is easier to name.

## Keep managed and native mutation surfaces distinct

Managed state changes and managed patches delivered through a supported managed
plugin surface remain within this guide. If the retained mutation instead writes
JIT/native executable code or materially depends on a native/private runtime
layout, use the recovered transition evidence and the shared native delivery
contract.

When the retained deliverable is a BepInEx 5 regular plugin for Unity Mono, also
load [bepinex-delivery.md](bepinex-delivery.md). That delivery guide does not
change the selected mechanism class.

## Validate material Unity scope edges

Compare control and modified behavior at the recovered material instances and
invocation sources. Exercise only recovered edges capable of exposing the claimed
scope, such as a sibling/shared consumer, recreated object, scene/lifecycle edge,
or generated execution path. If validation reveals a missing or stale recovered
relation, return only that relation to `$analyze-game-logic`.
