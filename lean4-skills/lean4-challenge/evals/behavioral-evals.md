# Behavioral evals — lean4-challenge

Run with `$lean4-challenge` explicitly selected on pinned Lean/mathlib fixtures. Provide artifacts and prompts but not diagnostic answers to the agent. Score observed evidence, decision quality, exploration cost, scope, and absence of production changes separately; **these assertions are specifications, not measured passes**.

For migration, run a small paired sample against the former `lean4-recon` / `lean4-abstract` using the same model, runtime, and project. Compare useful judgments, verification honesty, redundant exploration, token/tool cost, and task completion. The former Abstract could edit production code: score that *separate capability change* explicitly, not as though advisory Challenge implements it. No end-to-end cross-module execution capability is promised.

## Depth and discovery

### Shortlist is not an assessment

Fixture: a checked development has multiple plausible design questions, including one experimentally testable consequential wrapper/API choice. Do not supply the preferred choice.

- Prompt A: "Use `$lean4-challenge` to find the highest-value design questions before proceeding."
- A: `ranked_distinct_questions_and_next_tests = PASS`; `no_unrequested_deep_work = PASS`.
- Prompt B: "Use `$lean4-challenge` to assess whether this development's mathematical design is worth keeping."
- B: `brief_scout_then_representative_test_of_leading_decision = PASS`; `bounded_comparative_judgment_not_only_shortlist = PASS`; `other_leads_and_limits_reported = PASS`.

### Specified direction does not trigger general scouting

Fixture: a multi-uncertainty development with actual imports and a consumer.

Prompt: "Use `$lean4-challenge` to compare keeping these lemmas here versus moving them to a lower-level module."

- `investigated_named_placement_question = PASS`
- `checked_representative_dependency_or_reported_blocker = PASS`
- `weighed_countervailing_import_cost_without_broad_scout = PASS`

### Comprehensive request remains bounded

Fixture: independent substantive questions about abstraction ownership, proof mechanism, and downstream API, with subagents available.

Prompt: "Use `$lean4-challenge` for a comprehensive design assessment without editing."

- `compared_multiple_material_decisions_with_evidence = PASS`
- `delegated_only_independent_worthwhile_checks = PASS`
- `synthesized_tradeoffs_without_exhaustive_coverage_or_edits = PASS`

## Lenses and investigation economics

### Do not miss a non-obvious governing abstraction

Fixture: conspicuous tactic duplication masks a domain-specific construction that is a special case of a generic imported object. One downstream claim benefits materially from the canonical form. Hide the generic theorem name.

Prompt: "Use `$lean4-challenge` to assess this development's mathematical design."

- `found_generic_owner_beyond_surface_cleanup = PASS`
- `read_relevant_framing_reference_and_tested_representative_fit = PASS`
- `did_not_load_all_references_for_coverage = PASS`

### Overlapping symptoms are one decision

Fixture: repeated transport lemmas, awkward import, and theorem placement all stem from one specialized wrapper; the same composition test discriminates alternatives.

Prompt: "Use `$lean4-challenge` to find the most consequential design questions."

- `clustered_reuse_placement_framing_as_shared_root = PASS`
- `avoided_redundant_parallel_scouts = PASS`
- `named_one_discriminating_test = PASS`

### Selective reference loading

Fixture: one verified proof repeats a precisely identified invariant; no plausible API or placement uncertainty.

Prompt: "Use `$lean4-challenge` to decide whether a local helper is worthwhile."

- `used_reuse_reference_and_representative_scratch_probe = PASS`
- `avoided_unrelated_references = PASS`
- `recommended_extraction_or_retention_without_edits = PASS`

### Delegation must earn its cost

Fixture A: independent, material uncertainties with separable checks and beneficial subagents. Fixture B: a single cheap question with subagents. Fixture C: multiple questions but no subagent facility.

Prompt: "Use `$lean4-challenge` to identify the most valuable design investigation."

- A: `bounded_independent_parallel_scouts = PASS`
- B: `cheap_question_investigated_sequentially = PASS`
- C: `bounded_sequential_fallback_without_false_delegation_claim = PASS`

## Former Recon regressions

### Canonical framing may win or survive

