# Diagnostic and Trust Repair Workflow

Use when the task is to repair a Lean/Lake diagnostic that is not primarily a proof-search problem, or to inspect/remove unwanted trust assumptions in formal-mathematics code. The shared invariants in `SKILL.md` remain in force.

## Contract

1. Inspect the exact current diagnostic, declaration, and nearby source before editing.
2. Classify the failure before choosing a repair. Load `references/compilation-errors.md` for diagnostic-specific guidance and `references/axiom-elimination.md` when the requested property concerns axioms, `sorry`/`admit`, or another trust-basis condition.
3. Make the smallest coherent change that addresses the identified cause rather than masking the symptom.
4. Verify the repaired target with the lightest sufficient gate; load `references/verification.md` when file, dependency, or integration scope matters. Verify trust properties separately when they are part of the request.
5. Continue only while new evidence supports a materially different bounded repair avenue.

## Stop and completion

Stop when no materially new bounded repair avenue remains. Report the blocker, evidence already gathered, and the smallest next action that could change the result.

A repair task is complete when the requested diagnostic or trust-basis condition is resolved, the affected scope satisfies the chosen verification gate, and any remaining uncertainty is explicitly reported.
