# Skill mechanics

Skill-specific mechanics for [`writing-for-agents`](SKILL.md). Use the main skill for general document design; this file only covers invocation and routing.

## Invocation

Choose between two modes.

### Model-invoked

Use when the agent must discover the skill on its own, or another skill must be able to reach it.

- Omit `disable-model-invocation`.
- Write a model-facing `description` that names the capability and the distinct cases that should trigger it.
- Remember that the description is always-loaded context.

Model invocation still allows explicit user invocation.

### User-invoked

Use when the skill should run only when the human chooses it.

- Set `disable-model-invocation: true`.
- Keep the `description` as a concise human-facing summary rather than a trigger list.
- The skill adds no model-discovery context, but the human must remember when to invoke it.

If two user-invoked skills need the same reference, put that reference in a plain shared file rather than duplicating it.

## Splitting by invocation

Create a separate model-invoked skill only when a distinct capability or branch needs independent discovery, or another skill must invoke it.

A new model-invoked skill adds another always-loaded description, so independent reach should justify that cost. Do not split merely because a prompting theory suggests it; validate routing changes when the tradeoff matters.

## Router skills

When many user-invoked skills become hard to remember, use one user-invoked **router skill** that lists them and explains when the human should choose each one.

A router reduces human indexing cost; it does not make user-invoked skills model-discoverable.
