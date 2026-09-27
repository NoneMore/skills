# ADR Format

ADRs live in `docs/adr/` and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc.

Create the `docs/adr/` directory lazily: only when the first ADR is needed.

ADRs describe the project's **current architectural decisions**. They are mutable current-state documents, not an immutable decision log. Git history preserves how a decision changed over time.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That's it. An ADR can be a single paragraph. The value is in making the current architectural choice and its rationale visible to future work, not in preserving every intermediate decision.

## Optional sections

Only include these when they add genuine value. Most ADRs won't need them.

- **Considered Options**: only when the rejected alternatives are worth remembering
- **Consequences**: only when non-obvious downstream effects need to be called out

Do not add lifecycle status. An ADR file exists only while the decision is current. Keep proposals in the task/spec; delete stale ADRs.

## Numbering

Scan `docs/adr/` for the highest existing number and increment by one.

## Updating an ADR

Keep `docs/adr/` as a view of the **current** architecture:

- **Edit in place** when the same architectural decision evolves.
- **Delete** the ADR when it no longer describes the current architecture.
- **Create a new ADR** when a genuinely different architectural concern deserves its own decision record.
- Do not keep deprecated, superseded, or amendment-only ADR files for chronology. Use Git history for that.

## When to offer an ADR

Offer an ADR when both are true:

1. **The decision reaches beyond the current task**: future work in this area should know or normally follow it.
2. **Its rationale is worth preserving**: it captures a meaningful architectural trade-off, convention, boundary, or direction that is not obvious from the code alone.

Reversibility is not a filter. ADRs record the project's current architecture, not only decisions that are expensive to undo.

If a choice is local to one feature, incidental to today's implementation, or obvious from the code, keep it in the task/spec/code instead of promoting it into architecture.

### What qualifies

- **Architectural shape.** "We use a monorepo so package boundaries stay explicit while changes can move together." "The write model is event-sourced and the read model is projected into Postgres." Record the rationale when the shape should guide future work.
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library: just the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; other contexts reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Constraints not visible in the code.** "We can't use AWS because of compliance requirements." "Response times must be under 200ms because of the partner API contract."
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it; otherwise someone will suggest GraphQL again in six months.
