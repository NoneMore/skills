---
name: math-paper-reader
description: Read mathematical papers and PDFs with visual checks for formulas, notation, theorem statements, proofs, equation labels, and dense derivations. Use when the user asks to understand a formula-heavy mathematical paper, interpret equations semantically, extract notation and assumptions, explain theorem or proof structure, resolve ambiguous symbols, review LaTeX/PDF math, or cite page and equation references.
---

# Math Paper Reader

Use this skill to read mathematical papers carefully, especially when formulas,
notation, theorem statements, proofs, or equation labels carry the meaning.

## Core Rules

- Prefer visual review for formulas. Render and inspect the relevant PDF pages
  before trusting extracted text, OCR, or copied LaTeX.
- Use PyMuPDF (`pymupdf` / `fitz`) as the preferred external PDF library for
  rendering pages, reading metadata, locating pages, and coarse text
  navigation.
- Use `pdfplumber`, `pypdf`, or similar libraries only as fallbacks or when a
  specific extraction feature is needed. Do not treat extracted formula text as
  authoritative.
- Build a notation ledger before interpreting important formulas.
- Tie every important claim to a page number, equation label, theorem label,
  section, or visible local context.
- Preserve ambiguity. If a symbol, index range, quantifier, convention, or
  dependency is unclear, say exactly what is unclear and what evidence would
  disambiguate it.
- Do not produce Lean declarations, leanblueprint routes, or formalization
  plans by default. Use `lean-blueprint-author` only when the user explicitly
  asks for Lean, formalization, blueprint dependencies, or proof routes.

## Workflow

1. Identify the user's reading target: whole paper, theorem, proof, equation,
   section, notation table, or ambiguity review.
2. Locate candidate pages with the table of contents, text extraction, search,
   bookmarks, or user-provided references.
3. Render and visually inspect the relevant PDF pages before transcribing or
   interpreting formulas. If the source is LaTeX rather than PDF, inspect the
   source around the target and any compiled output if available.
4. Build a notation ledger covering variables, domains, quantifiers, indices,
   assumptions, local definitions, theorem context, and equation labels.
5. For each important formula, provide:
   - location;
   - faithful transcription;
   - semantic reading in mathematical prose;
   - dependencies and local assumptions;
   - ambiguities or alternate readings.
6. Read proofs structurally: state the goal, hypotheses, key reductions,
   invoked results, hidden regularity or domain assumptions, and where each
   formula enters the argument.
7. Before finalizing, check the answer against
   `references/math-paper-reading-checklist.md`.

## Bundled References

- Read `references/formula-reading-workflow.md` when formulas, equation labels,
  or notation are central to the task.
- Read `references/math-paper-reading-checklist.md` before finalizing a dense
  paper review, theorem explanation, proof summary, or ambiguity report.

## Output Shape

Choose the smallest useful structure for the user's request. For formula-heavy
answers, prefer this shape:

```text
Location: page N, equation (X.Y)
Transcription: ...
Semantic reading: ...
Dependencies: ...
Ambiguities: ...
```

For theorem or proof explanations, include the statement context, notation
ledger, proof skeleton, formula-by-formula interpretation, and unresolved
ambiguities.
