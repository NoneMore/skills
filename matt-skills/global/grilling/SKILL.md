---
name: grilling
description: Interactively stress-test a user's plan, decision, or idea by surfacing high-leverage unresolved judgments and assumptions in dependency-aware rounds. Use when the user explicitly wants to be grilled, interrogated, pressure-tested, or challenged through iterative questions to clarify material assumptions, risks, tradeoffs, or a decision. Do not use for one-shot critique, ordinary clarification, or culinary grilling.
---

Treat grilling as **decision clarification**, not exhaustive interviewing. Improve decision quality with the minimum sufficient questioning needed for the user's requested outcome.

## Build the decision model

Maintain an evolving decision model around the user's actual objective. Track only material:

- **Decisions** — choices or judgments to resolve.
- **Facts** — state or constraints that can be recovered or authoritatively supplied by the user.
- **Assumptions** — beliefs whose failure could materially change the decision.

Track prerequisites among them. Actively surface material assumptions, failure modes, or conflicting alternatives the user has not named when they could change the recommendation, risk posture, or execution path.

Look for the upstream decision behind the surface question; distinguish means from ends, preferences from constraints, and reversible choices from commitments. Challenge answers that conflict with the objective, constraints, evidence, or earlier answers.

When a set of material choices is mutually coupled, treat it as a joint tradeoff to resolve rather than reciprocal prerequisites that deadlock eligibility.

Prune branches whose answers are unlikely to change a downstream decision, recommendation, material risk, or execution constraint.

## Select the next resolutions

The **resolution frontier** is the unresolved material nodes whose prerequisites are resolved or sufficiently characterized as nonblocking for that node under the uncertainty policy. Choose a resolution channel before deciding whether to ask the user:

- **User-owned value or judgment** — ask the user before deciding across it. If the user delegates that judgment, decide from the settled objective, constraints, and stated preferences. Instrumental or technical choices may be recommended from the settled decision state without requiring a separate delegation step. A user-owned judgment may remain explicitly deferred when the current staged or reversible path does not decide across it and preserves the future choice; revisit it before any dependent commitment.
- **Private or user-specific fact only the user can authoritatively state** — ask the user.
- **Externally recoverable fact, empirical assumption, or unresolved material uncertainty** — load `references/evidence-and-uncertainty.md` and follow it for that branch.

Prioritize eligible nodes by **decision leverage**: prefer resolutions most likely to eliminate or reshape downstream branches, resolve important uncertainty, expose material risk, or change the recommendation. Let answer or retrieval cost defer low-value nodes.

Select the minimum sufficient set of high-leverage eligible nodes. Ask the user only for selected nodes whose resolution genuinely requires user input; resolve selected recoverable nodes through their appropriate channel. Questions asked in the same round must be independent: if one answer could change whether another should be asked, what it means, its valid answers, or the recommendation, ask the upstream question first. Never batch a node with its descendant.

After each round and each newly recovered piece of material information, recompute the decision model. Do not mechanically resolve the whole frontier. Deferred material nodes remain unresolved and must be reconsidered before completion; low leverage justifies deferral, not pruning.

## Run the interaction

Prefer the harness's native structured question tool when available; treat each selected user question as a separate question and use choices when natural.

Offer a recommendation only when it serves the user's requested outcome and there is a defensible default. Avoid anchoring the user before eliciting a genuinely personal value or preference.

Without a structured question tool, use compact numbered questions and include a recommendation only when useful. Then wait for the user's answers before advancing dependent branches.

## Finish on material completeness

The grilling is complete when the material state is sufficient for the user's requested outcome. If the user wants a choice or recommendation, the state must be sufficient to choose or recommend responsibly. Otherwise it must be sufficient to state the materially relevant conclusions, assumptions, risks, and residual uncertainty without forcing a direction.

Every currently material node must be resolved, explicitly retained as nonblocking uncertainty, or—when it is a user-owned judgment—explicitly deferred because the current path does not decide across it and preserves the future choice. Nodes that become immaterial or dominated after upstream resolutions may be pruned.

At completion, present a compact decision snapshot containing:

- the objective and requested outcome,
- settled material decisions and constraints,
- important assumptions or residual risks,
- the current conclusion, recommendation, or chosen direction, as applicable,
- unresolved uncertainty and deferred user-owned judgments that still matter, why they are nonblocking or safely deferred, and when they must be revisited.

Ask the user to confirm or correct the snapshot. Confirmation completes grilling; it does not authorize consequential actions, which remain subject to normal runtime permission and confirmation rules.

If the user corrects the snapshot, update affected nodes, reopen dependent decisions whose basis changed, recompute the frontier, and continue until the revised snapshot is confirmed.

If applying the uncertainty policy in `references/evidence-and-uncertainty.md` results in a **blocked** state, present the current snapshot, name each blocker and its dependent decisions, and state what evidence or user input would unblock the session. Do not present the grilling as complete or ask for completion confirmation.

If the user asks to stop, summarize the current state and stop.
