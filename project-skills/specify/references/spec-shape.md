# A minimal specification shape

Use only the sections that help preserve the contract.

## Contract role / ownership

When this specification participates in a larger documentation system, state what semantics it owns and important adjacent semantics it does not own when that boundary would otherwise be ambiguous.

## Problem / outcome

What problem is being solved or what outcome is required, in terms meaningful to the requester or affected system.

## Intended behavior

Observable behavior, important interactions, and material constraints.

## Change from current contract

For revisions to an existing contract, describe added, modified, or removed semantics when doing so makes the proposed change easier to review. This is a working shape for the change, not a requirement to maintain a second permanent delta artifact.

## Scope and non-goals

What is included, plus exclusions that prevent likely scope ambiguity.

## Settled decisions

Product, domain, architecture, interface, data, compatibility, or operational choices that downstream work should not need to rediscover.

## Acceptance

Observable conditions that distinguish a satisfying result from an incomplete or incorrect one. Prefer behavioral acceptance over internal implementation steps unless the implementation constraint is itself part of the requirement.

## Unresolved material questions

Only questions whose answer can materially change the contract. Keep them explicit rather than fabricating closure to make the document look complete.

## References

Links or paths to authoritative issues, designs, ADRs, prototypes, or other sources when they add needed detail without duplicating it.
