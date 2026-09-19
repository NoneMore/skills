"""Read-only IDAPython triage for GameMaker YYC binaries.

Run inside an existing IDA database. The script prints string, metadata-field,
function, and candidate RValue evidence. It does not rename, comment, patch, or
save the database.

The helper intentionally uses Python 3.8-compatible syntax for older IDAPython
installations. Output is bounded independently by string count, xrefs per anchor,
and a global record budget.
"""

import argparse
import math
import struct
import sys
from dataclasses import dataclass
from typing import List, Optional, Sequence, Set, Tuple


@dataclass(frozen=True)
class DecodedRValue:
    raw_hex: str
    payload_u64: int
    payload_f64: float
    aux: int
    kind: int


class OutputBudget:
    """Global cap for emitted evidence records.

    Headings and final summaries are not records. Semantic strings, markers,
    descriptor probes, xrefs, and RValue probes are records.
    """

    def __init__(self, maximum: int) -> None:
        self.maximum = maximum
        self.used = 0
        self.truncated = False

    def consume(self) -> bool:
        if self.used >= self.maximum:
            self.truncated = True
            return False
        self.used += 1
        return True

    @property
    def exhausted(self) -> bool:
        return self.used >= self.maximum


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_integer(text: str) -> int:
    return int(text, 0)


def positive_integer(text: str) -> int:
    value = int(text, 0)
    if value <= 0:
        raise argparse.ArgumentTypeError("value must be a positive integer")
    return value


def is_data_xref(xref: object) -> bool:
    # idautils.XrefsTo() exposes `iscode`; descriptor metadata probing only
    # makes sense when the string is referenced from data, not from an
    # instruction address. Treat a missing attribute conservatively.
    return not bool(getattr(xref, "iscode", True))


def decode_rvalue(raw: bytes) -> DecodedRValue:
    if len(raw) != 16:
        raise ValueError("RValue probe requires exactly 16 bytes, got %d" % len(raw))
    payload_u64, aux, kind = struct.unpack("<QII", raw)
    payload_f64 = struct.unpack("<d", raw[:8])[0]
    return DecodedRValue(raw.hex(" "), payload_u64, payload_f64, aux, kind)


