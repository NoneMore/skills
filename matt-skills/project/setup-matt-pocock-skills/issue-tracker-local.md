# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Work-item role is `Work-Item-Role: <request|decision-map|decision-ticket|spec|implementation-ticket>` near the top of each participating file.
- Immediate provenance is `Derived-From: <path>, <path>` on the derived file; missing or `Derived-From: None` means no sources.
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings). When a publishing skill applies a triage role to the spec, record the same `Status:` line near the top of `spec.md`. This field is reserved for canonical triage roles; Wayfinder lifecycle uses a separate field.
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

Work-item role and provenance are independent from hierarchy, blocking, triage state, `Type:`, and `Wayfinder-State:`. After changing work-item metadata, re-read the file and verify the persisted fields.

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the referenced path. For a bare issue number, search `.scratch/*/issues/` and use it only if exactly one file has that number; otherwise ask for the feature or path.

## Relationships

- **Hierarchy:** record `Parent: <path>` near the top of a child file. Implementation tickets produced from a local spec use `Parent: ../spec.md`; Wayfinder decision tickets use `Parent: ../map.md`.
- **Blocking:** keep the existing `Blocked by:` convention used by the publishing workflow; hierarchy and blocking remain independent.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a file with one **child** file per ticket.

- **Map**: `.scratch/<effort>/map.md` (the Notes / Decisions-so-far / Fog body), with `Work-Item-Role: decision-map` and any immediate `Derived-From:` sources.
- **Child ticket**: `.scratch/<effort>/issues/NN-<slug>.md`, numbered from `01`, with `Work-Item-Role: decision-ticket`, `Parent: ../map.md`, and the question in the body. A `Type:` line records the ticket type (`research`/`prototype`/`grilling`/`task`); a separate `Wayfinder-State:` line records `open`/`claimed`/`resolved`/`closed`. Do not reuse the triage `Status:` field for this lifecycle.
- **Blocking**: a `Blocked by: NN, NN` line near the top. A ticket is unblocked when every file it lists has `Wayfinder-State: resolved` or `Wayfinder-State: closed`.
- **Frontier**: scan `.scratch/<effort>/issues/` for files with `Wayfinder-State: open` that are unblocked and unclaimed; first by number wins.
- **Claim**: set `Wayfinder-State: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Wayfinder-State: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`. For a ticket ruled out of scope, set `Wayfinder-State: closed` instead.
