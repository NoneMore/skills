# Unity Mono Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Unity
Mono mechanic to an authorized local/offline gameplay change. Select the
mechanism class first with [change-design.md](change-design.md); this guide only
refines Unity/Mono-specific implementation within that class.

## Target the recovered effective owner

Consume the recovered managed, serialized, and runtime scope facts instead of
re-deriving them here. Choose the narrowest application point whose effective
owner and fan-out match the requested behavior.

A declaration default is not the application target when the finding establishes
that a scene, prefab, asset, configured reference, or later runtime assignment is
the value or object consumed by the mechanic. Conversely, do not prefer an easier
serialized override when the finding establishes that initialization or another
managed path has already copied authoritative state elsewhere before consumption.

Serialized Unity content is application evidence in this guide, not a guaranteed
retained delivery surface. Direct scene, prefab, asset, AssetBundle, or other
installed-content rewriting remains governed by the mechanism ordering and
rollback requirements in `change-design.md` and the main Skill.

## Preserve Unity object scope

Preserve recovered identity, sharing, lifetime, and reset relations when they are
material to scope:

- `GameObject`/`Component` containment does not by itself make a change
  actor-local;
- a `ScriptableObject` reference may denote a shared asset, clone, or
  runtime-created instance;
- `static` state is shared managed state, not proof of save persistence or intended
  global ownership;
- `DontDestroyOnLoad` establishes scene/session lifetime only within the scope
  recovered by analysis.

Do not mutate shared state and describe the result as instance-local unless the
finding establishes the required narrowing relation. If that relation is missing,
return only that material scope question to `$analyze-game-logic`.

## Bind retained managed implementations semantically

For a retained managed change, keep the exact supported target/build and relevant
managed assembly hash together with the semantic managed identity: assembly,
namespace/type, and member/full managed signature.

Metadata tokens and IL offsets may support that locator only for the exact
assembly they came from. Runtime object identifiers, JIT code addresses, native
method pointers, and other session-scoped observations are not durable managed
locators.

When generated coroutine/state-machine, closure, iterator, async, backing-member,
or similar generated code contains the decisive behavior, preserve the recovered
relationship between the user-facing member and the generated implementation.
Do not retarget a retained change to the more readable surface member when the
finding places the decisive behavior elsewhere.

Likewise, preserve the recovered invocation class. An ordinary managed call,
Unity engine-dispatched message, serialized callback, delegate, or event may
require different placement even when the visible method names are similar.

## Keep managed and native delivery boundaries distinct

A managed field/state change or managed patch delivered through a supported
managed plugin surface remains within this guide. If the retained implementation
instead writes JIT/native executable code, depends on private runtime/native
layouts, or crosses into a native plugin or engine-native boundary as its
material mutation surface, use the recovered transition evidence and the shared
native delivery contract rather than extending managed locator assumptions across
the boundary.

When the retained deliverable is a BepInEx 5 regular plugin for Unity Mono, also
load [bepinex-delivery.md](bepinex-delivery.md). That delivery guide does not
change the mechanism class selected here.

## Validate only material Unity scope edges

Compare control and modified behavior at the recovered material instances and
invocation sources. Exercise only edges capable of exposing the claimed scope,
such as sibling component instances, shared asset consumers, pooled or recreated
objects, relevant scene transitions, lifecycle re-entry, or the generated
execution path that actually carries the mechanic.

If validation exposes a missing or stale effective owner, object-identity,
invocation, generated-implementation, or managed/native-boundary relation, return
only that relation to `$analyze-game-logic` instead of reconstructing analysis in
the application guide.
