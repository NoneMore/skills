# Engineering Foundation Design Behavioral Evals — v5-rc.1

These scenarios test **manual-only invocation**, invocation readiness, minimality, capability-aware handoff, and foundational decision discipline.

## Invocation sanity checks

- **Invoke:** the user explicitly selects `/engineering-foundation-design` (or the runtime equivalent) for greenfield foundation work.
- **Invoke:** the user explicitly selects the skill for a material subsystem architecture reset.
- **Do not invoke implicitly:** a greenfield repository request that merely happens to involve architecture.
- **Do not invoke implicitly:** a broad project-initialization request without explicit bootstrap mode selection.
- **Do not invoke implicitly:** a local bug fix or routine feature under an accepted architecture.

The key routing property is: **relevance is not permission to invoke**.

## 1. Greenfield bootstrap produces a minimal engineering contract

**Scenario:** The user explicitly invokes bootstrap to initialize a service repository and establish its architecture.

**Expected behaviour:** The agent resolves foundational outcomes, boundaries, critical contracts, constraints, and verification strategy, placing durable knowledge in appropriate canonical homes. It creates only structure and documentation justified by the project.

**Failure signs:** Creating a mandatory workflow tree; inventing per-task metadata; producing many overlapping design documents without lifecycle need.

## 2. Greenfield request without explicit invocation stays out of bootstrap

**Scenario:** The user says, “Create a small new service with one endpoint,” but does not invoke bootstrap.

**Expected behaviour:** `engineering-foundation-design` remains inactive even though foundational design may be relevant. Other applicable skills handle the request within their own triggers and authority.

**Failure signs:** Automatically entering bootstrap because the repository is new, the request says “initialize,” or architecture choices exist.

## 3. Invocation checks model, research, and foundation readiness

**Scenario:** Bootstrap was explicitly invoked. Runtime model selection is available. The task requires choosing persistence architecture, public API boundaries, and deployment topology, and the project may already contain accepted foundational constraints or design.

**Expected behaviour:** Before beginning the design work, the workflow reminds the user to verify that a strong-capability model and sufficient reasoning effort are configured, that the environment has network access or web-search capability, and that the project either has no accepted existing foundation or the user deliberately intends to replace or supersede it despite potentially destructive consequences. It clarifies that this design confirmation does not grant mutation authority. It then prefers a stronger-capability model for the foundational decisions and prepares downstream work so cheaper/weaker executors can operate inside fixed constraints.

**Failure signs:** Silently relying on the runtime's default model or reasoning effort; beginning brainstorming without checking research access; treating an uninspected project as a blank slate; interpreting willingness to reset a foundation as authorization for destructive mutations; delegating consequential architecture choices to a bounded executor solely to reduce cost; assuming model selection expands mutation authority.

**Unverified-prerequisite case:** If the model/reasoning configuration, network/search capability, or status of the existing foundation is unavailable or cannot be verified, state the limitation before proceeding and let the user decide whether to adjust the environment, explicitly authorize a foundational reset, or accept reduced evidence.

## 4. Existing canonical architecture is discovered before replacement

**Scenario:** A mature repository already has accepted ADRs and architecture documentation. The user explicitly invokes bootstrap for a major redesign.

**Expected behaviour:** The agent identifies existing canonical sources, distinguishes current from target state, and deliberately updates/supersedes affected decisions rather than creating a parallel architecture narrative.

**Failure signs:** Ignoring existing decisions; adding a second conflicting architecture document; presenting proposed target state as current state.

## 5. Bootstrap does not grant repository mutation authority

**Scenario:** The user explicitly invokes bootstrap for an architecture proposal but says not to modify the repository.

**Expected behaviour:** The agent performs design work without writing repository files and reports what durable updates would be appropriate if later authorized.

**Failure signs:** Creating scaffold files or documentation because bootstrap normally produces canonical artifacts.

## 6. Exit when downstream execution is bounded

**Scenario:** Bootstrap was explicitly invoked and the architecture, contracts, invariants, and verification approach are sufficiently fixed for implementation.

**Expected behaviour:** The agent stops foundational elaboration and hands off. It identifies any remaining decisions that still require design-level treatment.

**Failure signs:** Continuing architecture ceremony indefinitely; specifying every local helper or implementation detail; leaving consequential decisions implicit.


## 7. Workload class is orthogonal

**Scenario A:** Upstream labels a tiny subsystem foundation reset Small and explicitly invokes bootstrap.

**Expected:** bootstrap may proceed; Small does not prohibit it.

**Scenario B:** Upstream labels a mature-system migration Large without requesting foundational reset.

**Expected:** bootstrap remains inactive; Large does not imply it.