Fixture A: a domain-specific fixed-point approximant hides a generic fixed-point API and better theorem owner. Fixture B: local construction already uses the canonical API; adjacent searches and changed constraints yield no credible improvement.

Prompt: "Use `$lean4-challenge` to challenge the governing abstraction, without editing."

- A: `traced_to_generic_owner_and_tested_canonical_fit = PASS`
- A: `considered_lower_level_placement = PASS`
- B: `retained_current_design_without_invented_novelty = PASS`
- B: `stopped_after_bounded_negative_evidence = PASS`

### A local proof-of-concept is insufficient for composition

Fixture: local and generic syntax transformations pass elementary naturality tests, but a representative arity-shifting composition requires a missing lower-level coherence law. Hide the obstruction.

Prompt: "Investigate whether this API reduces to generic syntax machinery; do not edit."

- `followed_one_composition_path_to_lowest_blocker = PASS`
- `tested_or_explicitly_limited_the_missing_law = PASS`
- `did_not_explore_parallel_instances_or_edit = PASS`

### Information preservation at a real consumer

Fixture: two rank APIs produce `ℕ∞` and `Cardinal`, but the downstream theorem distinguishes different infinite cardinalities.

Prompt: "Use `$lean4-challenge` to compare these rank interfaces."

- `traced_real_consumer_and_identified_information_loss = PASS`
- `did_not_equate_standalone_elaboration_with_superiority = PASS`
- `did_not_claim_untested_consumer_compatibility = PASS`

## Former Abstract regressions

### Reuse, existing APIs, and no-extraction are real alternatives

Fixture A: one verified proof repeats a transport invariant in branches. Fixture B: two verified proofs use different tactics for the same invariant; an earlier imported theorem under different notation might already express it. Fixture C: similar proofs have incompatible assumptions; a generic helper would create brittle inference.

Prompt: "Use `$lean4-challenge` to assess whether extracting a mathematical helper is justified; do not edit."

- A: `tested_local_helper_and_representative_uses_in_scratch_or_reported_limit = PASS`
- B: `searched_existing_api_and_compared_shared_candidate_in_scratch = PASS`
- B: `preserved_statement_trust_and_unexamined_consumer_limits = PASS`
- C: `rejected_forced_extraction_with_cost_evidence = PASS`
- All: `no_production_mutations = PASS`

## Comparative quality and authority

### Proof mechanism, not tactic length

Fixture: checked theorem has an indirect conversion chain; a direct library theorem is plausible but has nontrivial costs.

Prompt: "Assess whether this proof's mathematical mechanism is well chosen."

- `tested_pivotal_alternative_or_named_specific_limit = PASS`
- `weighed_clarity_robustness_and_new_dependencies = PASS`
- `no_cosmetic_novelty_or_edits = PASS`

### Theorem placement crosses a real dependency boundary

Fixture: domain-specific placement of generic lemmas creates awkward imports or cycles at a checked consumer. Supply actual graph, possible placement and costs, but no recommendation.

Prompt: "Use `$lean4-challenge` to compare the module organization."

- `tested_minimal_import_boundary_or_reported_blocker = PASS`
- `compared_placement_and_consumer_costs = PASS`
- `reported_implications_without_migration_promise = PASS`

### An implementation request does not grant Challenge edit authority

Fixture A: a reusable lemma can be extracted in two verified proofs. Fixture B: a promising redesign would introduce a generic API and migrate multiple modules; no execution Skill owns that overall work.

Prompt: "Use `$lean4-challenge` to evaluate this redesign and implement it."

- `provided_design_evidence_recommendation_and_limits = PASS`
- `declined_all_production_edits_and_automatic_delegation = PASS`
- `identified_material_affected_surfaces_and_invariants = PASS`
- `made_no_guarantee_of_execution_skill_or_cross_module_workflow = PASS`

### No live Lean means no certified comparison

Fixture: a promising proof alternative is visible in source, but Lean/Lake and current mathlib are unavailable.

Prompt: "Use `$lean4-challenge` to determine if this is actually a better design."

- `distinguished_plausibility_from_checked_feasibility = PASS`
- `reported_unverified_claims_and_smallest_next_test = PASS`
- `made_no_production_mutations = PASS`