def run_self_test() -> None:
    raw = struct.pack("<dII", 210.0, 0, 0)
    decoded = decode_rvalue(raw)
    require(decoded.payload_u64 == struct.unpack("<Q", raw[:8])[0], "payload_u64")
    require(decoded.payload_f64 == 210.0, "payload_f64")
    require(decoded.aux == 0, "aux")
    require(decoded.kind == 0, "kind")
    require(parse_integer("0x20") == 32, "parse_integer")
    require(positive_integer("1") == 1, "positive_integer decimal")
    require(positive_integer("0x20") == 32, "positive_integer hex")

    for invalid in ("0", "-1"):
        try:
            positive_integer(invalid)
        except argparse.ArgumentTypeError:
            pass
        else:
            raise AssertionError("positive_integer accepted %r" % invalid)

    class DummyXref:
        def __init__(self, iscode: bool) -> None:
            self.iscode = iscode

    require(is_data_xref(DummyXref(False)), "data xref")
    require(not is_data_xref(DummyXref(True)), "code xref")
    require(not is_data_xref(object()), "missing iscode")

    budget = OutputBudget(2)
    require(budget.consume(), "budget record 1")
    require(budget.consume(), "budget record 2")
    require(not budget.consume(), "budget overflow")
    require(budget.truncated, "budget truncated flag")
    print("yyc_triage self-test: OK")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only GameMaker YYC string/xref/RValue triage for IDA"
    )
    parser.add_argument(
        "--term",
        action="append",
        default=[],
        help="case-insensitive string term to find; repeat as needed",
    )
    parser.add_argument(
        "--gml-markers",
        action="store_true",
        help="list gml_Script_* and gml_Object_* string markers",
    )
    parser.add_argument(
        "--descriptor-id-offset",
        type=parse_integer,
        default=8,
        help="heuristic runtime-ID field offset from a direct data xref (default: 8)",
    )
    parser.add_argument(
        "--rvalue",
        action="append",
        default=[],
        type=parse_integer,
        help="candidate 16-byte RValue address to decode; repeat as needed",
    )
    parser.add_argument(
        "--max-strings",
        type=positive_integer,
        default=200,
        help="maximum semantic strings or GML markers printed per scan (default: 200)",
    )
    parser.add_argument(
        "--max-xrefs-per-anchor",
        type=positive_integer,
        default=50,
        help="maximum xrefs printed for one string/field/RValue anchor (default: 50)",
    )
    parser.add_argument(
        "--max-total-records",
        type=positive_integer,
        default=2000,
        help="global cap across strings, markers, probes, and xrefs (default: 2000)",
    )
    parser.add_argument(
        "--limit",
        type=positive_integer,
        default=None,
        help=(
            "legacy compatibility shorthand: set --max-strings and "
            "--max-xrefs-per-anchor to the same value"
        ),
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run pure-Python decoder/budget tests without importing IDA modules",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        run_self_test()
        return 0

    if args.limit is not None:
        args.max_strings = args.limit
        args.max_xrefs_per_anchor = args.limit

    try:
        import ida_auto
        import ida_bytes
        import ida_funcs
        import ida_kernwin
        import ida_nalt
        import idautils
    except ModuleNotFoundError as exc:
        parser.error("IDA modules are required unless --self-test is used: %s" % exc)

    ida_auto.auto_wait()
    image_base = ida_nalt.get_imagebase()
    budget = OutputBudget(args.max_total_records)

    terms = [term.strip() for term in args.term if term.strip()]
    if not terms and not args.gml_markers and not args.rvalue:
        entered = ida_kernwin.ask_str(
            "",
            0,
            "YYC semantic search terms (comma-separated)",
        )
        if entered:
            terms = [term.strip() for term in entered.split(",") if term.strip()]

    if not terms and not args.gml_markers and not args.rvalue:
        print("No terms, marker scan, or RValue addresses supplied.")
        parser.print_help()
        return 2

    def format_address(ea: int) -> str:
        return "%#x (module+%#x)" % (ea, ea - image_base)

    def function_owner(ea: int) -> str:
        func = ida_funcs.get_func(ea)
        if func is None:
            return "<no function>"
        name = ida_funcs.get_func_name(func.start_ea) or "<unnamed>"
        return "%s@%s" % (name, format_address(func.start_ea))

    def limited_xrefs_to(ea: int) -> Tuple[List[object], bool]:
        refs = []
        truncated = False
        for xref in idautils.XrefsTo(ea):
            if len(refs) >= args.max_xrefs_per_anchor:
                truncated = True
                break
            refs.append(xref)
        return refs, truncated

    def note_budget() -> None:
        if budget.exhausted:
            budget.truncated = True
        if budget.truncated:
            print(
                "\n[YYC] global record budget reached: %d/%d; remaining evidence omitted"
                % (budget.used, budget.maximum)
            )
            budget.truncated = False  # print the notice at most once

    if terms and not budget.exhausted:
        print("\n[YYC] semantic string scan, terms=%r" % terms)
        lowered = [term.casefold() for term in terms]
        match_count = 0
        probed_fields: Set[int] = set()

        for item in idautils.Strings():
            if budget.exhausted or match_count >= args.max_strings:
                break
            value = str(item)
            if not any(term in value.casefold() for term in lowered):
                continue

            if not budget.consume():
                break
            match_count += 1
            print("\nSTRING %s: %r" % (format_address(item.ea), value))
            direct_refs, direct_truncated = limited_xrefs_to(item.ea)
            if not direct_refs:
                print("  no direct xrefs")

            for xref in direct_refs:
                if not budget.consume():
                    break
                print(
                    "  direct xref %s type=%s owner=%s"
                    % (format_address(xref.frm), xref.type, function_owner(xref.frm))
                )

                if not is_data_xref(xref):
                    continue

                candidate_field = xref.frm + args.descriptor_id_offset
                if candidate_field in probed_fields:
                    continue
                probed_fields.add(candidate_field)
                field_refs, field_truncated = limited_xrefs_to(candidate_field)
                if field_refs:
                    if not budget.consume():
                        break
                    print(
                        "    heuristic descriptor-ID field from data xref %s:"
                        % format_address(candidate_field)
                    )
                    for field_xref in field_refs:
                        if not budget.consume():
                            break
                        print(
                            "      code/data xref %s type=%s owner=%s"
                            % (
                                format_address(field_xref.frm),
                                field_xref.type,
                                function_owner(field_xref.frm),
                            )
                        )
                    if field_truncated and not budget.exhausted:
                        print(
                            "      xrefs truncated at --max-xrefs-per-anchor=%d"
                            % args.max_xrefs_per_anchor
                        )

            if direct_truncated and not budget.exhausted:
                print(
                    "  direct xrefs truncated at --max-xrefs-per-anchor=%d"
                    % args.max_xrefs_per_anchor
                )

        if match_count >= args.max_strings:
            print("\nstring match limit reached (%d)" % args.max_strings)
        print("\n[YYC] semantic strings printed: %d" % match_count)
        note_budget()

    if args.gml_markers and not budget.exhausted:
        print("\n[YYC] native GML markers")
        marker_count = 0
        for item in idautils.Strings():
            if budget.exhausted or marker_count >= args.max_strings:
                break
            value = str(item)
            if not (value.startswith("gml_Script_") or value.startswith("gml_Object_")):
                continue
            if not budget.consume():
                break
            marker_count += 1
            print("\nMARKER %s: %s" % (format_address(item.ea), value))
            refs, refs_truncated = limited_xrefs_to(item.ea)
            for xref in refs:
                if not budget.consume():
                    break
                print(
                    "  xref %s type=%s owner=%s"
                    % (format_address(xref.frm), xref.type, function_owner(xref.frm))
                )
            if refs_truncated and not budget.exhausted:
                print(
                    "  xrefs truncated at --max-xrefs-per-anchor=%d"
                    % args.max_xrefs_per_anchor
                )

        if marker_count >= args.max_strings:
            print("\nmarker limit reached (%d)" % args.max_strings)
        print("\n[YYC] GML markers printed: %d" % marker_count)
        note_budget()

    for ea in args.rvalue:
        if budget.exhausted:
            break
        if not budget.consume():
            break
        raw = ida_bytes.get_bytes(ea, 16)
        print("\nRVALUE %s" % format_address(ea))
        if raw is None or len(raw) != 16:
            print("  unable to read 16 bytes")
            continue
        decoded = decode_rvalue(raw)
        f64 = decoded.payload_f64
        f64_text = repr(f64) if math.isfinite(f64) else str(f64)
        print("  raw: %s" % decoded.raw_hex)
        print("  payload_u64: %d" % decoded.payload_u64)
        print("  payload_f64: %s" % f64_text)
        print("  aux: %#x" % decoded.aux)
        print("  kind: %#x" % decoded.kind)
        refs, refs_truncated = limited_xrefs_to(ea)
        printed_refs = 0
        for xref in refs:
            if not budget.consume():
                break
            printed_refs += 1
            print(
                "    %s type=%s owner=%s"
                % (format_address(xref.frm), xref.type, function_owner(xref.frm))
            )
        suffix = " (truncated)" if refs_truncated or printed_refs < len(refs) else ""
        print("  direct xrefs printed: %d%s" % (printed_refs, suffix))

    note_budget()
    print("\n[YYC] evidence records emitted: %d/%d" % (budget.used, budget.maximum))
    print("[YYC] read-only triage complete")
    return 0


if __name__ == "__main__":
    # IDAPython treats SystemExit(0) as a script failure in batch mode.
    # argparse still reports genuine argument errors with a non-zero exit.
    main(sys.argv[1:])
