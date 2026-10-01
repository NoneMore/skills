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

Work from whatever is already in the conversation context. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments plus its persisted work-item role and relationships.

### 2. Use codebase context

Use codebase context already available in the conversation to align ticket terminology with the project's domain vocabulary and ADRs.

If a prerequisite refactor is required before an independently verifiable slice can land, model that refactor as a blocking ticket.

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but complete path through every layer required by the behaviour, rather than isolating one implementation layer
- A completed slice is demoable or verifiable on its own

</vertical-slice-rules>

Give each ticket its **blocking edges**: the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

A mechanical refactor does not need to be forced into vertical slices when affected subsets cannot land green independently. Represent whatever sequencing or integration work is required explicitly in the ticket graph.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each blocker have to finish before the blocked ticket can start?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Publish the tickets to the configured tracker

Publish one tracker item per approved ticket, blockers first so relationship targets already exist. Give every published item work-item role `implementation-ticket`. Use the configured tracker's hierarchy, blocking, and triage-state representations rather than inventing platform behavior.

When the source is an existing tracker spec, make every generated ticket its child. If there is no source spec tracker item, do not invent a parent. Wire blocking edges independently and apply the configured `ready-for-agent` state unless instructed otherwise. Do not add `derived-from` merely to mirror the spec parent, and never copy the spec's upstream provenance chain onto implementation tickets.

**Hierarchy, blocking, and provenance are orthogonal.** Parent/child says what larger work a ticket belongs to; blocking says what must finish first; provenance says which earlier artifact directly informed a newly derived artifact. Never infer one from another.

Use `<local-ticket-template>` for local Markdown; when a local spec is the source, insert `Parent: ../spec.md` immediately after the work-item role, and omit that line when there is no source spec. Otherwise use `<issue-template>` unless the configured tracker requires another body shape.

Do not close, relabel, or rewrite the parent merely because tickets were published; adding the configured child relationship is expected.

After publishing, re-read every created ticket when the tracker supports it and verify its work-item role, parent, blockers, and triage state. The persisted graph, not the intended write, is the completion condition.

Then tell the user that the user-invoked `implement` skill is the normal next step for any frontier ticket (all blockers done), and that they must invoke it explicitly using their harness's user-invocation mechanism. Do not invoke or emulate `implement` yourself.

<local-ticket-template>

# <NN>: <Ticket title>

Work-Item-Role: implementation-ticket

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective, not a layer-by-layer implementation list.

Blocked by: the relative paths of the local ticket files that gate this one, or "None (can start immediately)".

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


