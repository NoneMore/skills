# Web / JavaScript Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Web/JavaScript mechanic to an authorized local/offline gameplay change. Require only the authority, ownership/shared-use, provenance, and version facts material to the currently viable mechanism and requested scope.

## Refine a Web/JS intervention from recovered scope

First select the mechanism class using [change-design.md](change-design.md); this guide does not override its cross-class ordering. Within the selected class, choose the narrowest local implementation point supported by the recovered facts:

- For a configuration or supported mod path, use the existing configuration/data owner of the intended rule.
- For a reversible local source/build override, prefer a source-level value or pure function whose consumers are within the requested scope.
- For a caller/event-limited intervention, use a narrow module wrapper, reducer/action boundary, worker handler, or call site when the underlying function/state is shared.
- For a shared intervention, use a broader state/update function only after materially distinct consumers and side effects are mapped and the requested behavior intentionally covers them.

Preserve original bundles. Apply source/bundle changes in a copied build/analysis tree, supported mod layer, or other reversible local override unless the user explicitly authorizes a destructive installed-file modification.

## Authority and order guards

Do not use a client-side display/prediction path as a substitute for a server-authoritative rule. If the finding establishes remote authority and the authoritative local artifact is unavailable, stop that application path rather than presenting a client change as authoritative.

For order-sensitive behavior, validate against the original bundle or another order-preserving representation; inspection-oriented module decomposition alone does not establish initialization order.

If a relation required by the selected candidate mechanism is missing or stale, return only that relation to `$analyze-game-logic` before applying the change.
