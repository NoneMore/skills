# Triage Queue

Use this reference for read-only listing requests routed here by [SKILL.md](SKILL.md). The canonical state machine, tracker sources, and mutation invariants remain there.

## Show what needs attention

Query the configured tracker's **external request discovery** operation and account for three buckets, oldest first:

1. **Untriaged** — no triage state yet.
2. **`needs-triage`** — evaluation is in progress.
3. **`needs-info` with reporter activity since the last triage note** — ready for re-evaluation.

Incoming-work discovery must include only submissions from people outside the configured project's internal contributor/member set. Internal roadmap issues, specs, decision items, and implementation tickets are not part of this queue even if they currently lack a triage-state label.

If external PRs/MRs are configured as a request surface, apply the same external-author filter to them. Explicitly named items use the single-item triage path rather than queue discovery, but still respect the phase boundary: do not triage an internal `implementation-ticket` produced by `to-tickets`.

**Completion condition:** show the count for every bucket and a one-line summary for every returned item, then let the maintainer choose one by tracker identity, URL/path, or list position.

## Show work already ready for agents

When the maintainer asks to show work already ready for agents, resolve `ready-for-agent` through the configured triage-label mapping and query the configured tracker.

