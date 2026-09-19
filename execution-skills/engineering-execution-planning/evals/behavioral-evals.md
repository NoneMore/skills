# Engineering Execution Planning Behavioral Evals — v5-rc.1

## 1. Explicit Medium planning

**Scenario:** Upstream explicitly selects the Medium profile and assigns this Skill its written execution-plan responsibility. An accepted written specification exists.

**Expected:** create a written concrete execution plan with bounded units, real dependencies, verification, and likely handoff seams. Do not reconsider workload class.

## 2. Large-looking task without planning request

**Scenario:** A many-file migration is directly assigned for execution with accepted intent and no explicit planning mode.

**Expected:** this Skill does not invoke merely because planning seems useful or the task looks large.

## 3. Hidden architecture choice

**Scenario:** Planning reveals that execution depends on choosing between two incompatible persistence models.

**Expected:** stop treating the choice as a task detail and return it to specification/shaping or the decision owner.

## 4. Fake dependency avoidance

**Scenario:** Three independently verifiable packages can proceed against disjoint mutable scopes.

**Expected:** do not serialize them simply to produce a neat numbered sequence.

## 5. Actual handoff

**Scenario:** The plan is now being handed from a primary agent to two coding executors.

**Expected:** compose `engineering-handoff` for each real receiving boundary.

## 6. Hypothetical delegation

**Scenario:** The plan mentions that a future subagent might own testing, but no handoff is occurring yet.

**Expected:** do not create a work package merely because delegation is possible.

## 7. Negative evidence in verification plan

**Scenario:** A feature changes a module boundary while satisfying visible behaviour.

**Expected:** plan evidence for both behaviour and absence of architectural regression/unnecessary coupling; tests-passing alone is not the full acceptance contract.

## 8. Plan lifecycle

**Scenario:** A persisted Medium plan is complete and its long-term truths have been incorporated into canonical specs/contracts.

**Expected:** treat the plan as coordination state and retire/archive it according to repository convention rather than promoting it automatically into permanent architecture documentation.

## 9. Capacity label with ordinary plan revision

**Scenario:** Metadata says Medium, but no profile is selected. The user provides accepted intent in chat and asks only to revise the verification sequence of an existing plan.

**Expected:** make the requested plan revision. Do not create a specification, request its approval, or activate the Medium pipeline from the label.

## 10. Missing input under an assigned profile

**Scenario:** Upstream explicitly selects the Medium profile and assigns written planning; the required accepted specification has not been supplied or made discoverable.

**Expected:** report the missing input to its upstream owner. Do not invent accepted design, silently take over specification, or call the execution plan ready. Continue useful repository fact gathering within scope.

## 11. Planning alone without companions

**Scenario:** Only this skill is installed. The user supplies accepted intent and requests a plan in chat. There is no capacity class, repository specification, or actual handoff.

**Expected:** provide bounded units, real dependencies, decision constraints, and verification directly. No installation request, permanent artifact, or work-package invocation is required.
