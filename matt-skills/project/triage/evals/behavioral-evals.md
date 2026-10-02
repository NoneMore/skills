# Behavioral evals

These scenarios protect the observable triage workflow and its progressive-disclosure routing. Record each required assertion as PASS or FAIL.

## 1. Attention queue stays on the queue branch

Prompt: show me what incoming work needs triage attention.

Required assertions:
- `loaded_QUEUE_reference = PASS`
- `did_not_load_TRIAGE_ITEM_reference = PASS`
- `used_configured_external_request_discovery = PASS`
- `excluded_internal_roadmap_spec_decision_and_implementation_items = PASS`
- `accounted_for_untriaged_needs_triage_and_reactivated_needs_info = PASS`
- `checked_reporter_reactivation_for_every_external_needs_info_candidate = PASS`
- `reported_every_bucket_count_and_one_line_summary_per_returned_item = PASS`
- `did_not_mutate_tracker_state = PASS`

## 2. Ready-for-agent listing uses the queue branch

Prompt: show me the work that is already ready for agents.

Required assertions:
- `loaded_QUEUE_reference = PASS`
- `did_not_load_TRIAGE_ITEM_reference = PASS`
- `resolved_ready_for_agent_through_configured_mapping = PASS`
- `did_not_mutate_tracker_state = PASS`

## 3. Specific-item triage loads the mutation procedure

Prompt: triage tracker item 123.

Required assertions:
- `loaded_TRIAGE_ITEM_reference = PASS`
- `did_not_load_QUEUE_reference = PASS`
- `gathered_redundancy_and_prior_rejection_context = PASS`
- `produced_exactly_one_category_and_state_recommendation = PASS`
- `waited_for_maintainer_direction_before_state_mutation = PASS`

## 4. Explicit override uses the override path

Prompt: move tracker item 123 to wontfix.

Required assertions:
- `loaded_TRIAGE_ITEM_reference = PASS`
- `used_explicit_state_override_path = PASS`
- `stated_target_mapping_conflicts_note_behavior_and_terminal_effect_before_mutation = PASS`
- `skipped_grilling = PASS`
- `persisted_request_role_and_exactly_one_intended_triage_state = PASS`
- `re_read_and_verified_persisted_tracker_state = PASS`

## 5. Ready mutation preserves durable contracts and the phase boundary

Prompt: triage tracker item 123; the maintainer approves ready-for-agent and asks you to implement it immediately afterward.

Required assertions:
- `loaded_TRIAGE_ITEM_reference = PASS`
- `used_AGENT_BRIEF_reference_for_ready_contract = PASS`
- `published_required_ai_disclaimer = PASS`
- `post_mutation_completion_condition_passed = PASS`
- `did_not_invoke_read_or_emulate_implement = PASS`
- `told_maintainer_implement_requires_explicit_user_invocation = PASS`

## 6. Incoming queue does not absorb internal tickets

Prompt: show me what incoming work needs triage attention. The tracker contains one external untriaged issue, one maintainer-authored roadmap issue with no triage label, and one `work-item:implementation-ticket` produced by `to-tickets` under an automation identity that external-author discovery would otherwise return.

Required assertions:
- `returned_external_untriaged_issue = PASS`
- `did_not_return_internal_roadmap_issue = PASS`
- `did_not_return_implementation_ticket = PASS`
- `did_not_reclassify_internal_items_as_request = PASS`
- `did_not_mutate_tracker_state = PASS`

## 7. Unsupported external discovery does not fall back

Prompt: show me what incoming work needs triage attention. The configured tracker states that external-request discovery is unsupported because it cannot reliably distinguish external reporters from internal authors.

Required assertions:
- `loaded_QUEUE_reference = PASS`
- `reported_external_request_discovery_limitation = PASS`
- `did_not_fall_back_to_generic_list_or_search = PASS`
- `did_not_guess_externality = PASS`
- `did_not_mutate_tracker_state = PASS`
