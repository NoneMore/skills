# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Work-item role is `Work-Item-Role: <request|decision-map|decision-ticket|spec|implementation-ticket>` near the top of each participating file.
- Provenance is `Derived-From: <path>, <path>` on the derived file; missing or `Derived-From: None` means no sources.
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings). When a publishing skill applies a triage role to the spec, record the same `Status:` line near the top of `spec.md`. This field is reserved for canonical triage roles; Wayfinder lifecycle uses a separate field.
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

Work-item role and provenance are independent from hierarchy, blocking, triage state, `Type:`, and `Wayfinder-State:`.

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the referenced path. For a bare issue number, search `.scratch/*/issues/` and use it only if exactly one file has that number; otherwise ask for the feature or path.

## Hierarchy

Record `Parent: <path>` near the top of a child file. Implementation tickets produced from a local spec use `Parent: ../spec.md`; Wayfinder decision tickets use `Parent: ../map.md`.

## Implementation execution and delivery

Used by `implement`. Triage `Status:`, implementation execution, repository delivery, and terminal tracker state are separate fields/sections.

- **Delivery policy:** setup writes `Delivery-Mode: <direct-commit|pr-mr>` and `Delivery-Target: <branch>` into this section of the generated tracker config, plus a concrete PR/MR publication/inspection operation when `pr-mr` is selected. If no remote delivery surface exists, `pr-mr` is unsupported rather than guessed.
- **Tracker terminal state:** missing `Tracker-State:` means `open` for backward compatibility. Finalization writes `Tracker-State: closed`; do not reuse triage `Status:` for terminal state.
- **Execution frontier:** scan participating request/spec/implementation-ticket files whose tracker state is open and whose mapped triage `Status:` is `ready-for-agent`. Exclude files with unresolved `Blocked by`, or `Execution-State: claimed|blocked|awaiting-delivery|finalized`. Missing `Execution-State:` means unclaimed/open. A spec with any child carrying `Work-Item-Role: implementation-ticket` is not an execution leaf; its children own execution.
- **Claim:** set `Execution-State: claimed` and save before any code/test mutation. Re-read the file and frontier to verify the claim persisted and the item disappeared from normal discovery.
- **Blocked / awaiting delivery:** replace the execution field with `Execution-State: blocked` or `Execution-State: awaiting-delivery`. This transition releases the active claim while keeping the item outside the frontier. A real blocker should also be recorded in `Blocked by`.
- **Implementation Result:** maintain exactly one `## Implementation Result` section using the semantic result shape required by `implement`; create it when absent and replace its contents on re-entry.
- **Delivery evidence:** for direct-commit mode, refresh the configured target ref and require `git merge-base --is-ancestor <implementation-sha> <target-ref>` to succeed. For `pr-mr`, use the concrete publication/inspection operation written here by setup and require merged/target-branch evidence; do not infer completion from an open request or local commit.
- **Finalize delivered:** upsert `Outcome: delivered`, set `Execution-State: finalized` and `Tracker-State: closed`, then re-read the file. Seeing those same values with one canonical result is an idempotent no-op.
- **Abandon:** upsert `Outcome: abandoned`, set `Execution-State: finalized` and `Tracker-State: closed`, then re-read the terminal file.

## Wayfinding operations

Used by the `wayfinder` skill. The **map** is a file with one **child** file per ticket.

- **Map**: `.scratch/<effort>/map.md` (the Notes / Decisions-so-far / Fog body).
- **Child ticket**: `.scratch/<effort>/issues/NN-<slug>.md`, numbered from `01`, with the question in the body. A `Type:` line records the ticket type (`research`/`prototype`/`grilling`/`task`); a separate `Wayfinder-State:` line records `open`/`claimed`/`resolved`/`closed`. Do not reuse the triage `Status:` field for this lifecycle.
- **Blocking**: a `Blocked by: NN, NN` line near the top. A ticket is unblocked when every file it lists has `Wayfinder-State: resolved` or `Wayfinder-State: closed`.
- **Frontier**: scan `.scratch/<effort>/issues/` for files with `Wayfinder-State: open` that are unblocked and unclaimed; first by number wins.
- **Claim**: set `Wayfinder-State: claimed` and save before any work.
- **Resolve**: append the answer under an `## Answer` heading, set `Wayfinder-State: resolved`, then append a context pointer (gist + link) to the map's Decisions-so-far in `map.md`. For a ticket ruled out of scope, set `Wayfinder-State: closed` instead.
