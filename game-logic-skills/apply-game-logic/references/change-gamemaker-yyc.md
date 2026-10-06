# GameMaker YYC Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered GameMaker YYC mechanic to an authorized local/offline gameplay change. Require only the YYC facts material to the currently viable mechanism and requested scope; do not demand unrelated ownership, caller, type/lifetime, or locator facts up front.

## Refine a YYC intervention from recovered scope

First select the mechanism class using [change-design.md](change-design.md); this guide does not override its cross-class ordering. Within the selected class, choose the narrowest YYC implementation point supported by the recovered facts:

- For a reversible runtime data change, use a uniquely referenced static numeric runtime value when it controls only the intended source, or a live global/instance value only after its `RValue` kind, owner, lifetime, reference-management behavior, and reset path are established.
- For a caller/event-limited hook, intercept one call site or discriminate by return address when a shared callee receives materially different values from different sources.
- For a shared hook, use the shared script/event only when the requested behavior intentionally applies to every evidenced source that reaches it.

Shared refresh functions are a common source of scope leakage. Do not choose a shared hook merely because it is convenient or reversible; caller/source evidence must justify the requested fan-out.

## Runtime guards and restoration

For writes or hooks, guard on the strongest available combination of exact target hash, module identity/size, expected original bytes/value, validated `module + RVA` or signature, argument/runtime-value kind, and the caller/source relation that establishes scope.

Detaching instrumentation does not necessarily restore a raw memory write. Capture the control/original state and use an explicit restoration path appropriate to the selected mechanism.

If a relation required by the selected candidate mechanism is missing or stale, return only that relation to `$analyze-game-logic` before applying the change.
