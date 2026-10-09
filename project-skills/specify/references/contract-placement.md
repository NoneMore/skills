# Choosing contract persistence

Use this guidance when the user wants a durable specification but the persistence source or convention is not yet explicit.

## Require an explicit persistence choice

Do not infer which existing artifact should become authoritative merely because it mentions the relevant behavior or appears to be the strongest candidate.

Persist only when one of these choices is established:

1. the user designates an existing source to update;
2. established project policy designates the source; or
3. the user explicitly chooses to establish a specification source or convention.

If none applies, return the complete specification in conversation and surface the missing persistence decision instead of creating repository structure.

## Follow the designated convention

When an existing source is designated, preserve its established shape unless the requested change explicitly includes restructuring it.

When the user explicitly chooses to establish a specification source, use the designated or selected specification convention. Do not silently substitute another placement model or create a broader hierarchy as a side effect.

## Done when

The specification has either been persisted to an explicitly designated source/convention, or the complete contract has been returned without inventing a persistence decision on the user's behalf.
