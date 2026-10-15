# Lean JSON Patterns

Use when constructing, encoding, or inspecting `Lean.Json` values.

## Construction choices

- Use `json%` syntax for mostly static JSON structure with value antiquotation.
- Use `Json.mkObj` when keys are computed dynamically.
- Use `ToJson` instances to encode project data rather than hand-building every nested value.

Verify exact elaborator syntax against the active Lean toolchain when working near version-sensitive JSON macros.

## Static skeleton with values

```lean
import Lean.Data.Json
open Lean

def payload (name : String) (count : Nat) : Json :=
  json%{name: $name, count: $count}
```

Antiquotations require a suitable `ToJson` instance. If a field is already `Json`, embedding it should preserve that value rather than double-encoding a string representation.

## Dynamic keys

`json%` is best for static object keys. For computed keys, build the object explicitly:

```lean
Json.mkObj [(key, toJson value)]
```

Be aware that object implementations may canonicalize or collapse duplicate keys; do not rely on insertion duplicates as meaningful data.

## Debugging

When elaboration fails, distinguish:

- invalid JSON macro syntax;
- missing `ToJson` instances;
- a dynamic-key requirement that should use `Json.mkObj`;
- a value whose serialized representation differs from the intended external schema.

Validate the produced JSON value/schema, not just Lean elaboration.
