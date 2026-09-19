---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS - not the current workspace.

Include a "suggested skills" section in the document, but preserve invocation ownership:

- For **model-invoked** skills, name the skill and say the next agent should call the Skill tool for it.
- For **user-invoked** skills (`disable-model-invocation: true` / implicit invocation disabled), do not tell the next agent to call or read them. Put them under a separate "suggested user workflows" subsection and say that the human must invoke them explicitly using the destination harness's user-invocation mechanism (for example the `to-spec` skill), without inventing a slash, dollar, shell, or file-read invocation.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
