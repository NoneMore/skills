# Evidence, retrieval, and uncertainty

Load this reference when the selected resolution frontier contains an externally recoverable fact, an empirical assumption that needs evidence, or material uncertainty that cannot yet be resolved.

## Recover facts and evidence

Do not ask the user for facts or external evidence that can be recovered reliably with available tools at reasonable cost. Use available tools or delegated agents when the runtime supports them. User-owned values and judgments remain the user's to decide.

Treat a recovered fact as settled only when its source authority, freshness, and specificity are adequate for the decision. Otherwise keep it as explicit uncertainty rather than silently upgrading weak evidence to fact.

For an **empirical assumption**, gather relevant evidence and update confidence in the assumption. Supporting evidence is not automatically a fact about the user's specific case. Treat the assumption as resolved only when the evidence is strong and specific enough for the downstream decision; otherwise keep the remaining uncertainty explicit.

If a required fact cannot be recovered and the user cannot authoritatively provide it, or an empirical assumption cannot be supported strongly enough to settle it, keep the uncertainty explicit and continue only where dependencies permit.

## Respect runtime retrieval semantics

If the runtime supports **background retrieval that can remain in flight across user turns**, continue with independent question-frontier nodes while retrieval is pending.

If retrieval is synchronous—even when multiple tool calls can run in parallel—finish the selected retrieval before emitting the next user-facing round. Do not assume sub-agents, background execution, or cross-turn concurrency exist.

## Decide responsibly under irreducible uncertainty

Material uncertainty does not automatically block a decision. Treat it as decision input and test whether the dependent decision can proceed responsibly through one or more of:

- robustness across plausible outcomes,
- reversibility,
- staged commitment,
- bounded downside,
- contingency planning,
- an explicit risk tradeoff.

Retain material residual uncertainty in the decision state when it is nonblocking, including why it is nonblocking and how the proposed direction accounts for it.

Enter a **blocked** state only when the unresolved uncertainty prevents any responsible recommendation or execution path. Before blocking, verify that no robust, reversible, staged, bounded-downside, or contingent path can proceed without resolving it.
