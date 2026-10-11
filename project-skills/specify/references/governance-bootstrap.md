# Bootstrapping specification governance

Use this guidance only when a specification is being persisted as a durable project contract and no established project source of truth or specification lifecycle clearly applies.

## Goal

Surface the smallest governance decisions needed for this contract to remain identifiable, reviewable, and safely evolvable. Reuse clearly established project mechanisms; for any new governance choice, require explicit user resolution rather than inferring a conventional answer.

Ask for a governance decision only when omitting it could plausibly cause a material problem such as changing the wrong source, treating unsettled material as authoritative, silently choosing between conflicting requirements, or leaving obsolete material apparently current.

Do not persist bootstrap governance by mutating project state beyond the user's authorized scope. Keep any choice that would require such a mutation unresolved until the user explicitly authorizes it.

## Minimum questions

Ask the user to resolve only the questions needed to keep the contract reliable. Keep materially unresolved choices explicit.

### Authority

Use an existing project location or convention when it is clearly established. Otherwise require the user to identify the authority needed for the contract. If several sources may be authoritative, require explicit resolution of any materially necessary scope or precedence rule.

Do not infer authority from recency, naming, or location unless the project explicitly makes that property authoritative.

### Change boundary

Use an existing change boundary when it is clearly established. Otherwise require the user to resolve what makes revised contract text authoritative when that distinction matters. Do not invent proposal, approval, adoption, or promotion states when an existing mechanism already makes the boundary clear.

### Conflict and supersession

Prevent silent winner selection when authoritative material conflicts or authority cannot be established reliably. Preserve the conflict as unresolved unless an existing owner, review process, or explicit user decision resolves it.

When obsolete material could still be mistaken for current authority, require explicit resolution of any new supersession mechanism needed to prevent that failure. If the project safely maintains a single authoritative source and version-control history is sufficient, no separate archive or supersession mechanism is required.

### Provenance

Preserve references to issues, designs, decisions, prior specifications, or other sources only when they are needed to understand the contract, justify a material constraint, or trace a meaningful change.

Do not create a mandatory history log when the information is cheaply recoverable and not needed for verification or maintenance.

### Placement and history

Prefer existing repository conventions. Add naming rules, indexes, archival behavior, or historical retention only when a concrete need makes them necessary, and require explicit user resolution before introducing any new project convention.

## Check the bootstrap

Before retaining any governance mechanism, ask what concrete behavioral or verification regression would appear if it were removed. Simplify or remove mechanisms without a convincing answer.

For the scope being established, a future reader should be able to determine:

- what the authoritative contract is;
- how a material change to it is made reviewable;
- when revised contract text becomes authoritative, if that boundary is materially relevant;
- what happens when authority or requirements conflict or remain ambiguous;
- how obsolete material avoids being mistaken for current authority when that risk exists.

The bootstrap is complete when those questions are answerable to the degree the project needs, remaining material uncertainty is explicit, every new governance choice has been explicitly resolved by the user, and no retained mechanism exists only for procedural completeness.
