# Evidence, retrieval, and uncertainty

Load this reference when a selected resolution involves an externally recoverable fact, an empirical assumption that needs evidence, or material uncertainty that cannot yet be resolved.

## Recover facts and evidence

Do not ask the user for facts or external evidence that can be recovered reliably with available tools at reasonable cost. Use available tools or delegated agents when the runtime supports them.

Treat a recovered fact as settled only when its source authority, freshness, and specificity are adequate for the decision. Otherwise keep it as explicit uncertainty rather than silently upgrading weak evidence to fact.

For an **empirical assumption**, gather relevant evidence and update confidence in the assumption. Supporting evidence is not automatically a fact about the user's specific case. Treat the assumption as resolved only when the evidence is strong and specific enough for the downstream decision; otherwise keep the remaining uncertainty explicit.

If a required fact cannot be recovered and the user cannot authoritatively provide it, or an empirical assumption cannot be supported strongly enough to settle it, keep the uncertainty explicit and continue only where dependencies permit.

## Respect runtime retrieval semantics

If the runtime supports **background work that can remain in flight across user turns**, continue with independent user questions while retrieval is pending.

If retrieval is synchronous—even when multiple tool calls can run in parallel—do not leave started retrieval in flight across a user turn. It is valid to ask an independent user question before starting retrieval; once synchronous retrieval has started, finish it before emitting the next user-facing round. Do not assume sub-agents, background execution, or cross-turn concurrency exist.

## Decide responsibly under irreducible uncertainty

Material uncertainty does not automatically block a dependent decision. Treat it as decision input and test whether the dependent decision can proceed responsibly through one or more of:

- robustness across plausible outcomes,
- reversibility,
- staged commitment,
- bounded downside,
- contingency planning,
- an explicit risk tradeoff where the downside is within the user's authority and compatible with applicable constraints.

For each dependent decision, once the uncertainty is characterized well enough to judge those protections, treat it as **nonblocking for that decision** when a responsible path exists. That dependent decision may then become eligible even though the uncertainty itself remains unresolved.

Retain material residual uncertainty when it is nonblocking, including why it is nonblocking and how the current conclusion or direction accounts for it.

Enter a **blocked** state only when unresolved uncertainty prevents responsible completion of the user's requested outcome—for example, when no responsible recommendation, choice, or execution path can be formed and one is required. Before blocking, verify that no robust, reversible, staged, bounded-downside, or contingent path can proceed without resolving it.
