#!/usr/bin/env python3
"""Smoke test public ASE agent-readable endpoints."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from typing import Any


def fetch(url: str) -> tuple[int, dict[str, str], bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "ASE endpoint smoke"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status, {k.lower(): v for k, v in resp.headers.items()}, resp.read()


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="https://agentskillexchange.com")
    parser.add_argument("--min-total", type=int, default=1400)
    args = parser.parse_args()
    base = args.base.rstrip("/")
    errors: list[str] = []

    json_endpoints = {
        "skills.json": f"{base}/skills.json",
        "openclaw.json": f"{base}/openclaw.json",
        "codex.json": f"{base}/codex.json",
    }
    parsed: dict[str, Any] = {}
    for name, url in json_endpoints.items():
        status, headers, body = fetch(url)
        require(status == 200, f"{name}: expected 200, got {status}", errors)
        require("application/json" in headers.get("content-type", ""), f"{name}: wrong content-type {headers.get('content-type')}", errors)
        require("max-age=300" in headers.get("cache-control", ""), f"{name}: missing cache header {headers.get('cache-control')}", errors)
        try:
            parsed[name] = json.loads(body.decode("utf-8"))
        except Exception as exc:
            errors.append(f"{name}: invalid JSON: {exc}")

    skills = parsed.get("skills.json", {})
    require(skills.get("version") == "2.0", "skills.json: expected version 2.0", errors)
    require(int(skills.get("total") or 0) >= args.min_total, f"skills.json: total below {args.min_total}", errors)
    require(len(skills.get("skills") or []) == int(skills.get("total") or -1), "skills.json: skills length != total", errors)
    if skills.get("skills"):
        first = skills["skills"][0]
        require("title" in first and "slug" in first and "verification" in first, "skills.json: first skill missing canonical keys", errors)
        require("name" not in first and "verification_status" not in first and "verified_metadata" not in first, "skills.json: first skill exposes internal/stale keys", errors)

    for manifest_name in ("openclaw.json", "codex.json"):
        manifest = parsed.get(manifest_name, {})
        require(manifest.get("schema_version") == "2.0", f"{manifest_name}: expected schema_version 2.0", errors)
        require((manifest.get("catalog") or {}).get("skills_url") == f"{base}/skills.json", f"{manifest_name}: wrong skills_url", errors)

    status, headers, body = fetch(f"{base}/llms.txt")
    text = body.decode("utf-8", "replace")
    require(status == 200, f"llms.txt: expected 200, got {status}", errors)
    require("text/plain" in headers.get("content-type", ""), f"llms.txt: wrong content-type {headers.get('content-type')}", errors)
    require("max-age=300" in headers.get("cache-control", ""), f"llms.txt: missing cache header {headers.get('cache-control')}", errors)
    for needle in ("Full catalog JSON", f"{base}/skills.json", "OpenClaw manifest", "Codex manifest"):
        require(needle in text, f"llms.txt: missing {needle}", errors)

    if errors:
        print("FAIL — ASE agent endpoint smoke test")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS — ASE agent endpoints healthy: skills.json, openclaw.json, codex.json, llms.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
