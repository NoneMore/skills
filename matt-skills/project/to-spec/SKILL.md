---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
disable-model-invocation: true
---

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user; just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to invoke the user-invoked `setup-matt-pocock-skills` skill explicitly using their harness's user-invocation mechanism.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. Resolve the testing seams from what has already been agreed. Existing seams should be preferred to new ones, and the highest useful seam should win; the fewer seams across the codebase, the better - the ideal number is one. If the conversation did **not** already settle the seams, treat that as an unresolved design decision rather than starting a new interview inside this skill.

3. Check that the conversation is **decision-complete enough to implement**. Material architectural branches, unresolved product choices, or unverified assumptions that would force the implementing agent to make a design decision are blockers. Do not invent answers just to finish the spec, and do not mark a blocked spec `ready-for-agent`. Instead, tell the user which unresolved decisions remain and suggest the appropriate **user-invoked** workflow by canonical skill name (normally `grill-with-docs`, or `wayfinder` for a multi-session decision space). Tell the human to invoke it explicitly using their harness's user-invocation mechanism; do not invoke, read, shell out to, or emulate those workflows yourself.

4. Write the spec using the template below, then publish it to the project issue tracker. Apply the configured `ready-for-agent` triage role - no need for additional triage. For a local-markdown tracker, record the configured role string as `Status: <role>` near the top of the spec.

5. After publishing, tell the user that the user-invoked `to-tickets` skill is the normal next workflow when they want implementation tickets, and that they must invoke it explicitly using their harness's user-invocation mechanism. Do not invoke or emulate it yourself.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A LONG, numbered list of user stories. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

This list of user stories should be extremely extensive and cover all aspects of the feature.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Which modules will be tested
- Prior art for the tests (i.e. similar types of tests in the codebase)

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>
