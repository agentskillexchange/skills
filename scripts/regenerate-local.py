#!/usr/bin/env python3
"""Compatibility wrapper for the portable public API sync.

Historically this script depended on local OpenClaw workspace snapshots. Public repo
regeneration is now reproducible via scripts/sync-from-api.sh and ASE_API_BASE.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    repo_dir = script_dir.parent
    env = os.environ.copy()
    env.setdefault("ASE_API_BASE", "https://agentskillexchange.com")
    return subprocess.call([str(script_dir / "sync-from-api.sh"), str(repo_dir)], env=env)


if __name__ == "__main__":
    raise SystemExit(main())
