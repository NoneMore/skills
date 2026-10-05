---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, keeping domain docs and current architecture decisions up to date.
disable-model-invocation: true
---

Call the Skill tool twice, for "grilling" and "domain-modeling".

Treat those two model-invoked skills as the whole design phase: grilling drives the decision tree, while domain-modeling keeps the glossary and current architectural decisions up to date. Task-local design and implementation choices remain ephemeral unless they grow into decisions future work should know about.

When the user confirms that shared understanding has been reached, stop this workflow. Do not create a spec, tickets, or implementation merely because the design is now settled: those are separate **user-invoked** phase transitions. If formalization would be useful, tell the user to invoke the user-invoked `to-spec` skill explicitly using their harness's user-invocation mechanism; if the work is small enough to implement directly, suggest the user-invoked `implement` skill the same way. Do not emulate a user-invoked skill by reading its `SKILL.md`, shelling out to it, or translating it into a host-specific command syntax yourself.
