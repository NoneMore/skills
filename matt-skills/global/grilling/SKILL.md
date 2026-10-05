---
name: grilling
description: Interactively stress-test a user's plan, decision, or idea by surfacing high-leverage unresolved judgments and assumptions in dependency-aware rounds. Use when the user explicitly wants an interactive questioning process: to be grilled, interrogated, challenged through questions, or to iteratively resolve assumptions before a recommendation. Do not use for one-shot critique or culinary grilling.
---

Treat grilling as **decision clarification**, not exhaustive interviewing. The goal is to improve decision quality with the fewest useful questions.

## Build the decision model

Maintain an evolving **decision graph** around the user's actual objective.

Represent only nodes that can materially affect the recommendation, risk posture, or execution path:

- **Decisions** — choices or judgments the user must own.
- **Facts** — state or constraints that can be recovered from the environment or supplied authoritatively by the user.
- **Assumptions** — beliefs whose failure could materially change the decision.
- **Dependencies** — which nodes must be resolved before another node becomes meaningful.

Look for the upstream decision behind the surface question. Distinguish means from ends, preferences from constraints, and reversible choices from commitments. Challenge answers that conflict with the stated objective, constraints, evidence, or earlier answers.

Do not expand a branch merely because more questions are possible. Prune branches whose answers are unlikely to change a downstream decision, recommendation, material risk, or execution constraint.

## Select the next resolutions

The **resolution frontier** is the set of unresolved material decision, fact, or assumption nodes whose prerequisites are already resolved.

For each eligible node, choose the resolution channel before deciding whether to ask a question:

- **User-owned decision or value** — ask the user.
- **Private or user-specific fact only the user can authoritatively state** — ask the user.
- **Externally recoverable fact** — recover it with available tools at reasonable cost.
- **Empirical assumption** — gather relevant evidence with available tools at reasonable cost and update confidence in the assumption; do not convert supporting evidence into a fact about the user's case.
- **Material node that neither tools nor the user can currently resolve** — mark it as a blocker.

Eligibility is not enough: prioritize the resolution frontier by **decision leverage**. Prefer nodes whose resolution is most likely to eliminate or reshape downstream branches, resolve important uncertainty, expose material risk, or change the recommendation. Treat answer or retrieval cost as a reason to defer low-value nodes.

The **question frontier** is the subset of the selected resolution frontier that requires a user response.

Questions in the same round must be independent. If answering one could change whether another should be asked, what it means, which answers are valid, or what you would recommend, they are not parallel. Ask the upstream question first. Never batch a node with its descendant.

Ask the smallest useful set of high-leverage question-frontier nodes, resolve selected tool-recoverable nodes, then recompute the graph and resolution frontier after every round and after any newly recovered fact or material evidence. Do not mechanically ask or resolve the whole frontier.

## Recover facts and evidence instead of outsourcing research

Do not ask the user for facts or external evidence that can be recovered reliably with available tools at reasonable cost. Use available tools or delegated agents to recover them.

Ask the user when a fact is private, user-specific, unavailable to the runtime, or something only they can authoritatively state. User-owned values and judgments remain theirs to decide.

Treat a recovered fact as settled only when its source authority, freshness, and specificity are adequate for the decision. Otherwise keep it as an explicit uncertainty rather than silently upgrading weak evidence to fact.

Treat an empirical assumption as resolved only when the available evidence is strong and specific enough for the downstream decision at stake. Evidence may raise or lower confidence without settling the assumption. If uncertainty could still materially change the recommendation, risk posture, or execution path, keep the assumption explicit or mark it as a blocker rather than relabeling it as fact.

If the runtime supports **background retrieval that can remain in flight across user turns**, continue with independent question-frontier nodes while retrieval is pending. If the runtime only supports synchronous retrieval—even when multiple tool calls can run in parallel—finish the selected retrieval before emitting the next user-facing round. Do not assume sub-agents, background execution, or cross-turn concurrency exist.

If a required fact cannot be recovered and the user cannot authoritatively provide it, or if a required empirical assumption cannot be supported strongly enough for the dependent decision, mark the uncertainty as a blocker and continue only on branches that do not depend on it.

## Run the interaction

Prefer the harness's native structured question tool when available. Treat each selected question-frontier node as a separate question and use choices when natural.

Offer your current recommendation when there is a defensible default and doing so helps expose the tradeoff. Do not invent a recommendation, and avoid anchoring the user before eliciting a genuinely personal value or preference.

Without a structured question tool, format a round compactly, for example:

```
❓ **Q1 — <title>**: <question, with choices when useful>

➡️ <current recommendation and rationale, when useful>

---

❓ **Q2 — <title>**: <question>
```

Then wait for the user's answers before advancing dependent branches.

## Finish on material completeness

The grilling is complete when no unresolved material decision, fact, or assumption is reasonably likely to change the user's objective, recommendation, material risk posture, or execution path. Do not continue merely to make the graph exhaustive.

At completion, present a compact decision snapshot containing:

- the objective,
- the material decisions and constraints now settled,
- the important assumptions or residual risks,
- the current recommendation or chosen direction,
- any unresolved uncertainty that still matters but does not block the direction.

Ask the user to confirm or correct that snapshot so shared understanding is observable. Confirmation completes the grilling; it is not authorization for consequential actions, which remain subject to the runtime's normal permission and confirmation rules.

If the user corrects the snapshot, update the affected nodes, reopen any dependent decisions whose basis changed, recompute the resolution frontier, and continue the grilling. Do not treat the session as complete until the revised snapshot is confirmed.

If all independent branches are exhausted but a material unresolved node still could change the recommendation, risk posture, or execution path and cannot currently be resolved, stop in a **blocked** state. Present the current snapshot, name each blocker and the decisions that depend on it, and state what evidence or user input would unblock the session. Do not present the grilling as complete or ask for completion confirmation.

If the user asks to stop, summarize the current state and stop.
