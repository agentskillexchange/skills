#!/usr/bin/env python3
"""Index project-related Codex and Claude session JSONLs without copying content."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Iterable


CWD_KEYS = {"cwd", "project_path", "projectPath"}
TIMESTAMP_KEYS = {"timestamp", "created_at", "createdAt"}


def canonical_root(root: Path) -> Path:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    return Path(result.stdout.strip()).resolve() if result.returncode == 0 else root.resolve()


def values_for_keys(value: Any, keys: set[str]) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in keys and isinstance(child, str):
                yield child
            yield from values_for_keys(child, keys)
    elif isinstance(value, list):
        for child in value:
            yield from values_for_keys(child, keys)


def belongs_to_project(cwd: str, root: Path) -> bool:
    try:
        root = root.resolve()
        candidate = Path(cwd).expanduser().resolve()
        return candidate == root or root in candidate.parents
    except (OSError, RuntimeError, ValueError):
        return False


def session_ids(event: dict[str, Any]) -> set[str]:
    found: set[str] = set()
    for key in ("sessionId", "session_id", "thread_id"):
        value = event.get(key)
        if isinstance(value, str) and value:
            found.add(value)
    if event.get("type") == "session_meta":
        payload = event.get("payload")
        if isinstance(payload, dict) and isinstance(payload.get("id"), str):
            found.add(payload["id"])
    return found


def inspect_jsonl(path: Path, source: str, root: Path) -> dict[str, object] | None:
    digest = hashlib.sha256()
    matched_cwds: set[str] = set()
    matched_lines: list[int] = []
    ids: set[str] = set()
    timestamps: list[str] = []
    parse_errors = 0
    lines = 0

    try:
        with path.open("rb") as handle:
            for lines, raw_line in enumerate(handle, start=1):
                digest.update(raw_line)
                try:
                    event = json.loads(raw_line)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    parse_errors += 1
                    continue
                if not isinstance(event, dict):
                    continue
                ids.update(session_ids(event))
                metadata = event.get("payload", {}) if event.get("type") in {"session_meta", "turn_context"} else event
                if not isinstance(metadata, dict):
                    metadata = {}
                timestamps.extend(value for key, value in event.items() if key in TIMESTAMP_KEYS and isinstance(value, str))
                event_cwds = {
                    cwd for key, cwd in metadata.items()
                    if key in CWD_KEYS and isinstance(cwd, str) and belongs_to_project(cwd, root)
                }
                if event_cwds:
                    matched_cwds.update(event_cwds)
                    matched_lines.append(lines)
    except OSError:
        return None

    if not matched_cwds:
        return None
    stat = path.stat()
    return {
        "source": source,
        "path": str(path.resolve()),
        "sha256": digest.hexdigest(),
        "bytes": stat.st_size,
        "lines": lines,
        "parse_errors": parse_errors,
        "session_ids": sorted(ids),
        "matched_cwds": sorted(matched_cwds),
        "matched_lines": matched_lines,
        "first_timestamp": timestamps[0] if timestamps else None,
        "last_timestamp": timestamps[-1] if timestamps else None,
    }


def discover(session_root: Path, source: str, project_root: Path) -> list[dict[str, object]]:
    if not session_root.exists():
        return []
    return [
        item
        for path in sorted(session_root.rglob("*.jsonl"))
        if path.is_file() and not path.is_symlink()
        for item in [inspect_jsonl(path, source, project_root)]
        if item is not None
    ]


def build_inventory(
    root: Path,
    codex_root: Path | None,
    claude_root: Path | None,
    codex_archived_root: Path | None = None,
) -> dict[str, object]:
    project_root = canonical_root(root)
    stores = [(source, path.expanduser()) for source, path in
              (("codex", codex_root), ("claude", claude_root)) if path is not None]
    if codex_archived_root is not None:
        stores.append(("codex", codex_archived_root.expanduser()))
    sessions = [
        item
        for source, session_root in stores
        for item in discover(session_root, source, project_root)
    ]
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "project_root": str(project_root),
        "stores": [
            {"source": source, "path": str(path.resolve())}
            for source, path in stores
        ],
        "unavailable_stores": [
            {"source": source, "path": str(path.resolve())}
            for source, path in stores
            if not path.exists()
        ],
        "sessions": sessions,
        "coverage_note": "Metadata-only output, not a privacy scrubber. Input bytes are read to match and hash. Unmatched, unreadable, symlinked, or metadata-poor JSONLs require separately authorized review.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--codex-root", type=Path)
    parser.add_argument(
        "--codex-archived-root", type=Path
    )
    parser.add_argument("--claude-root", type=Path)
    args = parser.parse_args()
    if not any((args.codex_root, args.codex_archived_root, args.claude_root)):
        parser.error("provide at least one explicitly approved session store")
    payload = build_inventory(
        args.root, args.codex_root, args.claude_root, args.codex_archived_root
    )
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
