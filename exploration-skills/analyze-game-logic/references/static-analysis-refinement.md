# Static Analysis Refinement

Load this reference when a writable disassembler/decompiler project is available
and recovered static semantics will materially improve subsequent analysis. The
goal is to turn a one-off understanding into a maintainable reverse-engineering
workspace without confusing analyst interpretation with original evidence.

## First-class refinement outputs

Refine only the material slice of the program. Useful outputs include:

- a concise statement of each material function's purpose and side effects;
- meaningful names for functions, parameters, locals, globals, and fields where
  the evidence supports them;
- recovered or improved function signatures, calling conventions, enums, partial
  structures/classes, and field offsets;
- annotations for decisive eligibility checks, state transitions, resets,
  authoritative mutations, and other key branches;
- clean C++-like semantic pseudocode that expresses the recovered mechanic with
  runtime/decompiler noise removed.

These outputs should improve the analysis database or an equivalent structured
workspace when tool access permits. A report remains useful for synthesis and
navigation, but it should not be the only place where reusable static semantics
exist.

## Preserve the evidence boundary

Raw instructions, original decompiler output, symbol/RTTI data, strings, xrefs,
and source-level artifacts remain evidence. Renames, comments, reconstructed
types, and clean pseudocode are derived interpretations.

Do not count a rewritten name or type as an independent consistency check for the
claim that motivated it. Preserve enough original evidence and stable locators to
audit or reverse a semantic annotation later.

## Confidence-aware naming and typing

Prefer names that encode only what the evidence supports. When a precise semantic
name would overstate the conclusion, use a partial or neutral name and retain the
uncertainty in a comment or finding.

Recover structures incrementally. Known offsets may coexist with unknown
`field_xxx` members. Do not invent padding semantics, inheritance, ownership, or
field meaning merely to make a structure look complete.

When a type or function signature is version-sensitive, scope it to the target
build and record the evidence that justified applying it.

## Key branch annotation

Mark branches only when their role is material to the mechanic, such as:

- eligibility or guard conditions;
- actor/source discrimination;
- timer expiry or reset;
- RNG acceptance/rejection;
- lifecycle transitions;
- the authoritative state mutation;
- shared-path filtering that affects modification scope.

The goal is navigability, not commenting every basic block.

## Clean C++-like reconstruction

Produce semantic pseudocode at the level needed to explain the mechanic. Collapse
compiler scaffolding, generated runtime-value lifetime management, redundant
temporaries, and other non-semantic noise only when doing so does not hide a
material side effect.

The reconstruction is not original source code. Preserve implementation locators
and call out material casts, ownership rules, exception/lifetime behavior, or
unknowns that were intentionally abstracted away.

## Write-back discipline

When a writable analysis database is available, apply or propose the semantic
refinements in the same focused scope used for the analysis. Do not make broad
speculative renames or type propagation across unrelated code.

If the database is read-only or write-back tooling is unavailable, emit a
structured refinement set that can be applied later rather than silently dropping
the database-level deliverable.

When project-store rules apply, retain reusable semantic conclusions as findings
and keep expensive original/generated evidence available for audit.
