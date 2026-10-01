---
name: wayfinder
description: Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the destination is clear.
disable-model-invocation: true
---

A loose idea has arrived, too big for one agent session, and wrapped in fog: the way from here to the **destination** isn't visible yet. Wayfinding is about finding that way, not charging at the destination. This skill charts the way as a **shared map** on the repo's issue tracker, then works its **decision tickets** (questions whose resolution is a decision, not slices of a build to execute) one at a time until the route is clear.

The destination varies per effort, and naming it is the first act of charting: it shapes every ticket. It might be a spec to hand off and iterate on, a decision to lock before planning starts, or a migration whose path must be decided before execution. The map is domain-agnostic: engineering work, course content, whatever fits the shape.

## Plan, don't do

Wayfinder is **planning, never execution**: each ticket resolves a decision, and the map is done when the way is clear, with nothing left to decide before someone goes and does the thing. The pull to just do the work is the signal you've reached the edge of the map and it's time to hand off. A destination may describe a built state, but that is what the downstream workflow reaches; it does not authorize Wayfinder to build it. Notes cannot override this boundary.

## Refer by name

Every map and ticket has a **name**: its title. In everything the human reads (narration, the map's Decisions-so-far), refer to it by that name, never by a bare id, number, or slug. A wall of `#42, #43, #44` is illegible; names read at a glance. Tracker identities and links don't vanish; they ride _inside_ the name, never stand in for it.

## The Map

Once published, the map is the configured tracker's canonical artifact, with tickets as its children. Before publication, it exists only as a **draft** in the conversation: reviewable, editable, and non-canonical. The tracker-specific Wayfinding operations define the physical representation, labels, links, and claim mechanism.

The map is an **index**, not a store. It lists the decisions made and points at the tickets that hold their detail; a decision lives in exactly one place, its ticket, so the map never restates it, only gists it and links.

A published map has work-item role `decision-map`; record any material immediate tracker sources as its `derived-from` provenance.

**Where the map, its child tickets, blocking, and frontier queries physically live is tracker-specific.** The issue tracker should have been provided to you. Consult its "Wayfinding operations" section for how _this_ repo expresses them. If no tracker has been configured, the draft may remain in the conversation, but do not publish it; tell the user to invoke the user-invoked `setup-matt-pocock-skills` skill explicitly before publication.

### The map body

The whole map at low resolution, loaded once per session. Open tickets are **not** listed: find them through the configured tracker's frontier query.

```markdown
## Destination

<what reaching the end of this map looks like: the spec, decision, or change this effort is finding its way to. One or two lines; every session orients to it before choosing a ticket.>

## Notes

<domain; skills every session should consult; standing preferences for this effort>

## Decisions so far

<!-- the index: one line per resolved ticket, enough to judge relevance, then zoom the link for the detail the ticket holds -->

- [<resolved ticket title>](link): <one-line gist of the answer>

## Not yet specified

<!-- see "Fog of war": in-scope fog you can't ticket yet; graduates as the frontier advances -->

## Out of scope

<!-- see "Out of scope": work ruled beyond the destination; closed, never graduates -->
```

### Tickets

Each ticket has work-item role `decision-ticket` and is a **child** of the map; the tracker's ticket identity is its identity. Its body is the question, sized to one 100K token agent session:

```markdown
## Question

<the decision or investigation this ticket resolves>
```

Each ticket records one Wayfinder type: `research`, `prototype`, `grilling`, or `task` (see [Ticket Types](#ticket-types)); the configured tracker defines how that type is represented separately from work-item role.

A session **claims** a ticket **first**, before any work, using the configured tracker's claim mechanism so concurrent sessions skip it.

Use the configured tracker's blocking representation, preferring a native dependency relationship where it has one. A ticket is **unblocked** when every ticket blocking it is resolved; the **frontier** is the open, unblocked, unclaimed children, the edge of the known.

The answer isn't part of the body; it's recorded on resolution (see [Work through the map](#work-through-the-map)). Assets created while resolving a ticket are linked from the ticket, not pasted in.

## Ticket Types

Every ticket is either **HITL** (human in the loop, worked _with_ a human who speaks for themselves) or **AFK**, driven by the agent alone. A HITL ticket only resolves through that live exchange; the agent never stands in for the human's side of it (a grilling agent that answers its own questions has broken this).

- **Research** (AFK): Reading documentation, third-party APIs, or local resources like knowledge bases to surface a fact a decision waits on. Resolved by a subagent that calls the Skill tool with "research". Use when knowledge outside the current working directory is required.
- **Prototype** (HITL): Raise the fidelity of the discussion by making a cheap, rough, concrete artifact to react to (an outline, a rough take, a stub, or UI/logic code) by calling the Skill tool with "prototype". Links the prototype as an asset. Use when "how should it look" or "how should it behave" is the key question.
- **Grilling** (HITL): Conversation. The default case. Always call the Skill tool twice, for "grilling" and "domain-modeling".
- **Task** (HITL or AFK): Manual work that must happen before a _decision_ can be made: nothing to decide, prototype, or research, but the discussion is blocked until it's done. Signing up for a service so its API can be judged, provisioning access, moving data so its shape can be seen. This is the one type that _does_ rather than decides, and it earns its place by unblocking a decision, not by delivering the destination. The agent drives it alone where it can (AFK); otherwise it hands the human a precise checklist (HITL). Resolved when the work is done; the answer records what was done and any resulting facts (credentials location, new URLs, row counts) later tickets depend on.

## Fog of war

The map is _deliberately_ incomplete: don't chart what you can't yet see. Beyond the live tickets lies the **fog of war**: the dim view of decisions and investigations you can tell are coming but can't yet pin down, because they hang on questions still open. Resolving a ticket clears the fog ahead of it, graduating whatever's now specifiable into fresh tickets, one at a time, until the way to the destination is clear and no tickets remain.

The map's **Not yet specified** section is where that dim view is written down: the suspected question, the area to revisit later. It's the undiscovered frontier _toward_ the destination: everything here is in scope, just not sharp enough to ticket. Write as loosely or as fully as the view allows; it doubles as a signpost for collaborators reading where the effort is headed.

**Fog or ticket?** The test is whether you can state the question precisely now, _not_ whether you can answer it now.

- **Ticket when** the question is already sharp, even if it's blocked and you can't act on it yet.
- **Not yet specified when** you can't yet phrase it that sharply. Don't pre-slice the fog into ticket-sized pieces: it's coarser than a ticket, and one patch may graduate into several tickets, or none, once the frontier reaches it.

**Not yet specified** excludes what's already decided (Decisions so far), what's already a live ticket, and what's out of scope (the next section).

## Out of scope

Fog only ever gathers _toward_ the destination. The destination fixes the scope, so work beyond it is **out of scope**: it isn't fog, and it doesn't belong in **Not yet specified**. It gets its own **Out of scope** section on the map: work you've consciously ruled out of _this_ effort. Scope, not sharpness, lands it here.

Out-of-scope work never graduates (the frontier stops at the destination), so it returns only if the destination is redrawn, and then as a fresh effort, not a resumption.

Ruling something out of scope is a scoping act, not a step on the route. When an existing ticket turns out to sit past the destination, move it to the configured tracker's terminal state so it leaves the frontier, then leave one line in **Out of scope** with the gist and reason, linking the ticket. It stays out of **Decisions so far**: a scope boundary isn't a decision on the route.

## Invocation

Two modes. Either way, **never resolve more than one ticket per session**, with the exception of research tickets.

### Chart the map

User invokes with a loose idea.

1. **Name the destination.** Call the Skill tool twice, for "grilling" and "domain-modeling", to pin down what this map is finding its way to: the spec, decision, or change. The destination fixes the scope, so it's settled first.
2. **Map the frontier.** Grill again, **breadth-first** this time: fan out across the whole space rather than deep on any one thread, surfacing the open decisions and the first steps takeable now. **If this surfaces no fog** (the way to the destination is already clear, the whole journey small enough for one session), you don't need a map. Stop and ask the user how they'd like to proceed.
3. **Draft the map in conversation.** Show the proposed Destination, Notes, fog, ticket titles/questions/types, and blocking relationships, plus the configured tracker if one exists. This is the candidate decision graph, not yet canonical.
4. **Review the draft with the human.** They may mark tickets already decided, change a type, add/remove/reword tickets, change dependencies, or move something to fog or out of scope. Do not write to the tracker or start research until they approve the graph. Publication is either to the repo's configured tracker or nowhere; changing trackers is a repo-level setup change, not a per-map choice.
5. **Publish the approved map.** If the human keeps it conversation-only, publish nothing and stop after the reviewed draft. Otherwise use the configured tracker's Wayfinding operations to create the canonical map with its work-item role, immediate provenance, Destination and Notes filled in, and the approved fog in **Not yet specified**.
6. **Create the approved tickets** as children of the map using the ticket contract above, including tickets the human marked already decided. Wire blocking edges in a **second pass** where the tracker requires created identities before relationships; do not copy the map's provenance onto its children. Immediately resolve each already-decided ticket with its existing answer and append its context pointer to **Decisions so far**. Use the configured post-mutation readback (or its fallback) to verify the map and created tickets' work-item metadata and relationships before proceeding.
7. **Fire the research subagents.** Draft approval also authorizes launching approved `research` tickets that are on the frontier. Spin those up in parallel, each calling the Skill tool with "research" and capturing its findings on a throwaway `research/<name>` branch with a context pointer from the ticket. Blocked research waits for its prerequisites like any other ticket.
8. Stop: charting is one session's work; it hand-resolves nothing beyond recording decisions the human had already settled before publication.

### Work through the map

User invokes with a map reference. A ticket is **optional**: without one, you pick the next decision, not the user.

1. Load the **map**: the low-res view, not every ticket body.
2. Choose the ticket. If the user named one, use it. Otherwise take the first frontier ticket in order. **Claim it before any work** using the configured tracker's Wayfinding operations.
3. Resolve it. **Zoom as needed**: fetch the full body of any related or resolved ticket on demand. For skills named in the `## Notes` block, call the Skill tool only when that skill is **model-invoked**. If Notes names a **user-invoked** workflow, do not call or read it; tell the user to invoke it explicitly when its phase is reached. If in doubt about the decision work itself, call the Skill tool twice, for "grilling" and "domain-modeling".
4. Record the resolution using the configured tracker's Wayfinding operations, then **append a context pointer** to the map's Decisions-so-far.
5. Add newly-surfaced tickets using the same ticket contract (create-then-wire) and verify their persisted work-item metadata and relationships; graduate any fog the answer has made specifiable, clearing each graduated patch from **Not yet specified** so it lives only as its new ticket. If the answer reveals that a ticket (this one or another) sits beyond the destination, **rule it out of scope** rather than resolving it on the route. If the decision invalidates other parts of the map, update or delete those tickets.

The user may run unblocked tickets in parallel, so expect other sessions to be editing the tracker concurrently.

When the map has no remaining frontier, blocked tickets, or in-scope fog and the destination is now clear, stop the wayfinding workflow. If the next phase is to synthesize a buildable spec, tell the user to invoke the user-invoked `to-spec` skill explicitly using their harness's user-invocation mechanism; if the effort turned out small enough to build directly, suggest the user-invoked `implement` skill the same way. Both are user-invoked phase transitions: do not call, read, shell out to, or emulate them yourself.
