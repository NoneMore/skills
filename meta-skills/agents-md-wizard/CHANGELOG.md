# Changelog

## 0.6 — 2026-09-10

- Change the default from autonomous authoring to a guided, user-controlled workflow: a bare invocation permits focused read-only inspection and interviewing, not an artifact write.
- Separate observed workspace mechanics from human policy. Authority, independence, mutability, lifecycle, synchronization, ownership, approval, and scope hypotheses now require user confirmation before they become instructions.
- Require a compact checkpoint containing observed facts, recommended interpretations, unresolved choices, and the proposed target/scope.
- Require a reviewable draft or policy-level patch plus explicit user approval before create or refresh writes.
- Stop silently substituting a harness-effective target, even for result-oriented requests; recommend it and include it in the approval checkpoint.
- Keep best-effort, no-interview, and write-without-review behavior as explicit user-selected exceptions.
- Strengthen sensitive-inspection guidance and keep instruction-only verification from expanding into tests of unchanged project files or configuration.
- Add symmetric regression coverage for mandatory policy questions, pre-write approval, secret-value read avoidance, durable-content checks, and proportional verification.

## 0.5 — 2026-09-10

- Consolidate the runtime architecture around one self-sufficient core plus two common exception references; ordinary create/refresh runs should use `SKILL.md` alone.
- Reduce common runtime references from seven to two: merge topology + nested overlay guidance into `references/scoped-composition.md`, and merge drafting/pointer/completion/migration guidance into `references/authoring-patterns.md`.
- Remove runtime interview, workspace-archetype, audit-checklist, generic harness-profile, and duplicate topology references; their essential behavior now lives once in the core instead of being re-encoded across layers.
- Keep concrete Codex and Pi harness profiles as thin version-sensitive loader adapters. Unknown harnesses now use a short conservative fallback directly in `SKILL.md`.
- Remove per-stage `Done when` repetition and simplify reference dispatch while preserving the zero-question draft-delta gate, target-vs-loader distinction, inherit/extend/narrow/override model, policy migration, and observable completion checks.
- Add v0.5 consolidation regressions for reference-count budget, no reference-cascade behavior, and core-size discipline.

## 0.4.1 — 2026-09-10

- Make runtime reference loading explicitly demand-driven: ordinary create/refresh runs should use `SKILL.md` alone or only the one concrete harness profile needed, instead of preloading the reference catalog.
- Add a zero-question bias and a concrete draft-delta gate: ask only when a non-discoverable choice changes a specific instruction line, policy branch, or write target; default first rounds to 0–3 questions.
- Separate explicit artifact identity from effective harness targeting. Generic/result-oriented setup may choose the nearest effective target, while an explicitly named inert file is diagnosed rather than silently substituted without authorization.
- Correct the Codex profile for empty override behavior: candidate selection is based on the first existing filename, so an empty `AGENTS.override.md` can shadow same-directory `AGENTS.md` without contributing instruction text.
- Add quantitative eval evidence for inspection reads, reference loads, question counts, artifact bytes, and duplicated inherited rules.
- Expand behavioral regressions from 26 to 35 scenarios, including Codex empty-override shadowing, inert-target handling, zero-question creation, reference-load budgets, and downstream pointer/status/scoped-delta/validation behavior.

## 0.4 — 2026-09-10

- Split **target intent** from **loader semantics** so user-selected scope/artifact and runtime discovery/composition no longer compete in one contradictory precedence chain.
- Make create/setup target the active harness/profile's effective project-instruction artifact, with generic `AGENTS.md` only as the fallback when no target is otherwise established.
- Rename evaluation assertions so `PASS` always denotes a positive observed property; add regressions for no-ceremony create behavior.
- Reduce pre-write ceremony: preview only expectation-changing migrations, target/scope substitutions, intentional overrides, or consequential best-effort assumptions.
- Add verified concrete harness profiles for OpenAI Codex and Pi Coding Agent, including discovery boundaries, candidate precedence, composition, and write-target guidance.
- Add Codex- and Pi-specific profile regression scenarios.

