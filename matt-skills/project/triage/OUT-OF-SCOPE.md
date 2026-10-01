# Out-of-Scope Knowledge Base

Use `.out-of-scope/` only for **maintainer-rejected enhancement concepts**. It is current decision memory, not a graveyard for every closed item.

It serves two purposes:

1. preserve the durable reason a capability is outside project scope;
2. surface that decision when a conceptually similar request arrives later.

Do not record bugs, temporary deferrals, or requests closed because the behavior already exists.

## One concept, one file

Store one file per rejected concept:

```text
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

Several tracker items requesting the same concept belong in the same file.

Use a short kebab-case filename that names the concept without needing to open the file.

## Record shape

```markdown
# <Concept>

<one-sentence statement of the current scope decision>

## Why this is out of scope

<durable product, architectural, technical, or strategic reason>

## Prior requests

- <tracker reference> — "<request title>"
```

The reasoning must survive schedule changes and team turnover. "We are too busy right now" is a deferral, not an out-of-scope decision.

Use the configured tracker's normal reference form for prior requests.

## During triage

Compare the incoming request to existing files by **domain concept**, not only by wording.

When a likely match exists, surface the prior decision and its reason to the maintainer. The maintainer chooses one of three outcomes:

- **Confirm:** keep the decision, append the new request reference, then move the item to the configured `wontfix` state.
- **Reconsider:** update or delete the stale scope record, then continue normal triage.
- **Different concept:** leave the prior record unchanged and continue normal triage.

Do not silently treat semantic similarity as a maintainer decision.

## When writing or updating a record

Only write after the maintainer has rejected an enhancement.

1. Find an existing file for the same concept.
2. Update that file, or create one if none exists.
3. Ensure the durable reason and current decision are explicit.
4. Add the new tracker reference exactly once.
5. Publish the required triage note using the disclaimer and tracker mechanics defined by `SKILL.md` and the configured issue-tracker document.
6. Move the item to the configured terminal state.

## Completion check

The out-of-scope step is complete only when:

- exactly one current concept record represents the decision;
- its reason is durable rather than temporary;
- the new request is referenced once;
- the tracker item points back to the recorded decision;
- the tracker item is in the maintainer-approved terminal state.

If the maintainer reverses the decision later, update or delete the record so `.out-of-scope/` continues to describe **current** scope rather than obsolete history.
