# Theory organization and theorem placement

Use when definitions, theorems, or module boundaries may contradict the mathematical dependency structure or impose material consumer costs.

## Search path

1. Identify the mathematical prerequisites and genericity of each relevant result independently of existing file names. Ask which layer owns the theorem and who consumes it.
2. Inspect relevant import directions and representative consumers. Look for generic results trapped in specialized modules, repeated wrappers, awkward imports, missing lower-level laws, and potential cycles.
3. Compare retaining the placement, moving a result, introducing a generic lower-level theorem, or exposing a local facade.
4. Follow **one representative dependency or composition path** across the proposed boundary; a standalone compiling theorem does not establish integration fitness.
5. Identify material affected declarations, consumer and import boundaries, and unverified risks; do not design or promise a migration workflow.

## Discriminating evidence

- Inspect a minimal relevant import graph and the requirements of one real downstream consumer.
- Use scratch files with minimal imports to check whether a lower-level owner can state or prove the candidate without circular dependencies.
- Compare current duplication, conversion and coupling costs with new abstraction, import, and migration costs.

## Judgment and stop

Prefer the narrowest placement change that repairs a consequential layering problem. Not every generic theorem belongs in the lowest imaginable module. Stop when a representative boundary resolves the placement choice; leave bulk migration for authorized execution and report untested consumers.

If placement is downstream of a [framing](mathematical-framing.md) or [reuse](abstraction-reuse.md) choice, investigate the shared governing decision first.
