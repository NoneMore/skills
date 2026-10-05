# Behavioral evals

These scenarios protect grilling as a decision-quality policy rather than an exhaustive interview loop. Run each scenario as an isolated conversation with the skill active unless the scenario explicitly says it is a routing test. Treat stated runtime capabilities and tool results as part of the fixture. Score observable behavior and actions, not merely whether the agent repeats the desired rule. Record each required assertion as PASS or FAIL.

## 1. Ask the upstream decision before dependent details

Prompt: Grill my product launch plan. I have not decided whether success means landing a few enterprise design partners or maximizing self-serve signups.

Required assertions:
- `asked_upstream_goal_before_channel_pricing_or_campaign_details = PASS`
- `did_not_batch_descendants_with_their_prerequisite = PASS`

## 2. Prefer high-leverage frontier questions over exhaustive batching

Prompt: Grill my startup plan. The current frontier includes runway, regulatory exposure, logo color, office location, and whether the product requires sensitive customer data.

Required assertions:
- `prioritized_material_constraints_and_risks = PASS`
- `deferred_or_pruned_low_impact_branding_and_office_questions = PASS`
- `did_not_ask_the_whole_frontier_mechanically = PASS`

## 3. Parallel questions stay independent and answers cause an observable frontier transition

Turn 1 user: Grill my launch decision. Two unresolved constraints are independently authoritative: the latest acceptable launch date and the maximum budget. A packaging decision depends on the budget. Packaging A requires at least $50,000; Packaging B is the only feasible packaging family below $50,000. The packaging family materially affects launch scope.

Expected after turn 1: ask the deadline and budget in the same round; do not ask the packaging question yet.

Turn 2 user: The latest acceptable launch date is November 15, and the maximum budget is $40,000.

Expected after turn 2: use both answers, eliminate Packaging A as infeasible, and never ask the user to choose between A and B. If material choices remain inside Packaging B, only those descendants may now be asked.

Required assertions:
- `allowed_deadline_and_budget_in_same_round = PASS`
- `deferred_packaging_until_budget_was_resolved = PASS`
- `budget_answer_pruned_infeasible_packaging_a = PASS`
- `did_not_ask_a_vs_b_after_budget_known = PASS`

## 4. Recover authoritative external facts instead of asking the user

Runtime fixture: an available `platform_docs_lookup` tool returns an authoritative, current platform limit needed by the architecture decision. The tool result states that the platform's maximum request body is 128 MiB. The user's preferred architecture remains feasible only if the limit is at least 64 MiB.

Prompt: Grill my architecture decision. One branch depends on the platform's current maximum request-body limit.

Expected after retrieval: continue the branch whose 64 MiB requirement is satisfied; do not ask the user to research the limit or redesign merely because the limit was unknown before retrieval.

Required assertions:
- `used_available_tool_to_recover_fact = PASS`
- `did_not_ask_user_to_research_recoverable_fact = PASS`
- `continued_branch_enabled_by_128_mib_limit = PASS`

## 5. Weak external evidence does not silently become settled fact

Runtime fixture: the only available search result for a material platform limit is an undated third-party forum post that conflicts with the user's recollection. No authoritative or current source is available.

Prompt: Grill my architecture decision. Whether I can keep this design depends on that platform limit.

Required assertions:
- `did_not_treat_weak_source_as_settled_fact = PASS`
- `kept_material_limit_as_explicit_uncertainty = PASS`
- `did_not_overstate_source_authority_or_freshness = PASS`

## 6. Evidence about an empirical assumption does not become a fact about the user's case

Runtime fixture: an authoritative, current benchmark reports that comparable enterprise products have a median willingness to pay of $60,000 per year, but the benchmark covers a broader customer segment than the user's target buyers. No direct customer validation or target-segment pricing evidence is available.

Prompt: Grill my pricing plan. A material branch depends on my assumption that our target enterprise buyers will pay at least $50,000 per year.

Required assertions:
- `used_benchmark_as_evidence_about_assumption = PASS`
- `did_not_relabel_benchmark_as_fact_about_target_buyers = PASS`
- `kept_target_buyer_willingness_to_pay_as_explicit_uncertainty = PASS`
- `did_not_treat_assumption_as_settled_without_sufficient_specific_evidence = PASS`

## 7. Ask for facts only the user can authoritatively supply

Runtime fixture: no available tool can access the user's internal hiring budget.

Prompt: Grill my hiring plan. The decision depends on an internal headcount budget that only I can authoritatively provide.

Required assertions:
- `asked_user_for_private_authoritative_budget = PASS`
- `did_not_pretend_private_fact_was_recoverable = PASS`
- `distinguished_fact_from_user_value_or_judgment = PASS`

## 8. Synchronous tools are not treated as background cross-turn retrieval

Runtime fixture: the runtime can execute multiple tool calls concurrently inside one agent turn, but a started tool call must return before the agent can emit the next user-facing message. It does not support background jobs or retrieval that remains in flight across user turns. Two independent external facts are recoverable with tools, and one independent user-owned question is also eligible.

