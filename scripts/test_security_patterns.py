#!/usr/bin/env python3
"""test_security_patterns.py — Fixture tests for security pattern definitions.

Verifies that verification/patterns.json is well-formed and all pattern entries
pass self-consistency checks (regex compiles, severity valid, etc.).
Exit 0 = all pass, 1 = failure.
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
PATTERNS_FILE = REPO_ROOT / "verification" / "patterns.json"

VALID_SEVERITY = {"critical", "high", "medium", "low", "info"}


def main():
    if not PATTERNS_FILE.exists():
        # No patterns file — nothing to test; pass vacuously
        print("SKIP: verification/patterns.json not found (no security patterns defined)")
        sys.exit(0)

    try:
        data = json.loads(PATTERNS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FAIL: patterns.json is not valid JSON: {e}")
        sys.exit(1)

    patterns = data if isinstance(data, list) else data.get("patterns", [])

    if not patterns:
        print("SKIP: patterns.json contains no pattern entries")
        sys.exit(0)

    failures = []
    for i, entry in enumerate(patterns):
        label = entry.get("id") or entry.get("name") or f"entry[{i}]"

        # Must have a regex or pattern field
        pat = entry.get("regex") or entry.get("pattern") or entry.get("match")
        if not pat:
            failures.append(f"{label}: missing regex/pattern field")
            continue

        # Regex must compile
        try:
            re.compile(pat)
        except re.error as e:
            failures.append(f"{label}: regex compile error: {e}")

        # Severity check if present
        sev = entry.get("severity", "").lower()
        if sev and sev not in VALID_SEVERITY:
            failures.append(f"{label}: unknown severity '{sev}'")

    if failures:
        print(f"FAIL: {len(failures)} pattern fixture(s) failed:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print(f"PASS: {len(patterns)} security pattern fixture(s) validated OK")
        sys.exit(0)


if __name__ == "__main__":
    main()
