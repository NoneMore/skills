# Run Persistence

Persistence is optional operational machinery, not part of ordinary Lean reasoning. Load this branch only when the user explicitly asks to preserve reusable run history or a compatible host activates persistence.

## Contract

Persist evidence that is costly to rediscover: dispatch scope, accepted file baselines, failed approaches, useful search results, review/replan summaries, and the final handoff. Historical evidence is not proof certification.

The persistence mechanism must fail honestly: an unconfirmed write is not a stored event, and a storage failure must not be hidden while proof work continues under false assumptions.

When the imported helper runtime is available, `../run-store.md` and `../handoff-contract.md` describe the upstream storage and handoff formats. Load those implementation references only after persistence is selected.

Do not make normal proving depend on persistence; absence of a run store must leave the non-persistent workflow usable.