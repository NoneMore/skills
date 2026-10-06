# Gameplay Change Design

Load this reference only for a requested local/offline gameplay change.

## Establish scope before mechanism

Determine whether the candidate value, object, definition, field, or call path is shared across actors, sides, event sources, or gameplay contexts. Unresolved ownership/fan-out is a material unknown when it can broaden the effect.

When scope is missing, recover only that relation before choosing the change mechanism.

## Prefer the least invasive adequate mechanism

Among options with acceptable behavioral scope, prefer:

1. existing configuration or supported mod interface;
2. reversible runtime data change with version/value guards;
3. hook limited to the relevant caller/event source;
4. shared hook with evidence-backed filtering;
5. destructive installed-file modification only with explicit authorization.

Reversibility does not prove narrow scope.

After behavioral scope is established, load only the matching engine/runtime application guide when one is available and material to mechanism choice:

| Material implementation boundary | Application guide |
| --- | --- |
| GameMaker YYC | [change-gamemaker-yyc.md](change-gamemaker-yyc.md) |
| Web / JavaScript | [change-web-javascript.md](change-web-javascript.md) |

These application guides may rank engine-specific intervention choices. Analysis-side engine adapters supply the evidence and scope facts; they do not select the modification mechanism.

## Guard the target

Bind the change to the exact target version/build/hash. For native interventions use stable module + RVA locators and verify address conversions before use. A raw runtime address is not a stable cross-launch locator.

If the installed target no longer matches the evidence, stop and revalidate the material relation before applying the change.

## Preserve control state

Before destructive modification, record the original bytes/content, replacement, target hash, locator mapping, expected effect, known shared-use risk, and restoration procedure.

For retained/deployed changes follow [application-artifacts.md](application-artifacts.md).

## Validate scope

Compare control and modified behavior. Exercise only edge cases that can expose the claimed scope, such as other actors/event sources, pause/death/loading, scene transitions, save/reload, or relevant state variants.

If the result contradicts the recovered mechanic itself, return the discrepancy to analysis instead of adding ad hoc filters.
