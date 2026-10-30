# LaTeX Research Note Curator

A **user-invoked** Skill for creating and maintaining one user-selected, thematically coherent mathematical LaTeX research note project per invocation. Each project has a canonical root `.tex` file, may include multiple source files, and produces one internally navigable PDF. The topic bounds relevance, not depth, page count, or file count.

## Operations

- **Create:** initialize a minimal LaTeX note project from a designated theme, destination, and any supplied material, without inventing mathematical results or citations.
- **Integrate:** place new research fragments in the right mathematical context, preserve proof gaps and provenance, and add meaningful cross-file references.
- **Curate:** detect genuine overlap, clarify argument organization, and propose or apply a few high-signal connections without broad rewriting.

All three operations follow the **Note Project Contract** in [SKILL.md](SKILL.md): thematic coherence, one root and unified PDF, mathematical organization, epistemic integrity, provenance, stable references, and consistent conventions. The Skill is standalone; it requires no other Skill or custom supporting infrastructure.

## Contents

- `SKILL.md`: authoritative project contract, operations, decision policy, and verification.
- `agents/openai.yaml`: optional runtime-specific interface metadata.
- `evals/cases.md`: inspectable behavioral scenarios; not a claim that tests have been executed.

## Install

Copy the **Skill folder** into the runtime's skills directory (for Codex, `${CODEX_HOME:-$HOME/.codex}/skills/`), or configure the runtime to discover it at its repository path. Invoke it explicitly as `$latex-research-note-curator`.

The former `math-writing-editor` Skill has been removed from this repository. If you previously installed it as a separate local folder, remove that installed copy yourself; updating this repository does not automatically uninstall it.

