# Cheat Engine Deployment

Load this reference only when a validated native PC gameplay change is being delivered through Cheat Engine, or when a Cheat Engine table/Auto Assembler artifact is the material deployment option. It complements `change-design.md`; it does not replace mechanic recovery or runtime validation.

## Role in the workflow

Treat Cheat Engine primarily as a deployment and targeted runtime-inspection surface after the relevant mechanic, ownership/fan-out, and version-scoped modification point are understood.

Do not make Cheat Engine the default research tool merely because the final artifact may use it. Frida, a debugger, static analysis, or another observational tool may be better for discovering callers, arguments, lifecycle, or causal control. Conversely, discovery instrumentation does not have to remain in the final deliverable.

If a material mechanic relation is missing or stale, return only that relation to $analyze-game-logic instead of guessing it during deployment.

## Delivery contract

A reusable Cheat Engine artifact should make the following explicit when applicable:

- exact target game/module version or hash;
- stable `module + RVA` locator or a validated unique signature;
- expected original bytes/value/state before applying the change;
- the intended semantic effect and its actor/source/context scope;
- enable behavior and disable/restoration behavior;
- assumptions about object lifetime, pointer validity, or state initialization;
- known side effects and conditions under which the artifact must refuse to act.

Prefer a direct guarded data or code change when it expresses the requested behavior completely. Use an injected trampoline or more dynamic mechanism only when the required scope cannot be preserved by the simpler form.

## Evidence boundaries

A successful memory edit, freeze, or patch demonstrates that the intervention worked in the observed scenario; it does not by itself establish what the field, function, or branch means. Keep semantic claims tied to the finding/mechanic evidence that established them.

Do not promote pointer chains, signatures, structure layouts, or field meanings from convenience guesses into confirmed facts. Version-sensitive assumptions remain version-scoped findings.

## Runtime-cost considerations

When two mechanisms preserve the same intended scope and reliability, prefer the one that performs less work in a hot gameplay path. In particular, avoid keeping a high-frequency managed callback solely because it was convenient during research when a guarded native write or patch can express the same behavior.

This is a selection principle, not a blanket claim that one tool is always faster or more appropriate than another. Dynamic context filtering, lifecycle handling, or observation requirements can justify a runtime hook.

## Validation and cleanup

Validate the delivered artifact against the same control/modified comparison used for other gameplay changes. Confirm that disable/restoration returns the modified code or persistent state to the documented control condition where technically possible, and state any restoration limitations explicitly.

For retained/deployed artifacts, keep the authoritative table/script source, target identity, consumed mechanic finding, validation result, and rollback/control state together under the normal application-artifact rules.
