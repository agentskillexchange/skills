#!/usr/bin/env python3
"""smoke-agent-endpoints.py — Smoke test for public ASE agent endpoints.

Usage:
  python3 scripts/smoke-agent-endpoints.py --base https://agentskillexchange.com

Checks:
  - /skills.json   — parseable JSON, has 'skills' list, total > 0
  - /openclaw.json — parseable JSON, has 'skills' list
  - /codex.json    — parseable JSON, has 'skills' list
  - /llms.txt      — non-empty text, contains at least one '## '

Exit 0 = all pass, 1 = any failure.
"""

import argparse
import json
import sys
import urllib.request

ENDPOINTS = [
    ("skills.json",   "json",  lambda d: isinstance(d, dict) and int(d.get("total", 0)) > 0),
    ("openclaw.json", "json",  lambda d: isinstance(d, dict) and ("skills" in d or "catalog" in d)),
    ("codex.json",    "json",  lambda d: isinstance(d, dict) and ("skills" in d or "catalog" in d)),
    ("llms.txt",      "text",  lambda d: "## " in d and len(d) > 100),
]


def check(base: str, path: str, fmt: str, validator) -> tuple[bool, str]:
    url = f"{base.rstrip('/')}/{path}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ASE smoke-test/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            status = resp.status
            body = resp.read().decode("utf-8")
    except Exception as e:
        return False, f"Request failed: {e}"

    if status != 200:
        return False, f"HTTP {status}"

    if fmt == "json":
        try:
            data = json.loads(body)
        except json.JSONDecodeError as e:
            return False, f"JSON parse error: {e}"
    else:
        data = body

    if not validator(data):
        snippet = body[:120].replace("\n", " ")
        return False, f"Validator check failed. Body snippet: {snippet}"

    count = ""
    if fmt == "json" and isinstance(data, dict):
        n = data.get("total") or len(data.get("skills", []))
        if n:
            count = f" ({n} skills)"

    return True, f"OK{count}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="https://agentskillexchange.com")
    args = parser.parse_args()

    base = args.base
    print(f"Smoke testing agent endpoints at {base}")

    results = []
    for path, fmt, validator in ENDPOINTS:
        ok, msg = check(base, path, fmt, validator)
        status = "PASS" if ok else "FAIL"
        print(f"  {status}  {path}: {msg}")
        results.append(ok)

    passed = sum(results)
    total  = len(results)
    print(f"\nEndpoint smoke: {passed}/{total} passed.")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
