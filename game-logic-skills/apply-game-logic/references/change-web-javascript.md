# Web / JavaScript Change Guidance

Load this reference only when `$apply-game-logic` is applying a recovered Web/JavaScript mechanic to an authorized local/offline gameplay change. The mechanic finding must already establish the local authority boundary, relevant module/state owner, shared-use risks, stable provenance, and version/hash scope.

## Choose a Web/JS intervention from recovered scope

After the generic mechanism ordering in [change-design.md](change-design.md), prefer the narrowest local mechanism supported by the recovered facts:

1. Existing configuration or data tables that own the intended rule.
2. A local source-level value or pure function whose consumers are within the requested scope.
3. A narrow local module wrapper, reducer/action boundary, worker handler, or call site when the underlying function/state is shared.
4. A broader shared state/update function only after materially distinct consumers and side effects are mapped and the requested behavior intentionally covers them.

Preserve original bundles. Apply source/bundle changes in a copied build/analysis tree, supported mod layer, or other reversible local override unless the user explicitly authorizes a destructive installed-file modification.

## Authority and order guards

Do not use a client-side display/prediction path as a substitute for a server-authoritative rule. If the finding establishes remote authority and the authoritative local artifact is unavailable, stop that application path rather than presenting a client change as authoritative.

For order-sensitive behavior, validate against the original bundle or another order-preserving representation; inspection-oriented module decomposition alone does not establish initialization order.

If the required authority, shared-state, module provenance, or version relation is missing or stale, return only that relation to `$analyze-game-logic` before applying the change.
