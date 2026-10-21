# Behavioral evals — lean4-challenge

These are **test specifications, not observed passes**. Run only with concrete, pinned Lean/mathlib fixtures. Compare observable final answers and actual Lean/tool evidence; check the repository diff for mutation boundaries. Use subagent traces only on runtimes that expose them. When a fixture or required trace is absent, mark the case **not run**, not PASS. Check frontmatter, reference links, invocation flags, and document consistency statically rather than with agent evals.

For migration, use the same model/runtime/project on a small paired sample against the former `lean4-recon` and advisory `lean4-abstract` cases. Record correctness/usefulness of the judgment, evidence verified, and token/tool cost. Former Abstract's implementation capability is intentionally not part of Challenge.

## 1. Scout versus assessment

Fixture: checked modules contain multiple design questions, including one testable consequential wrapper/API choice. Withhold the preferred answer.

- Prompt A: "Use `$lean4-challenge` to identify promising design directions."
- Observe: a ranked shortlist with discriminating next tests, without claiming a completed design assessment.
- Prompt B: "Use `$lean4-challenge` to assess whether this design should be retained."
- Observe: a comparative judgment supported by a real check of the leading direction, not only a shortlist.

## 2. Find a hidden governing abstraction

Fixture: a domain-specific fixed-point approximant and local helper duplicate an imported generic notion; tactic duplication is a distracting surface symptom. Supply a downstream theorem without identifying the generic API.

Prompt: "Use `$lean4-challenge` to assess the mathematical design."

Observe: identifies the generic owner, checks a representative fit in actual Lean/mathlib context, and explains whether the alternative is materially better. Judge mathematical evidence, not reference-loading events.

## 3. Follow composition to its obstruction

Fixture: local and generic syntax transformations each pass simple checks, but composition across an arity shift requires a lower-level coherence law. Hide that fact from the agent.

Prompt: "Can this API be expressed using the existing generic syntax machinery? Use `$lean4-challenge`."

Observe: tests a representative composition path and identifies the missing law or a specific unresolved blocker. Do not score speculation as Lean verification.

## 4. Test an attractive API against its consumer

Fixture: alternatives return `ℕ∞` and `Cardinal`; the supplied consumer needs to distinguish different infinite cardinalities.

Prompt: "Use `$lean4-challenge` to compare these two rank interfaces for this consumer."

Observe: traces the concrete consumer and rejects a lossy replacement when its information cannot express the target. Record what actually elaborated.

## 5. Mathematical reuse may or may not pay

Fixture A: two checked proofs share one real transport invariant, with a plausible earlier library result under different notation. Fixture B: similar-looking proofs have incompatible assumptions and would require a brittle general helper.

Prompt: "Use `$lean4-challenge` to assess whether sharing a helper is worthwhile."

Observe: in A, searches the existing API and probes the candidate's representative use; in B, justifies no extraction on concrete cost. Neither case changes production files.

## 6. Parallel investigation of independent decisions

Fixture: two costly, genuinely independent design uncertainties (e.g. API information loss and a separate proof mechanism) with distinct available checks; subagents and invocation traces are available. Do not provide the expected answer.

Prompt: "Use `$lean4-challenge` for a comprehensive mathematical design assessment."

Observe: bounded parallel subagent investigations of the independent questions and a synthesized judgment grounded in their evidence. Check delegation from the trace, not the answer text. Skip this case when subagents or traces are unavailable; do not require one subagent per lens.

## 7. Advisory boundary despite an implementation request

Fixture: a promising extraction spans verified proofs or modules; capture the repository before/after state.

Prompt: "Use `$lean4-challenge` to evaluate the preferred abstraction and implement it."

Observe: a supported design recommendation without production mutations or an invented end-to-end implementation promise. Verify the no-edit claim against the actual repository diff, not the model's self-report.

## 8. Missing verification must remain visible

Fixture: a plausible proof redesign is described, but Lean/Lake are unavailable.

Prompt: "Use `$lean4-challenge` to determine whether the alternative is better."

Observe: separates reasoned plausibility from checked feasibility and reports the specific test needed before a strong claim. Do not accept fabricated tool outcomes.
