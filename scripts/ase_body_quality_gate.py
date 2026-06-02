#!/usr/bin/env python3
"""Fail-closed body quality gate for security-reviewed ASE skills.

This catches severe extraction/provenance defects that the schema validator does
not see: upstream table-of-contents fragments copied into skill bodies and stale
numeric GitHub-star claims in prose.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

STRICT_NAV_LABELS = {
    "contents",
    "introduction",
    "installation",
    "table of contents",
}

STAR_WORD_RE = re.compile(
    r"(?P<num>\d[\d,]*(?:\.\d+)?)\s*(?P<suffix>[kKmM])?\s*\+?\s*(?:GitHub\s+)?stars?\b",
    re.I,
)
STRICT_BULLET_RE = re.compile(r"^\s*[-*]\s+(?P<label>[^#|\[\]]{1,90})\s*$")
ANY_BULLET_RE = re.compile(r"^\s*[-*]\s+(?P<label>[^|\[\]]{1,90})\s*$")
NUMBERED_TOC_RE = re.compile(r"^\s*[-*]\s+\d+(?:\.\d+)+\.?\s+[A-Z][^:]{0,90}\s*$")
DOTTED_TOC_RE = re.compile(r"^\s*(?:[-*]\s*)?\S.{0,120}?\.{3,}\s*\d{1,4}\s*$")
FORMATTED_TOC_RE = re.compile(r"^\s*[-*]\s+(?:\*\*)?table of contents(?:\*\*)?\s*:", re.I)
HEADING_BULLET_RE = re.compile(r"^\s*[-*]\s+(?:#+\s*)?(?P<label>[A-Z][A-Za-z0-9 /&()'.,:-]{2,90})\s*$")


def parse_frontmatter(text: str) -> tuple[dict[str, Any], int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, -1
    end = -1
    for idx, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end = idx
            break
    if end < 0:
        return {}, -1

    fields: dict[str, Any] = {}
    in_tool_ecosystem = False
    for line in lines[1:end]:
        if not line.startswith(" "):
            in_tool_ecosystem = False
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            raw = m.group(2).strip().strip('"').strip("'")
            if key == "tool_ecosystem":
                fields.setdefault("tool_ecosystem", {})
                in_tool_ecosystem = True
            elif raw:
                fields[key] = raw
            continue
        if in_tool_ecosystem:
            nested = re.match(r"^\s{2}([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
            if nested:
                fields.setdefault("tool_ecosystem", {})[nested.group(1)] = nested.group(2).strip().strip('"').strip("'")
    return fields, end


def as_int(value: Any) -> int | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "")
    if not text:
        return None
    try:
        return int(float(text))
    except ValueError:
        return None


def structured_stars(fields: dict[str, Any]) -> int | None:
    top = as_int(fields.get("github_stars"))
    if top is not None:
        return top
    tool = fields.get("tool_ecosystem") if isinstance(fields.get("tool_ecosystem"), dict) else {}
    return as_int(tool.get("github_stars"))


def star_claim_value(match: re.Match[str]) -> int:
    value = float(match.group("num").replace(",", ""))
    suffix = (match.group("suffix") or "").lower()
    if suffix == "k":
        value *= 1_000
    elif suffix == "m":
        value *= 1_000_000
    return int(round(value))


def star_claim_matches(claim: int, actual: int) -> bool:
    if claim == actual:
        return True
    # Prose star counts are usually rounded snapshots. Fail only when the
    # claim has materially drifted from the structured source-aligned count.
    relative_tolerance = int(round(actual * 0.10))
    if actual >= 100_000:
        return abs(claim - actual) <= max(1_000, relative_tolerance)
    if actual >= 10_000:
        return abs(claim - actual) <= max(500, relative_tolerance)
    if actual >= 1_000:
        return abs(claim - actual) <= max(100, relative_tolerance)
    return abs(claim - actual) <= max(10, relative_tolerance)


def body_start_line(fm_end: int) -> int:
    if fm_end < 0:
        return 1
    return fm_end + 2


def scan_file(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    fields, fm_end = parse_frontmatter(text)
    lines = text.splitlines()
    start = body_start_line(fm_end)
    verification = str(fields.get("verification") or "").strip()
    actual_stars = structured_stars(fields)

    toc_fragments: list[dict[str, Any]] = []
    heading_warnings: list[dict[str, Any]] = []
    for idx, line in enumerate(lines, 1):
        if idx < start:
            continue
        stripped = line.strip()
        strict = False
        reason = ""
        bullet = ANY_BULLET_RE.match(line)
        if bullet:
            label = re.sub(r"\s+", " ", bullet.group("label").strip())
            label = re.sub(r"^(?:#+\s*)+", "", label)
            label = label.strip("*_ :").lower()
            if label in STRICT_NAV_LABELS:
                strict = True
                reason = "navigation heading copied as bullet"
        if not strict and NUMBERED_TOC_RE.match(line):
            strict = True
            reason = "numbered table-of-contents fragment"
        if not strict and DOTTED_TOC_RE.match(line):
            strict = True
            reason = "dotted table-of-contents page reference"
        if not strict and FORMATTED_TOC_RE.match(line):
            strict = True
            reason = "formatted table-of-contents fragment"
        if strict:
            toc_fragments.append({"line": idx, "text": stripped, "reason": reason})
            continue
        warning = HEADING_BULLET_RE.match(line)
        if warning:
            label = re.sub(r"\s+", " ", warning.group("label").strip()).lower()
            if label in STRICT_NAV_LABELS or label.startswith(("build and run", "basic usage", "requirements")):
                heading_warnings.append({"line": idx, "text": stripped, "reason": "markdown/doc heading shaped as bullet"})

    star_claims: list[dict[str, Any]] = []
    for match in STAR_WORD_RE.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        claim = star_claim_value(match)
        ok = actual_stars is not None and star_claim_matches(claim, actual_stars)
        if actual_stars is None or not ok:
            star_claims.append({
                "line": line,
                "text": match.group(0),
                "claim": claim,
                "structured_github_stars": actual_stars,
            })

    return {
        "path": str(path),
        "slug": path.parent.name,
        "verification": verification,
        "toc_fragments": toc_fragments,
        "stale_star_claims": star_claims,
        "markdown_heading_bullet_warnings": heading_warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="ASE body-quality gate")
    parser.add_argument("files", nargs="*", help="SKILL.md files to scan")
    parser.add_argument("--all", action="store_true", help="Scan all skills in the repo")
    parser.add_argument("--json", action="store_true", help="Emit JSON report")
    parser.add_argument("--quiet", action="store_true", help="Only print failures in text mode")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    if args.all:
        targets = sorted((repo / "skills").glob("*/SKILL.md"))
    else:
        targets = [Path(item) for item in args.files]
        targets = [target if target.is_absolute() else repo / target for target in targets]
    if not targets:
        print("No files to scan.", file=sys.stderr)
        return 0

    reports = [scan_file(path) for path in targets]
    security = [item for item in reports if item["verification"] == "security_reviewed"]
    failing = [
        item for item in security
        if item["toc_fragments"] or item["stale_star_claims"]
    ]
    warning_items = [item for item in reports if item["markdown_heading_bullet_warnings"]]
    summary = {
        "ok": not failing,
        "scanned": len(reports),
        "toc_fragment_security_reviewed_count": sum(len(item["toc_fragments"]) for item in security),
        "stale_star_claim_security_reviewed_count": sum(len(item["stale_star_claims"]) for item in security),
        "markdown_heading_bullet_warning_count": sum(len(item["markdown_heading_bullet_warnings"]) for item in reports),
        "affected_security_reviewed": [
            item for item in security if item["toc_fragments"] or item["stale_star_claims"]
        ],
        "warning_items": warning_items,
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        if not args.quiet or failing:
            print(json.dumps({
                "ok": summary["ok"],
                "toc_fragment_security_reviewed_count": summary["toc_fragment_security_reviewed_count"],
                "stale_star_claim_security_reviewed_count": summary["stale_star_claim_security_reviewed_count"],
                "markdown_heading_bullet_warning_count": summary["markdown_heading_bullet_warning_count"],
            }, indent=2))
        for item in failing:
            print(f"FAIL {item['path']}")
            for hit in item["toc_fragments"]:
                print(f"  TOC line {hit['line']}: {hit['text']}")
            for hit in item["stale_star_claims"]:
                print(f"  STAR line {hit['line']}: {hit['text']} (structured={hit['structured_github_stars']})")
    return 0 if not failing else 1


if __name__ == "__main__":
    raise SystemExit(main())
