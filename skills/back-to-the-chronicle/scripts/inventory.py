#!/usr/bin/env python3
"""Create a read-only Git and artifact inventory for a Chronicle backfill."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys


ARTIFACT_TERMS = {
    "artifact",
    "checkpoint",
    "chronicle",
    "control",
    "event",
    "ledger",
    "manifest",
    "metric",
    "progress",
    "receipt",
    "result",
    "summary",
}
SECRETISH_PARTS = {
    ".env",
    ".netrc",
    "credential",
    "credentials",
    "id_ed25519",
    "id_rsa",
    "private_key",
    "secret",
    "tokens.json",
}


def git(root: Path, *args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def secretish(path: str) -> bool:
    parts = {part.lower() for part in Path(path).parts}
    return any(
        part in SECRETISH_PARTS
        or part.startswith(".env.")
        or part.startswith("token.")
        or part.endswith(".token")
        for part in parts
    )


def candidate(path: str) -> bool:
    lowered = path.lower()
    return not secretish(path) and any(term in lowered for term in ARTIFACT_TERMS)


def commits(root: Path) -> list[dict[str, object]]:
    delimiter = "\x1f"
    record = "\x1e"
    output = git(
        root,
        "log",
        "--all",
        "--reverse",
        f"--format={record}%H{delimiter}%aI{delimiter}%an{delimiter}%P{delimiter}%s",
        "--name-only",
    )
    items: list[dict[str, object]] = []
    for block in output.split(record):
        block = block.strip()
        if not block:
            continue
        lines = block.splitlines()
        fields = lines[0].split(delimiter)
        if len(fields) != 5:
            raise ValueError(f"unexpected git log record: {lines[0]!r}")
        items.append(
            {
                "commit": fields[0],
                "authored_at": fields[1],
                "author": fields[2],
                "parents": fields[3].split() if fields[3] else [],
                "subject": fields[4],
                "files": [line for line in lines[1:] if line and not secretish(line)],
            }
        )
    return items


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if not (root / ".git").exists():
        parser.error(f"not a Git root: {root}")

    files = sorted(
        line
        for line in git(
            root,
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
        ).splitlines()
        if line and not secretish(line)
    )
    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "head": git(root, "rev-parse", "HEAD").strip(),
        "branch": git(root, "branch", "--show-current").strip(),
        "status": [
            line
            for line in git(root, "status", "--short").splitlines()
            if not secretish(line[3:] if len(line) > 3 else line)
        ],
        "submodules": git(root, "submodule", "status", "--recursive", check=False).splitlines(),
        "commits": commits(root),
        "chronicle_files": [path for path in files if Path(path).name in {"CHRONICLE.md", "CHRONICLES.md"}],
        "artifact_candidates": [path for path in files if candidate(path)],
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with os.fdopen(os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "w", encoding="utf-8") as handle:
            handle.write(encoded)
        print(args.output)
    else:
        sys.stdout.write(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
