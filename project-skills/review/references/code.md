# Code and implementation review

Establish the object being reviewed: a diff against a meaningful fixed point, a PR, or the relevant current implementation. Do not invent a diff requirement when the user wants current-state verification.

Use the expectations that actually apply. Common independent dimensions include:

- **intent / behavior**: requested behavior is present, correct, and not accompanied by material unintended scope;
- **repository constraints**: documented local standards, compatibility rules, and architectural decisions are respected;
- **regression risk**: important existing behavior, error handling, data integrity, concurrency, security, or performance is not accidentally degraded;
- **maintainability**: the change does not introduce material duplication, shotgun surgery, leaky seams, speculative abstraction, or other structural cost without corresponding value.

Treat smell language as heuristic, not a violation by itself. A documented repository rule can be a hard expectation; an architectural preference needs evidence that it creates material cost in this change.

When the requested scope cannot be reviewed reliably as one context, split it into coherent review units while tracking what remains unreviewed. Keep semantically coupled changes together when correctness crosses their boundary, such as interface/implementation, producer/consumer, schema/serializer, migration/model, or configuration/runtime behavior.

Use additional context to confirm or refute a concrete candidate finding. When a claim depends on code outside the visible diff, inspect the smallest relevant surrounding implementation, caller, contract, or configuration needed to resolve it; do not infer absence from a partial diff.

On a follow-up review, treat prior findings as context rather than proof: revalidate them against the current result, do not repeat findings that are gone, and do not let them replace fresh coverage of the requested scope.

Verify behavior directly when a material claim depends on runtime behavior and an affordable check exists. Keep findings concrete: identify the affected location or behavior, the expectation, the evidence, and the consequence. Anchor a finding to an exact reviewed location when it can be verified; otherwise identify the affected file or behavior without inventing line precision.
