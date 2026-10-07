---
name: triage
description: Assess incoming issues and pull requests until the next action is clear. Use when the user explicitly wants tracker intake triaged, clarified, verified, accepted for action, deferred, or declined.
disable-model-invocation: true
---

# Triage

## Purpose

Turn raw incoming tracker work into a justified next action without imposing a second workflow state machine on the project.

## Accepts

Issues, pull requests, bug reports, feature requests, or similar incoming work that needs maintainer assessment.

## Owns

- establishing what the incoming item is actually asking for and what relevant project state already exists;
- checking material claims when the triage outcome depends on whether they are true;
- identifying the smallest unresolved information or decision that prevents a responsible disposition;
- distinguishing work that is actionable from work that needs reporter input, maintainer judgment, deferral, rejection, deduplication, or no action because the behavior already exists;
- when work is actionable, making the requested behavior and success conditions clear enough that the next actor is not forced to reconstruct the intake decision;
- when the user asks for tracker mutation, expressing the result through the project's existing tracker conventions and native states rather than inventing suite-specific roles or labels.

Use [references/intake-assessment.md](references/intake-assessment.md) when a substantive intake decision needs verification or sharpening.

## Invariants

Do not present reporter claims, producer explanations, or nearby code as verified facts unless the available evidence establishes them.

Do not make an item appear actionable by silently making unresolved product, scope, or architecture decisions on the next actor's behalf. Resolve those decisions when they are within the user's delegated authority; otherwise keep the blocker explicit.

Do not require canonical triage labels, work-item roles, agent briefs, claim/release protocols, or a fixed readiness state. Existing project conventions may use such mechanisms; if so, treat them as project state rather than `triage` semantics.

Triage prepares or classifies incoming work. It may inspect or verify code and behavior, but it does not need to implement the requested production change in order to finish.

## Done when

The item has a justified disposition, the next action and responsible party are clear, and any material uncertainty that still affects that action is explicit. If the user asked to update the tracker, the persisted item reflects that result using the project's own conventions.
