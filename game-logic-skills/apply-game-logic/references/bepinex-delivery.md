# BepInEx 5 Regular Plugin Delivery

Load this reference when the retained Unity Mono deliverable is a BepInEx 5
regular plugin under `BepInEx/plugins`. This guide adds only BepInEx-specific
build, lifecycle, and acceptance requirements; it does not select the gameplay
change mechanism.

This guaranteed delivery surface does not cover BepInEx 6, preloader patchers,
IL2CPP, or direct Unity serialized-content patching.

## Build for the supported target

Retain the source project and build configuration that produce the shipped plugin
as the authoritative implementation under
[application-artifacts.md](application-artifacts.md). Reuse an existing project
when suitable; no fixed project template is required.

Target framework, Unity API compatibility, BepInEx 5 dependencies, and game
references must be compatible with the supported target. When a referenced game
assembly's exact binary identity, member shape, or generated implementation is
part of the consumed evidence, build against the matching identity/hash;
successful compilation against another build does not extend that evidence.
Other dependencies need only satisfy the supported target unless their exact
binary identity is itself material.

How target assemblies are resolved for compilation is an implementation detail,
not part of the application contract.

## Require BepInEx-native acceptance

A retained BepInEx 5 regular plugin is not delivery-complete merely because it
builds. Before calling delivery complete:

- build the authoritative project for the supported target;
- deploy the produced plugin to `BepInEx/plugins`;
- start the supported target under actual BepInEx 5 and confirm the plugin loads;
- exercise the material application path; and
- validate the claimed gameplay effect and behavioral scope under the main Skill.

If the supported target or BepInEx 5 runtime is unavailable, preserve the build
result but report it as an **unvalidated BepInEx draft** and name the missing
runtime acceptance check.

## Validate only the lifecycle the plugin claims

Do not require hot unload solely to satisfy delivery. If the plugin exposes an
in-session disable, restoration, cleanup, config toggle, command, or equivalent
control path, exercise the claimed path. Otherwise a documented remove/disable
plus restart lifecycle is sufficient when that is the retained restoration claim.

## When the selected implementation uses HarmonyX

Apply this section only when the already-selected mechanism is implemented with
HarmonyX. HarmonyX does not make a hook preferable to a narrower mechanism.

Use plugin-owned patch identity and limit cleanup to this plugin's patches. A
claimed disable or cleanup path must not remove unrelated Harmony patches.
Exercise any claimed in-session patch removal/restoration path as part of BepInEx
acceptance.

## Retain BepInEx delivery evidence

Follow [application-artifacts.md](application-artifacts.md) and additionally retain
the produced plugin artifact plus the BepInEx acceptance result or named gap.
