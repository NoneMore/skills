# Compatibility and migration

Use this guidance when existing callers, stored data, deployed versions, or operational constraints materially limit how a target design can be reached.

## Treat the transition as a design constraint

A target architecture is incomplete when the transition path can change its interfaces, data model, ownership boundaries, or invariants. Identify which old and new components or representations must coexist, which compatibility direction actually matters, and what must remain true at each material transition.

Do not call rollback safe without examining state written after the change. When a migration makes old software or data semantics invalid, make that point of irreversibility explicit and establish a credible forward-recovery path instead of assuming rollback remains available.

## Pay temporary complexity deliberately

Expand-contract changes, dual reads or writes, backfills, translation layers, shadow traffic, and feature flags are migration tools, not default architecture. Introduce only the mechanisms needed to contain a concrete transition risk. For each temporary mechanism, make the authoritative path during overlap and the condition for removing the mechanism clear.

Prefer transitions that preserve one authoritative source of truth. When dual writes or multiple representations are unavoidable, define their failure and reconciliation semantics rather than assuming atomicity.

A migration is sufficiently designed when the important invariants survive the path from current to target state and temporary complexity has an explicit exit condition.
