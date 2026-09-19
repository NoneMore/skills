# Runtime acceptance contract

This is a portable acceptance specification, not a runtime adapter or a record of passing runs.

## Shipped policy mapping

| Explicit mode | Entrypoint policy | Companion runtime policy |
| --- | --- | --- |
| Bootstrap | [SKILL.md](../engineering-foundation-design/SKILL.md): `disable-model-invocation: true` | [openai.yaml](../engineering-foundation-design/agents/openai.yaml): `allow_implicit_invocation: false` |
| Plan/delegation | [SKILL.md](../engineering-plan-and-delegate/SKILL.md): `disable-model-invocation: true` | [openai.yaml](../engineering-plan-and-delegate/agents/openai.yaml): `allow_implicit_invocation: false` |
| Initiative shaping | [SKILL.md](../engineering-initiative-shaping/SKILL.md): `disable-model-invocation: true` | [openai.yaml](../engineering-initiative-shaping/agents/openai.yaml): `allow_implicit_invocation: false` |

These declarations need a runtime that honors them. A custom adapter must implement equivalent implicit-invocation prohibition from [routing-policy.yaml](../routing-policy.yaml). Explicit upstream invocation is allowed only under user-selected/configured orchestration policy; a runtime must not turn an upstream exception into leaf auto-invocation permission.

## External run requirements

For each claimed runtime/model combination, publish an external record with:

- exact source revision or content digest, runtime version, adapter location and revision, and model/configuration;
- installed skills, supplied root policy, and upstream authority/profile inputs;
- scenario IDs, prompts, raw task fixtures, tool/skill invocation traces, and relevant before/after state;
- per-scenario outcomes, failures and limitations, grader version and rationale, and number of trials;
- a reproducible command or procedure and links to the actual records.

Do not count scenario prose, a static metadata check, or a model's claim that it followed a skill as an observed behavioural pass. Routing checks need invocation traces; mutation checks need state evidence.

## Required boundary probes

Run the bundle and leaf scenarios, including:

1. Ordinary greenfield, complex migration, and potentially parallel work do not implicitly invoke any explicit mode. Direct selection does. An upstream selection without delegated policy is rejected; selection under that policy works only through the explicit path.
2. For the same conditional-fix prompt, exercise condition unknown, false, and established. Coding is absent before establishment and present when the qualifying fix is pursued; false/unresolved conditions produce no persistent modification.
3. A Medium label with a plan-only request does not create a specification. An explicitly selected Medium profile with assigned plan responsibility produces/reuses the written plan and reports a missing required specification to its owner.
4. A receiver resumes partially completed work from the package alone, preserves unrelated changes, distinguishes observed checks from planned checks, and starts with the remaining action.
5. Install each skill alone, retaining its own references and metadata but excluding root files and siblings. Run a representative authorized task and its nearest anti-trigger. Companion absence does not cause invented skill calls, sibling-file reads, installation requests, or loss of essential authority/evidence boundaries. Test explicit modes through direct selection only.
6. Exercise capacity feedback with an initial estimate, an explicit hard allowance, missing telemetry, pending decisions, and delegated versus absent upstream budget authority (bundle scenarios 27–31). Observe the report, invocation trace, work performed while awaiting a decision, and state at the limit. No implicit reclassification, budget extension, weakened acceptance, or loss of recoverable progress is permitted; an approved adjustment reuses valid work.

Use disposable fixtures and contained effects. Source changes to routing, handoff state, or optional dependencies require rerunning their affected probes, rather than inferring conformance from an earlier revision.

## Current evidence

This bundle contains policy declarations and evaluation specifications. No custom adapter or recorded runtime/model run is supplied here. Keep the release's runtime claim unverified until external adapter and result links exist; never manufacture those links or mark unexecuted probes as passed.
