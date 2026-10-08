---
name: grilling
description: Interactively pressure-test a user's plan, decision, or idea through iterative questions. Use when the user explicitly wants to be grilled, interrogated, pressure-tested, or challenged through questions. Do not use for ordinary clarification, one-shot critique, or culinary grilling.
disable-model-invocation: true
---

Treat grilling as **decision clarification**, not exhaustive interviewing. Improve decision quality with the minimum sufficient questioning needed for the user's requested outcome.

## Focus on material state

Track only decisions, facts, and assumptions that could materially change the requested outcome, recommendation, risk posture, or execution constraints. Track prerequisites only where they affect what is meaningful to resolve next.

Actively surface material assumptions, failure modes, or conflicting alternatives the user has not named. Look for the upstream decision behind the surface question; distinguish ends from means, preferences from constraints, and reversible choices from commitments. Challenge answers that conflict with the objective, constraints, evidence, or earlier answers.

When material choices are mutually coupled, treat them as a joint tradeoff instead of forcing an artificial prerequisite order. Drop branches that become immaterial or dominated after upstream resolutions.

## Choose the next resolution

Prefer unresolved material items with the highest **decision leverage**: items most likely to eliminate or reshape downstream work, resolve important uncertainty, expose material risk, or change the recommendation. Let answer or retrieval cost defer lower-value items, but do not silently prune something that remains material.

Ask the user only when resolution genuinely requires user input:

- Ask for personal values or judgments when the outcome depends on them. If the user delegates such a judgment, decide from the stated objective, constraints, and preferences.
- Ask for private or user-specific facts only the user can authoritatively provide.
- Recover external facts or evidence with available tools when doing so is reasonably cheap and relevant to a material decision.

Treat recovered information as settled only when its authority, freshness, and specificity are adequate for the decision. Do not turn weak, stale, generic, or indirect evidence into a fact about the user's case; keep material uncertainty explicit when the evidence is insufficient.

Select the minimum sufficient set of independent user questions. If one answer could change whether another question should be asked, what it means, its valid answers, or the recommendation, ask the upstream question first. Never batch a question with its dependent descendant. Re-evaluate the material state after each user round and after newly recovered material information.

If material uncertainty cannot be resolved, test whether the requested outcome can still be handled responsibly through robustness across plausible outcomes, reversibility, staged commitment, bounded downside, or contingency planning. Keep the uncertainty explicit when such a path exists. Treat it as a blocker only when it prevents responsible completion of the requested outcome.

## Run the interaction

Prefer the harness's native structured question tool when available; otherwise use compact numbered questions. Avoid anchoring the user before eliciting a genuinely personal value or preference. Offer a recommendation when it serves the requested outcome and there is a defensible basis; do not require a separate delegation ceremony for instrumental or technical recommendations once the relevant objective, constraints, and preferences are clear.

Wait for the user's answers before advancing dependent branches.

## Finish on material completeness

The grilling is complete when the material state is sufficient for the user's requested outcome. If the user wants a choice or recommendation, the state must be sufficient to choose or recommend responsibly. Otherwise it is enough to make the materially relevant conclusions, assumptions, risks, and residual uncertainty clear without forcing a direction.

At completion, present a compact decision snapshot with the objective and requested outcome, settled material decisions and constraints, important assumptions or risks, the current conclusion or recommendation when applicable, and any residual uncertainty that still matters. Invite corrections; if a correction invalidates the basis of a dependent decision, reopen that decision and continue from the revised state.

If unresolved uncertainty blocks responsible completion, present the current snapshot, name the blocker and affected decisions, and state what evidence or user input would unblock the session.

If the user asks to stop, summarize the current state and stop.
