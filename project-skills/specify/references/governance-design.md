# Designing specification governance

Use this guidance only when the user explicitly asks to establish or materially redesign how a project governs specifications. It is a decision framework, not a default lifecycle.

## Goal

Define the smallest project-specific governance that makes the current contract and its evolution reliable, reviewable, and unambiguous enough for the project's needs.

Start from concrete failure modes rather than governance vocabulary. Add a durable rule or mechanism only when its absence could plausibly cause a material problem such as changing the wrong source, treating an unadopted proposal as current, silently reconciling conflicting requirements, leaving superseded material apparently authoritative, or losing provenance needed to understand a contract.

Reuse existing project mechanisms when they already provide the needed property. A repository may use ordinary files, pull requests, reviews, ownership rules, issue links, or other existing conventions without introducing specification-specific states or artifacts.

## Decisions to settle

Resolve only the dimensions that matter to the requested governance. Keep any materially unresolved choice explicit rather than filling it with a conventional answer.

### Authority

Define how a reader can identify the current authoritative contract. If several sources may be authoritative, define their scope or precedence only where the project actually needs it.

Do not use file recency, naming, or location as authority unless the governance explicitly makes it authoritative.

### Change representation

Define how material semantic changes become reviewable. The governance should make important additions, modifications, removals, or renames visible enough that reviewers do not have to infer the contract delta from an opaque rewrite.

Choose the lightest representation that provides that property; do not require a separate proposal artifact when an existing project mechanism already makes the delta clear.

### Adoption

Define what makes a proposed requirement part of the current contract when that distinction matters. Prefer an existing project action or decision boundary when one is already authoritative.

Do not invent approval stages merely to make the lifecycle look complete.

### Conflict and ambiguity

Define what happens when authoritative material conflicts, concurrent changes disagree, or authority cannot be established reliably. The governance should prevent silent reconciliation or accidental winner selection.

Resolution may be delegated to an existing owner, review process, or explicit user decision; otherwise preserve the conflict as unresolved.

### Supersession

When obsolete specifications could still be mistaken for current authority, define how supersession is made explicit enough to prevent that failure. Do not infer supersession from a newer timestamp or nearby replacement.

If the project can safely maintain a single authoritative source without retaining competing material, no additional supersession mechanism is required.

### Provenance

Preserve references to issues, designs, decisions, prior specifications, or other sources only when they are needed to understand the contract, justify a material constraint, or trace a meaningful change.

Do not turn provenance into a mandatory history log when the information is cheaply recoverable and not needed for verification or maintenance.

### Storage, discovery, and history

Define repository layout, naming, indexing, archival behavior, or historical retention only when the project needs them to find authoritative material reliably, avoid ambiguity, satisfy audit or maintenance needs, or support an established workflow.

Prefer existing project conventions over a specification-specific repository structure.

## Check the design

Before retaining any governance mechanism, ask what concrete behavioral or verification regression would appear if it were removed. Simplify or remove mechanisms without a convincing answer.

The resulting governance should make it possible, for the scope where governance is needed, to determine:

- what the current contract is;
- how a material change is represented and reviewed;
- what makes that change current, when an adoption boundary is necessary;
- what happens when authority, adoption, or requirements conflict or remain ambiguous;
- how obsolete material stops being mistaken for current authority when that risk exists.

The governance is complete when those questions are answerable to the degree required by the project, remaining material decisions are explicit, and no retained mechanism exists only for procedural completeness.
