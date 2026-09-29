# Gameplay Change Design

Load this reference only for a requested local/offline gameplay change.

## Establish scope before mechanism

Determine whether the candidate value, object, definition, field, or call path is shared across actors, sides, event sources, or gameplay contexts. Unresolved ownership/fan-out is a material unknown when it can broaden the effect.

When scope is missing, recover only that relation before choosing the change mechanism.

## Separate research instrumentation from deployment

Do not assume that the tool used to discover or validate a modification point must also be the final user-facing modification. Frida, debuggers, tracing hooks, or temporary runtime writes may be ideal for observing arguments, discriminating callers, and validating causal control while still being unnecessarily expensive or operationally awkward as a persistent delivery mechanism.

After the semantic modification point is established, choose the deployment artifact independently. Prefer the least runtime mediation that still preserves the required scope, lifecycle behavior, reversibility, and version safety.

## Prefer the least invasive adequate mechanism

Among options with acceptable behavioral scope, prefer:

1. existing configuration or supported mod interface;
2. reversible guarded runtime data change when a stable data target is sufficient;
3. guarded native instruction/data patch or narrow trampoline when the requested behavior can be expressed without ongoing high-frequency mediation;
4. dynamic hook/instrumentation runtime when caller/context filtering, lifecycle logic, or ongoing observation materially requires it;
5. destructive installed-file modification only with explicit authorization.

Reversibility does not prove narrow scope. This ordering is a deployment-selection heuristic, not a blanket performance ranking between tools.

For native PC targets where Cheat Engine is the selected delivery surface, load [cheat-engine-deployment.md](cheat-engine-deployment.md). That reference defines the delivery contract; it does not make Cheat Engine the default research or deployment tool.

## Guard the target

Bind the change to the exact target version/build/hash. For native interventions use stable module + RVA locators or a validated unique signature, and verify address conversions before use. A raw runtime address is not a stable cross-launch locator.

Before mutation, guard the expected original bytes/value/state where practical. If the installed target no longer matches the evidence or expected original state, stop and revalidate the material relation before applying the change.

## Preserve control state

Before destructive modification, record the original bytes/content, replacement, target hash, locator mapping, expected effect, known shared-use risk, and restoration procedure.

For retained/deployed changes follow [application-artifacts.md](application-artifacts.md).

## Validate scope

Compare control and modified behavior. Exercise only edge cases that can expose the claimed scope, such as other actors/event sources, pause/death/loading, scene transitions, save/reload, or relevant state variants.

A successful edit, freeze, hook, or patch demonstrates that the intervention worked in the observed scenario; it does not independently prove the underlying field/function semantics.

If the result contradicts the recovered mechanic itself, return the discrepancy to analysis instead of adding ad hoc filters.
