#!/usr/bin/env python3
"""Fail-closed checks for a typed GitHub WIF workflow."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PINS = {
    "actions/checkout": "11d5960a326750d5838078e36cf38b85af677262",
    "google-github-actions/auth": "7c6bc770dae815cd3e89ee6cdf493a5fab2cc093",
    "google-github-actions/setup-gcloud": "aa5489c8933f4cc7a4f7d45035b3b1440c9c10db",
}


def validate(text: str) -> list[str]:
    failures: list[str] = []
    lowered = text.lower()
    if not re.search(r"(?m)^\s*id-token:\s*write\s*$", text):
        failures.append("permissions.id-token must be write")
    if not re.search(r"(?m)^\s*contents:\s*read\s*$", text):
        failures.append("permissions.contents must be read")
    extra_writes = [name for name in re.findall(
        r"(?m)^\s*([a-z][a-z0-9-]*):\s*write\s*$", text) if name != "id-token"]
    if extra_writes:
        failures.append(f"unexpected write permissions: {sorted(set(extra_writes))}")
    if not re.search(r"(?ms)^\s*operation:\s*.*?type:\s*choice\s*$", text):
        failures.append("workflow_dispatch.operation must be a choice input")
    if re.search(r"(?mi)^\s*(command|cmd|script|shell):\s*$", text):
        failures.append("arbitrary command-like workflow input is forbidden")
    for action, pin in PINS.items():
        uses = re.findall(rf"(?m)^\s*-?\s*uses:\s*{re.escape(action)}@([^\s#]+)", text)
        if uses != [pin]:
            failures.append(f"{action} must appear once at exact pin {pin}")
    for action, ref in re.findall(r"(?m)^\s*-?\s*uses:\s*([^@\s]+)@([^\s#]+)", text):
        if not re.fullmatch(r"[0-9a-f]{40}", ref):
            failures.append(f"action is not pinned to a full commit SHA: {action}@{ref}")
    forbidden = ("credentials_json", "service_account_key", "google_credentials")
    for marker in forbidden:
        if marker in lowered:
            failures.append(f"forbidden credential pattern: {marker}")
    run_blocks = re.findall(r"(?ms)^\s*run:\s*\|\s*\n(.*?)(?=^\s{0,8}[A-Za-z_-]+:|\Z)", text)
    if any(re.search(r"\$\{\{\s*inputs\.[^}]+\}\}", block) for block in run_blocks):
        failures.append("workflow inputs must not be interpolated directly into shell blocks")
    if re.search(r"(?mi)^\s*run:.*\$\{\{\s*inputs\.", text):
        failures.append("workflow inputs must not be interpolated directly into inline shell")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow", type=Path)
    args = parser.parse_args()
    text = args.workflow.read_text(encoding="utf-8")
    failures = validate(text)
    print(json.dumps({
        "schema": "gcp-keyless-workflow-validation-v1",
        "workflow": str(args.workflow),
        "verdict": "PASS" if not failures else "FAIL",
        "failures": failures,
    }, sort_keys=True, indent=2))
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
