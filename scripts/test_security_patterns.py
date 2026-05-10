#!/usr/bin/env python3
"""Regression tests for the executable ASE security scanner contract."""
from __future__ import annotations

import sys
from pathlib import Path

import security_scan

ROOT = Path(__file__).resolve().parent.parent
PATTERNS_PATH = ROOT / "verification" / "patterns.json"
FIXTURE_DIR = ROOT / "verification" / "fixtures" / "security"

EXPECTED_FIXTURE_CLASSES = {
    "prompt_injection.md": {"prompt_injection"},
    "data_exfiltration.md": {"data_exfiltration"},
    "destructive_command.md": {"destructive_command"},
    "credential_harvesting.md": {"credential_harvesting"},
    "social_engineering.md": {"social_engineering"},
}


def fail(message: str) -> int:
    print(f"❌ {message}")
    return 1


def main() -> int:
    patterns = security_scan.load_patterns(PATTERNS_PATH)
    if not patterns:
        return fail("no patterns loaded")

    pattern_ids = [pattern.id for pattern in patterns]
    if len(pattern_ids) != len(set(pattern_ids)):
        return fail("pattern ids must be unique")

    expected_classes = {"prompt_injection", "data_exfiltration", "destructive_command", "credential_harvesting", "social_engineering"}
    actual_classes = {pattern.klass for pattern in patterns}
    missing_classes = expected_classes - actual_classes
    if missing_classes:
        return fail(f"patterns missing classes: {sorted(missing_classes)}")

    for fixture_name, expected in EXPECTED_FIXTURE_CLASSES.items():
        path = FIXTURE_DIR / fixture_name
        findings = security_scan.scan_text(path.read_text(encoding="utf-8"), path, patterns)
        found_classes = {finding.klass for finding in findings}
        missing = expected - found_classes
        if missing:
            return fail(f"{fixture_name} did not trigger expected classes: {sorted(missing)}")

    benign_path = FIXTURE_DIR / "benign_security_warning.md"
    benign_findings = security_scan.scan_text(benign_path.read_text(encoding="utf-8"), benign_path, patterns)
    if benign_findings:
        details = ", ".join(finding.pattern_id for finding in benign_findings[:5])
        return fail(f"benign fixture produced findings: {details}")

    print(f"✅ PASS — {len(patterns)} security patterns and {len(EXPECTED_FIXTURE_CLASSES)} positive fixture classes tested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
