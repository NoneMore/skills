---
name: analyze-native-binaries
description: Evidence-first static reverse engineering of native executables and libraries with IDA/idalib, Ghidra, Binary Ninja, or comparable tools. Use when Codex needs to inspect a binary or existing analysis database, locate code from symbols, strings, or addresses, recover function behavior or calling conventions, trace xrefs, callers, callees, or data flow, reconcile findings across tools or builds, or preserve target-specific discoveries as a versioned reusable analysis report.
---

# Analyze Native Binaries

Perform bounded, evidence-first static analysis. Treat decompiler output, recovered types, function boundaries, and domain-specific runtime patterns as hypotheses until independent evidence supports them. Preserve reusable target knowledge in a fingerprinted report instead of turning one binary's layout into a universal rule.

## 1. Bound the question

- Work only on targets the user is authorized to inspect.
- State the exact question, target artifact, expected output, and stop boundary before deep analysis.
- Separate analysis from implementation, patching, deployment, dynamic execution, and analysis-database mutation. Do not expand into those activities unless requested.
- Preserve the user's tool choice. Reuse a compatible existing analysis database before creating or converting one.

Complete this step when the target and the smallest sufficient answer are explicit.

## 2. Fingerprint before reusing evidence

Record the binary path, SHA-256, size, format, architecture, endianness, preferred image base, and relevant companion files. Record the analysis tool and version, database/project identity, loader settings, and analysis state.

- Reuse **Observed** findings directly only when the relevant fingerprint matches.
- Treat addresses, function boundaries, recovered types, and table layouts from another build as search leads until revalidated.
- Prefer RVA plus representative bytes over tool-generated names when correlating tools or rebased images.
- Reject an existing database when its input path, hash, architecture, or image mapping disagrees with the target.

Search for an existing report under `<project-root>/analysis/<build-id>/` before rediscovering target facts. If no project root exists, use the current task workspace as `<project-root>`.

## 3. Select the tool adapter

- For IDA or the idalib MCP, read [ida-idalib.md](references/ida-idalib.md) before invoking the tool.
- For another tool, inspect its actual callable interface, installed help, and project state before use. Map the common analysis intentions below to capabilities that really exist; do not invent command names or assume semantic parity with IDA.
- Add a new tool reference only after its workflow has been exercised and validated on real artifacts. Keep unvalidated Ghidra or Binary Ninja instructions out of this skill.

Record any unavailable capability as a limitation rather than silently switching tools. Switch tools only for a named unanswered question that another representation or analysis engine can materially answer.

## 4. Advance from shallow to focused analysis

Start at the least expensive level that can answer the question:

1. **Classify** — inspect headers, segments, imports, exports, symbols, strings, architecture, and compiler/runtime markers.
2. **Locate** — search exact symbols, strings, constants, byte patterns, or known addresses; verify each match's actual value and section.
3. **Relate** — inspect xrefs, callers, callees, adjacent data, and control-flow context.
4. **Profile** — establish function boundaries, size, complexity, references, and truncation risk before decompiling a large target.
5. **Interpret** — inspect the minimum useful disassembly, IR, or pseudocode; trace parameters, return values, state accesses, and decisive helpers.
6. **Corroborate** — confirm material conclusions with at least one independent signal such as a caller, callee, embedded string, raw instruction, data layout, or a second tool.

Do not run every level as a routine pipeline. Stop once the user's question is answered to the stated evidence boundary.

## 5. Control inference

- Distinguish exact search matches from prefix, substring, wildcard, or family matches.
- Treat executable-section xrefs, data-section xrefs, and unreferenced strings differently.
- Infer a table or structure only after checking multiple aligned entries, section membership, pointer validity, and an independent semantic relationship.
- Infer a calling convention or argument role from use sites: register/stack placement, argument-count guards, return-slot writes, callers, and forwarded values. Do not label business meaning from one arithmetic expression alone.
- Decompile small operator, conversion, or dispatch helpers when they decide the target's meaning. Prefer implementation behavior and diagnostic strings over guesses based on address proximity.
- Treat decompiler variable names, casts, recovered prototypes, and structured control flow as derived views. Check raw instructions or another representation when they carry a material claim.
- Preserve rejected and superseded hypotheses so later analyses do not repeat them.

Classify every material claim:

- **Observed** — directly supported by the exact artifact or deterministic tool output.
- **Inferred** — derived from stated observations; include confidence and a disproof condition.
- **Pending** — unresolved; name the next action or missing artifact required.

## 6. Normalize findings across tools

Before transferring a locator between IDA, Ghidra, Binary Ninja, or another tool:

1. Confirm the binary hash and architecture.
2. Normalize VA to RVA using the recorded image base; include file offset when meaningful.
3. Compare representative bytes and section membership.
4. Revalidate function boundaries and instruction mode in the destination tool.
5. Preserve each tool's recovered names and types as aliases, not ground truth.
6. Record disagreements and the evidence used to resolve or leave them pending.

Agreement between decompilers raises confidence but does not replace validation against the binary.

## 7. Preserve a reusable analysis record

Create or update a compact report when the task discovers build-specific facts, invokes a reverse-engineering tool beyond a transient lookup, produces costly output, compares tools/builds, or rejects a plausible hypothesis.

- Copy [analysis-record-template.md](assets/analysis-record-template.md) to `<project-root>/analysis/<build-id>/<target-slug>.md`.
- Store bulk pseudocode, disassembly exports, databases, projects, logs, and copied proprietary inputs under `<project-root>/.assets/<build-id>/<tool>/`.
- Keep `analysis/` reviewable and version-controlled when repository policy permits. Exclude `.assets/` from source control.
- Record exact project-relative artifact paths, tool versions, relevant invocations, and output limitations in the report.
- Do not paste an entire decompiler dump into the report. Preserve only the smallest excerpts or locators needed to support claims.

Update `analysis_revision` for the same fingerprint. Create a new build directory instead of silently overwriting a report for a different binary.

## 8. Protect analysis state

- Default to read-only investigation.
- Do not rename functions, apply types, add comments, patch bytes, rebase, rerun destructive analysis, or save derived database changes unless the user requests that mutation.
- Record automatic database changes caused by opening, upgrading, or resuming analysis when the tool exposes them.
- Keep scratch artifacts bounded. Promote useful results into the report or `.assets/` before cleanup.

## Handoff

Report the question answered, fingerprint, tool and database used, strongest observations, inferences with confidence, rejected hypotheses, artifact/report paths, compatibility boundary, and concrete pending work. State whether the analysis database was changed.
