# Code and implementation review

Establish the object being reviewed: a diff against a meaningful fixed point, a PR, or the relevant current implementation. Do not invent a diff requirement when the user wants current-state verification.

Use the expectations that actually apply. Common independent dimensions include:

- **intent / behavior**: requested behavior is present, correct, and not accompanied by material unintended scope;
- **repository constraints**: documented local standards, compatibility rules, and architectural decisions are respected;
- **regression risk**: important existing behavior, error handling, data integrity, concurrency, security, or performance is not accidentally degraded;
- **maintainability**: the change does not introduce material duplication, shotgun surgery, leaky seams, speculative abstraction, or other structural cost without corresponding value.

Treat smell language as heuristic, not a violation by itself. A documented repository rule can be a hard expectation; an architectural preference needs evidence that it creates material cost in this change.

Verify behavior directly when a material claim depends on runtime behavior and an affordable check exists. Keep findings concrete: identify the affected location or behavior, the expectation, the evidence, and the consequence.