## 0.3.2 — 2026-09-10

- Refactor the core workflow around a harness-agnostic **instruction topology**: scope, precedence, composition, and effective contract.
- Add a thin harness-profile contract so runtime-specific filenames, discovery roots, precedence, and loader semantics stay at the boundary instead of leaking into core authoring logic.
- Stop assuming path nesting implies instruction inheritance; scoped delta authoring now applies only when the active topology establishes composition.
- Change material refresh behavior from "important edit requires confirmation" to "unresolved material decision requires confirmation"; well-grounded requested updates may proceed after a useful preview without a redundant approval gate.
- Make Mixed Workspace guidance conditional: destructive-change, privacy, and approval rules are introduced only when relevant rather than treated as default global invariants.
- Add OpenAI `default_prompt` metadata and remove the non-portable `disable-model-invocation` frontmatter key.
- Extend eval guidance with two-stage outcome testing, including harness-portability and downstream-agent behavior scenarios.

## 0.3.1 — 2026-09-10

- Rebalance the Skill around AGENTS.md authoring rather than repository security review: workspace documentation is explicitly useful project evidence and may directly support inferred agent rules.
- Narrow prompt-injection handling to a lightweight rule: inspected content may inform project understanding but cannot redirect the wizard, expand scope, trigger unrelated actions, or override governing instructions.
- Remove the redundant final-confirmation requirement for a new root `AGENTS.md` when the user already requested creation and consequential decisions are settled.
- Keep exact patch previews and confirmation for material changes to existing human-authored policy, while preserving no-extra-gate behavior for semantic-preserving refreshes.
- Collapse trust, filesystem, secret, and privacy audit sections into a short safety-hygiene check so behavioral quality, grounding, scope, inheritance, and completion remain the audit focus.
- Replace the duplicate notebook/data prompt-injection eval with a regression case that verifies explicit create flows do not ask twice; recast symlink and ancestor cases as focused-inspection/scope behavior.
- Clarify the interview stopping rule: infer from strong workspace evidence and ask only about consequential choices that remain unsupported or ambiguous.

## 0.3.0 — 2026-09-10

- Add an explicit trust boundary: ordinary workspace content is evidence, not agent-instruction authority, preventing embedded prompt-injection text from being promoted into `AGENTS.md`.
- Harden workspace scope handling: resolve boundaries before broad inspection, avoid irrelevant recursive trees, and do not follow symlinks outside the agreed scope without authorization.
- Make confirmation risk-aware: material policy migrations show exact patch/replacement text and require confirmation, while verified semantic-preserving refreshes can avoid redundant gates.
- Expand audit checks for prompt injection, scope escape, symlinks, change authorization, and untrusted-content promotion.
- Upgrade evaluation scenarios with binary PASS/FAIL assertions and adversarial cases for prompt injection, scope escape, large repositories, material authority changes, and blind overwrite risks.
- Reduce `SKILL.md` duplication and keep the main file focused on orchestration while retaining nested-scope behavior.

## 0.2.0 — 2026-09-10

- Add first-class nested/subdirectory `AGENTS.md` mode.
- Read ancestor instruction chains before interviewing or drafting a child file.
- Model child instructions as an overlay: inherit, extend, narrow, or explicitly override.
- Detect ancestor drift that makes child rules redundant or conflicting.
- Add nested-inheritance reference, child example, audit checks, and evaluation scenarios.

## 0.1.0 — 2026-09-10

Initial standalone release.

- Interactive decision-frontier interview.
- Workspace archetype detection across research, knowledge, writing, analytics, software, operations, creative, learning, and mixed workspaces.
- Create, refresh, audit-only, and best-effort modes.
- Existing-instruction drift handling.
- Progressive-disclosure authoring guidance.
- Nested `AGENTS.md` scope rules.
- Safety guidance for secrets and broad personal-corpus reads.
- Codex metadata configured for explicit user invocation.
- Example outputs and behavioral evaluation scenarios.
