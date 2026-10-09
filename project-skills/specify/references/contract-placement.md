# Choosing contract persistence

Use this guidance when the user wants a durable specification but has not yet chosen how it should be persisted.

## Require an explicit user choice

Do not infer which existing artifact should become authoritative merely because it mentions the relevant behavior or appears to be the strongest candidate.

Persist only when the user chooses one of these paths:

1. designate an existing source to update; or
2. establish or normalize persistence using the unified specification convention.

If neither path has been chosen, return the complete specification in conversation and surface the missing persistence decision instead of creating repository structure.

## Follow the selected path

When the user designates an existing source, preserve its established shape unless the requested change explicitly includes restructuring it.

When the user chooses the unified specification convention, use that convention without silently substituting another placement model or creating a broader hierarchy as a side effect.

## Done when

The specification has either been persisted according to the user's explicit choice, or the complete contract has been returned without inventing a persistence decision on the user's behalf.
