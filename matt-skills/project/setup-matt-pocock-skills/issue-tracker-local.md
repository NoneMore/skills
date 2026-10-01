# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Work-item identity is recorded as `Work-Item-Role: <request|decision-map|decision-ticket|spec|implementation-ticket>` near the top of each participating file.
- Immediate provenance is recorded on the derived file as `Derived-From: <path>, <path>`. A missing line or `Derived-From: None` means zero immediate sources. Record only material immediate sources, never the transitive root chain.
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings). When a publishing skill applies a triage role to the spec, record the same `Status:` line near the top of `spec.md`. This field is reserved for canonical triage roles; do not reuse it for work-item identity or provenance.
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

`Work-Item-Role:`, `Derived-From:`, hierarchy, `Blocked by:`, `Status:`, `Type:`, and `Wayfinder-State:` are independent fields. Read and update them independently; never infer one from another.

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the referenced path. For a bare issue number, search `.scratch/*/issues/` and use it only if exactly one file has that number; otherwise ask for the feature or path.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a file with one **child** file per ticket.

- **Map**: `.scratch/<effort>/map.md` (the Notes / Decisions-so-far / Fog body), with `Work-Item-Role: decision-map` and any immediate `Derived-From:` sources.
- **Child ticket**: `.scratch/<effort>/issues/NN-<slug>.md`, numbered from `01`, with `Work-Item-Role: decision-ticket` and the question in the body. A `Type:` line records the ticket type (`research`/`prototype`/`grilling`/`task`); a separate `Wayfinder-State:` line records `open`/`claimed`/`resolved`/`closed`. `Type:` is not the work-item role. Do not reuse the triage `Status:` field for this lifecycle.
- **Blocking**: a `Blocked by: NN, NN` line near the top. A ticket is unblocked when every file it lists has `Wayfinder-State: resolved` or `Wayfinder-State: closed`.
- **Frontier**: scan `.scratch/<effort>/issues/` for files with `Wayfinder-State: open` that are unblocked and unclaimed; first by number wins.
- **Claim**: set `Wayfinder-State: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Wayfinder-State: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`. For a ticket ruled out of scope, set `Wayfinder-State: closed` instead.
