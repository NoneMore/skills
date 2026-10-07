# Engine Adapter Contract

Engine adapters map the core evidence protocol and
[gameplay semantic model](gameplay-semantics.md) onto one engine, backend,
compilation mode, or runtime boundary. Keep adapters engine-specific: inherit
scope, permission, evidence states, validation rules, and mechanic closure from
`SKILL.md` instead of restating them.

Omit a section only when it is genuinely inapplicable; prefer
`Unknown / version-dependent` over invented details.

## 1. Applicability and detection

Document the exact covered boundary, mutually supporting detection indicators,
nearby modes/versions that require different treatment, and important false
positives. Do not rely on one filename when stronger corroboration is available.

## 2. Implementation model

Explain the implementation layers material to a mechanic, distinguishing primary
logic owners from supporting metadata/resource containers and identifying
engine-specific cross-layer transitions or opaque calls.

### Gameplay semantic mapping

Map applicable semantic primitives to concrete engine/runtime constructs. For
each useful mapping, state the construct/subsystem, whether it is a strong
convention or search heuristic, the strongest locating anchors, and material
version/runtime caveats. Reference the canonical model rather than repeating its
generic stages or closure rules.

## 3. Semantic anchors

List the highest-value engine-specific entry points—such as script/event names,
registration tables, symbols/RTTI/reflection, generated naming conventions,
resource identifiers, diagnostic strings, or runtime helpers—and state what
each anchor proves and does not prove.

## 4. ABI, runtime values, and object model

Document only evidence-backed conventions for signatures/calling conventions,
object representation, runtime/tagged values, field/metadata lookup, and
ownership/lifetime/reference counting. Treat non-public conventions as
version-sensitive and explain how to validate them before applying types or
writes.

## 5. Recommended tracing workflow

Give the shortest engine-specific progression from a strong anchor to the
state-changing implementation. Include only engine-specific ownership, lifetime,
shared-use, validation pivots, and transition evidence relevant to the core
layer-escalation rule; do not restate generic escalation policy, scope, or the
canonical semantic stages.

## 6. Static-analysis guidance

Document engine-specific tactics, noisy/generated patterns to collapse,
decisive instruction/data-flow evidence, false positives, and cases where broad
scanning is counterproductive.

## 7. Runtime-observation guidance

Document engine-specific observation points, value/type/version guards,
detach/restore limitations, and runtime observations that materially improve
confidence. Runtime-action permissions and generic validation criteria remain in
`SKILL.md`.

## 9. Version-sensitive assumptions

Keep a compact list of layouts, offsets, kind values, registration formats,
helper names, runtime/tool behavior, or other details that require per-version
revalidation.

## 10. Common failure modes

List mistakes specific to this boundary rather than generic reverse-engineering
or scope failures already covered by the core.

## 11. Evidence checklist

List only engine-specific evidence that supplements the core mechanic record,
evidence states, and independence rules.

## 12. Bundled tools

For bundled helpers, state what they automate, where they run, whether they
modify source/runtime state, their material version/heuristic assumptions, and
what still requires manual interpretation. Note preferred persistent or
structured interfaces only as optional optimizations. Keep helpers mechanical.

If third-party-tool recipes or volatile CLI/version details become lengthy, put
them in a focused support reference and load it only when that recovery/tooling
path is needed.
