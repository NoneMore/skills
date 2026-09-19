# Formula Reading Workflow

Use this reference when the task depends on accurate interpretation of
displayed mathematics, equation labels, dense notation, or a proof derivation.

## Visual First

Render the relevant PDF pages before transcribing formulas. Use extracted text
only to find candidate pages, section headings, theorem labels, or equation
labels.

Prefer PyMuPDF (`pymupdf` / `fitz`) for PDF operations:

- render relevant pages to images for visual inspection;
- read metadata, page counts, and page dimensions;
- search or extract coarse text for navigation.

Use `pdfplumber`, `pypdf`, Poppler, or other tools only as fallbacks or for a
specific capability PyMuPDF does not cover well enough for the task.

Preferred local rendering pattern:

```python
import fitz

doc = fitz.open("input.pdf")
page = doc[page_index]
pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
pix.save("tmp/paper-pages/page-001.png")
```

Poppler fallback:

```sh
pdftoppm -png input.pdf tmp/paper-pages/page
```

Inspect the rendered pages directly. Confirm subscripts, superscripts, primes,
bars, hats, calligraphic letters, bold symbols, Greek letters, fraction
structure, delimiters, and multi-line alignment from the rendered image, not
from extracted text.

If rendering is unavailable, tell the user which dependency is missing and
continue only with a caveat that formula fidelity is limited.

## Notation Ledger

Create the ledger before interpreting formulas. Capture only notation that is
used in the requested target or nearby dependencies.

For each symbol or family, record:

- symbol as rendered;
- verbal name or role;
- domain, codomain, type, or ambient space;
- quantifiers and fixed-versus-variable status;
- index ranges and summation/product conventions;
- assumptions such as smoothness, integrability, measurability, positivity,
  compactness, boundary conditions, or normalization;
- local definition, equation label, theorem label, or page where introduced;
- overloaded meanings or changes across sections.

When a paper uses the same symbol in multiple roles, keep separate ledger
entries with scope notes.

## Formula Pass

For every important displayed formula:

1. Record location: page, section, theorem, proof paragraph, and equation label.
2. Transcribe faithfully enough for discussion. Keep line breaks if they affect
   alignment or dependencies.
3. Identify the formula type: definition, hypothesis, conclusion, recurrence,
   estimate, identity, inequality, asymptotic, construction, or proof step.
4. Read the formula semantically in prose. Explain what mathematical relation
   it asserts, not just how to pronounce symbols.
5. List local dependencies: definitions, assumptions, previous equations,
   theorem hypotheses, cited results, or conventions needed for the formula to
   make sense.
6. Note hidden obligations: domains of composition, convergence, well-defined
   denominators, boundary terms, integrability, measurability, differentiability,
   sign conditions, and compatibility of indices.
7. Flag ambiguities and give the most likely reading with evidence.

## Proof Reading

For theorem/proof tasks, separate statement interpretation from proof
interpretation.

Statement pass:

- identify all hypotheses and conclusions;
- expand local notation needed to parse the statement;
- distinguish global assumptions from theorem-local assumptions;
- explain any quantified objects and their dependencies.

Proof pass:

- state the proof goal in plain mathematical language;
- break the proof into reductions or cases;
- map each displayed equation to its role in the argument;
- identify cited results, imported lemmas, or "standard" facts;
- mark steps that depend on omitted regularity, compactness, convergence, or
  algebraic closure arguments;
- separate what is explicitly proved from what is asserted or cited.

## Ambiguity Handling

Do not silently normalize unclear math. Common ambiguity sources include:

- visually similar symbols such as `l`, `1`, `I`, `O`, `0`, `o`, `nu`, and `v`;
- missing index ranges or implicit quantifiers;
- overloaded notation across sections;
- equation references extracted incorrectly;
- minus signs versus hyphens in OCR;
- subscripts that may be text labels rather than variables;
- transpose, adjoint, closure, complement, and dual notation;
- asymptotic notation whose limiting variable is implicit.

Report the ambiguity with the local evidence and the consequence for the
interpretation.
