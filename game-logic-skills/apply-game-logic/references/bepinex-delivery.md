# BepInEx 5 Regular Plugin Delivery

Load this reference when the retained Unity Mono deliverable is a BepInEx 5
regular plugin under `BepInEx/plugins`. It adds only BepInEx-specific build,
lifecycle, and acceptance requirements and does not select the gameplay-change
mechanism.

This delivery surface does not cover BepInEx 6, preloader patchers, IL2CPP, or
direct Unity serialized-content patching.

## Build for the supported target

Retain the source project and build configuration under
[application-artifacts.md](application-artifacts.md); reuse an existing project
when suitable, and do not require a fixed template.

Target framework, Unity API compatibility, BepInEx 5 dependencies, and game
references must fit the supported target. If a referenced game assembly's exact
binary identity, member shape, or generated implementation is material to the
consumed evidence, build against the matching identity/hash; compilation against
another build does not extend that evidence. Other dependencies need only satisfy
the supported target unless their exact binary identity is itself material.

Reference layout is an implementation detail, not part of the application
contract.

## Require BepInEx-native acceptance

A retained regular plugin is not delivery-complete merely because it builds.
Before calling delivery complete:

- build the authoritative project for the supported target;
- deploy the produced plugin to `BepInEx/plugins`;
- start the supported target under actual BepInEx 5 and confirm the plugin loads;
- exercise the material application path and validate the claimed effect/scope
  under the main Skill.

If the supported target or BepInEx 5 runtime is unavailable, preserve the build
result as an **unvalidated BepInEx draft** and name the missing runtime acceptance
check. Retain the produced plugin plus the acceptance result or named gap under
`application-artifacts.md`.

## Validate only the claimed lifecycle

Do not require hot unload solely for delivery. Exercise any claimed in-session
disable, restoration, cleanup, config, command, or equivalent control path;
otherwise a documented remove/disable plus restart lifecycle is sufficient when
that is the retained restoration claim.

## Keep HarmonyX conditional and scoped

When the already-selected mechanism is implemented with HarmonyX, HarmonyX does
not make a hook preferable to a narrower mechanism. Use plugin-owned patch
identity and limit cleanup to this plugin's patches; do not remove unrelated
Harmony patches.
