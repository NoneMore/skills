---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
disable-model-invocation: true
---

Call the Skill tool twice, for "grilling" and "domain-modeling".

Treat those two model-invoked skills as the whole design phase: grilling drives the decision tree, while domain-modeling keeps the glossary and ADRs current as decisions crystallize.

When the user confirms that shared understanding has been reached, stop this workflow. Do not create a spec, tickets, or implementation merely because the design is now settled: those are separate **user-invoked** phase transitions. If formalization would be useful, tell the user to invoke the user-invoked `to-spec` skill explicitly using their harness's user-invocation mechanism; if the work is small enough to implement directly, suggest the user-invoked `implement` skill the same way. Do not emulate a user-invoked skill by reading its `SKILL.md`, shelling out to it, or translating it into a host-specific command syntax yourself.
