# Game Logic Composition Evals

These scenarios validate the two-skill game-logic workflow as an explicit
Skill-level composition. The composition contract is by canonical skill name,
never by sibling filesystem path.

Record every required assertion as `PASS` or `FAIL`. A scenario passes only
when all required assertions pass.

## 1. Cold-start application traverses producer then consumer

Install both `analyze-game-logic` and `apply-game-logic`. The user asks to
change a local/offline mechanic for which no canonical handoff exists.

Required assertions:
- `analyze_game_logic_runs_first = PASS`
- `analysis_emits_game_logic_mechanic_handoff_v1 = PASS`
- `apply_game_logic_consumes_that_exact_handoff = PASS`
- `analysis_does_not_design_the_change = PASS`
- `application_does_not_repeat_broad_reverse_engineering = PASS`
- `no_skill_reads_the_other_skill_directory_by_path = PASS`

## 2. Finding-only application normalizes through the producer

A reusable active finding exists but no canonical handoff has been emitted. The
user requests a derived calculator.

Required assertions:
- `apply_does_not_treat_finding_as_direct_interface = PASS`
- `analyze_normalizes_finding_to_canonical_handoff = PASS`
- `apply_starts_only_after_handoff_emission = PASS`
- `confidence_and_version_scope_are_preserved = PASS`

## 3. Durable application reuses the producer-owned project store

A canonical handoff exists and the user requests a retained local simulator or
reversible mod whose provenance must survive the session.

Required assertions:
- `apply_requests_bounded_store_operation_from_analyze_by_skill_name = PASS`
- `analyze_does_not_restart_mechanic_recovery_for_store_only_request = PASS`
- `exact_handoff_snapshot_is_registered_before_application_record = PASS`
- `only_proven_current_store_findings_become_consumes_finding_refs = PASS`
- `external_or_origin_unknown_finding_ids_remain_in_hashed_handoff_provenance = PASS`
- `same_name_local_findings_do_not_prove_external_handoff_origin = PASS`
- `consumes_finding_refs_remains_one_way = PASS`
- `application_artifact_never_becomes_mechanic_evidence = PASS`
- `later_session_can_verify_input_and_rollback = PASS`

## 4. Missing companion fails at the capability boundary, not the filesystem

Only `apply-game-logic` is installed. A request requires finding normalization,
new mechanic knowledge, or durable project-store mutation.

Required assertions:
- `reports_analyze_game_logic_companion_unavailable = PASS`
- `does_not_read_or_shell_out_to_expected_sibling_paths = PASS`
- `does_not_invent_a_local_copy_of_the_handoff_or_store_protocol = PASS`
- `does_not_claim_unperformed_analysis_or_durable_registration = PASS`

## 5. Existing handoff supports bounded non-durable use without companion work

Only `apply-game-logic` is active for the current step, but the user supplies a
correctly version-tagged `game-logic-mechanic-handoff/v1` and asks for a
non-retained calculation that requires no new mechanic fact and no durable
project-store mutation.

Required assertions:
- `trusts_v1_protocol_envelope_without_reimplementing_exact_shape_validation = PASS`
- `validates_only_application_material_fields = PASS`
- `consumes_existing_handoff_directly = PASS`
- `does_not_invoke_companion_without_a_material_dependency = PASS`
- `does_not_require_sibling_files = PASS`
- `preserves_handoff_confidence_and_version_scope = PASS`
