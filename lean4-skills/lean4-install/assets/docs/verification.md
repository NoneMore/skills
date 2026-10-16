<!-- lean4-install: managed-guidance -->
# Lean Verification

Repository-specific verification policy and configured project gates take precedence over this generic guidance.

Use the lightest gate that establishes the property the task actually needs. Report which gate ran rather than collapsing all successful checks into "verified".

## Live feedback

When available, live goals and diagnostics are the preferred editing loop. They establish facts about the active source state quickly, but they do not replace dependency or project integration checks when those are material.

## File-local check

`lake env lean path/to/File.lean` runs `lean` in Lake's environment.

Use it as a fast file-local check when the imported artifacts consumed by the file are known to be current. It does not itself build changed imports, so after modifying an imported module do not treat a passing `lake env lean` check as dependency-aware verification.

## Dependency-aware file check

`lake lean path/to/File.lean` builds the imports of the given file and then runs `lean` on that source file in Lake's environment.

Prefer this after cross-file changes when the required verification scope is still one target file. It is stronger than a file-local check with respect to changed imports, but it is still not a project-wide integration gate.

## Project integration

Use the project's own build/test/lint gate when the requested scope or change surface requires integration verification. In an ordinary Lean project this is often `lake build`, but repository conventions and configured project targets take precedence.

## Trust and claims

Elaboration proves only what the checked declaration and its dependencies establish. If the task cares about axioms, `sorry`/`admit`, generated artifacts, tests, or other trust/integration properties, verify those separately rather than inferring them from a successful compile.

If the required gate cannot run, state the strongest check that did run and the property that remains unverified.
