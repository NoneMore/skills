# Out-of-Scope Knowledge Base

The `.out-of-scope/` directory in a repo stores persistent records of **rejected enhancement concepts**. It serves two purposes:

1. **Institutional memory:** preserve why a feature was rejected after the tracker item is closed or terminally marked.
2. **Deduplication:** when a new request matches a prior rejection, surface the existing decision instead of re-litigating it from scratch.

This knowledge base is tracker-agnostic. Request references may be GitHub/GitLab links or ids, or repo-relative local-markdown issue paths.

## Directory structure

```text
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

Use one file per **concept**, not one file per issue. Multiple requests for the same underlying thing belong in the same record.

## File format

Write the file as a short, readable design note rather than a database row. It should be understandable to someone who was not present for the original triage.

```markdown
# Dark Mode

This project does not support dark mode or user-facing theming.

## Why this is out of scope

<durable explanation of the product, architectural, or strategic reason>

## Prior requests

- <tracker reference or local issue path> — "Add dark mode support"
- <tracker reference or local issue path> — "Night theme for accessibility"
```

### Naming the file

Use a short descriptive kebab-case concept name such as `dark-mode.md`, `plugin-system.md`, or `graphql-api.md`. The filename should communicate the rejected concept without requiring the file to be opened.

### Writing the reason

The reason must be substantive and durable. Good reasons reference:

- Project scope or philosophy.
- Technical or architectural constraints.
- Strategic decisions already made.

Avoid temporary circumstances such as "we are too busy right now". That is a deferral, not a durable rejection.

Code samples are allowed when they explain the architectural constraint, but the decision should remain understandable if implementation details later move.

## When to check `.out-of-scope/`

During triage's context-gathering step, read the files under `.out-of-scope/` and compare the incoming request by **concept**, not just keywords.

For example, "night theme" may match an existing `dark-mode.md` record even if the words are different.

If a likely match exists, surface it to the maintainer and summarize the prior reason. The maintainer may then:

- **Confirm:** append the new request to the existing record and move the item to the configured `wontfix` state.
- **Reconsider:** delete or update the out-of-scope record and continue normal triage.
- **Disagree:** treat the requests as related but materially distinct and continue normal triage.

Do not make the final scope judgment silently; the maintainer owns that decision.

## When to write to `.out-of-scope/`

Write here only when an **enhancement** is deliberately rejected as `wontfix`.

This applies equally to rejected enhancement issues and external PRs/MRs. For a local-markdown tracker, use the repo-relative issue path as the prior-request reference.

Do **not** write here when an item is terminal because the requested behavior is **already implemented**. That is a built feature, not a rejected concept, and recording it as out-of-scope would poison future deduplication.

The flow:

1. The maintainer decides the enhancement is out of scope.
2. Check for an existing matching concept record.
3. If it exists, append the new tracker reference under `## Prior requests`.
4. Otherwise create a new concept file with the decision, durable reason, and first request reference.
5. Publish a triage note on the tracker item that explains the decision and references the `.out-of-scope/` file.
6. Apply the configured `wontfix` state and close the item where the tracker has a close operation. For local markdown, the terminal `Status:` value is sufficient.

Any tracker note generated in step 5 must use the standard triage AI disclaimer from `SKILL.md`.

## Updating or removing out-of-scope files

If the maintainer changes their mind about a previously rejected concept:

- Delete or update the `.out-of-scope/` file so it no longer states a decision that is not current.
- Historical tracker items do not need to be reopened automatically.
- The new item that triggered reconsideration proceeds through normal triage.

Treat these files as current scope decisions, not an append-only archive of obsolete policy.
