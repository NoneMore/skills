# ADR Format

ADRs live in `docs/adr/` and use sequential numbering: `0001-slug.md`, `0002-slug.md`, etc.

Create the `docs/adr/` directory lazily: only when the first ADR is needed.

ADRs describe the **current durable constraints** of the project. They are not an immutable decision log. Git history already preserves how a decision changed over time.


## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That's it. An ADR can be a single paragraph. The value is in making a durable constraint and its rationale visible to future work, not in preserving every intermediate decision.

## Optional sections

Only include these when they add genuine value. Most ADRs won't need them.

- **Status** frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`): useful when the current state cannot be expressed cleanly by editing or deleting the ADR
- **Considered Options**: only when the rejected alternatives are worth remembering
- **Consequences**: only when non-obvious downstream effects need to be called out

## Numbering

Scan `docs/adr/` for the highest existing number and increment by one.

## Updating an ADR

Prefer the smallest representation of the **current** decision:

- **Edit in place** when the same underlying constraint evolves.
- **Delete** the ADR when the decision is no longer a durable constraint and preserving it would only mislead future agents.
- **Deprecate** it when readers still need to know that the old constraint existed, but must not treat it as current.
- **Supersede** it with a new ADR only when keeping the old and new decisions as separate named concepts is genuinely useful.
- Do not append amendment history inside the ADR just to preserve chronology. Use Git history for that.

## When to offer an ADR

An ADR qualifies when either the user explicitly declares a decision to be a durable project constraint, or all three of these are true:

1. **Future implementations must obey it** beyond the current task.
2. **Changing it is meaningfully expensive or externally observable** — compatibility, persisted data, users, integrations, or coordinated migration are good signals.
3. **Its rationale is not obvious from the code** and records a real trade-off a future reader would otherwise re-litigate.

If a choice is easy to replace, local to one feature, or merely reflects today's implementation, keep it in the task/spec/code instead of promoting it into architecture.

### What qualifies

- **Architectural shape only when it is load-bearing.** "The write model is event-sourced because external consumers depend on the event contract." A monorepo layout by itself is not enough if it can be changed without broader consequences.
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library: just the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; other contexts reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Constraints not visible in the code.** "We can't use AWS because of compliance requirements." "Response times must be under 200ms because of the partner API contract."
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it; otherwise someone will suggest GraphQL again in six months.
