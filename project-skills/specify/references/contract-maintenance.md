# Maintaining an existing contract

Use this guidance when the requested outcome modifies, reconciles, or clarifies an existing durable project contract whose source has been designated by the user or established project policy.

## Use the designated source

Do not choose a different source because another document, test, implementation, issue, ADR, example, or research artifact appears more authoritative.

Other artifacts may reveal inconsistencies or useful evidence. Report material conflicts rather than silently changing which source owns the persisted contract.

## Specify the delta

When useful, describe only what changes relative to the current contract:

- added semantics;
- modified semantics;
- removed semantics;
- explicitly unchanged semantics when needed to prevent likely ambiguity.

No particular delta heading or syntax is required unless the designated source or project convention requires one.

## Fold into current truth

When persistence of the requested change is authorized, update the designated contract source so it directly describes the resulting current truth.

Do not leave the delta as a second current-state specification unless the project intentionally uses that convention.

## Keep roles clear

A durable contract should emphasize semantics that downstream work must preserve. Keep implementation details, migration state, history, rationale, and supporting evidence distinguishable when mixing them would make requirements ambiguous.

If code, tests, documentation, or other evidence conflicts with the designated contract source, report or reconcile that discrepancy within the requested scope. Do not silently promote the conflicting artifact into a replacement contract source.
