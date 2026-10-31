#!/usr/bin/env python3
"""test_security_patterns.py — Fixture tests for security pattern definitions.

Verifies that verification/patterns.json is well-formed and all pattern entries
pass self-consistency checks (regex compiles, severity valid, etc.).
Exit 0 = all pass, 1 = failure.
"""

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import security_scan

REPO_ROOT = Path(__file__).parent.parent
PATTERNS_FILE = REPO_ROOT / "verification" / "patterns.json"
FIXTURE_DIR = REPO_ROOT / "verification" / "fixtures" / "security"

VALID_SEVERITY = {"critical", "high", "medium", "low", "info"}
REQUIRED_CLASSES = {
    "credential_harvesting", "crypto_mining", "data_exfiltration",
    "destructive_command", "obfuscated_payload", "prompt_injection",
    "reverse_shell", "social_engineering",
}
FIXTURE_CLASSES = {
    "credential_harvesting.md": "credential_harvesting",
    "data_exfiltration.md": "data_exfiltration",
    "destructive_command.md": "destructive_command",
    "prompt_injection.md": "prompt_injection",
    "social_engineering.md": "social_engineering",
    "benign_security_warning.md": None,
}


def main():
    failures = []
    if not PATTERNS_FILE.exists():
        print("FAIL: verification/patterns.json not found")
        sys.exit(1)

    try:
        data = json.loads(PATTERNS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FAIL: patterns.json is not valid JSON: {e}")
        sys.exit(1)

    patterns = data if isinstance(data, list) else data.get("patterns", [])

    if not patterns:
        print("FAIL: patterns.json contains no pattern entries")
        sys.exit(1)

    classes = {entry.get("class") for entry in patterns}
    missing_classes = REQUIRED_CLASSES - classes
    if missing_classes:
        failures.append(f"missing required classes: {', '.join(sorted(missing_classes))}")

    for i, entry in enumerate(patterns):
        label = entry.get("id") or entry.get("name") or f"entry[{i}]"

        # Must have a regex or pattern field
        pat = entry.get("regex") or entry.get("pattern") or entry.get("match")
        if not pat:
            failures.append(f"{label}: missing regex/pattern field")
            continue

        # Regex must compile
        try:
            security_scan.compile_pattern(entry)
        except (re.error, ValueError) as e:
            failures.append(f"{label}: regex compile error: {e}")

        # Severity check if present
        sev = entry.get("severity", "").lower()
        if sev and sev not in VALID_SEVERITY:
            failures.append(f"{label}: unknown severity '{sev}'")

    classes_by_id = {entry.get("id"): entry.get("class") for entry in patterns}
    patterns_by_id = {entry.get("id"): entry for entry in patterns}
    for filename, expected_class in FIXTURE_CLASSES.items():
        fixture = FIXTURE_DIR / filename
        if not fixture.is_file():
            failures.append(f"missing security fixture: {filename}")
            continue
        findings = security_scan.scan_file(fixture, patterns)
        found_classes = {classes_by_id.get(finding["id"]) for finding in findings}
        if expected_class is None and findings:
            failures.append(f"{filename}: benign fixture produced {len(findings)} finding(s)")
        elif expected_class is not None and expected_class not in found_classes:
            failures.append(f"{filename}: no finding for expected class '{expected_class}'")

    flag_cases = [
        ("i", "needle", "NEEDLE"),
        ("im", "^second$", "first\nsecond"),
        ("is", "first.*second", "first\nsecond"),
    ]
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / "SKILL.md"
        for flags, regex, text in flag_cases:
            temp_file.write_text(text, encoding="utf-8")
            if not security_scan.scan_file(temp_file, [{"id": flags, "regex": regex, "flags": flags}]):
                failures.append(f"declared regex flags '{flags}' did not match their test input")

        positive_cases = [
            ("prompt.system_heading", "### SYSTEM", "prompt_injection"),
            ("prompt.system_heading", "### SYSTEM:", "prompt_injection"),
            ("prompt.system_heading", "### SYSTEM INSTRUCTIONS", "prompt_injection"),
            (
                "credentials.read_secret_file",
                "head ~/.ssh/id_rsa",
                "credential_harvesting",
            ),
            (
                "credentials.read_secret_file",
                "secret=$(head -n 1 ~/.ssh/id_rsa)",
                "credential_harvesting",
            ),
            (
                "credentials.read_secret_file",
                "Run `head ~/.ssh/id_rsa` to read the private key.",
                "credential_harvesting",
            ),
            (
                "credentials.read_secret_file",
                "- `head ~/.ssh/id_rsa`",
                "credential_harvesting",
            ),
            (
                "credentials.read_secret_file",
                "- head ~/.ssh/id_rsa",
                "credential_harvesting",
            ),
            (
                "credentials.read_secret_file",
                "printf x | grep x ~/.ssh/id_rsa",
                "credential_harvesting",
            ),
        ]
        for pattern_id, text, expected_class in positive_cases:
            pattern = patterns_by_id.get(pattern_id)
            if pattern is None:
                failures.append(f"missing pattern required by boundary test: {pattern_id}")
                continue
            temp_file.write_text(text, encoding="utf-8")
            findings = security_scan.scan_file(temp_file, patterns)
            matched = any(
                finding["id"] == pattern_id
                and classes_by_id.get(finding["id"]) == expected_class
                for finding in findings
            )
            if not matched:
                failures.append(
                    f"{pattern_id}: expected class '{expected_class}' to match {text!r}"
                )

        negative_cases = [
            ("prompt.system_heading", "### System Dependencies"),
            ("prompt.system_heading", "### System Requirements"),
            ("prompt.system_heading", "- #### System Dependencies"),
            ("prompt.system_heading", "- ### System Requirements"),
            (
                "credentials.read_secret_file",
                "- [More about log management](https://pm2.keymetrics.io/docs/usage/log-management/)",
            ),
        ]
        for pattern_id, text in negative_cases:
            temp_file.write_text(text, encoding="utf-8")
            findings = security_scan.scan_file(temp_file, patterns)
            if findings:
                failures.append(
                    f"{pattern_id}: benign text produced {len(findings)} finding(s): {text!r}"
                )

        direct_file = Path(temp_dir) / "positive-direct.md"
        direct_file.write_text(
            "secret=$(head -n 1 ~/.ssh/id_rsa)", encoding="utf-8"
        )
        leaf_dir = Path(temp_dir) / "positive-leaf"
        leaf_dir.mkdir()
        (leaf_dir / "SKILL.md").write_text(
            "secret=$(head -n 1 ~/.ssh/id_rsa)", encoding="utf-8"
        )
        for label, target in (
            ("direct-file", direct_file),
            ("leaf-directory", leaf_dir),
        ):
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "security_scan.py"),
                    str(target),
                    "--github-annotations",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            if (
                result.returncode != 1
                or "[credentials.read_secret_file]" not in result.stdout
            ):
                failures.append(
                    f"{label} CLI expected exit 1 with credentials.read_secret_file, "
                    f"got exit {result.returncode}: {result.stdout.strip()}"
                )

        empty_dir = Path(temp_dir) / "empty"
        empty_dir.mkdir()
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "security_scan.py"), str(empty_dir), "--quiet"],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if result.returncode != 2 or "no SKILL.md files" not in result.stderr:
            failures.append(f"empty-directory CLI expected exit 2, got {result.returncode}: {result.stderr.strip()}")

    leaf = REPO_ROOT / "skills" / "agent-media-ugc-video"
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "security_scan.py"), str(leaf), "--quiet"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0 or "across 1 skill file(s)" not in result.stdout:
        failures.append(f"leaf-directory CLI expected one clean skill file, got exit {result.returncode}: {result.stdout.strip()}")

    if failures:
        print(f"FAIL: {len(failures)} pattern fixture(s) failed:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print(
            f"PASS: {len(patterns)} patterns and {len(FIXTURE_CLASSES)} fixtures validated; "
            "flags, pattern boundaries, and CLI checks OK"
        )
        sys.exit(0)


if __name__ == "__main__":
    main()
