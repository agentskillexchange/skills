#!/usr/bin/env python3
"""Validate logical cross-archive links and registered home anchors."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote

from discover_archivums import load_registry


URI_PATTERN = re.compile(r"archivum://([a-zA-Z0-9._-]+)/([^\s)\]>]+)")


def resolve_uri(
    uri_archive: str, uri_path: str, roots: dict[str, Path]
) -> Path | None:
    if uri_archive not in roots:
        return None
    relative = unquote(uri_path).split("#", 1)[0]
    root = roots[uri_archive].resolve()
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        return None
    return target


def validate(registry_path: Path) -> list[str]:
    registry = load_registry(registry_path)
    roots = {
        name: Path(entry["root"]).expanduser().resolve()
        for name, entry in registry["archives"].items()
    }
    home_name = registry["home"]
    index_relative = registry.get("index", "00_meta/cross_archive_index.md")
    index = roots[home_name] / index_relative
    failures: list[str] = []
    if not index.is_file():
        return [f"missing home index: {index}"]

    index_text = index.read_text()
    referenced_archives: set[str] = set()
    for name, path in URI_PATTERN.findall(index_text):
        referenced_archives.add(name)
        target = resolve_uri(name, path, roots)
        if name not in roots:
            failures.append(f"unknown archive in index: archivum://{name}/{path}")
        elif target is None:
            failures.append(
                f"target escapes archive root: archivum://{name}/{path}"
            )
        elif not target.exists():
            failures.append(f"missing target: archivum://{name}/{path} -> {target}")

    home_uri = f"archivum://{home_name}/{index_relative}"
    for name, entry in registry["archives"].items():
        if name == home_name:
            continue
        anchor_relative = entry.get("home_anchor")
        if anchor_relative:
            anchor = roots[name] / anchor_relative
            if not anchor.is_file():
                failures.append(f"missing home anchor for {name}: {anchor}")
            elif home_uri not in anchor.read_text():
                failures.append(
                    f"home anchor for {name} does not link to {home_uri}: {anchor}"
                )
        if entry.get("kind") not in {"public", "external"} and name not in referenced_archives:
            failures.append(f"registered private archive is absent from home index: {name}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True, type=Path)
    args = parser.parse_args()
    try:
        failures = validate(args.registry.expanduser().resolve())
    except (OSError, ValueError) as error:
        print(f"argus: {error}", file=sys.stderr)
        return 2
    if failures:
        for failure in failures:
            print(f"FAIL  {failure}")
        return 1
    print("PASS  cross-archive links and home anchors are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
