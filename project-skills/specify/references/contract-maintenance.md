# Maintaining an existing contract

Use this guidance when the requested outcome modifies, reconciles, or clarifies an existing durable project contract.

## Find ownership first

Identify which established source owns the semantics being changed.

Ownership may be narrower than a whole file, such as an entry or section, or broader than one file, such as a contract set or external project-owned source. Do not widen or relocate the contract merely to normalize its shape.

Prefer established project ownership over creating a new specification surface. A nearby document, test, implementation, issue, ADR, example, or research artifact is not automatically authoritative merely because it mentions the behavior.

If multiple artifacts disagree, distinguish their roles where possible:

- current intended contract;
- proposed or not-yet-incorporated change;
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

Do not restate the whole system merely to describe a narrow change. No particular delta heading or syntax is required unless the project already requires one.

## Fold into current truth

When persistence of the requested change is authorized, update the established contract owner so it directly describes the resulting current truth.

Do not leave the delta as a second current-state specification unless the project intentionally uses that convention.

## Separate contract from implementation

A durable contract should emphasize semantics that downstream work must preserve.

Keep current implementation structure, migration status, historical narrative, temporary compatibility state, and supporting evidence separate when their presence would make it unclear whether they are requirements.

Implementation details may remain beside contract semantics when useful, but keep their role clear. Do not mechanically split or rewrite existing documents merely to produce a standard shape.

## Reconcile evidence

Acceptance tests should make important contract semantics observable where appropriate, but do not infer that every existing test is a durable product requirement.

Likewise, current code does not automatically override a stated contract, and a stale document does not automatically override demonstrated project reality.

When they disagree, identify the owning contract and reconcile the discrepancy as part of the requested specification work, or report the unresolved conflict when the available authority is insufficient.
