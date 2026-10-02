# Triage Queue

Use this reference for read-only listing requests routed here by [SKILL.md](SKILL.md). The canonical state machine, tracker sources, and mutation invariants remain there.

## Show what needs attention

Query the configured tracker and account for three buckets, oldest first:

1. **Untriaged** — no triage state yet.
2. **`needs-triage`** — evaluation is in progress.
3. **`needs-info` with reporter activity since the last triage note** — ready for re-evaluation.

If external PRs/MRs are in scope, include only external submissions during discovery; an explicitly named PR/MR belongs to the single-item triage branch and is triaged regardless of author.

**Completion condition:** show the count for every bucket and a one-line summary for every returned item, then let the maintainer choose one by tracker identity, URL/path, or list position.

## Show work already ready for agents

When the maintainer asks to show work already ready for agents, resolve `ready-for-agent` through the configured triage-label mapping and query the configured tracker.

