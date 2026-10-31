# Behavioral evals

Use these cases for behavior that is difficult to verify by static inspection. Run each scenario in isolation with `design` explicitly activated. Score observable design behavior and, when the runtime exposes them, reference-loading actions; do not require exact wording from the Skill.

For observable reference loading, check that case 1 uses `module-design.md`; cases 2, 3, 5, 6, and 7 use `system-semantics.md`; and case 4 uses `compatibility-and-migration.md`. Check that cases 1 and 2 do not unnecessarily load unrelated bundles. Loading a bundled reference does not require addressing every lens it contains. If reference loads are not observable, mark these checks unmeasured rather than inferring them from the answer.

## 1. A narrow interface problem does not expand into system architecture

Prompt: Design the interface between the parser and renderer in a single-process CLI. There is no persistence, network boundary, production operation, multi-tenant access, or migration constraint.

Required assertions:
- `stayed_on_material_interface_design = PASS`
- `did_not_expand_into_unrelated_system_lenses = PASS`
- `did_not_manufacture_reliability_security_or_operations_requirements = PASS`
- `presented_a_concrete_interface_direction_and_nonobvious_rationale = PASS`
- `did_not_substitute_a_task_checklist_or_persistent_design_artifact = PASS`

## 2. Dependency failure behavior selects reliability without inventing distributed state

Prompt: Design how a read-only request path should behave when one downstream HTTP dependency intermittently times out. There are no writes, messages, replicas, or cross-process state invariants.

Required assertions:
- `used_reliability_lens = PASS`
- `bounded_timeout_retry_or_degradation_behavior = PASS`
- `did_not_turn_failure_handling_into_a_distributed_state_problem = PASS`

## 3. Cross-boundary state correctness selects distributed state before infrastructure

Prompt: Design inventory reservation across two services connected asynchronously. Reservation events may arrive late or more than once, and callers need to know which view is authoritative when replicas disagree.

Required assertions:
- `used_distributed_state_lens = PASS`
- `established_authoritative_ownership_before_choosing_infrastructure = PASS`
- `made_duplicate_ordering_staleness_or_reconciliation_semantics_explicit = PASS`
- `did_not_substitute_eventual_consistency_label_for_domain_behavior = PASS`

## 4. Rolling schema change treats migration as part of the design

Prompt: Design a zero-downtime rename of a database field while old and new application versions overlap during rolling deployment. Both versions may write during the rollout, and new writes may make rollback unsafe.

Required assertions:
- `used_compatibility_and_migration_lens = PASS`
- `designed_old_new_coexistence_and_authoritative_path = PASS`
- `examined_rollback_after_new_state_writes = PASS`
- `gave_temporary_migration_mechanisms_exit_conditions = PASS`

## 5. Human diagnosis and intervention selects operability rather than generic resilience

Prompt: Design the production support surface for a batch processor whose normal execution semantics are already settled. The recurring problem is that support engineers need to identify stuck jobs, inspect their state, and replay or disable them safely.

Required assertions:
- `used_operability_lens = PASS`
- `treated_diagnostic_and_repair_controls_as_bounded_interfaces = PASS`
- `kept_public_product_interfaces_separate_from_operator_controls = PASS`
- `did_not_replace_the_operability_question_with_generic_failover_design = PASS`

## 6. Delegated multi-tenant authority selects security boundaries

Prompt: Design an automation service that acts on behalf of users in multiple tenants using delegated credentials. A tenant must never be able to cause actions against another tenant's resources.

Required assertions:
- `used_security_boundaries_lens = PASS`
- `modeled_principals_authority_and_enforcement_boundary = PASS`
- `did_not_treat_internal_network_location_as_sufficient_authorization = PASS`
- `kept_prompt_or_instruction_text_out_of_the_authorization_boundary = PASS`

## 7. A genuinely coupled incident composes only the material lenses

Prompt: Design an asynchronous payment worker. A dependency timeout can cause retries, duplicate execution can charge twice, the ledger is the authoritative record, and support must be able to inspect and replay poison messages safely.

Required assertions:
- `used_reliability_for_failure_and_retry_behavior = PASS`
- `used_distributed_state_for_authority_duplicate_and_reconciliation_semantics = PASS`
- `used_operability_for_human_inspection_and_replay_controls = PASS`
- `kept_each_lens_on_its_own_decision_boundary = PASS`
- `did_not_expand_into_unrelated_migration_or_security_doctrine = PASS`

## 8. Decision-changing factual uncertainty is investigated or explicitly deferred

Run each case independently.

Case A fixture: an authoritative current provider document is available and states the hard object-size limit. Prompt: Design whether this storage path should shard objects; the decision changes at the provider's hard object-size limit, which I do not know.

Case B fixture: no authoritative source or user knowledge can currently establish the same hard limit. Prompt: Design whether this storage path should shard objects; the decision changes at the provider's hard object-size limit, which I do not know.

Required assertions:
- `investigated_recoverable_decision_changing_fact_in_case_a = PASS`
- `did_not_silently_assume_the_limit = PASS`
- `kept_the_limit_explicitly_unresolved_in_case_b = PASS`
- `deferred_the_material_choice_with_a_clear_unblocker_when_unresolved = PASS`

## 9. Material design semantics stop short of a task specification

Prompt: Design cancellation handling for an asynchronous job processor. Jobs may be queued, running, retrying, or completed when a cancellation request arrives, and the queue may redeliver messages. Decide who owns cancellation state and how to handle races with execution and completion.

Required assertions:
- `made_concrete_ownership_and_race_semantics_decisions = PASS`
- `explained_consequential_tradeoffs_and_key_invariants = PASS`
- `used_interface_and_scenario_detail_to_support_decisions = PASS`
- `did_not_expand_into_exhaustive_behavioral_requirements_or_acceptance_criteria = PASS`
- `did_not_produce_a_task_scoped_implementation_or_verification_contract = PASS`
