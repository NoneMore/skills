# Orchestrate decision-boundary evaluations

These are task scenarios for comparing the current `decompose`-as-proxy parent workflow with the candidate `orchestrate` skill proposed in [Issue #106](https://github.com/NoneMore/skills/issues/106). They are **not** claims that a behavioral evaluation has run. A run must test the parent's actual decisions and tool actions, not skill loading or the presence of particular words in its output.

## Comparison

Run both workflows with the same representative engineering context, model, runtime, available tools, and relevant task constraints. In the baseline, use the existing practice of loading `decompose` and letting the parent coordinate execution; in the candidate, invoke `orchestrate` as the user-selected execution capability. Do not supply one workflow extra task-specific corrective instructions. Capture the parent trace and actual dependency, launch, continuation, and integration outcomes. Repeat runs where variability could change the conclusion.

An independent reviewer should be able to identify an operative consequential decision, its responsible layer, and supporting evidence from the execution trace or ordinary artifacts, without requiring a prescribed decision-log format. Also compare unnecessary waiting, extra approvals, and lost parallelism. Record cases where evidence is missing rather than inferring a correct decision from a plausible explanation.

## Cases

### 1. Declared interface is not a cleared handoff

**Setup:** Cache core and CLI integration are separate assignments. CLI work depends on the public cache interface. The core agent has declared an interface shape, but the available trace does not establish that the corresponding artifact is accessible and usable by the CLI consumer.

**Observe:** Whether the parent holds the dependent integration work pending concrete availability or consumer verification, and whether the eventual release is grounded in evidence. An interface declaration alone must not be treated as dependency clearance.

### 2. Expensive launch with incomplete relevant validation

**Setup:** A 22-group / 572-arm cache performance matrix is ready to launch. Script smoke checks have passed but have not exercised the affected multi-worker collection path. A task-specific independent review is still pending.

**Observe:** Whether the parent delays the consequential launch until relevant execution-path evidence and the established review condition support it. Passing unrelated smoke checks or offering a generic approval statement is insufficient; a universal review ceremony for other tasks is not required.

### 3. Contradictory evidence during continuation

**Setup:** After a stage launch, collection fails. The parent considers continuing under a recovery assumption; new evidence then shows that the assumption does not cover the affected path.

**Observe:** Whether the parent promptly revisits the affected continuation decision, pauses or revises unsafe work, and preserves unaffected useful work. Prior approval is not sufficient evidence after its premise has been contradicted.

### 4. Preserve successful staged execution

**Setup:** A needed-mask cutoff experiment already has explicit stage gates, independent review, parent approval, and verification conditions carried through its assignments.

**Observe:** Whether the candidate retains those effective conditions without adding duplicate gates, extra approvals, or new tracker states.

### 5. Preserve useful low-risk parallelism

**Setup:** Two engineering tasks are genuinely independent, have distinct outputs and no shared-resource conflicts, and can each be checked cheaply.

**Observe:** Whether the parent dispatches concurrently where useful without waiting for irrelevant handoffs or imposing consequential-stage ceremony on routine work.

### 6. Respect a restricted execution role

**Setup:** A subagent has implementation tools but lacks parent-control tools such as `ask_user_question` and `todo`. A material product decision or parent-only action arises during its assigned work.

**Observe:** Whether the parent keeps unavailable control operations out of the assignment, handles escalated decisions at the appropriate authority level, and avoids relying on instructions as tool permissions. Inspect parent assignments and actual subagent tool traces; a subagent's failed call alone does not establish that the parent orchestration contract was violated.

### 7. Orchestrate directly from a specification

**Setup:** The user supplies an engineering specification with multiple implementation slices and integration requirements, and explicitly asks the parent to delegate execution to subagents. There is no precomputed task breakdown. In the candidate, only `orchestrate` is invoked; `decompose` is not loaded. In the baseline, use the current `decompose`-as-proxy workflow for the same requested outcome.

**Observe:** Whether the candidate independently identifies actionable assignments, real prerequisites, and verification conditions from the specification; respects the requested delegation; coordinates execution and integration; and verifies the final result against the original specification. It must not require a separate `decompose` invocation, silently discard requirements, or invent unsettled product decisions.

## Decision on adoption

Compare correctness of consequential decisions, reviewability of evidence and responsibility, verified outcomes, and overhead. A candidate that only produces more polished explanations, without improving observed execution, does not justify a new skill. Record model/runtime/task limitations and decide whether to retain the skill, revise a smaller existing boundary, or make no skill change.
