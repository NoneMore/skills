# Web / JavaScript Recovery Tooling

Load this reference only when the Web/JavaScript adapter requires bundle
recovery, deobfuscation, formatting, source-map extraction, or detailed operation
of `scripts/web_js_triage.py`. The engine adapter remains authoritative for
gameplay semantics and evidence boundaries.

## Tool roles

Prefer original readable source or a verified source map when available. When
transformation is needed:

- **webcrack**: use for clear obfuscator-style transforms or deobfuscation needs;
  it can also unpack supported webpack/Browserify bundles.
- **Wakaru**: use for production-JS recovery and bundle decomposition. It is not
  a general-purpose deobfuscator.
- **Prettier**: formatting only; it does not recover or validate semantics.

Do not force one linear pipeline if a transform destroys structure needed by
another. Running tools independently on the original bundle can preserve
different useful structure, but those views still derive from the same evidence
and are not independent semantic checks. Retain the clearest useful view by
default; keep alternatives only when they preserve materially distinct,
easy-to-lose information.

Source-map matching, provenance, and association-strength rules remain in
[engine-web-javascript.md](engine-web-javascript.md) §6; do not duplicate them
here.

## webcrack

Run outputs outside the original game tree and record the actual Node/webcrack
versions used.

```bash
webcrack bundle.js -o <artifacts>/webcrack
webcrack input.js > <artifacts>/webcrack.js
```

Process entry bundles, lazy chunks, and workers as distinct inputs; one unpack
does not necessarily reconstruct a dynamic chunk graph. A failed unpack is a
tool-capability result, not evidence that the input is not bundled; wrappers or
unsupported bundler variants may defeat detection. Generated variable names are
not recovered originals without separate support.

Do not pre-create the webcrack `-o` leaf directory unless the invocation
deliberately uses the tool's overwrite semantics.

When analyzing untrusted code, use a constrained environment without secrets and
preferably without network access because deobfuscation may use code-evaluation
mechanisms.

## Wakaru

`--unpack=inspect` is useful for finer module decomposition;
`--unpack=strict` avoids heuristic fallback when ambiguous splits would be
misleading. `--source-map` can improve name recovery, and `wakaru extract`
can recover embedded `sourcesContent`.

```bash
wakaru bundle.js --unpack=inspect -o <artifacts>/wakaru
wakaru input.js --source-map input.js.map -o <artifacts>/wakaru-source-aware.js
wakaru extract input.js.map -o <artifacts>/sourcemap-sources
```

Inspection-oriented decomposition may not preserve executable initialization
order. Trace order-sensitive claims to the original bundle or another
order-preserving representation. Use aggressive/speculative rewrites only when
needed and record the choice.

## Prettier

Never format original evidence in place. Format a generated copy:

```bash
prettier --write --no-config --no-editorconfig <generated-copy>
```

Record the formatter version when line-based locators depend on its output.
Prefer module/function/AST-structural locators for durable findings.

## Versioning

Record the actual tool and runtime versions used in each analysis. Treat
third-party compatibility and behavior as version-sensitive rather than relying
on documentation snapshots.

## Bundled orchestrator

`scripts/web_js_triage.py` accepts JS/TS files or directories and creates
stable isolated analysis IDs. It hashes material inputs, source maps, and
retained generated artifacts; records map-association strength; resolves
installed webcrack/Wakaru/Prettier commands (or pinned `npx` packages only when
explicitly enabled); and writes a `triage-manifest.json` containing status,
commands, versions, hashes, provenance, associations, outcomes, and generated
paths.

Default `--retention lean` uses temporary staging and promotes a canonical
recovery view, retaining webcrack output only when obvious obfuscation is
detected or `--force-webcrack` is requested. `--retention all` keeps parallel
raw recovery views for difficult comparison work. Failed/timeout logs are kept
for diagnosis; successful routine logs need not become durable evidence.

`--force` removes only helper-managed outputs from a recognizable prior run.
The helper refuses to guess ownership of pre-existing managed-looking paths. It
returns non-zero when no analyzer step can run.

The helper never edits input bundles/maps, executes the game, or contacts a
service. Electron `app.asar` is detected only as a container indicator; expose
authorized contents before routing them through the helper.

Examples:

```bash
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py game.bundle.js --source-map game.bundle.js.map \
  --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py dist/ --out <analysis-root>/artifacts/js-triage
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage \
  --allow-npx
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage \
  --force-webcrack
python scripts/web_js_triage.py game.bundle.js --out <analysis-root>/artifacts/js-triage \
  --retention all
python scripts/web_js_triage.py --self-test
```

Generated recovery output is working evidence. It does not establish mechanic
ownership or independently validate a gameplay claim.
