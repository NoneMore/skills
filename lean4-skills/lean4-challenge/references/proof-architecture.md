# Proof architecture

Use when a proof's **mathematical mechanism** may be indirect or fragile; ordinary tactic cleanup belongs elsewhere.

- Recover the theorem's central invariant and how the existing proof establishes it. Do not infer correctness solely from source appearance.
- Compare mechanisms such as induction, transport, universal properties, normal forms, or canonical library theorems—not line counts or tactic syntax.
- Test the pivotal alternate step against the same statement and trust assumptions using a small scratch proof or representative subgoal.
- Examine definitional accidents, rewrite ordering, automation opacity, new hypotheses, imports, and inference costs.
