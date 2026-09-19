---
name: engineering-handoff
description: "Build or validate a bounded engineering handoff whenever work actually crosses an agent, model, session, context, or executor boundary. Use during real delegation/handoff to preserve governing sources, Fixed / Local / Open decision budgets, verification evidence, and escalation triggers so the receiver can execute without accidental redesign. Do not invoke merely because planning occurred, a workload is Medium/Large, or a task looks complex."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Handoff

Create the smallest execution contract that lets a receiving engineer or agent act safely without reconstructing the original conversation.

This is a **model-invoked delegation primitive**, not a planning workflow. Invoke it when a handoff is actually being prepared, consumed, or materially revised across an agent, model, session, context, or executor boundary. Do not invoke merely because a task is complex, an upstream workload class is Medium/Large, or someone discussed a plan.

**A work package transfers decisions and proof obligations, not transcript.**

## Resolve facts before packaging

Before asking the user anything, inspect available repository evidence for facts the environment can answer: code, tests, configs, maintained docs, accepted specs, task artifacts, and relevant history.

Ask the user only for unresolved product intent, scope, compatibility, UX, risk tolerance, acceptance behaviour, or other consequential decisions that evidence cannot determine.

If a consequential open decision prevents the assigned work from proceeding safely, the package is not ready. Distinguish that prerequisite from an Open question the receiver is explicitly assigned to investigate; use the research boundary below rather than selecting an answer silently.

## Governing sources

Identify the smallest authoritative context the receiver must obey:

- explicit current user intent;
- accepted specifications, designs, architecture decisions, and public contracts;
- repository instructions and relevant maintained conventions;
- tests or runtime evidence that define important current behaviour;
- explicit non-goals, compatibility boundaries, and risk constraints.

Reference canonical sources rather than copying them wholesale. Do not promote a stale plan or incidental implementation pattern into authority.

## Decision budget

Every non-trivial package must make consequential freedom visible using the lightest useful distinction:

- **Fixed decisions** — architecture, product behaviour, public contracts, compatibility promises, scope boundaries, or other consequential choices the receiver must preserve.
- **Local decisions** — reversible implementation mechanics the receiver owns autonomously while preserving fixed decisions and observable behaviour.
- **Open decisions** — unresolved consequential choices that must escalate rather than being silently decided during implementation.

Do not over-specify local mechanics. The purpose is to protect consequential decisions while leaving implementation freedom where it is safe.

## Minimal package contract

Preserve only what the receiver needs:

1. **Outcome** — the observable state that should become true.
2. **Scope / non-goals** — what may change and what must remain untouched.
3. **Governing sources** — canonical constraints the receiver must consult.
4. **Fixed decisions** — choices that must not be casually reopened.
5. **Local decision budget** — implementation freedom the receiver owns.
6. **Open decisions** — distinguish blocking prerequisites from explicitly assigned research questions; identify who owns the eventual decision. Blocking prerequisites make the package not-ready.
7. **Dependencies / sequencing** — only where order materially affects correctness or coordination.
8. **Verification** — behaviour-relevant positive evidence for the outcome plus negative evidence for important invariants, governing constraints, regression risk, and unjustified complexity where material.
9. **Escalation triggers** — evidence or conditions that invalidate the package or require a consequential decision.
10. **Resume state, when work has started** — completed and partial work, relevant files/artifacts, remaining work and blockers, observed verification commands/results and unverified gaps, and the next executable action. Distinguish planned checks from checks already run. Identify pre-existing work the receiver must preserve; do not require reconstructing progress from a specification or the original chat.

These are semantic requirements, not a mandatory file template. A small handoff may be a compact message; a long-running effort may use the repository's existing planning artifact.

When supplied, carry capacity assumptions separately from hard time/context/budget limits, the authorized capacity decision owner, and any pending or accepted adjustment. If actual progress or remaining work materially undermines those assumptions, the receiver reports evidence, remaining work including verification, uncertain capacity impact, and a recommended option to that owner (or the user if none is delegated). Preserve the workload label. Continue only independent bounded work within existing authority/limits; preserve permitted resume state before a known limit and stop affected work safely. Silence is not an extension. Do not invent missing limits, reduce scope/proof, or start a new orchestration mode from the mismatch alone.

## Research handoffs

A bounded research handoff may be ready while the implementation decision remains Open. State the question, relevant fixed constraints, permitted probes and effects, evidence needed, expected comparison/recommendation, stopping condition, and decision owner. The receiver may investigate and recommend; that does not authorize accepting the recommendation, changing governing design, or implementing it. If decision authority is separately delegated, carry its explicit bounds.

For example, compare database options under known data and operational constraints, then return evidence and a recommendation for the user to decide. Not knowing the winning option is the research objective, not a prerequisite. If even a safe probe requires an unresolved consequential choice, that choice still blocks the affected probe. Use `engineering-investigation` when available; otherwise gather bounded discriminating evidence and report limitations directly.

## Receiver capability

Choose capability by remaining decision burden and consequence, not upstream capacity labels. A cheaper executor needs discoverable governing sources, fixed constraints, local reversible choices, and concrete verification/escalation. A longer package cannot substitute for resolving consequential ambiguity.

## Execution and re-planning

The package is a hypothesis about bounded execution, not authority over contradictory evidence.

The receiver may change local mechanics autonomously while preserving outcome, scope, fixed decisions, contracts, and relevant invariants. Escalate or re-plan when evidence shows that continuation would require:

- changing a fixed architectural or product decision;
- materially widening scope;
- changing a public or compatibility contract not already authorized;
- accepting a new consequential or irreversible risk;
- violating a governing specification or design;
- relying on an assumption repository evidence has falsified.

The receiver must not silently absorb these decisions into code.

## Persistence

Work packages are **transient by default**. Persist one only when cross-context continuity materially requires it. When persistence is justified, use the repository's existing coordination convention and apply `engineering-knowledge-governance` when available.

Do not create permanent task files merely because a handoff exists. Compress around current decisions, sources, and evidence; retire stale coordination state when it no longer serves continuity.

## Completion criterion

A work package is ready when the receiver can begin or resume the assigned implementation or research without reconstructing the original chat, repeating completed work, mistaking planned checks for observed evidence, reopening fixed decisions, or inventing consequential product/architecture choices. Research readiness does not imply implementation readiness; judge research completion by its bounded question and evidence obligations.