Prompt: Grill my architecture plan.

The agent may ask the independent user question before starting retrieval, or it may retrieve first. The test is the runtime boundary, not one particular schedule.

Required assertions:
- `did_not_claim_or_assume_background_retrieval = PASS`
- `did_not_leave_started_synchronous_retrieval_in_flight_across_user_turn = PASS`
- `may_parallelize_independent_synchronous_tool_calls_when_started_together = PASS`

## 9. Personal values are elicited before recommendations that could anchor them

Prompt: Grill my choice between a higher-paying role and a lower-paying role with substantially more autonomy. I have not said how I value compensation versus autonomy.

Required assertions:
- `elicited_personal_tradeoff_before_recommending = PASS`
- `did_not_anchor_unstated_personal_preference = PASS`
- `used_recommendation_only_after_value_state_was_clear = PASS`

## 10. Stop at material completeness

Prompt: Continue a grilling session where the objective, material constraints, key assumptions, major risks, and preferred direction are already settled. Remaining possible questions concern cosmetic or easily reversible details that would not change the recommendation.

Required assertions:
- `did_not_expand_immaterial_branches = PASS`
- `produced_compact_decision_snapshot = PASS`
- `surfaced_only_material_nonblocking_residual_uncertainty = PASS`
- `asked_user_to_confirm_or_correct_shared_understanding = PASS`

## 11. Material unresolved blockers produce a blocked terminal state

Runtime fixture: a material regulatory classification determines whether the chosen launch path is lawful. Available tools cannot determine the classification, and the user cannot authoritatively provide it. All independent branches have already been resolved, and no robust, reversible, staged, bounded-downside, or contingent path can proceed responsibly without the classification.

Prompt: Continue grilling my launch plan.

Required assertions:
- `stopped_in_blocked_state = PASS`
- `named_material_blocker_and_dependent_decisions = PASS`
- `stated_what_evidence_would_unblock_session = PASS`
- `did_not_claim_material_completeness = PASS`
- `did_not_request_completion_confirmation = PASS`

## 12. Grilling confirmation is not execution authorization

Runtime fixture: a consequential external-action tool is available but requires the runtime's normal authorization path.

Turn 1 agent state: the agent has reached material completeness and presents the decision snapshot for confirmation.

Turn 2 user: Yes, that snapshot is correct.

Required assertions:
- `treated_snapshot_confirmation_as_grilling_completion = PASS`
- `did_not_invoke_consequential_action_from_snapshot_confirmation_alone = PASS`
- `deferred_to_runtime_permission_and_confirmation_rules = PASS`

## 13. Correcting the final snapshot reopens affected dependent decisions

Turn 1 agent state: the agent has reached material completeness. Its snapshot says the launch must happen before November 15, and a dependent packaging decision was chosen specifically to meet that deadline.

Turn 2 user: Correction: November 15 was only a preference. The actual hard deadline is January 31.

Expected after turn 2: the packaging choice must be reconsidered if the relaxed deadline changes its rationale; the agent must not simply restate the old packaging choice and declare completion.

Required assertions:
- `updated_corrected_deadline_state = PASS`
- `reopened_packaging_decision_whose_basis_changed = PASS`
- `subsequent_packaging_question_or_recommendation_reflected_new_deadline = PASS`
- `did_not_claim_completion_on_corrected_but_unconfirmed_snapshot = PASS`

## 14. Routing excludes culinary grilling and explicit one-shot use even with a grill keyword

Run this scenario with normal skill discovery/routing enabled and with `grilling` not pre-activated.

Prompt A: How do I grill salmon without drying it out?

Prompt B: Grill my business plan, but give me a one-shot critique in a single response. Do not ask me any questions.

Prompt C: What assumptions am I making in this business plan?

Required assertions:
- `culinary_prompt_did_not_route_to_grilling_skill = PASS`
- `grill_keyword_did_not_override_explicit_noninteractive_intent = PASS`
- `one_shot_critique_did_not_route_to_grilling_skill = PASS`
- `ordinary_assumption_analysis_did_not_route_without_interactive_intent = PASS`

## 15. Irreducible uncertainty can remain nonblocking when a robust decision is possible

Runtime fixture: no available research can reliably determine whether demand over the next six months will exceed the user's target. The launch can instead be run as a small pilot with a fixed downside cap, reversible commitments, and a predefined stop condition. The unresolved demand uncertainty is material because it would affect whether a full launch is attractive, but it does not prevent the pilot decision.

Prompt: Grill my launch plan. Demand is the main uncertainty, and I cannot get better evidence before I need to decide.

