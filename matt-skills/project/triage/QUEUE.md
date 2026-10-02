# Triage Queue

Use this reference for read-only listing requests routed here by [SKILL.md](SKILL.md). The canonical state machine, tracker sources, and mutation invariants remain there.

## Show what needs attention

Use the configured tracker's **external-request discovery**. If it is configured as `unsupported`, report that limitation and stop this listing branch.

Keep items with work-item role `request` or no role, then account for three buckets, oldest first:

1. **Untriaged** — no triage state yet.
2. **`needs-triage`** — evaluation is in progress.
3. **`needs-info` with reporter activity since the last triage note** — ready for re-evaluation.

For every `needs-info` candidate, read its comments/notes and include it only when reporter activity occurred after the last triage note.

If external PRs/MRs are configured as a request surface, apply the same queue rules to them.

**Completion condition:** show every bucket count and a one-line summary for every returned item, or report that external-request discovery is unsupported.

## Show work already ready for agents

When the maintainer asks to show work already ready for agents, resolve `ready-for-agent` through the configured triage-label mapping and query the configured tracker.
