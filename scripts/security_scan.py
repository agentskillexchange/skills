#!/usr/bin/env python3
"""security_scan.py — Security scan for ASE skill files using verification/patterns.json.

Usage:
  python3 scripts/security_scan.py skills [--github-annotations] [--quiet]
  python3 scripts/security_scan.py skills/my-skill/SKILL.md [--github-annotations]

Uses verification/patterns.json as the source of truth.
Exit 0 = no findings, 1 = findings detected.
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PATTERNS_FILE = REPO_ROOT / "verification" / "patterns.json"

# ── Built-in hardened patterns (used when patterns.json absent) ───────────────
BUILTIN_PATTERNS = [
    {
        "id":       "no-private-keys",
        "severity": "critical",
        "regex":    r"-----BEGIN (?:RSA|EC|DSA|OPENSSH) PRIVATE KEY",
        "message":  "Private key material in skill file",
    },
    {
        "id":       "no-aws-secret",
        "severity": "critical",
        "regex":    r"(?i)aws_secret_access_key\s*=\s*[A-Za-z0-9/+=]{20,}",
        "message":  "AWS secret key in skill file",
    },
    {
        "id":       "no-hardcoded-token",
        "severity": "high",
        "regex":    r"(?i)(api_?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}['\"]?",
        "message":  "Possible hardcoded credential",
    },
    {
        "id":       "no-eval-exec",
        "severity": "medium",
        "regex":    r"\beval\s*\(|exec\s*\([^)]{20,}\)",
        "message":  "Dynamic eval/exec usage",
    },
]


def load_patterns():
    if PATTERNS_FILE.exists():
        data = json.loads(PATTERNS_FILE.read_text(encoding="utf-8"))
        pats = data if isinstance(data, list) else data.get("patterns", [])
        if pats:
            return pats
    return BUILTIN_PATTERNS


def scan_file(path: Path, patterns: list, github_annotations: bool = False) -> list[dict]:
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        findings.append({"path": str(path), "id": "read-error", "line": 0, "message": str(e)})
        return findings

    lines = text.splitlines()
    for pat in patterns:
        regex = pat.get("regex") or pat.get("pattern") or pat.get("match")
        if not regex:
            continue
        try:
            compiled = re.compile(regex)
        except re.error:
            continue
        for lineno, line in enumerate(lines, 1):
            if compiled.search(line):
                finding = {
                    "path":     str(path),
                    "id":       pat.get("id", "unknown"),
                    "severity": pat.get("severity", "info"),
                    "line":     lineno,
                    "message":  pat.get("message", regex),
                }
                findings.append(finding)
                if github_annotations:
                    print(f"::error file={path},line={lineno}::[{finding['id']}] {finding['message']}")
    return findings


def main():
    parser = argparse.ArgumentParser(description="ASE security scanner")
    parser.add_argument("target", help="skills/ directory or single SKILL.md")
    parser.add_argument("--github-annotations", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    patterns = load_patterns()
    if not args.quiet:
        print(f"Loaded {len(patterns)} security pattern(s)")

    target = Path(args.target)
    if target.is_dir():
        files = sorted(target.glob("*/SKILL.md"))
    else:
        files = [target]

    total_findings = []
    for f in files:
        findings = scan_file(f, patterns, args.github_annotations)
        total_findings.extend(findings)
        if findings and not args.quiet:
            for finding in findings:
                print(f"  [{finding['severity'].upper()}] {finding['path']}:{finding['line']} — {finding['message']}")

    if total_findings:
        print(f"\nSecurity scan: {len(total_findings)} finding(s) in {len(files)} file(s).")
        sys.exit(1)
    else:
        print(f"Security scan: PASS — 0 findings across {len(files)} skill file(s).")
        sys.exit(0)


if __name__ == "__main__":
    main()
