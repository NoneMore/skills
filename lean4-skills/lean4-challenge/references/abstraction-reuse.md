# Mathematical abstraction and reuse

Use when mathematical content within or across declarations might be shared. Similar tactics alone do not establish a reusable invariant.

## Search path

1. Compare **hypotheses, constructions, conclusions, and underlying invariants** at representative sites, including repeated work within one proof.
2. Search local and imported mathlib APIs (and a plausible earlier module when relevant) for the same mathematical result under different notation.
3. Compare four real options: reuse an existing result; extract a local/private helper; introduce a justified public theorem; or do not extract.
4. Ask whether sharing requires unnatural parameters, stronger hypotheses, additional coercions, fragile inference, or bad dependency direction.
5. Separate the mathematical reuse decision from authorization to refactor the production consumers.

## Discriminating evidence

- State the candidate helper in scratch Lean and check representative uses; for cross-declaration reuse, include a meaningfully different consumer when it could reverse the recommendation.
- Check actual imports and elaboration cost, not only the existence of a theorem with a similar name.
- Compare the reduction in mathematical duplication against new API surface, dependency, inference, and maintenance burdens.

## Judgment and stop

Recommend the smallest justified option, including **no extraction**. Record what elaborated versus which consumers remain unexamined. State relevant public-statement and trust invariants in the recommendation. Scratch experiments do not authorize production edits. Stop once representative uses and costs distinguish the viable choices.

If reuse exposes a different generic mathematical owner or placement question, use [framing](mathematical-framing.md) or [theory organization](theory-organization.md) as needed, without duplicating the same underlying investigation.
