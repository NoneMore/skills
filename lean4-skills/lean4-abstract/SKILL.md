---
name: lean4-abstract
description: >-
  User-invoked Lean 4/mathlib study of suspected mathematical reuse within
  one proof or across declarations.
disable-model-invocation: true
license: MIT
---

# Lean 4 Abstract

Investigate a concrete suspected reusable argument or invariant, not an
open-ended repository survey. Shared tactic syntax alone is not evidence.

## Workflow

1. Identify the reuse hypothesis, representative sites, and whether the user
   requested assessment only or authorized edits.
2. Compare hypotheses, constructions, and conclusions. Search the current proof,
   nearby declarations, and existing APIs first; expand only toward a plausible
   specific match.
3. Prefer an existing result; otherwise weigh a local/private helper, a justified
   public theorem, or no extraction. Account for assumptions, dependency
   direction, elaboration cost, and maintenance.
4. Test the candidate and representative uses in the actual Lean context.
   Reject incompatible cases rather than weakening statements or trust.
5. Record the current verification state before authorized edits. Change
   only requested sites, then verify affected consumers and imports. Reading
   other consumers does not authorize migrating them.

## Completion

- **Assessment:** report the evidence, tradeoffs, and recommendation without
  editing production code.
- **Implementation:** report the reused or extracted result, changed consumers,
  and verification gate. If verification or extraction fails, report the blocker
  rather than claiming completion.
