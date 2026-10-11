# Bootstrapping specification governance

Use this guidance only when a specification is being persisted as a durable project contract and no established project source of truth or specification lifecycle clearly applies.

## Goal

Surface the smallest governance decisions needed for this contract to remain identifiable, reviewable, and safely evolvable. The user resolves any new governance choice explicitly; this bootstrap is not a request for the agent to design a general specification lifecycle or infer conventional answers.

Start from concrete failure modes. Ask for a governance decision only when omitting it could plausibly cause a material problem such as changing the wrong source, treating unsettled material as authoritative, silently choosing between conflicting requirements, or leaving obsolete material apparently current.

Reuse existing project mechanisms whenever they provide the needed property. Ordinary files, version control, pull requests, reviews, ownership rules, and issue links are often sufficient without specification-specific states or artifacts. Following a clearly established mechanism does not require a new governance decision; creating or choosing a new one does.

Do not persist bootstrap governance by mutating project state beyond the user's authorized scope. If a needed governance choice would require such a mutation, keep it unresolved until the user explicitly authorizes it.

## Minimum questions

Ask the user to resolve only the questions needed to keep the contract reliable. Keep any materially unresolved choice explicit rather than filling it with a conventional answer.

### Authority

Make it possible for a future reader to identify the authoritative contract for the relevant scope.

Use an existing project location or convention when it is clearly established. Otherwise require the user to identify the authority needed for the contract. If several sources may be authoritative, define scope or precedence only where ambiguity would otherwise be material and require explicit resolution of any new precedence rule.

Do not infer authority from recency, naming, or location unless the project explicitly makes that property authoritative.

### Change boundary

Make material semantic changes reviewable, and identify what existing project action makes revised contract text authoritative when that distinction matters.

Use an existing boundary such as merging the ordinary project change when it is clearly established. Otherwise require the user to resolve the boundary. Do not invent proposal, approval, adoption, or promotion states when an existing mechanism already makes the change boundary clear.

### Conflict and supersession

Prevent silent winner selection when authoritative material conflicts or authority cannot be established reliably. Preserve the conflict as unresolved unless an existing owner, review process, or explicit user decision resolves it.

When obsolete material could still be mistaken for current authority, require explicit resolution of any new supersession mechanism needed to prevent that failure. If the project safely maintains a single authoritative source and version-control history is sufficient, no separate archive or supersession mechanism is required.

### Provenance

Preserve references to issues, designs, decisions, prior specifications, or other sources only when they are needed to understand the contract, justify a material constraint, or trace a meaningful change.

Do not create a mandatory history log when the information is cheaply recoverable and not needed for verification or maintenance.

### Placement and history

Add naming rules, indexes, archival behavior, or historical retention only when they are needed to find authoritative material reliably, prevent ambiguity, satisfy a concrete maintenance or audit need, or fit an established project workflow. Require explicit user resolution before introducing any new project convention.

Prefer existing repository conventions over specification-specific structure.

## Check the bootstrap

Before retaining any governance mechanism, ask what concrete behavioral or verification regression would appear if it were removed. Simplify or remove mechanisms without a convincing answer.

For the scope being established, a future reader should be able to determine:

- what the authoritative contract is;
- how a material change to it is made reviewable;
- when revised contract text becomes authoritative, if that boundary is materially relevant;
- what happens when authority or requirements conflict or remain ambiguous;
- how obsolete material avoids being mistaken for current authority when that risk exists.

The bootstrap is complete when those questions are answerable to the degree the project needs, remaining material uncertainty is explicit, every new governance choice has been explicitly resolved by the user, and no retained mechanism exists only for procedural completeness.
