---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---

Implement the work described by the user in the spec or tickets.

Before making changes, record the current `HEAD` as the review fixed point unless the user or ticket already supplied a different fixed point. Keep that value for the final review.

Before writing any test or implementation code, call the Skill tool with "tdd" and follow it. If the spec or ticket explicitly names testing seams, treat those seams as already agreed. If it does not, follow `tdd` and get the user's confirmation before writing tests.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once implementation and tests are complete, call the Skill tool with "code-review" exactly once. Use the review fixed point captured before implementation as the review baseline; it counts as a fixed point supplied by this enclosing workflow, so do not ask the user to choose it again.

Commit your work to the current branch only after the review has been addressed.
