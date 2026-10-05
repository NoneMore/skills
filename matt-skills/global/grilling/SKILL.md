---
name: grilling
description: Interactively stress-test a user's plan, decision, or idea by surfacing high-leverage unresolved judgments and assumptions in dependency-aware rounds. Use when the user explicitly wants an interactive questioning process: to be grilled, interrogated, challenged through questions, or to iteratively resolve assumptions before a recommendation. Do not use for one-shot critique or culinary grilling.
---

Treat grilling as **decision clarification**, not exhaustive interviewing. Improve decision quality with the minimum sufficient questioning needed to resolve the material decision state.

## Build the decision model

Maintain an evolving **decision graph** around the user's actual objective. Represent only material:

- **Decisions** — choices or judgments the user must own.
- **Facts** — state or constraints that can be recovered or authoritatively supplied by the user.
- **Assumptions** — beliefs whose failure could materially change the decision.

Represent prerequisites as dependency edges, not another node type. Look for the upstream decision behind the surface question; distinguish means from ends, preferences from constraints, and reversible choices from commitments. Challenge answers that conflict with the objective, constraints, evidence, or earlier answers.

Prune branches whose answers are unlikely to change a downstream decision, recommendation, material risk, or execution constraint.

## Select the next resolutions

The **resolution frontier** is the unresolved material nodes whose prerequisites are resolved. Choose a resolution channel before deciding whether to ask the user:

- **User-owned decision or value** — ask the user.
- **Private or user-specific fact only the user can authoritatively state** — ask the user.
- **Externally recoverable fact, empirical assumption, or unresolved material uncertainty** — load `references/evidence-and-uncertainty.md` and follow it for that branch.

Prioritize eligible nodes by **decision leverage**: prefer resolutions most likely to eliminate or reshape downstream branches, resolve important uncertainty, expose material risk, or change the recommendation. Let answer or retrieval cost defer low-value nodes.

The **question frontier** is the selected resolution-frontier subset that requires a user response. Questions in the same round must be independent: if one answer could change whether another should be asked, what it means, its valid answers, or the recommendation, ask the upstream question first. Never batch a node with its descendant.

Ask the minimum sufficient set of high-leverage questions, resolve selected tool-recoverable nodes, then recompute the graph after every round and after newly recovered material information. Do not mechanically resolve the whole frontier. Deferred material nodes remain unresolved and must be reconsidered before completion; do not prune them merely to reduce question count.

## Run the interaction

Prefer the harness's native structured question tool when available; treat each selected question-frontier node as a separate question and use choices when natural.

Offer a current recommendation only when there is a defensible default and doing so helps expose the tradeoff. Avoid anchoring the user before eliciting a genuinely personal value or preference.

Without a structured question tool, use compact numbered questions and include a recommendation only when useful. Then wait for the user's answers before advancing dependent branches.

## Finish on material completeness

The grilling is complete when the material decision state is sufficient to choose or recommend a direction responsibly. Every material node must be resolved, explicitly retained as nonblocking uncertainty with its decision implications understood, or pruned for a stated reason such as immateriality or dominance.

At completion, present a compact decision snapshot containing:

- the objective,
- settled material decisions and constraints,
- important assumptions or residual risks,
- the current recommendation or chosen direction,
- unresolved uncertainty that still matters, why it is nonblocking, and how the direction accounts for it.

Ask the user to confirm or correct the snapshot. Confirmation completes grilling; it does not authorize consequential actions, which remain subject to normal runtime permission and confirmation rules.

If the user corrects the snapshot, update affected nodes, reopen dependent decisions whose basis changed, recompute the frontier, and continue until the revised snapshot is confirmed.

If a material unresolved node prevents any responsible recommendation or execution path after applying the uncertainty handling in `references/evidence-and-uncertainty.md`, stop in a **blocked** state. Present the current snapshot, name each blocker and its dependent decisions, and state what evidence or user input would unblock the session. Do not present the grilling as complete or ask for completion confirmation.

If the user asks to stop, summarize the current state and stop.
