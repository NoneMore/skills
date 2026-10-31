# Gameplay Change Design

Load this reference only for a requested local/offline gameplay change.

## Establish scope before mechanism

Determine whether the candidate value, object, definition, field, or call path is shared across actors, sides, event sources, or gameplay contexts. Unresolved ownership/fan-out is a material unknown when it can broaden the effect.

When scope is missing, recover only that relation before choosing the change mechanism.

## Prefer the least invasive adequate mechanism

Among options with acceptable behavioral scope, prefer:

1. existing configuration or supported mod interface;
2. reversible runtime data change with material target and runtime guards;
3. hook limited to the relevant caller/event source;
4. shared hook with evidence-backed filtering;
5. destructive installed-file modification only with explicit authorization.

Reversibility does not prove narrow scope.

After behavioral scope and mechanism class are established, load only the matching engine/runtime application guide when one is available and material to selecting an implementation point within that class:

| Material implementation boundary | Application guide |
| --- | --- |
| Godot GDScript / scene-resource graph | [change-godot-gdscript.md](change-godot-gdscript.md) |
| Unity Mono | [change-unity-mono.md](change-unity-mono.md) |
| Web / JavaScript | [change-web-javascript.md](change-web-javascript.md) |
| RPG Maker MV/MZ project, events and plugins | [change-rpgmaker-mv-mz.md](change-rpgmaker-mv-mz.md) |

For RPG Maker-owned gameplay, prefer its guide over generic Web/JavaScript guidance even when plugins use readable JavaScript. Load the Web/JavaScript guide additionally only for a distinct, material JS boundary.

This file remains authoritative for ordering across mechanism classes. Matching application guides refine engine-specific implementation points only within the selected class; they do not override this ordering. Analysis-side engine adapters supply the evidence and scope facts; they do not select the modification mechanism.

Windows LÖVE/Lua needs no separate application guide: consume the recovered Lua source/owner/scheduler/thread facts under this shared contract. If a retained Lua mod is delivered through Lovely Injector, load [lovely-delivery.md](lovely-delivery.md).

Native-code boundaries without independent application semantics, including GameMaker YYC, consume recovered engine-specific facts through the shared application contracts rather than an engine-specific application guide. When the selected mechanism is a retained native runtime mutation, the main Skill routes to `native-runtime-delivery.md`.

## Guard the target

Bind the change to the exact target version/build/hash. For native interventions, use the native locator policy from the main Skill.

If the installed target no longer matches the evidence, stop and revalidate the material relation before applying the change.

## Preserve control state

Before destructive modification, satisfy the rollback precondition in [SKILL.md](../SKILL.md), then record the original bytes/content, replacement, target hash, locator mapping, expected effect, known shared-use risk, and restoration procedure.

For retained/deployed changes follow [application-artifacts.md](application-artifacts.md).

## Validate scope

Compare control and modified behavior. Exercise only edge cases that can expose the claimed scope, such as other actors/event sources, pause/death/loading, scene transitions, save/reload, or relevant state variants.

If the result contradicts the recovered mechanic itself, return the discrepancy to analysis instead of adding ad hoc filters.
