# API expressivity and information

Use when type choices, hypotheses, codomains, or exposed laws change what consumers can express.

- Identify what a representative downstream theorem actually needs to distinguish, infer, or reconstruct.
- Test competing signatures at the **same consumer**, including necessary instances, coercions, and imports; consult existing mathlib APIs first.
- Probe information loss with boundary cases. For example, an `ℕ∞`-valued result cannot distinguish different infinite cardinalities retained by a `Cardinal`-valued result; this matters only if consumers need that distinction.
- Balance expressive power against complexity, elaboration stability, and specialized API convenience; a more general signature is not automatically better.