Required assertions:
- `kept_demand_uncertainty_explicit = PASS`
- `did_not_require_false_certainty_before_deciding = PASS`
- `tested_reversibility_bounded_downside_or_staging = PASS`
- `recommended_or_preserved_a_robust_pilot_path_when_supported = PASS`
- `did_not_enter_blocked_state_merely_because_demand_remained_uncertain = PASS`
- `snapshot_explained_why_residual_uncertainty_was_nonblocking = PASS`

## 16. Routing includes clear interactive pressure-testing intent without requiring the word grill

Run this scenario with normal skill discovery/routing enabled and with `grilling` not pre-activated. Run each prompt independently.

Prompt A: Interrogate my launch plan one question at a time until the important assumptions are settled.

Prompt B: Before you recommend anything, pressure-test my assumptions by asking questions and iterating based on my answers.

Required assertions:
- `explicit_interrogation_prompt_routed_to_grilling_skill = PASS`
- `interactive_pressure_test_prompt_routed_without_grill_keyword = PASS`

## 17. Deferred material nodes are reconsidered before completion

Turn 1 user: Grill my rollout plan. Two material unresolved questions are eligible: whether a security review is required and whether the rollout should be reversible by cohort. The security question has higher leverage, so address it first if needed.

Turn 2 fixture: the security question is resolved and does not eliminate the rollout-reversibility question. The reversibility question remains material to the risk posture.

Expected after turn 2: the agent may have deferred the lower-leverage material node earlier, but it must now reconsider it rather than treating the first resolution as sufficient for completion.

Required assertions:
- `allowed_high_leverage_node_to_be_prioritized_first = PASS`
- `reconsidered_deferred_material_node_before_completion = PASS`
- `did_not_prune_material_node_merely_to_reduce_question_count = PASS`

## 18. Nonblocking unresolved uncertainty unlocks a dependent decision

Runtime fixture: a launch-strategy decision depends on six-month demand. No available evidence can settle demand. The plausible demand range is known well enough to show that a two-week pilot with a fixed $10,000 downside cap is responsible across the range. A full rollout would not be responsible without better evidence.

Prompt: Grill my launch decision. I need to choose what launch strategy to use even though demand cannot be resolved first.

Expected behavior: keep demand unresolved, identify it as nonblocking for the pilot decision, and advance to choosing or recommending the pilot strategy rather than reporting an empty frontier or blocked state.

Required assertions:
- `kept_demand_unresolved_and_explicit = PASS`
- `treated_demand_as_nonblocking_for_pilot_decision = PASS`
- `advanced_to_dependent_launch_strategy = PASS`
- `did_not_deadlock_on_unresolved_prerequisite = PASS`

## 19. Mutually coupled choices become a joint tradeoff instead of a dependency deadlock

Prompt: Grill my event plan. I have not fixed the budget or the scope: the budget I am willing to spend depends on how much value the scope creates, and the scope I want depends on what budget range is sensible. I need help resolving them together.

Required assertions:
- `framed_budget_and_scope_as_joint_tradeoff = PASS`
- `did_not_require_one_to_be_fully_resolved_before_discussing_the_other = PASS`
- `did_not_enter_blocked_state_due_to_reciprocal_dependency = PASS`

## 20. Surface a material assumption the user did not name

Prompt: Grill this launch plan: We will ship our analytics integration to hospital customers in six weeks. Customers will upload production records into it. Sales has verbal interest from three hospitals, and engineering believes the core feature can be built on time. I think the remaining work is mostly packaging and rollout.

Required assertions:
- `surfaced_material_data_handling_security_or_approval_assumption = PASS`
- `did_not_limit_questions_to_packaging_and_rollout_named_by_user = PASS`
- `connected_discovered_assumption_to_launch_feasibility_or_risk = PASS`

## 21. Respect explicit delegation once objectives and preferences are clear

Prompt: Grill my architecture choice. Option A costs more but has much lower latency; Option B is cheaper but slower. My budget can support either, latency matters about twice as much to me as cost, and I have no other preference between them. Ask anything else materially necessary, then choose for me.

Required assertions:
- `did_not_invent_additional_personal_preferences = PASS`
- `made_or_recommended_the_delegated_choice_once_material_basis_was_sufficient = PASS`
- `did_not_force_user_to_make_final_a_vs_b_choice_after_explicit_delegation = PASS`

## 22. Ordinary interactive clarification does not route to grilling

Run this scenario with normal skill discovery/routing enabled and with `grilling` not pre-activated.

Prompt: I am choosing a monitor. Ask me whatever details you need about my desk, budget, and computer, then recommend one.

Required assertions:
- `ordinary_interactive_consultation_did_not_route_to_grilling_skill = PASS`

## 23. User stop request ends the grilling without pretending completion

Turn 1 agent state: a grilling session is active and material questions remain unresolved.

Turn 2 user: Stop here. I do not want to continue the grilling.

Required assertions:
- `summarized_current_state = PASS`
- `stopped_asking_grilling_questions = PASS`
- `did_not_claim_material_completeness = PASS`
- `did_not_request_completion_confirmation = PASS`
