# IDA and idalib Tool Card

Use this card for IDA databases accessed through the idalib MCP. Adapt argument shapes only to the tools actually exposed in the current session. Record the server/tool version when available.

## Open or resume the correct database

1. Call `idb_list` to discover adopted or running sessions. Treat an empty list only as “no discovered session,” not as proof that no `.i64` or `.idb` exists.
2. Inspect the target directory read-only when needed to identify an existing database. Treat its existence as a reuse candidate, not proof that automatic analysis completed.
3. Call `idb_open` with the exact input binary path. Prefer adopting the database chosen by idalib rather than opening a second copy manually.
4. Validate the returned input path, `idb_path`, module, image base, analysis state, Hex-Rays readiness, and string-cache readiness. Use `server_health` when the open result does not provide enough state.
5. Record cache warmup or analysis delay. Do not issue dependent queries while the server reports active analysis or an unready decompiler.

Use `auto_analysis_ready` or the current server's equivalent as the readiness signal. Do not infer readiness solely from database size or modification time.

## Classify without flooding context

- Use `survey_binary` only when the question requires a broad inventory. Its output can be large and truncated.
- For a narrow target, prefer focused segment, import, string, symbol, or function queries.
- Record truncation explicitly; absence from a truncated survey is not negative evidence.

## Locate a target

1. Use `find` or `find_regex` for strings and patterns.
2. Resolve returned addresses with `get_string` before calling a result an exact match. A string search may return suffix, prefix, substring, or family matches.
3. Use `lookup_funcs` for existing IDA function names or addresses. Do not assume a runtime string is also an IDA function name in a stripped binary.
4. Use `xrefs_to` on the exact string, data, or address. Separate xrefs inside functions from data-only references.
5. Prefer a direct code xref containing the target marker as a strong function candidate. Treat data-table relationships as inferred until multiple entries and independent evidence agree.
6. Use `get_bytes` and `get_string` to inspect bounded table context. Decode pointer width and endianness from the binary fingerprint rather than assuming them.

## Triage a function before decompiling it

- Use `func_profile` to capture boundaries, size, instruction/basic-block counts, callers, callees, strings, constants, and list truncation.
- Use `disasm` for prologues, call sites, short ranges, instruction-level evidence, or suspicious decompiler output.
- Use `decompile` for one function address at a time. The validated interface treated a serialized list of addresses as one invalid address; issue separate calls instead.
- Decompile small decisive helpers before reading an entire large target when an operator, conversion, dispatch, or ownership routine determines the answer.
- Inspect representative callers when assigning parameter roles or business meaning.

## Handle large results

When an idalib result is truncated and returns a local full-output URL:

1. Validate that the URL is the loopback endpoint returned by the tool.
2. Fetch it promptly to the task's ignored analysis-assets directory.
3. Bypass proxies only for loopback hosts, for example:

```bash
curl --fail --show-error --silent \
  --noproxy 127.0.0.1,localhost \
  -o <output.json> \
  http://127.0.0.1:<port>/output/<id>.json
```

4. Verify HTTP success, non-zero size, valid JSON, target address, and expected output field before using it.
5. Extract or search only the portions needed for the named question. Do not load a full decompiler dump into context merely because it is available.

If the request returns an empty file, inspect the HTTP status and proxy use before repeating the decompilation. Never disable proxies globally to reach a loopback endpoint.

## Corroborate IDA conclusions

- Pair pseudocode claims with relevant raw instructions, xrefs, embedded strings, callers/callees, or bytes.
- Treat IDA-generated `sub_*` names, guessed prototypes, stack variables, and types as aliases or hypotheses.
- Record VA, RVA, image base, section, and representative bytes for findings that may be opened in another tool.
- Note whether Hex-Rays output, lists, surveys, or tool serialization were truncated.

## Keep the database read-only by default

Do not rename, comment, apply types, patch bytes, rebase, or save new database state unless requested. If opening or upgrading the IDB changes persistent state, record the affected database and backup/recovery status in the analysis report.
