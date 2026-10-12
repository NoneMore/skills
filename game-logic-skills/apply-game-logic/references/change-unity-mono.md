# Unity Mono Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Unity
Mono mechanic to an authorized local/offline gameplay change. Select the
mechanism class first with [change-design.md](change-design.md); this guide only
refines Unity/Mono-specific implementation within that class.

## Apply recovered Unity relations

Use the recovered effective owner, object identity/sharing, lifetime/reset,
invocation, generated-implementation, and managed/native-boundary relations.
Choose the narrowest application point whose recovered fan-out matches the
requested behavior.

Target a declaration, serialized value/reference, or later managed state only
when the finding establishes that it is materially consumed. Do not mutate
recovered shared state and claim an instance-local result. If the selected
mechanism depends on a missing or stale relation, return only that relation to
`$analyze-game-logic`.

Serialized Unity content is evidence here, not a guaranteed retained delivery
surface; installed-content rewriting remains governed by
[change-design.md](change-design.md) and the main Skill.

## Bind retained managed targets

Preserve the recovered semantic managed target and supported target/build. Require
an exact managed assembly identity/hash only when its binary identity, member
shape, or generated implementation is material to the consumed evidence;
metadata tokens and IL offsets remain scoped to that assembly build.

Preserve recovered generated-implementation and invocation relations that control
placement rather than retargeting to a more convenient surface member.

## Respect mutation and delivery boundaries

If the retained implementation crosses into a native mutation surface or
materially depends on a native/private runtime layout, use the recovered
transition evidence and the shared native delivery contract.

For a BepInEx 5 regular plugin, also load
[bepinex-delivery.md](bepinex-delivery.md); it does not change the selected
mechanism class.

## Validate Unity-specific scope

Under the main Skill's validation rules, exercise only recovered edges capable of
exposing the claimed scope, such as a sibling/shared consumer, recreated object,
scene/lifecycle edge, or generated execution path.
