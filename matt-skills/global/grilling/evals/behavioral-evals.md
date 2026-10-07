# Behavioral evals

Use these cases only for behavior that is difficult to verify by static inspection. Run each scenario in isolation. Score observable behavior and actions, not whether the agent repeats wording from the Skill.

## 1. Routing distinguishes pressure-testing from nearby intents

Run with normal discovery/routing and `grilling` not pre-activated. Run each prompt independently.

Prompt A: Interrogate my launch plan one question at a time until the important assumptions are clear.

Prompt B: Grill my business plan, but give me a one-shot critique in one response and do not ask questions.

Prompt C: I am choosing a monitor. Ask whatever details you need, then recommend one.

Prompt D: How do I grill salmon without drying it out?

Required assertions:
- `interactive_pressure_test_routed_to_grilling = PASS`
- `explicit_one_shot_request_did_not_route = PASS`
- `ordinary_interactive_consultation_did_not_route = PASS`
- `culinary_prompt_did_not_route = PASS`

## 2. Prerequisites, batching, and pruning produce an observable transition

Turn 1 user: Grill my launch decision. The latest acceptable launch date and maximum budget are independent constraints. Packaging depends on budget. Packaging A requires at least $50,000; Packaging B is the only feasible family below $50,000.

Expected after turn 1: ask deadline and budget in the same round; do not ask packaging yet.

Turn 2 user: The deadline is November 15 and the budget is $40,000.

Expected after turn 2: eliminate Packaging A and do not ask the user to choose A versus B. Ask only still-material descendants of Packaging B.

Required assertions:
- `batched_independent_upstream_questions = PASS`
- `deferred_dependent_packaging_question = PASS`
- `pruned_infeasible_packaging_a_after_budget = PASS`
- `did_not_ask_dominated_a_vs_b_choice = PASS`

## 3. Decision leverage may defer but not silently discard material work

Turn 1 user: Grill my rollout plan. Whether a security review is required has the highest leverage. Rollback-by-cohort is lower leverage but still material to risk. Logo color and office location are immaterial.

Expected after turn 1: prioritize security; it is acceptable to defer rollback-by-cohort; do not ask the immaterial questions.

Turn 2 fixture: security is resolved and does not eliminate the rollback question.

Expected after turn 2: reconsider rollback-by-cohort before completion.

Required assertions:
- `prioritized_high_leverage_security_issue = PASS`
- `did_not_expand_immaterial_questions = PASS`
- `reconsidered_still_material_deferred_issue = PASS`

## 4. Fact and evidence boundaries change who is asked and what becomes settled

Run each prompt independently with the stated runtime fixture.

Prompt A fixture: an authoritative current platform-docs tool reports a 128 MiB request limit. Prompt: Grill my architecture decision; my preferred design needs at least 64 MiB.

Prompt B fixture: no available tool can access the user's internal hiring budget. Prompt: Grill my hiring plan; the decision depends on that budget.

Prompt C fixture: the only evidence for a material platform limit is an undated third-party forum post that conflicts with the user's recollection. Prompt: Grill my architecture decision; whether I can keep the design depends on that limit.

Required assertions:
- `used_authoritative_recoverable_fact_without_asking_user_to_research = PASS`
- `asked_user_for_private_authoritative_fact = PASS`
- `did_not_upgrade_weak_evidence_to_settled_fact = PASS`
- `kept_material_uncertainty_explicit_when_evidence_was_insufficient = PASS`

## 5. Personal values are elicited, while instrumental recommendations need no ceremony

Run each prompt independently.

Prompt A: Grill my choice between a higher-paying role and a lower-paying role with much more autonomy. I have not said how I value compensation versus autonomy.

Prompt B: Pressure-test my architecture and recommend A or B. My budget supports either; latency matters about twice as much as cost; I have no other preference between them.

Required assertions:
- `elicited_personal_tradeoff_before_recommending_job_choice = PASS`
- `did_not_anchor_unstated_personal_preference = PASS`
- `recommended_instrumental_architecture_choice_when_basis_was_sufficient = PASS`
- `did_not_require_delegation_formula_for_technical_recommendation = PASS`

## 6. Uncertainty is nonblocking when a responsible path exists and blocking when none does

Run each prompt independently.

Prompt A fixture: six-month demand cannot be resolved before the deadline, but the plausible range shows that a two-week pilot with a fixed $10,000 downside cap, reversible commitments, and a stop condition is responsible across the range. Prompt: Grill my launch decision; I need a strategy despite the unresolved demand.

Prompt B fixture: a regulatory classification determines whether the launch path is lawful. Neither tools nor the user can determine it, and no robust, reversible, staged, bounded-downside, or contingent path can proceed responsibly without it. Prompt: Continue grilling my launch plan.

Required assertions:
- `kept_unresolved_demand_explicit = PASS`
- `advanced_to_responsible_pilot_instead_of_demanding_false_certainty = PASS`
- `reported_regulatory_classification_as_blocker = PASS`
- `stated_what_would_unblock_the_blocked_case = PASS`

## 7. Coupled choices and unmentioned assumptions are handled without mechanical traversal

Run each prompt independently.

Prompt A: Grill my event plan. Budget, scope, and date are mutually coupled: each changes the sensible range of the others.

Prompt B: Grill this launch plan. We will ship an analytics integration to enterprise support teams in six weeks. Customers will connect live support inboxes, and we plan to retain representative conversations for evaluation. Sales has verbal interest and engineering believes the core feature can be built on time.

Required assertions:
- `treated_coupled_choices_as_joint_tradeoff = PASS`
- `did_not_deadlock_on_reciprocal_prerequisites = PASS`
- `surfaced_material_data_permission_or_retention_assumption = PASS`
- `connected_discovered_assumption_to_launch_feasibility_or_risk = PASS`

## 8. Completion follows the requested outcome and material corrections reopen reasoning

Run each case independently.

Case A prompt: Interrogate this product plan until the important assumptions and risks are clear. I do not want a go/no-go recommendation.

Expected A: once the material assumptions, constraints, risks, and residual uncertainty are sufficiently clear, finish with a compact snapshot without manufacturing a recommendation.

Case B established state: the current snapshot treats November 15 as a hard launch deadline, and a packaging recommendation depends materially on that deadline.

Case B user: Correction: November 15 is only a preference; January 31 is the hard deadline.

Expected B: update the deadline state and reopen the packaging reasoning if the corrected deadline changes its basis.

Required assertions:
- `completed_when_requested_pressure_test_outcome_was_satisfied = PASS`
- `did_not_force_unrequested_go_no_go_recommendation = PASS`
- `snapshot_exposed_material_conclusions_and_uncertainty = PASS`
- `reopened_affected_dependent_reasoning_after_material_correction = PASS`
