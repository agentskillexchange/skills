#!/usr/bin/env python3
"""Validate a Visual QA screenshot manifest without third-party dependencies."""

from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys
from typing import Any, Sequence


REQUIRED_FIELDS = ("label", "path", "flow", "state", "breakpoint", "theme")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}
WINDOWS_ABSOLUTE = re.compile(r"^[A-Za-z]:[\\/]")


def load_manifest(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        raise ValueError(f"could not read manifest: {error}") from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}"
        ) from error


def validate_manifest(
    data: Any,
    *,
    root: Path,
    check_files: bool = False,
) -> list[str]:
    if not isinstance(data, list):
        return ["$: manifest must be a JSON array"]
    if not data:
        return ["$: manifest must contain at least one screenshot entry"]

    errors: list[str] = []
    labels: set[str] = set()
    paths: set[str] = set()
    resolved_root = root.expanduser().resolve()

    for index, entry in enumerate(data):
        location = f"$[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{location}: entry must be an object")
            continue

        missing = [field for field in REQUIRED_FIELDS if field not in entry]
        if missing:
            errors.append(f"{location}: missing fields: {', '.join(missing)}")

        text_values: dict[str, str] = {}
        for field in ("label", "path", "flow", "state", "theme"):
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{location}.{field}: must be a non-empty string")
            else:
                text_values[field] = value.strip()

        breakpoint = entry.get("breakpoint")
        if isinstance(breakpoint, bool) or not isinstance(breakpoint, int) or breakpoint < 1:
            errors.append(f"{location}.breakpoint: must be a positive integer")

        label = text_values.get("label")
        if label:
            if label in labels:
                errors.append(f"{location}.label: duplicate label {label!r}")
            labels.add(label)

        screenshot_path = text_values.get("path")
        if screenshot_path:
            if screenshot_path in paths:
                errors.append(f"{location}.path: duplicate path {screenshot_path!r}")
            paths.add(screenshot_path)
            posix_path = PurePosixPath(screenshot_path)
            unsafe = (
                "\\" in screenshot_path
                or posix_path.is_absolute()
                or WINDOWS_ABSOLUTE.match(screenshot_path) is not None
                or ".." in posix_path.parts
                or posix_path == PurePosixPath(".")
            )
            if unsafe:
                errors.append(
                    f"{location}.path: must be a repository-relative forward-slash path"
                )
            elif posix_path.suffix.lower() not in IMAGE_SUFFIXES:
                errors.append(
                    f"{location}.path: expected one of {', '.join(sorted(IMAGE_SUFFIXES))}"
                )
            elif check_files:
                candidate = (resolved_root / Path(*posix_path.parts)).resolve()
                try:
                    candidate.relative_to(resolved_root)
                except ValueError:
                    errors.append(f"{location}.path: resolves outside the selected root")
                else:
                    if not candidate.is_file():
                        errors.append(f"{location}.path: screenshot does not exist: {screenshot_path}")

    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate a Visual QA screenshot manifest.")
    parser.add_argument("manifest", type=Path)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Repository root used to resolve screenshot paths (default: current directory).",
    )
    parser.add_argument(
        "--check-files",
        action="store_true",
        help="Require every screenshot path to exist below --root.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        data = load_manifest(args.manifest)
    except ValueError as error:
        print(f"manifest error: {error}", file=sys.stderr)
        return 1

    errors = validate_manifest(data, root=args.root, check_files=args.check_files)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"valid entries={len(data)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
