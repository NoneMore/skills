---
name: grilling
description: Interactively stress-test a user's plan, decision, or idea by surfacing high-leverage unresolved judgments and assumptions in dependency-aware rounds. Use when the user explicitly wants to be grilled, interrogated, challenged through questions, or wants assumptions resolved before a recommendation. Do not use for one-shot critique or culinary grilling.
---

Treat grilling as **decision clarification**, not exhaustive interviewing. The goal is to improve decision quality with the fewest useful questions.

## Build the decision model

Maintain an evolving **decision graph** around the user's actual objective.

Represent only nodes that can materially affect the recommendation, risk posture, or execution path:

- **Decisions** — choices or judgments the user must own.
- **Facts** — state or constraints that can be recovered from the environment or supplied authoritatively by the user.
- **Assumptions** — beliefs whose failure could materially change the decision.
- **Dependencies** — which nodes must be resolved before another question becomes meaningful.

Look for the upstream decision behind the surface question. Distinguish means from ends, preferences from constraints, and reversible choices from commitments. Challenge answers that conflict with the stated objective, constraints, evidence, or earlier answers.

Do not expand a branch merely because more questions are possible. Prune branches whose answers are unlikely to change a downstream decision, recommendation, material risk, or execution constraint.

## Select the next questions

The **frontier** is the set of unresolved decision or assumption nodes whose prerequisites are already resolved.

Eligibility is not enough: prioritize the frontier by **decision leverage**. Prefer questions whose answers are most likely to eliminate or reshape downstream branches, resolve important uncertainty, expose material risk, or change the recommendation. Treat answer cost as a reason to defer low-value questions.

Questions in the same round must be independent. If answering one could change whether another should be asked, what it means, which answers are valid, or what you would recommend, they are not parallel. Ask the upstream question first. Never batch a node with its descendant.

Ask the smallest useful set of high-leverage frontier questions, then recompute the graph and frontier after every round and after any newly recovered fact. Do not mechanically ask the whole frontier.

## Recover facts instead of outsourcing research

Do not ask the user for facts that can be recovered reliably with available tools at reasonable cost. Use available tools or delegated agents to resolve them.

Ask the user when the fact is private, preference-dependent, unavailable to the runtime, or something only they can authoritatively state. User-owned values and judgments remain theirs to decide.

If the runtime supports concurrent retrieval, continue with independent frontier questions while facts are being recovered. Otherwise resolve the prerequisite before advancing its dependent branch. Do not assume sub-agents or asynchronous execution exist.

If a required fact cannot be recovered and the user cannot authoritatively provide it, mark the uncertainty explicitly and continue only on branches that do not depend on it.

## Run the interaction

Prefer the harness's native structured question tool when available. Treat each selected frontier node as a separate question and use choices when natural.

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

The grilling is complete when no unresolved decision, assumption, or missing fact is reasonably likely to change the user's objective, recommendation, material risk posture, or execution path. Do not continue merely to make the graph exhaustive.

At completion, present a compact decision snapshot containing:

- the objective,
- the material decisions and constraints now settled,
- the important assumptions or residual risks,
- the current recommendation or chosen direction,
- any unresolved uncertainty that still matters.

Ask the user to confirm or correct that snapshot so shared understanding is observable. Confirmation completes the grilling; it is not authorization for consequential actions, which remain subject to the runtime's normal permission and confirmation rules.

If the user asks to stop, summarize the current state and stop.