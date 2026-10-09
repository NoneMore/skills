# Maintaining an existing contract

Use this guidance when the requested outcome modifies, reconciles, or clarifies an existing durable specification.

## Find ownership first

Identify which existing artifact owns the semantics being changed.

Prefer established project ownership over creating a new specification surface. A nearby document, test, implementation, issue, ADR, example, or research artifact is not automatically authoritative merely because it mentions the behavior.

If multiple artifacts disagree, distinguish their roles where possible:

- current intended contract;
- proposed or accepted-but-undelivered change;
- implementation reality;
- executable evidence;
- rationale or history;
- research, examples, or diagnostics.

Do not silently collapse those roles. If the project does not establish enough authority to resolve a material conflict, keep the conflict explicit.

## Specify the delta

When useful, describe only what changes relative to the current contract:

- added semantics;
- modified semantics;
- removed semantics;
- explicitly unchanged semantics when needed to prevent likely ambiguity.

Do not restate the whole system merely to describe a narrow change.

## Fold into current truth

When persisting an accepted change, update the established authoritative contract so it directly describes the resulting current truth.

Do not leave the delta as a second current-state specification unless the project intentionally uses that convention.

## Separate contract from implementation

A durable contract should emphasize semantics that downstream work must preserve.

Keep current implementation structure, migration status, historical narrative, temporary compatibility state, and supporting evidence separate when their presence would make it unclear whether they are requirements.

Implementation details may remain in the same document when useful, but make their non-normative role clear.

A useful document shape, when the existing structure does not already communicate the same boundaries, is:

1. contract role or ownership;
2. current contract;
3. scope, unsupported behavior, or non-goals;
4. current implementation notes, when useful;
5. references or rationale.

Do not mechanically rewrite documents into this shape.

## Reconcile evidence

Acceptance tests should make important contract semantics observable where appropriate, but do not infer that every existing test is a durable product requirement.

Likewise, current code does not automatically override a stated contract, and a stale document does not automatically override demonstrated project reality.

When they disagree, identify the owning contract and reconcile the discrepancy as part of the requested specification work, or report the unresolved conflict when the available authority is insufficient.
