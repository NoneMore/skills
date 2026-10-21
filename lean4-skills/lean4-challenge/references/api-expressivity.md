# API expressivity and information

Use for choices of types, hypotheses, codomains, and interfaces that affect what downstream mathematics can express and use.

## Search path

1. Identify intended mathematical statements and a decision-critical downstream consumer. Record which distinctions, assumptions, and invariants the consumer needs.
2. Compare representation, theorem signatures, output types, implicit parameters, and exposed laws. Determine what information each alternative preserves, forgets, or forces users to reconstruct.
3. Check existing mathlib APIs before introducing a wrapper or new general signature; specialized surfaces may have real elaboration benefits.
4. Trace one representative consumer through each live candidate when their prerequisites or expressivity differ. Do not claim compatibility for unexamined consumers.
5. Weigh elaboration, typeclass search, coercions, imports, ergonomics, and migration costs, not just signature length.

## Discriminating evidence

- Test alternative signatures in minimal scratch declarations at the **same downstream use site**.
- Use concrete boundary examples to test information loss. An `ℕ∞` result cannot distinguish different infinite cardinalities that a `Cardinal`-valued API retains; whether this matters depends on the consumer.
- Check inferred instances and theorem prerequisites with `#check` or `#synth`; distinguish tested feasibility from comparative superiority.

## Judgment and stop

Choose based on retained information, faithful assumptions, usability, inferential stability, and consumer needs. Retain a simpler API when its lost information does not matter. Stop once representative evidence resolves the choice or establishes a genuine tradeoff.

If the API issue is a symptom of a deeper [framing](mathematical-framing.md) or [theorem placement](theory-organization.md) choice, resolve that shared question rather than re-running the same probe under another label.
