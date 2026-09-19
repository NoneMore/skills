---
name: engineering-investigation
description: "Evidence-seeking discipline for research, diagnosis, exploratory testing, measurement, reproduction, audits, and disposable experiments whose intended outcome is understanding rather than a persistent code change."
metadata:
  version: "v5-rc.1"
  invocation: "model"
---

# Engineering Investigation

Resolve an engineering question by turning uncertainty into evidence without silently converting investigation into implementation.

The core loop is:

> **Question → Probe → Evidence → Implication**

## Invocation boundary

Invoke when the primary requested outcome is understanding, diagnosis, measurement, reproduction, research, exploratory testing, or a disposable experiment and **persistent repository mutation is not the intended deliverable**.

Typical cases include:

- investigating a bug or performance regression before deciding a fix;
- researching an API, library, protocol, or platform constraint;
- reproducing a failure;
- measuring current behaviour;
- exploring alternatives with disposable prototypes or experiments;
- checking whether an assumption is true;
- read-only technical audits whose main purpose is fact finding rather than acceptance judgment.

When available, prefer `engineering-review` for judgment against requirements or governing constraints, and `engineering-implementation` for unconditional implementation or a qualifying conditional fix now being pursued. A conditional fix request remains investigation until its condition is established.

This Skill does not grant tracked-content mutation, VCS, deployment, publication, credential, or other external-effect authority.

## Frame the question

Before probing, state the smallest useful question or hypothesis. Separate:

- what is already known;
- what is assumed;
- what observation would materially change the conclusion;
- what evidence would falsify the leading explanation.

Avoid broad research when a narrow discriminating observation can answer the decision-relevant question.

## Inspect before asking

Use available repository and environment evidence for facts before asking the user:

- code, tests, configs, logs, schemas, and maintained docs;
- reproducible runtime behaviour;
- build/tooling metadata;
- relevant history when it can explain current state;
- authoritative primary technical sources when external research is authorized and needed.

Ask the user for product intent, scope, risk tolerance, inaccessible environment facts, or consequential decisions that evidence cannot settle.

## Choose discriminating probes

Prefer probes that can distinguish competing explanations rather than merely collect more data.

Useful probes include:

- focused reproduction;
- targeted test execution;
- instrumentation or logging that can be removed/discarded;
- controlled input variation;
- minimal examples;
- performance measurement with a relevant baseline;
- source/specification inspection;
- disposable prototypes whose result answers a specific design question.

Keep experiments bounded. A prototype that starts accumulating production obligations has crossed into implementation and needs explicit mutation authority and `engineering-implementation`.

## Read-only and disposable state

Observation may create ordinary disposable artifacts such as caches, coverage files, temporary logs, generated benchmark output, or scratch prototypes when they are normal, contained, and do not create consequential external effects.

Do not intentionally modify tracked production content, accept snapshots, update dependencies/lockfiles, or leave experimental instrumentation in maintained code unless persistent mutation becomes separately authorized.

If a supposedly safe probe would invoke commands with uncertain external effects, inspect or constrain the command path first.

## Update the model from evidence

After each meaningful probe, record the implication:

- supports hypothesis;
- weakens hypothesis;
- falsifies hypothesis;
- reveals a new material uncertainty;
- shows the question was framed incorrectly.

Do not keep extending a favored theory after direct evidence falsifies it.

Escalate when evidence shows that answering the question now requires a consequential product/architecture/risk decision rather than more observation.

## Scope feedback

Investigation may discover that the requested question is materially broader or narrower than expected.

Continue autonomously when the adjustment is still necessary to answer the same question and remains within read-only/disposable authority.

Request decision-owner intervention when continuation would:

- change the question's consequential scope;
- require persistent implementation work not already authorized;
- require changing an accepted design or contract;
- depend on a risk or product trade-off rather than an empirical fact;
- exceed an upstream work package's Fixed/Local decision budget.

## Capacity feedback

If observed probe progress or remaining evidence needs materially undermine a supplied capacity assumption or threaten a known limit, report changed assumptions, evidence, completed/remaining work, uncertain capacity impact, and a recommendation to the user or authorized upstream owner. Preserve the workload label; unknown limits/telemetry remain unknown. Continue only independent bounded probes within existing authority and limits while awaiting a decision. Preserve permitted resume state before a known limit and stop affected work safely; do not start a probe that cannot reasonably fit including recovery. Silence grants no extension, and a shorter budget does not justify weaker conclusions or an invented implementation transition. Apply the owner's decision without repeating valid probes unnecessarily.

## Evidence quality

Seek both confirming and disconfirming evidence.

Prefer evidence that is:

- close to the behaviour or claim;
- reproducible where practical;
- independent of the assumption being tested;
- specific enough to distinguish alternatives;
- explicit about environmental limitations and uncertainty.

Do not convert "no failure observed" into proof of absence when the probe had weak coverage.

## Findings and durable knowledge

The default deliverable is a concise evidence-backed finding, not a permanent research document.

Perform a lightweight knowledge-impact check: did the investigation establish a fact, constraint, design decision, operational truth, or contradiction that future engineering work materially needs to know?

If yes, use `engineering-knowledge-governance` when available; otherwise preserve provenance and uncertainty in the existing canonical home, within task authority. In a read-only task, report the reconciliation need. If no, keep the result transient.

## Transition to mutation

If the task conditionally authorizes a fix after diagnosis, establish the condition first. Once the condition is established and persistent mutation is being pursued, use `engineering-implementation` when available. Otherwise make only the qualifying fix, preserve unrelated work, verify the changed behaviour and regressions, and report evidence gaps. If the condition is false or unresolved, remain read-only.

Do not retroactively treat earlier read-only investigation as mutation authority.

## Completion

A useful investigation report states:

- the question answered;
- the strongest relevant evidence;
- the resulting conclusion and confidence/limitations;
- important evidence against the conclusion or remaining uncertainty;
- any consequential implication requiring user/design intervention;
- whether a durable-knowledge reconciliation or authorized implementation should follow.

Do not bury the conclusion under a transcript of probes.
