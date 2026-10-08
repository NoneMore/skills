# Domain modeling

Use this guidance when the design problem depends on precise domain language or durable architectural knowledge.

## Sharpen language

Treat fuzzy or overloaded terms as design signals. Prefer one canonical term per material concept, and distinguish concepts that have different rules or lifecycles even when casual language conflates them.

When an existing `CONTEXT.md` or equivalent glossary defines a term differently from the current discussion, surface the conflict instead of silently creating two meanings. Use concrete scenarios and edge cases to test whether proposed terms and relationships actually hold.

Cross-check claims about the domain against current code and behavior when that evidence matters. A mismatch is a design question: decide whether the model or the implementation is stale rather than assuming either source wins automatically.

## Persist selectively

A domain glossary should capture domain concepts and language, not task-local implementation details or scratch notes. Create or edit it only when the project benefits from durable shared terminology.

An ADR should record a current architectural decision when both are true:

1. future work in the area should know or normally follow the decision; and
2. the rationale or tradeoff is not obvious from the code alone.

Do not create an ADR merely because a choice occurred during a task. Follow established project conventions for artifact location and format; do not invent repository-wide governance merely to persist a design result. When a current architectural decision changes, update the natural source of truth rather than preserving a second active version for history; version control is the history.
