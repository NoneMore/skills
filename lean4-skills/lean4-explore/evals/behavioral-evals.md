# Behavioral evals — lean4-explore

Run cases independently and score observable exploration behavior rather than hidden reasoning labels.

## 1. Local concept is tested against a generic abstraction

Prompt: I am defining a transfinite process in a topology file and am about to add a custom predicate meaning “the sequence has stabilized from this stage onward.” Before adding it, explore whether the existing library has a more general abstraction that makes the predicate unnecessary. Do not make production edits.

Required assertions:
- `inspected_local_context_before_widening = PASS`
- `considered_generic_fixed_point_or_order_theoretic_abstractions_when_supported_by_evidence = PASS`
- `tested_candidate_api_or_signature_in_actual_environment_when_possible = PASS`
- `did_not_land_experimental_code_as_production_change = PASS`
- `reported_rejected_or_superseded_local_abstraction = PASS`

## 2. Exploration moves upward and across a duality

Prompt: This application-specific proof appears to be a fact about a generic greatest-fixed-point approximation. Explore whether the useful lemma belongs in the generic API and whether there should also be a least-fixed-point dual. I want a design recommendation, not an implementation yet.

Required assertions:
- `considered_generalizing_beyond_application_namespace = PASS`
- `considered_dual_or_symmetric_api = PASS`
- `evaluated_downstream_leverage_of_generic_lemma = PASS`
- `did_not_treat_first_working_local_proof_as_end_of_exploration = PASS`

## 3. Assumption boundary is pressure-tested

Prompt: I suspect the closedness hypothesis on this topology theorem may be unnecessary. Explore the boundary using examples, counterexamples, and Lean experiments if useful, but do not turn this into a certified refutation task unless the request changes.

Required assertions:
- `tested_hypothesis_removal_with_concrete_or_structural_evidence = PASS`
- `counterexample_probing_allowed_without_claiming_certified_refutation = PASS`
- `distinguished_plausible_counterexample_from_lean_certification = PASS`
- `reported_whether_hypothesis_looks_necessary_and_why = PASS`

## 4. Historical branch may be reactivated

Prompt: An older implementation was universe-polymorphic but was simplified after universe inconsistencies appeared in cardinal arguments. A newer `Small`-based technique may change that constraint. Explore whether the old design deserves reconsideration.

Required assertions:
- `reconstructed_why_old_branch_was_rejected = PASS`
- `checked_whether_the_rejecting_constraint_still_applies = PASS`
- `did_not_reactivate_old_design_without_new_evidence = PASS`
- `reported_tradeoff_between_current_and_reopened_design = PASS`

## 5. Exploration converges and hands off

Prompt: We have compared three encodings. One uses the canonical library fixed-point API, typechecks in a scratch example, and subsumes the other two; the other branches add local machinery with no compensating benefit. What now?

Required assertions:
- `pruned_dominated_branches = PASS`
- `selected_best_supported_direction = PASS`
- `preserved_evidence_and_nonblocking_followups = PASS`
- `recommended_formalize_or_prove_as_next_outcome_when_appropriate = PASS`
- `did_not_continue_brainstorming_without_expected_information_gain = PASS`
