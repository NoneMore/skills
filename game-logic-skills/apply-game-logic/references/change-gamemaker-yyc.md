# GameMaker YYC Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered GameMaker YYC mechanic to an authorized local/offline gameplay change. The mechanic finding must already contain the YYC ownership, caller/source, type/lifetime, locator, and version facts material to scope.

## Choose a YYC intervention from recovered scope

After the generic mechanism ordering in [change-design.md](change-design.md), prefer the narrowest YYC intervention that matches the evidenced behavior:

1. Change a uniquely referenced static numeric runtime value when the finding shows it controls only the intended source.
2. Intercept one call site or discriminate by return address when a shared callee receives materially different values from different sources.
3. Hook a shared script/event only when the requested behavior intentionally applies to every evidenced source that reaches it.
4. Modify a live global/instance runtime value only after its `RValue` kind, owner, lifetime, reference-management behavior, and reset path are established.

Shared refresh functions are a common source of scope leakage. Do not choose a shared hook merely because it is convenient or reversible; caller/source evidence must justify the requested fan-out.

## Runtime guards and restoration

For writes or hooks, guard on the strongest available combination of exact target hash, module identity/size, expected original bytes/value, validated `module + RVA` or signature, argument/runtime-value kind, and the caller/source relation that establishes scope.

Detaching instrumentation does not necessarily restore a raw memory write. Capture the control/original state and use an explicit restoration path appropriate to the selected mechanism.

If the required YYC type, ownership, caller discrimination, or version relation is missing or stale, return only that relation to `$analyze-game-logic` before applying the change.
