# Choosing contract persistence

Use this guidance when the user wants a durable specification but has not yet chosen how it should be persisted.

## Require an explicit user choice

Do not infer which existing artifact should become authoritative merely because it mentions the relevant behavior or appears to be the strongest candidate.

Persist only when the user chooses one of these paths:

1. designate an existing source to update; or
2. designate a destination for a dedicated specification source using the unified specification shape described in [spec-shape.md](spec-shape.md).

If neither path has been chosen, return the complete specification in conversation and surface the missing persistence decision instead of creating repository structure.

## Follow the selected path

When the user designates an existing source, preserve its established shape unless the requested change explicitly includes restructuring it.

When the user chooses a dedicated specification source, use [spec-shape.md](spec-shape.md) for its semantic shape while preserving the user-designated destination. The specification shape does not itself define repository placement, naming, hierarchy, or lifecycle.

## Done when

The specification has either been persisted according to the user's explicit choice, or the complete contract has been returned without inventing a persistence decision on the user's behalf.
