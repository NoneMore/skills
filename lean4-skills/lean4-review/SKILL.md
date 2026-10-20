---
name: lean4-review
description: "Use for independent review of Lean 4/mathlib statements or proof code, including fidelity to the intended mathematical claim, correctness, trust dependencies, robustness, library integration, maintainability, and proof quality. Review-only requests are read-only."
license: MIT
---

# Lean 4 Review

Review only the requested scope. Review-only requests are read-only; if fixes are explicitly requested, substantiate each material finding before making the corresponding bounded change.

## Review order

1. **Statement fidelity and assumptions:** when statement correctness is requested (including for unchanged or already-proven declarations), or when new/changed claims pose material semantic risk, compare exact quantifiers, carriers, and assumptions with the intended mathematical result and prerequisites of reused theorems. Probe a consequential boundary case when useful, without open-ended refutation. A checked proof establishes its formal proposition under the accepted trust basis, not fidelity to the intended claim; distinguish semantic concerns from Lean-certified counterexamples. For a changed API with a known downstream consumer, check one representative use for required hypotheses and retained information without expanding into abstraction discovery; report that the sample does not establish compatibility for unexamined consumers.
2. **Correctness and trust:** diagnostics, unresolved `sorry`/`admit`, material trust concerns, and a verification gate that exercises any dependency or integration boundary behind the claim. When the request is a trust audit, inspect the declaration's actual axiom/assumption dependencies (for example with `#print axioms <declaration>` when relevant), distinguish project axioms, unresolved placeholders, transitive assumptions, and ordinary Lean/kernel principles, and interpret them against the requested policy. Successful elaboration alone is not a trust audit.
3. **Robustness:** unnecessary automation, brittle rewrites, typeclass/coercion sensitivity, and accidental definitional dependence.
4. **Library integration:** existing mathlib lemmas, duplicated helpers, canonical abstractions, and avoidable imports; validate candidate APIs in context.
5. **Maintainability:** proof structure, naming, comments/docstrings, and project conventions. Consider optimization only when it materially improves directness, determinism, performance, or clarity.

## Completion

Return prioritized findings with location, evidence, impact, and recommendation. Distinguish blockers from advisory suggestions; if there are no material findings, say so rather than inventing nits. State verification limits that prevent a conclusive correctness claim. For a trust audit, also state the declaration checked, policy used, assumptions found, and any material trust uncertainty.
