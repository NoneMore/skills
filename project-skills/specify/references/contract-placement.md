# Choosing contract placement and granularity

Use this guidance when durable specification is part of the requested outcome but the project does not already establish where the relevant contract should live or how large that contract surface should be.

## Preserve the smallest usable durable contract

Choose the smallest durable granularity that remains usable for future implementation, verification, and change.

Granularity is not a maturity level and does not imply a required hierarchy. A durable contract may be a single entry or section, a document, a directory or contract set, or an external project-owned source when project convention makes that source authoritative.

Do not create a standalone specification, directory, or new source-of-truth hierarchy merely because a larger structure is possible.

## Reuse before creating

Prefer, in order:

1. a destination explicitly requested by the user;
2. an established project source that already owns the relevant semantics;
3. when establishing a new source is genuinely part of the delegated outcome, the smallest new surface that fits existing project conventions.

Do not move or split an existing contract merely to normalize its shape.

## Keep the contract small when possible

An entry or section is often sufficient when the behavior is narrow, locally owned, easy to find, and unlikely to require independent navigation or coordination.

A standalone document may be useful when the contract contains several related requirements, needs stable independent reference, or would make its containing document materially harder to use.

A directory or contract set is justified only when the contract has enough independent structure that one document becomes difficult to navigate, review, or evolve safely.

These are heuristics, not required levels.

## Expand only when the current surface stops working

A larger contract surface can be warranted when, for example:

- the same contract is repeatedly changed by independent work;
- multiple independently meaningful requirements need stable reference or ownership;
- several modules, interfaces, or teams rely on the same semantics;
- compatibility, security, data, protocol, or operational constraints make omissions materially risky;
- the current document creates recurring navigation, merge-conflict, or review problems.

Do not expand preemptively for hypothetical future complexity.

## Avoid unnecessary persistent specs

A new persistent contract source is usually unnecessary when the requested work is implementation-only, the relevant durable semantics are already owned elsewhere, or the user only asked for an in-conversation specification.

When persistence is not requested, return the complete contract in conversation rather than creating project structure solely for durability.

## Done when

The chosen location is durable enough that future work can find, understand, and update the contract without maintaining a second current source of truth, while introducing no more structure than the contract actually needs.
