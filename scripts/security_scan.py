#!/usr/bin/env python3
"""Executable security pattern scanner for Agent Skill Exchange content."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

FLAG_MAP = {
    "i": re.IGNORECASE,
    "m": re.MULTILINE,
    "s": re.DOTALL,
}


@dataclass(frozen=True)
class Pattern:
    id: str
    klass: str
    severity: str
    regex: str
    flags: str
    compiled: re.Pattern[str]


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    pattern_id: str
    klass: str
    severity: str
    excerpt: str


def github_escape(value: str) -> str:
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A").replace(":", "%3A").replace(",", "%2C")


def compile_flags(raw: str) -> int:
    flags = 0
    for char in raw:
        try:
            flags |= FLAG_MAP[char]
        except KeyError as exc:
            raise ValueError(f"unsupported regex flag {char!r}") from exc
    return flags


def load_patterns(path: Path) -> list[Pattern]:
    data = json.loads(path.read_text(encoding="utf-8"))
    raw_patterns = data.get("patterns")
    if not isinstance(raw_patterns, list):
        raise ValueError(f"{path} must contain a top-level patterns list")

    patterns: list[Pattern] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_patterns, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"pattern #{index} must be an object")
        for field in ("id", "class", "severity", "regex"):
            if not isinstance(raw.get(field), str) or not raw[field].strip():
                raise ValueError(f"pattern #{index} has invalid {field!r}")
        pattern_id = raw["id"]
        if pattern_id in seen:
            raise ValueError(f"duplicate pattern id: {pattern_id}")
        seen.add(pattern_id)
        flags = raw.get("flags", "")
        if not isinstance(flags, str):
            raise ValueError(f"pattern {pattern_id} flags must be a string")
        try:
            compiled = re.compile(raw["regex"], compile_flags(flags))
        except re.error as exc:
            raise ValueError(f"pattern {pattern_id} has invalid regex: {exc}") from exc
        patterns.append(
            Pattern(
                id=pattern_id,
                klass=raw["class"],
                severity=raw["severity"],
                regex=raw["regex"],
                flags=flags,
                compiled=compiled,
            )
        )
    return patterns


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def excerpt(value: str, max_len: int = 140) -> str:
    compact = re.sub(r"\s+", " ", value).strip()
    if len(compact) <= max_len:
        return compact
    return compact[: max_len - 1] + "…"


def scan_text(text: str, path: Path, patterns: Iterable[Pattern]) -> list[Finding]:
    findings: list[Finding] = []
    for pattern in patterns:
        for match in pattern.compiled.finditer(text):
            findings.append(
                Finding(
                    path=path,
                    line=line_number(text, match.start()),
                    pattern_id=pattern.id,
                    klass=pattern.klass,
                    severity=pattern.severity,
                    excerpt=excerpt(match.group(0)),
                )
            )
    return findings


def discover_files(inputs: Iterable[str]) -> list[Path]:
    files: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        else:
            files.append(path)
    return files


def print_findings(findings: list[Finding], github_annotations: bool) -> None:
    for finding in findings:
        message = f"{finding.pattern_id} [{finding.severity}/{finding.klass}] matched: {finding.excerpt}"
        if github_annotations:
            print(
                f"::error file={github_escape(str(finding.path))},line={finding.line},"
                f"title=ASE security scan::{github_escape(message)}"
            )
        print(f"❌ {finding.path}:{finding.line}: {message}")


def default_patterns_path() -> Path:
    return Path(__file__).resolve().parent.parent / "verification" / "patterns.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scan ASE markdown files with executable security patterns.")
    parser.add_argument("paths", nargs="*", help="Files or directories to scan")
    parser.add_argument("--all", action="store_true", help="Scan skills, verification docs, scripts docs, and top-level markdown")
    parser.add_argument("--patterns", default=str(default_patterns_path()), help="Pattern JSON file")
    parser.add_argument("--github-annotations", action="store_true", help="Emit GitHub Actions annotations")
    parser.add_argument("--quiet", action="store_true", help="Only print findings and summary")
    args = parser.parse_args(argv)

    patterns = load_patterns(Path(args.patterns))
    inputs = list(args.paths)
    if args.all:
        inputs.extend(["skills", "verification", "scripts"])
        inputs.extend(str(path) for path in Path(".").glob("*.md"))
    if not inputs:
        parser.error("provide paths to scan, or use --all")

    files = discover_files(inputs)
    if not files:
        print("No files found", file=sys.stderr)
        return 1

    all_findings: list[Finding] = []
    for path in files:
        if not path.exists() or not path.is_file():
            print(f"Missing file: {path}", file=sys.stderr)
            return 1
        text = path.read_text(encoding="utf-8", errors="replace")
        findings = scan_text(text, path, patterns)
        if findings:
            all_findings.extend(findings)
        elif not args.quiet:
            print(f"✅ {path}")

    if all_findings:
        print_findings(all_findings, args.github_annotations)
        print(f"\nFAIL — {len(all_findings)} security finding(s) across {len(files)} file(s)")
        return 1

    print(f"✅ PASS — {len(files)} file(s) scanned with {len(patterns)} pattern(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
