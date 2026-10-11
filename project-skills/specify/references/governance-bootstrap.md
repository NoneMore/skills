# Bootstrapping specification governance

Use this guidance only when a specification is being persisted as a durable project contract and no established project source of truth or specification lifecycle clearly applies.

## Goal

Establish the smallest governance needed for this contract to remain identifiable, reviewable, and safely evolvable. This bootstrap is part of making the first durable contract reliable; it is not a request to design a general specification lifecycle.

Start from concrete failure modes. Add a rule or mechanism only when omitting it could plausibly cause a material problem such as changing the wrong source, treating unsettled material as authoritative, silently choosing between conflicting requirements, or leaving obsolete material apparently current.

Reuse existing project mechanisms whenever they provide the needed property. Ordinary files, version control, pull requests, reviews, ownership rules, and issue links are often sufficient without specification-specific states or artifacts.

## Minimum questions

Resolve only the questions needed to keep the contract reliable. Keep any materially unresolved choice explicit rather than filling it with a conventional answer.

### Authority

Make it possible for a future reader to identify the authoritative contract for the relevant scope.

Prefer an existing project location or convention when one is already suitable. If several sources may be authoritative, define scope or precedence only where ambiguity would otherwise be material.

Do not infer authority from recency, naming, or location unless the project explicitly makes that property authoritative.

### Change boundary

Make material semantic changes reviewable, and identify what existing project action makes revised contract text authoritative when that distinction matters.

Prefer an existing boundary such as merging the ordinary project change that updates the contract. Do not invent proposal, approval, adoption, or promotion states when an existing mechanism already makes the change boundary clear.

### Conflict and supersession

Prevent silent winner selection when authoritative material conflicts or authority cannot be established reliably. Preserve the conflict as unresolved unless an existing owner, review process, or explicit user decision resolves it.

When obsolete material could still be mistaken for current authority, make supersession explicit enough to prevent that failure. If the project safely maintains a single authoritative source and version-control history is sufficient, no separate archive or supersession mechanism is required.

### Provenance

Preserve references to issues, designs, decisions, prior specifications, or other sources only when they are needed to understand the contract, justify a material constraint, or trace a meaningful change.

Do not create a mandatory history log when the information is cheaply recoverable and not needed for verification or maintenance.

### Placement and history

Add naming rules, indexes, archival behavior, or historical retention only when they are needed to find authoritative material reliably, prevent ambiguity, satisfy a concrete maintenance or audit need, or fit an established project workflow.

Prefer existing repository conventions over specification-specific structure.

## Check the bootstrap

Before retaining any governance mechanism, ask what concrete behavioral or verification regression would appear if it were removed. Simplify or remove mechanisms without a convincing answer.

For the scope being established, a future reader should be able to determine:

- what the authoritative contract is;
- how a material change to it is made reviewable;
- when revised contract text becomes authoritative, if that boundary is materially relevant;
- what happens when authority or requirements conflict or remain ambiguous;
- how obsolete material avoids being mistaken for current authority when that risk exists.

The bootstrap is complete when those questions are answerable to the degree the project needs, remaining material uncertainty is explicit, and no retained mechanism exists only for procedural completeness.
