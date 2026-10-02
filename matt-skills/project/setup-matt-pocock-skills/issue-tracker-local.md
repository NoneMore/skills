# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

Shared tracker semantics are defined in [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md). This file defines only the local-markdown representation, operations, and verification used to realize that contract.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Work-item role is `Work-Item-Role: <request|decision-map|decision-ticket|spec|implementation-ticket>` near the top of each participating file.
- Provenance is `Derived-From: <path>, <path>` on the derived file; missing or `Derived-From: None` means no sources.
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings). When a publishing skill applies a triage role to the spec, record the same `Status:` line near the top of `spec.md`. This field is reserved for canonical triage roles; Wayfinder lifecycle uses a separate field.
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the referenced path. For a bare issue number, search `.scratch/*/issues/` and use it only if exactly one file has that number; otherwise ask for the feature or path.

## External-request discovery

**Unsupported:** Local Markdown has no reporter/member identity.

## Hierarchy

Record `Parent: <path>` near the top of a child file. Implementation tickets produced from a local spec use `Parent: ../spec.md`; Wayfinder decision tickets use `Parent: ../map.md`.

## Implementation execution and delivery

Used by `implement`. Eligibility, frontier, coordination, result, and terminal semantics come from [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md); this section defines their local-markdown realization.

- **Delivery policy:** setup writes `Delivery-Mode: <direct-commit|pr-mr>` and `Delivery-Target: <branch>`, plus concrete PR/MR publication and inspection operations when `pr-mr` is selected. If no remote delivery surface exists, `pr-mr` is unsupported.
- **Tracker terminal state:** missing `Tracker-State:` means `open`; terminal work uses `Tracker-State: closed`.
- **Execution frontier realization:** scan participating files and read `Work-Item-Role:`, mapped `Status:`, `Tracker-State:`, `Blocked by:`, `Execution-State:`, and child roles. Preserve file/ticket ordering and apply the eligibility/frontier predicates from [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md). Missing `Tracker-State:` represents provider-open; missing `Execution-State:` represents no local claim/suspension marker.
- **Claim / release / suspend:** claim with `Execution-State: claimed`. Release by removing `Execution-State:`. Suspend by replacing the active claim with `Execution-State: suspended`; resume by writing `claimed` before clearing/replacing the suspended representation as one verified file update.
- **Implementation Result:** maintain exactly one `## Implementation Result` section using the semantic result required by `implement`; create it when absent and replace its contents on re-entry.
- **Delivery evidence:** for direct-commit mode, refresh the configured target ref and require `git merge-base --is-ancestor <implementation-sha> <target-ref>` to succeed. For `pr-mr`, use the publication/inspection operation written by setup and require merged/target-branch evidence.
- **Terminal operation:** set `Tracker-State: closed` and clear `Execution-State:`. The operation is safe to repeat.

## Post-mutation verification

After each mutation, re-read the affected markdown file from disk and verify the canonical line, relationship, state, or uniquely keyed result/note required by [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md). File-write success alone is not sufficient when a workflow depends on the exact persisted representation.

## Upstream reconciliation

Used by `reconcile`. The workflow decides requirement satisfaction; this adapter only persists and verifies its inputs/results.

- **Reconciliation Result:** maintain exactly one `## Reconciliation Result` section using the semantic record defined by `reconcile`; create it when absent and replace its contents on rerun.
- **Source-keyed upstream note:** under one `## Reconciliation` section on each direct provenance source, maintain one `### From <spec-path>` subsection per satisfied spec. Replace the matching subsection on rerun rather than appending a duplicate.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a file with one **child** file per ticket.

- **Map**: `.scratch/<effort>/map.md` (the Notes / Decisions-so-far / Fog body).
- **Child ticket**: `.scratch/<effort>/issues/NN-<slug>.md`, numbered from `01`, with the question in the body. A `Type:` line records the ticket type (`research`/`prototype`/`grilling`/`task`); a separate `Wayfinder-State:` line records `open`/`claimed`/`resolved`/`closed`. Do not reuse the triage `Status:` field for this lifecycle.
- **Blocking**: a `Blocked by: NN, NN` line near the top; resolve each referenced file's `Wayfinder-State:` when evaluating the shared blocking predicate.
- **Frontier**: enumerate `.scratch/<effort>/issues/` in ticket-number order, read the Wayfinder lifecycle/claim/blocking facts, and apply the shared frontier rule from [TRACKER-CONTRACT.md](./TRACKER-CONTRACT.md).
- **Claim**: set `Wayfinder-State: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Wayfinder-State: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`. For a ticket ruled out of scope, set `Wayfinder-State: closed` instead.
