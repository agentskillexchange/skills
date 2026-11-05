#!/usr/bin/env python3
"""Discover registered and nearby Archivum workspaces without mutating them."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import tomllib
from typing import Any, Iterable


IGNORED_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "dist",
    "build",
    "vendor",
    "__pycache__",
}

CONFIG_VERSION_PATTERN = re.compile(r"^version:\s*([0-9]+)\s*(?:#.*)?$")
AGENT_CONTRACTS = (
    "AGENTS.md",
    "CLAUDE.md",
    ".cursor/rules/archivum.mdc",
    ".cursorrules",
)


def find_registry(
    explicit: str | Path | None = None, cwd: Path | None = None
) -> Path | None:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    if os.environ.get("ARCHIVUM_REGISTRY"):
        candidates.append(Path(os.environ["ARCHIVUM_REGISTRY"]).expanduser())
    if os.environ.get("ARCHIVUM_HOME"):
        candidates.append(
            Path(os.environ["ARCHIVUM_HOME"]).expanduser()
            / "00_meta"
            / "archivum_registry.toml"
        )
    start = (cwd or Path.cwd()).resolve()
    for parent in (start, *start.parents):
        candidates.append(parent / "00_meta" / "archivum_registry.toml")
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    return None


def load_registry(path: Path) -> dict[str, Any]:
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    archives = data.get("archives")
    if not isinstance(archives, dict) or not archives:
        raise ValueError(f"Registry has no [archives.*] entries: {path}")
    home = data.get("home")
    if home not in archives:
        raise ValueError(f"Registry home {home!r} is not an archive entry: {path}")
    return data


def is_archivum(root: Path) -> bool:
    return (root / "config.yaml").is_file() and (
        (root / "00_meta").is_dir() or (root / "AGENTS.md").is_file()
    )


def inspect_workspace(root: Path) -> dict[str, Any]:
    config = root / "config.yaml"
    config_version: int | None = None
    if config.is_file():
        for line in config.read_text().splitlines():
            match = CONFIG_VERSION_PATTERN.match(line)
            if match:
                config_version = int(match.group(1))
                break
    return {
        "config_file": str(config) if config.is_file() else None,
        "config_version": config_version,
        "agent_contracts": [
            relative for relative in AGENT_CONTRACTS if (root / relative).is_file()
        ],
    }


def walk_candidates(search_root: Path, max_depth: int = 4) -> Iterable[Path]:
    search_root = search_root.expanduser().resolve()
    if is_archivum(search_root):
        yield search_root
    for current, dirs, _files in os.walk(search_root):
        path = Path(current)
        depth = len(path.relative_to(search_root).parts)
        dirs[:] = [
            name
            for name in dirs
            if name not in IGNORED_DIRS and not name.startswith(".")
        ]
        if depth >= max_depth:
            dirs[:] = []
            continue
        if path != search_root and is_archivum(path):
            yield path
            dirs[:] = []


def discover(
    registry_path: Path | None,
    search_roots: Iterable[Path] = (),
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "registry": str(registry_path) if registry_path else None,
        "home": None,
        "archives": [],
    }
    seen: set[Path] = set()
    if registry_path:
        registry = load_registry(registry_path)
        result["home"] = registry["home"]
        for name, entry in registry["archives"].items():
            root = Path(entry["root"]).expanduser().resolve()
            seen.add(root)
            result["archives"].append(
                {
                    "name": name,
                    "kind": entry.get("kind", "unspecified"),
                    "root": str(root),
                    "registered": True,
                    "exists": root.is_dir(),
                    "is_archivum": is_archivum(root),
                    **inspect_workspace(root),
                }
            )
    for search_root in search_roots:
        for root in walk_candidates(search_root):
            if root in seen:
                continue
            seen.add(root)
            result["archives"].append(
                {
                    "name": root.name,
                    "kind": "discovered",
                    "root": str(root),
                    "registered": False,
                    "exists": True,
                    "is_archivum": True,
                    **inspect_workspace(root),
                }
            )
    result["archives"].sort(
        key=lambda item: (not item["registered"], item["name"])
    )
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", help="Path to archivum_registry.toml")
    parser.add_argument(
        "--search-root", action="append", default=[], help="Bounded root to scan"
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    registry = find_registry(args.registry)
    roots = [Path(value) for value in args.search_root]
    if not roots and not registry:
        roots = [Path.cwd()]
    try:
        result = discover(registry, roots)
    except (OSError, ValueError, tomllib.TOMLDecodeError) as error:
        print(f"argus: {error}")
        return 2
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if result["registry"]:
            print(f"registry: {result['registry']} (home={result['home']})")
        for archive in result["archives"]:
            marker = "registered" if archive["registered"] else "discovered"
            print(
                f"{archive['name']}\t{archive['kind']}\t{marker}\t{archive['root']}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
