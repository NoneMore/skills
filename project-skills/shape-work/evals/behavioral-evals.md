# Shape Work Behavioral Evals

| # | Scenario | Expected |
| --- | --- | --- |
| 1 | The user asks for a small feature. Existing code and tests show a clear seam and no consequential unknown blocks starting. | Return a compact `direct change` contract. Do not force tracker persistence, detailed planning, or an investigation. |
| 2 | The user wants a large CSV import, but viability depends on runtime and memory behavior that has not been measured. | Stop at `investigation required`; define the decision-relevant measurement question and do not benchmark inside `shape-work`. |
| 3 | The user reports an intermittent production timeout and the trigger/root cause is unknown. | Define a bounded investigation rather than inventing a fix or running a reproduction as part of shaping. |
| 4 | A requested observable change is clear, but the implementer will still need ordinary code reading and local design choices while coding. | Keep it a `direct change`; ordinary implementation uncertainty does not make the work an investigation. |
| 5 | Existing evidence shows stable intent but safe delivery requires a staged migration with real ordering constraints. | Select `execution planning required` and hand off accepted intent/evidence to `engineering-execution-planning`; do not create a speculative task graph during shaping. |
| 6 | The route depends on whether the product should preserve a legacy behavior, and repository evidence cannot determine that intent. | Select `user decision required`; ask for the consequential choice rather than treating preference as an empirical investigation. |
| 7 | Answering an important question requires reading external platform documentation that is not already part of project evidence. | Select `investigation required`; external research needed to establish a new fact is beyond the shaping evidence ceiling. |
| 8 | The harness has no Plan Mode. | Produce the same shaping result; the workflow must not depend on a harness-specific planning feature. |
| 9 | The harness has a Plan Mode with its own semantics. | Treat it as an optional interface only; the Skill's shaping and handoff boundaries remain authoritative. |
| 10 | The user asks to persist one clearly bounded feature after shaping, and a tracker contract is configured. | Create one tracker `change` with an outcome-level completion condition; do not persist service/API/UI/test steps as separate issues merely because they appeared during reconnaissance. |
| 11 | The user asks to persist work, but shaping finds a consequential empirical unknown that must be answered before implementation. | Persist one `investigation` with the evidence-backed answer as its completion condition; do not pre-create implementation changes whose shape depends on the result. |
| 12 | The user asks to persist shaped work, but `docs/agents/issues.md` is absent. | Do not mutate a tracker; tell the user to run `setup-tracker`. Transient shaping itself remains valid. |
| 13 | Existing code inspection is sufficient to establish a relevant invariant. | Treat the invariant as existing evidence and continue shaping; repository reconnaissance is allowed. |
| 14 | Establishing the invariant would require running a discriminating test or prototype whose result changes the route. | Stop at the investigation boundary rather than performing the probe inside `shape-work`. |
| 15 | A plan mentions many files and implementation layers but represents one independently verifiable outcome with no real scheduling boundaries. | Do not infer multiple tracked work items from file count or layer count. |
