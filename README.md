# Skills: Curated Agent Capabilities Collection

A modular, evidence-driven, and composable collection of Agent Skills designed for modern AI coding harnesses and agentic workflows (e.g., [Pi](https://github.com/earendil-works/pi-coding-agent), [Codex](https://github.com/openai/codex), Claude Code, and compatible agent environments).

This repository provides production-grade capabilities covering the **full software engineering lifecycle**, **game logic analysis and reverse engineering**, **mathematics research and formalization**, **pragmatic engineering mental models**, and **meta-governance for agent instructions**.

---

## Table of Contents

- [Overview of Capabilities](#overview-of-capabilities)
  - [1. Execution Skills (Engineering Lifecycle)](#1-execution-skills-engineering-lifecycle)
  - [2. Matt Skills (Pragmatic Engineering & Mental Models)](#2-matt-skills-pragmatic-engineering--mental-models)
  - [3. Math Skills (Mathematical Research & Lean Formalization)](#3-math-skills-mathematical-research--lean-formalization)
  - [4. Exploration Skills (Game Logic & Reverse Engineering)](#4-exploration-skills-game-logic--reverse-engineering)
  - [5. Meta Skills (Agent Instruction Governance)](#5-meta-skills-agent-instruction-governance)
- [Repository Structure](#repository-structure)
- [Installation & Usage](#installation--usage)
- [Core Engineering Principles](#core-engineering-principles)
- [Contributing & License](#contributing--license)

---

## Overview of Capabilities

### 1. Execution Skills (Engineering Lifecycle)
> **Directory**: [`execution-skills/`](execution-skills/) | Detailed guides: [README](execution-skills/README.md) & [Chinese Guide](execution-skills/GUIDE_CN.md)

A composable engineering toolbox built for long-lived software systems. It enforces intent preservation, verified evidence loops, and systematic knowledge governance regardless of repository scale.

- **Foundations & Orchestration**:
  - `engineering-initiative-shaping`: Shapes large, ambiguous initiatives into accepted, bounded medium-capacity requirements.
  - `engineering-foundation-design`: Establishes or materially resets architectural foundations and governing contracts.
  - `engineering-plan-and-delegate`: Deliberately evaluates task decomposition and coordinates concrete handoffs across sub-agents.
  - `engineering-specification`: Drafts explicitly requested, unambiguous requirements and accepted designs.
  - `engineering-execution-planning`: Sequences dependencies, verification protocols, and coordination from accepted specifications.
- **Implementation & Review**:
  - `engineering-implementation`: High-fidelity, test-backed code authoring, bug fixing, and refactoring under explicit authorization.
  - `engineering-investigation`: Evidence-seeking diagnosis, root-cause analysis, reproducible benchmarks, and disposable experiments.
  - `engineering-review`: Read-only, multi-perspective evaluation against specifications, regressions, and operational maintenance cost.
  - `engineering-handoff`: Preserves reproducible runtime state, unblocking resumption of interrupted work across sessions.
  - `engineering-knowledge-governance`: Manages document lifecycle, canonical truth reconciliation, and decision records.

### 2. Matt Skills (Pragmatic Engineering & Mental Models)
> **Directory**: [`matt-skills/`](matt-skills/)

A comprehensive collection of agentic workflows inspired by Matt Pocock's software design philosophy, structured into global utility skills and project-level engineering workflows.

- **Global Skills**:
  - `grilling`: Relentless Socratic questioning to stress-test plans, architectures, assumptions, and critical decisions.
  - `writing-for-agents`: Guidelines and heuristics for crafting concise, unambiguous instruction manuals and prompt context for AI agents.
- **Project Workflows**:
  - `ask-matt`: High-level consulting, idiomatic architectural advice, and opinionated technical guidance.
  - `code-review`: Rigorous, adversarial code inspection focusing on readability, edge cases, and maintainability.
  - `codebase-design`: Clean domain boundary mapping and architectural layout.
  - `diagnosing-bugs`: Systematic, hypothesis-driven defect isolation and root-cause verification.
  - `domain-modeling`: Ubiquitous language definition, type-level invariants, and domain boundary design.
  - `grill-with-docs`: Document-grounded critical interrogation of proposals and specs.
  - `handoff`: Context packaging and next-step capture for seamless handoffs.
  - `implement`: Focused, disciplined implementation conforming strictly to established specs.
  - `improve-codebase-architecture`: Incremental refactoring and technical debt remediation.
  - `prototype`: Rapid proof-of-concept exploration while isolating experimental code.
  - `research`: Structured technology evaluations and tradeoff analyses.
  - `setup-matt-pocock-skills`: Workspace bootstrapping for the Matt skills suite.
  - `tdd`: Red-Green-Refactor test-driven development discipline.
  - `to-spec`: Distills ambiguous requirements into actionable, structured engineering specifications.
  - `to-tickets`: Decomposes large features into independently executable, atomic issues/tickets.
  - `wayfinder`: Regains bearing and charts recovery steps when an agent is disoriented or stalled.

### 3. Math Skills (Mathematical Research & Lean Formalization)
> **Directory**: [`math-skills/`](math-skills/) | Detailed guide: [README](math-skills/README.md)

Tailored for mathematical document processing, rigorous literature analysis, and interactive formal verification.

- `math-paper-reader`: In-depth mathematical paper deconstruction, notation ledgers, equation reference tracking, and theorem/proof sanity checks.
- `math-writing-editor`: Restructuring, copyediting, and polishing for mathematical `.tex` and `.md` documents with variable autonomy levels.
- `lean-blueprint-author`: Generates insertion-ready `leanblueprint` LaTeX architectures, proof routes, and formalization roadmaps targeting Lean 4.

### 4. Exploration Skills (Game Logic & Reverse Engineering)
> **Directory**: [`exploration-skills/`](exploration-skills/)

A disciplined protocol for authorized binary analysis and execution tracing.

- `analyze-game-logic`: Reproducible, evidence-backed static and dynamic reverse engineering of offline/single-player game logic (Windows PC, Web/JavaScript). Traces formulas, timers, internal state, and native/managed call stacks while generating verifiable audit reports. Strictly excludes multiplayer cheating, DRM bypass, or proprietary asset extraction.

### 5. Meta Skills (Agent Instruction Governance)
> **Directory**: [`meta-skills/`](meta-skills/) | Detailed guide: [README](meta-skills/agents-md-wizard/README.md)

Meta-level capabilities for authoring and optimizing how agents behave across diverse runtimes.

- `agents-md-wizard`: A workspace-agnostic wizard for generating, updating, and auditing `AGENTS.md` and related instruction files. Follows an interactive paradigm: *Inspect facts → Present choices → Ask decisions → Confirm draft → Encode behavior*, avoiding arbitrary autonomous file rewrites.

---

## Repository Structure

```text
.
├── README.md                          # Repository overview and guide
├── execution-skills/                  # Agentic Engineering Suite (v5-rc.1)
│   ├── engineering-implementation/    # Verified coding & refactoring
│   ├── engineering-investigation/     # Diagnosis & benchmarking
│   ├── engineering-review/            # Read-only verification & review
│   ├── engineering-specification/     # Precise requirements & specs
│   ├── engineering-execution-planning/# Step sequencing & acceptance
│   ├── engineering-handoff/           # Resumable session state handoffs
│   ├── engineering-knowledge-governance/# Canonical truth reconciliation
│   ├── engineering-foundation-design/ # Architectural reset & design
│   ├── engineering-plan-and-delegate/ # Decomposition & sub-agent planning
│   ├── engineering-initiative-shaping/# Macro-to-medium initiative shaping
│   ├── routing-policy.yaml            # Capacity policy & routing contracts
│   └── GUIDE_CN.md                    # Chinese supplementary handbook
├── exploration-skills/                # Reverse engineering & analysis
│   └── analyze-game-logic/            # Game state, formula & call-path tracing
├── math-skills/                       # Mathematical reading & formalization
│   └── skills/
│       ├── math-paper-reader/         # Paper interpretation & notation ledger
│       ├── math-writing-editor/       # LaTeX/Markdown notes editing
│       └── lean-blueprint-author/     # Lean 4 blueprint authoring
├── matt-skills/                       # Matt Pocock skill collection
│   ├── global/                        # Cross-project capabilities (grilling, etc.)
│   └── project/                       # Project lifecycle (tdd, implement, etc.)
└── meta-skills/                       # Agent meta-governance
    └── agents-md-wizard/              # AGENTS.md authoring & auditing wizard
```

---

## Installation & Usage

Each skill folder is designed to be self-contained and modular. You can install individual skills or complete bundles depending on your harness and needs.

### 1. Pi Agent (`~/.agents/skills/` or project `.agents/skills/`)

```bash
# Install a specific skill globally (e.g., grilling)
mkdir -p ~/.agents/skills
cp -r matt-skills/global/grilling ~/.agents/skills/

# Install the entire execution skills suite into your active workspace
mkdir -p .agents/skills
cp -r execution-skills/engineering-* .agents/skills/
```

### 2. OpenAI Codex (`~/.codex/skills/`)

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"

# Install math skills
cp -r math-skills/skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"

# Install the AGENTS.md wizard
cp -r meta-skills/agents-md-wizard "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### 3. Claude Code / Other Runtimes

Copy desired skill directories to your harness's designated skill path (e.g., `~/.claude/skills/` or `.claude/skills/`).

---

## Core Engineering Principles

1. **Intent → Feedback → Evidence**: Every material change begins with established intent, generates positive and negative evidence (tests, diffs, execution logs), and ceases when the authorized boundary is satisfied.
2. **Minimal Necessary Context**: Skills are loosely coupled. Detailed references are loaded strictly when specific triggers fire, keeping token overhead minimal.
3. **Strict Authorization Boundaries**: Tools act only within the delegated authority. Explicit orchestrations require deliberate human confirmation.
4. **Recoverable State & Clean Handoffs**: Long-horizon workflows maintain checkpoints and transparent evidence trails to withstand session interruption or handoff.

---

## Contributing & License

Contributions, new skills, and issue reports are welcome! Please ensure new skills follow the directory convention (`SKILL.md`, `evals/`, `references/`) and adhere to bounded authority patterns.

This repository is distributed under the [MIT License](LICENSE).
