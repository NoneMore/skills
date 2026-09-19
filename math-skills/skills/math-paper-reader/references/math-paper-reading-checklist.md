# Math Paper Reading Checklist

Use this checklist before finalizing formula, theorem, proof, or ambiguity
reviews.

## Source Handling

- Relevant PDF pages were rendered and visually inspected when a PDF is
  available.
- Text extraction was used only for navigation or search, not as the source of
  formula truth.
- Page numbers, theorem labels, section labels, and equation labels match the
  rendered source.
- Any missing rendering dependency or unavailable source page is disclosed.

## Notation

- Main symbols have ledger entries with domains or ambient spaces.
- Quantifiers, fixed parameters, variables, and index ranges are identified.
- Local assumptions needed for the requested formulas are recorded.
- Overloaded notation or scope changes are called out.
- The explanation does not introduce unsupported notation.

## Formula Interpretation

- Each important formula has a location, transcription, semantic reading,
  dependencies, and ambiguity notes when needed.
- Superscripts, subscripts, primes, bars, hats, bold symbols, and Greek letters
  were checked visually.
- The formula's role is clear: definition, hypothesis, conclusion, estimate,
  recurrence, identity, construction, or proof step.
- Hidden well-definedness obligations are identified when relevant.

## Proof And Theorem Reading

- The theorem statement is separated from the proof route.
- Hypotheses and conclusions are stated explicitly.
- Displayed formulas are connected to their proof roles.
- Cited or standard results are distinguished from arguments supplied in the
  paper.
- Gaps, omitted justifications, and ambiguous dependencies are reported without
  overstating certainty.

## Output

- The answer stays focused on the user's requested paper region or question.
- Ambiguities are preserved rather than guessed away.
- No Lean, formalization, or leanblueprint output is produced unless explicitly
  requested.
