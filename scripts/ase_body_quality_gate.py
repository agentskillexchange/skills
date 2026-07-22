#!/usr/bin/env python3
"""Fail-closed body quality gate for security-reviewed ASE skills.

This catches severe extraction/provenance defects that the schema validator does
not see: upstream table-of-contents fragments copied into skill bodies, malformed
Installation sections, and stale numeric GitHub-star claims in prose.
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
SAFE_INSTALL_FALLBACK = "No source-backed install or usage instructions could be extracted automatically."
RAW_INSTALL_FRAGMENT_RE = re.compile(
    r"<\s*/?\s*(?:details|summary|img|table|thead|tbody|tr|td|th)\b|"
    r"!\[[^\]]*(?:badge|shield|build|coverage|version)[^\]]*\]\([^)]*(?:shields\.io|badge|svg)[^)]*\)",
    re.I,
)
COMMAND_START_RE = re.compile(
    r"^(?:\$+\s*)?(?:brew|npm|pnpm|yarn|npx|pipx?|uv|cargo|go\s+install|"
    r"docker(?:\s+compose)?|git\s+clone|make|cmake|conda|gem|composer|python\s+-m\s+pip)\b",
    re.I,
)
INSTALL_COMMAND_RE = re.compile(
    r"^(?:\$+\s*)?(?:"
    r"brew\s+install\b|npm\s+(?:install|i|add)\b|pnpm\s+(?:add|install)\b|"
    r"yarn\s+(?:add|install)\b|npx\b|pipx\s+install\b|pip\s+install\b|"
    r"python\s+-m\s+pip\s+install\b|uv\s+(?:tool\s+install|add|pip\s+install)\b|"
    r"cargo\s+install\b|go\s+install\b|gem\s+install\b|composer\s+(?:require|install)\b|"
    r"conda\s+install\b|brew\s+tap\b|git\s+clone\b|docker\s+(?:pull|compose\s+up)\b"
    r")",
    re.I,
)
NON_INSTALL_COMMAND_RE = re.compile(
    r"^(?:\$+\s*)?(?:"
    r"npm\s+(?:run\s+)?(?:test|bench|benchmark|build|lint|dev)\b|"
    r"pnpm\s+(?:test|bench|benchmark|build|lint|dev)\b|"
    r"yarn\s+(?:test|bench|benchmark|build|lint|dev)\b|"
    r"pytest\b|make\s+(?:test|bench|benchmark|build|lint|clean|uninstall)\b|"
    r"cargo\s+(?:test|bench|build)\b|go\s+test\b|"
    r"pip\s+uninstall\b|npm\s+(?:uninstall|remove|rm)\b|brew\s+uninstall\b"
    r")",
    re.I,
)
TRUNCATED_INSTALL_RE = re.compile(r"(?:\\\s*$|&&\s*$|\|\|\s*$|\|\s*$|;\s*$)", re.I)
PROSE_AS_COMMAND_RE = re.compile(
    r"^(?:make mistakes|click here|learn more|read more|see below|table of contents|"
    r"contents|installation|features?|screenshots?|badges?)(?:\.|\s|$)",
    re.I,
)
MANUAL_SETUP_RE = re.compile(
    r"\b(?:configure|set up|setup|create|copy|add|enable|install|place|download|follow|review)\b"
    r".*\b(?:env(?:ironment)? variable|api key|credential|token|config|configuration|workspace|"
    r"skill|extension|plugin|package|upstream|source|docs?|instructions?|directory|folder|destination)\b",
    re.I,
)


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


def normalize_source_terms(fields: dict[str, Any], path: Path) -> set[str]:
    terms: set[str] = set()
    for key in ("name", "slug", "source"):
        value = str(fields.get(key) or "").lower()
        if value:
            terms.add(value)
            for part in re.split(r"[^a-z0-9@._/-]+", value):
                part = part.strip("/")
                if part.endswith(".git"):
                    part = part[:-4]
                if len(part) >= 3:
                    terms.add(part)
    terms.add(path.parent.name.lower())
    tool = fields.get("tool_ecosystem") if isinstance(fields.get("tool_ecosystem"), dict) else {}
    for key in ("github_repo", "npm_package", "parent_repo"):
        value = str(tool.get(key) or "").lower()
        if value:
            terms.add(value)
            terms.update(part for part in re.split(r"[/\s]+", value) if len(part) >= 3)
    ignored = {"skill", "agent", "agents", "github", "main", "master", "https", "http", "com", "www"}
    return {term for term in terms if term not in ignored}


def clean_install_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
    line = re.sub(r"^\s*(?:\$+\s*)", "", line)
    line = line.strip("` \t")
    line = re.sub(r"\s+", " ", line).strip()
    if re.fullmatch(
        r"(?:bash|sh|shell|console|terminal|text|markdown|md|html|json|yaml|yml|python|js|ts)",
        line,
        re.I,
    ):
        return ""
    return line


def installation_section(text: str) -> str:
    match = re.search(r"^## Installation\s*\n([\s\S]*?)(?=^##\s+|\Z)", text, re.M)
    return match.group(1).strip() if match else ""


def command_mentions_source(command: str, terms: set[str]) -> bool:
    command_l = command.lower()
    if command_l.startswith("git clone "):
        return True
    return any(term and term in command_l for term in terms)


def installation_issues(text: str, fields: dict[str, Any], path: Path) -> list[dict[str, Any]]:
    section = installation_section(text)
    if not section:
        return [{"line": 0, "text": "", "reason": "missing Installation section"}]

    verification = str(fields.get("verification") or "").strip()
    if SAFE_INSTALL_FALLBACK in section:
        if verification == "listed":
            return []
        return [{
            "line": 0,
            "text": SAFE_INSTALL_FALLBACK,
            "reason": "safe fallback requires verification listed",
        }]

    issues: list[dict[str, Any]] = []
    if RAW_INSTALL_FRAGMENT_RE.search(section) or re.search(r"<\s*a\b|<\s*/?\s*p\b|<\s*/?\s*div\b", section, re.I):
        issues.append({"line": 0, "text": "raw HTML or badge markup", "reason": "raw README/HTML fragment in Installation section"})
    if re.search(r"(?:shields\.io|badge\.svg|coverage\.svg)", section, re.I):
        issues.append({"line": 0, "text": "badge markup", "reason": "badge markup in Installation section"})

    terms = normalize_source_terms(fields, path)
    actionable = False
    install_command = False
    non_install_commands: list[str] = []
    unrelated_commands: list[str] = []
    prose_commands: list[str] = []
    truncated: list[str] = []
    duplicate_commands: list[str] = []
    seen_commands: set[str] = set()
    marketing_lines = 0
    meaningful_lines = 0

    for original in section.splitlines():
        line = clean_install_line(original)
        if not line or line.lower().startswith("source: "):
            continue
        meaningful_lines += 1
        low = line.lower()
        if TRUNCATED_INSTALL_RE.search(line):
            truncated.append(line)
        if PROSE_AS_COMMAND_RE.match(low):
            prose_commands.append(line)
        if re.search(
            r"\b(?:screenshot|feature|features|powered by|star us|community|showcase|benchmark results?|quick start)\b",
            low,
            re.I,
        ):
            marketing_lines += 1
        if COMMAND_START_RE.search(line):
            command_key = re.sub(r"\s+", " ", line.rstrip("\\").strip()).lower()
            if command_key in seen_commands:
                duplicate_commands.append(line)
            seen_commands.add(command_key)
            if NON_INSTALL_COMMAND_RE.search(line):
                non_install_commands.append(line)
                continue
            if INSTALL_COMMAND_RE.search(line):
                install_command = True
                if command_mentions_source(line, terms):
                    actionable = True
                else:
                    unrelated_commands.append(line)
                continue
            prose_commands.append(line)
            continue
        if re.search(
            r"\b(?:clone|install|copy|add|configure|bootstrap|documented installer|marketplace|mcp server)\b",
            line,
            re.I,
        ) and command_mentions_source(line, terms):
            actionable = True
            continue
        if MANUAL_SETUP_RE.search(line):
            actionable = True

    if re.search(r"\[[^\]]+\]\(#[^)]+\)", section) and not actionable:
        issues.append({"line": 0, "text": "TOC links", "reason": "only TOC/navigation links in Installation section"})
    if truncated:
        issues.append({"line": 0, "text": truncated[0], "reason": "truncated or incomplete install line"})
    if duplicate_commands:
        issues.append({"line": 0, "text": duplicate_commands[0], "reason": "duplicate install command"})
    if prose_commands:
        issues.append({"line": 0, "text": prose_commands[0], "reason": "prose or non-install text classified as command"})
    if non_install_commands and not install_command and not actionable:
        issues.append({"line": 0, "text": non_install_commands[0], "reason": "only uninstall/test/benchmark/build commands found"})
    if unrelated_commands and not actionable:
        issues.append({"line": 0, "text": unrelated_commands[0], "reason": "package/tool command is not source-aligned"})
    if meaningful_lines and marketing_lines == meaningful_lines:
        issues.append({"line": 0, "text": "marketing-only install section", "reason": "only marketing/features/screenshots/badges found"})
    if not actionable and not issues:
        issues.append({"line": 0, "text": section[:160], "reason": "no actionable installation command or manual setup instruction"})
    return issues


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
        "installation_issues": installation_issues(text, fields, path),
        "stale_star_claims": star_claims,
        "markdown_heading_bullet_warnings": heading_warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="ASE body-quality gate")
    parser.add_argument("files", nargs="*", help="SKILL.md files to scan")
    parser.add_argument("--all", action="store_true", help="Scan all skills in the repo")
    parser.add_argument(
        "--enforce-installation",
        action="store_true",
        help="Fail security_reviewed skills with malformed Installation sections. Only allowed with explicit SKILL.md paths.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON report")
    parser.add_argument("--quiet", action="store_true", help="Only print failures in text mode")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    if args.enforce_installation and args.all:
        print("--enforce-installation cannot be combined with --all; pass explicit SKILL.md paths.", file=sys.stderr)
        return 2
    if args.enforce_installation and not args.files:
        print("--enforce-installation requires explicit SKILL.md paths.", file=sys.stderr)
        return 2
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
    installation_failures = [
        item for item in security
        if item["installation_issues"]
    ] if args.enforce_installation else []
    failing = [
        item for item in security
        if item["toc_fragments"] or item["stale_star_claims"] or (args.enforce_installation and item["installation_issues"])
    ]
    warning_items = [item for item in reports if item["markdown_heading_bullet_warnings"]]
    summary = {
        "ok": not failing,
        "scanned": len(reports),
        "toc_fragment_security_reviewed_count": sum(len(item["toc_fragments"]) for item in security),
        "stale_star_claim_security_reviewed_count": sum(len(item["stale_star_claims"]) for item in security),
        "installation_issue_security_reviewed_count": sum(len(item["installation_issues"]) for item in installation_failures),
        "markdown_heading_bullet_warning_count": sum(len(item["markdown_heading_bullet_warnings"]) for item in reports),
        "affected_security_reviewed": [
            item for item in security
            if item["toc_fragments"] or item["stale_star_claims"] or (args.enforce_installation and item["installation_issues"])
        ],
        "affected_installation_security_reviewed": [
            {
                "path": item["path"],
                "slug": item["slug"],
                "installation_issues": item["installation_issues"],
            }
            for item in installation_failures
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
                "installation_issue_security_reviewed_count": summary["installation_issue_security_reviewed_count"],
                "markdown_heading_bullet_warning_count": summary["markdown_heading_bullet_warning_count"],
            }, indent=2))
        for item in failing:
            print(f"FAIL {item['path']}")
            for hit in item["toc_fragments"]:
                print(f"  TOC line {hit['line']}: {hit['text']}")
            for hit in item["stale_star_claims"]:
                print(f"  STAR line {hit['line']}: {hit['text']} (structured={hit['structured_github_stars']})")
            if args.enforce_installation:
                for hit in item["installation_issues"]:
                    print(f"  INSTALL {hit['reason']}: {hit['text']}")
    return 0 if not failing else 1


if __name__ == "__main__":
    raise SystemExit(main())
