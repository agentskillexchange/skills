#!/usr/bin/env python3
"""Write reproducible sync metadata for generated ASE repo artifacts."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

GENERATOR_VERSION = "2026-05-10.portable-sync-v1"
DEFAULT_SCHEMA_VERSION = "2.0"


def git_commit(repo_dir: Path) -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short=12", "HEAD"],
            cwd=repo_dir,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out or None
    except Exception:
        return None


def main() -> int:
    repo_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    repo_dir = repo_dir.resolve()
    skills_path = repo_dir / "skills.json"
    if not skills_path.exists():
        print(f"skills.json not found: {skills_path}", file=sys.stderr)
        return 1

    raw = skills_path.read_bytes()
    try:
        skills_json: dict[str, Any] = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        print(f"skills.json is not parseable JSON: {exc}", file=sys.stderr)
        return 1

    site_base = os.environ.get("ASE_SITE_BASE", os.environ.get("ASE_API_BASE", "https://agentskillexchange.com")).rstrip("/")
    skills = skills_json.get("skills")
    total = len(skills) if isinstance(skills, list) else skills_json.get("total")
    schema_version = str(skills_json.get("version") or os.environ.get("ASE_SCHEMA_VERSION") or DEFAULT_SCHEMA_VERSION)

    metadata = {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source_api_base": site_base,
        "source_browse_endpoint": f"{site_base}/wp-json/ase-marketplace/v1/browse",
        "source_total": total,
        "source_etag_or_hash": "sha256:" + hashlib.sha256(raw).hexdigest(),
        "generator_version": GENERATOR_VERSION,
        "generator_commit": git_commit(repo_dir),
        "schema_version": schema_version,
        "generated_files": [
            "README.md",
            "CATALOG.md",
            "categories/",
            "industries/",
            "TOP-STARS.md",
            "TOP-DOWNLOADS.md",
            "skills.json",
            "openclaw.json",
            "codex.json",
            "llms.txt",
            ".claude-plugin",
            ".codex",
            ".cursor-plugin",
            ".opencode",
        ],
    }
    (repo_dir / "sync-metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote sync-metadata.json — {total} skills, {metadata['source_etag_or_hash'][:19]}…")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
