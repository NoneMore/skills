# Agentic Engineering Skills — v5-rc.1

A composable engineering toolbox for long-lived software systems. Repeated changes should preserve intent, evidence, architecture, and trustworthy knowledge, regardless of repository size.

> **Invocation is an API. Relevance is not permission to invoke.**

## Choose a capability

### Model-invoked disciplines

| Skill | Use for |
| --- | --- |
| [engineering-implementation](engineering-implementation/SKILL.md) | Authorized persistent implementation, fixes, and refactoring; conditional fixes join only after the condition is established and the fix is pursued. |
| [engineering-investigation](engineering-investigation/SKILL.md) | Evidence-seeking diagnosis, research, measurement, and disposable experiments. |
| [engineering-review](engineering-review/SKILL.md) | Read-only judgment against requirements, constraints, regressions, and maintenance cost. |
| [engineering-specification](engineering-specification/SKILL.md) | Explicitly requested written intent and accepted governing design. |
| [engineering-execution-planning](engineering-execution-planning/SKILL.md) | Explicitly requested sequencing, dependencies, verification, and coordination from accepted intent. |
| [engineering-knowledge-governance](engineering-knowledge-governance/SKILL.md) | Concrete persistence, canonicality, reconciliation, and document-lifecycle decisions. |
| [engineering-handoff](engineering-handoff/SKILL.md) | Real handoffs, including current state and evidence needed to resume interrupted work. |

### Explicit orchestration modes

These require an explicit user choice or an upstream decision under user-selected policy. Apparent relevance, complexity, or a capacity label is insufficient.

| Skill | Use for |
| --- | --- |
| [engineering-foundation-design](engineering-foundation-design/SKILL.md) | Establishing or materially resetting foundational architecture and contracts. |
| [engineering-plan-and-delegate](engineering-plan-and-delegate/SKILL.md) | Deliberately evaluating decomposition and coordinating actual handoffs. |
| [engineering-initiative-shaping](engineering-initiative-shaping/SKILL.md) | Shaping an explicitly selected Large initiative into upstream-accepted Medium requirements. |

The root is not a Skill. No capability expands the underlying task's repository, VCS, deployment, publication, or external-effect authority.

## Capacity policy belongs upstream

[routing-policy.yaml](routing-policy.yaml) owns the workload definitions and routing contract. Small / Medium / Large denotes the user's capacity envelope, which may reflect budget, context, or preferred execution topology. The user owns classification; a Meta-Agent may apply it only under delegated policy. Exact thresholds are deliberately unspecified.

Leaf skills preserve supplied labels and never infer them from LOC, file count, architecture, uncertainty, or risk. Those engineering properties scale rigor and executor capability independently.

The upstream layer may explicitly select these profiles:

| Selected profile | Orchestration responsibility |
| --- | --- |
| Small | State intent briefly, execute with the applicable discipline, and report evidence; no mandatory written plan. |
| Medium | Assign specification and written execution-plan responsibilities, then execute and accept. Create work packages only for actual handoffs. |
| Large | Explicitly select initiative shaping, settle macro direction, and propose units for upstream Medium-capacity acceptance. Downstream profiles own detailed execution. |

A label alone never selects a profile or assigns artifact responsibility. A leaf implementation or plan-revision task must not restart the upstream pipeline. Existing accepted artifacts should be reused. Bootstrap is independent: a Small subsystem may need an explicit foundation reset, while a Large mechanical migration may not.

If execution evidence materially undermines a supplied capacity assumption, report the changed assumptions, completed/remaining work including verification, estimated impact and uncertainty, and a recommendation. The user or authorized upstream owner decides whether to continue, adjust capacity, split/defer, or pause. Keep the class unchanged until that owner revises it. Pending decisions permit only independent bounded work within existing authority and limits; preserve permitted resume state before a known limit and stop affected work safely. Unknown limits are not invented, silence grants no extension, and a forecast mismatch does not activate another profile or weaken acceptance. The full contract is `workload_envelope.capacity_feedback` in the routing policy.

## Composition and independent use

Install selected skill directories with their bundled references and `agents/` files intact. A leaf skill must work without this README, the root routing file, sibling directories, or an installed Meta-Agent. Root policy is for bundle integration; essential invocation boundaries stay in each skill.

Use a companion only when its trigger holds and it is available. Load it through the runtime's supported skill mechanism; naming a skill in output is not invocation. Never bypass explicit-only policy by reading another orchestration skill as a substitute for authorized selection. Missing companions use the skill's bounded local guidance and do not force installation or stop ordinary authorized work.

Keep the commonly loaded entrypoints concise. Load references only for their stated situations; do not preload all supporting material. For example, coding's [governing-decisions reference](engineering-implementation/references/governing-decisions.md) covers source conflicts and invalidated plans.

## Engineering principles

- **Intent → Feedback → Evidence:** prove the outcome, challenge assumptions while change is cheap, and stop when the authorized work is complete.
- **Positive and negative evidence:** verify intended behaviour and materially relevant constraints, regressions, scope, and complexity.
- **Fixed / Local / Open:** preserve consequential accepted decisions, choose reversible mechanics autonomously, and surface unresolved consequential choices.
- **Conditional persistence:** consider knowledge impact, but persist only when future decisions or continuity need it. Use canonical homes and reconcile stale claims.
- **Recoverable handoffs:** transfer current state, remaining work, observed evidence and gaps, and the next action, alongside outcome and constraints.
- **Repository conventions first:** avoid a mandatory document tree or permanent master plan. Coordination state ends when its usefulness ends.

## Runtime integration and release evidence

Explicit modes carry `disable-model-invocation: true` and a matching `agents/openai.yaml` policy with `allow_implicit_invocation: false`. Custom runtimes must map the root policy to equivalent enforcement; YAML prose is not an executable router.

See the [runtime acceptance contract](evals/runtime-acceptance.md) for shipped policy files, isolated-install checks, and required external run evidence. An adapter permitting upstream invocation must preserve user-selected orchestration authority without enabling leaf relevance-based invocation.

Each skill's `evals/behavioral-evals.md` specifies portable scenarios. [Bundle routing evals](evals/bundle-routing-evals.md) cover composition. Runtime adapters, graders, transcripts, model matrices, and regression runs remain outside this source bundle.

**Release evidence status:** this source revision defines expected behaviour and ships native policy metadata. It does not include a tested custom adapter or recorded model runs. Static validation cannot establish runtime conformance. A runtime-qualified release must link the exact adapter and external results described in the acceptance contract.
