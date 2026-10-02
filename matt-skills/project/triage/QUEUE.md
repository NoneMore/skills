# Triage Queue

Use this reference for read-only listing requests routed here by [SKILL.md](SKILL.md). The canonical state machine, tracker sources, and mutation invariants remain there.

## Show what needs attention

Read the configured tracker's **external-request discovery** capability first. If it is explicitly unsupported or cannot establish externality reliably, report that incoming triage discovery is unavailable for this tracker and stop this listing branch. Do not fall back to a generic list/search operation or guess whether items are external.

When the capability is available, run it and account for three buckets, oldest first:

1. **Untriaged** — no triage state yet.
2. **`needs-triage`** — evaluation is in progress.
3. **`needs-info` with reporter activity since the last triage note** — ready for re-evaluation.

Incoming-work discovery includes only externally authored submissions. Exclude any discovered item whose persisted work-item role is `decision-map`, `decision-ticket`, `spec`, or `implementation-ticket`; those are internal workflow artifacts, not incoming requests. An external item with no role may remain in the untriaged bucket; the mutation path persists role `request` before changing triage state.

For every external `needs-info` candidate, read the comments/notes required by the configured tracker and determine whether reporter activity occurred after the last triage note before counting or returning it. Account for every such candidate, not only an item the maintainer later selects.

If external PRs/MRs are configured as a request surface, apply the same external-author rule and reactivation check to them. Explicitly named items use the single-item triage path rather than queue discovery, but still respect the phase boundary: do not triage an `implementation-ticket` produced by `to-tickets`.

**Completion condition:** if discovery is unavailable, state the configured limitation and stop without fallback. Otherwise show the count for every bucket and a one-line summary for every returned item, then let the maintainer choose one by tracker identity, URL/path, or list position.

## Show work already ready for agents

When the maintainer asks to show work already ready for agents, resolve `ready-for-agent` through the configured triage-label mapping and query the configured tracker.
