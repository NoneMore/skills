---
name: to-tickets
description: Break a plan, spec, or conversation into tracer-bullet tickets with explicit dependencies and publish them to the configured tracker.
disable-model-invocation: true
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets**: tracer-bullet vertical slices, each declaring the tickets that **block** it.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to invoke the user-invoked `setup-matt-pocock-skills` skill explicitly using their harness's user-invocation mechanism.

## Process

### 1. Gather context

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching. Every ADR file present should describe a current architectural decision.

Look for opportunities to prefactor the code to make the implementation easier. "Make the change easy, then make the easy change."

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests): vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prefactoring should be done first

</vertical-slice-rules>

Give each ticket its **blocking edges**: the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket; green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Publish the tickets to the configured tracker

Publish one tracker item per approved ticket, blockers first so relationship targets already exist. Use the configured tracker's hierarchy, blocking, and triage-state representations rather than inventing platform behavior.

When the configured tracker defines hierarchy for this publishing workflow and the source is an existing tracker issue/spec, make every generated ticket its child. If there is no source tracker item, do not invent a parent. Wire blocking edges independently and apply the configured `ready-for-agent` state unless instructed otherwise.

**Hierarchy and blocking are orthogonal.** Parent/child says what larger work a ticket belongs to; blocking says what must finish first. Never infer one from the other.

Use `<local-ticket-template>` for local Markdown; otherwise use `<issue-template>` unless the configured tracker requires another body shape.

Do not close, relabel, or rewrite the parent merely because tickets were published; adding the configured child relationship is expected.

After publishing, tell the user that the user-invoked `implement` skill is the normal next step for any frontier ticket (all blockers done), and that they must invoke it explicitly using their harness's user-invocation mechanism. Do not invoke or emulate `implement` yourself.

<local-ticket-template>

# <NN>: <Ticket title>

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective, not a layer-by-layer implementation list.

Blocked by: the numbers/titles of the tickets that gate this one, or "None (can start immediately)".

Status: <configured ready-for-agent role string>

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

<issue-template>

## Parent

Include only when the configured tracker represents hierarchy in the body or requires a textual parent pointer.

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective, not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None (can start immediately)".

</issue-template>

In either form, avoid specific file paths or code snippets: they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.
