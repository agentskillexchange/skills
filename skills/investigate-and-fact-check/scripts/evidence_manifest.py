#!/usr/bin/env python3
"""Create and verify a local SHA-256 evidence baseline using Python only.

This checks byte equality against a baseline. It does not establish authenticity,
capture time, immutable custody, or protection if the manifest is also changed.
Keep an independently protected copy of the manifest and a separate collection log.
Run against a stable directory under your control, not a concurrently changing tree.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys


class ManifestError(Exception):
    """An input or filesystem condition prevents a reliable comparison."""


def local_path(value):
    path = Path(os.path.abspath(os.path.expanduser(value)))
    for component in (path, *path.parents):
        if component.is_symlink():
            raise ManifestError(f"Symlink refused: {component}")
    return path


def evidence_root(value):
    root = local_path(value)
    if not root.is_dir():
        raise ManifestError(f"Evidence root is not a directory: {root}")
    return root


def tree_files(root):
    paths = []
    def walk_error(error):
        raise error
    for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        dirs.sort()
        for name in sorted(dirs + files):
            path = Path(directory) / name
            mode = path.lstat().st_mode
            if stat.S_ISLNK(mode):
                raise ManifestError(f"Symlink refused: {path.relative_to(root)}")
            if not stat.S_ISDIR(mode) and not stat.S_ISREG(mode):
                raise ManifestError(f"Special file refused: {path.relative_to(root)}")
            if stat.S_ISREG(mode):
                paths.append(path)
    return sorted(paths)


def fingerprint(path):
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as stream:
        before = os.fstat(stream.fileno())
        if not stat.S_ISREG(before.st_mode):
            raise ManifestError(f"Non-regular file refused: {path}")
        digest = hashlib.sha256()
        length = 0
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
            length += len(chunk)
        after = os.fstat(stream.fileno())
    identity = lambda s: (s.st_dev, s.st_ino, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    if identity(before) != identity(after) or length != after.st_size:
        raise ManifestError(f"File changed while being read: {path}")
    return {"bytes": length, "sha256": digest.hexdigest()}


def safe_relative_name(name):
    if not isinstance(name, str) or not name or "\\" in name or "\x00" in name:
        raise ManifestError("Invalid manifest path.")
    parts = name.split("/")
    if any(part in ("", ".", "..") for part in parts) or ":" in parts[0] or PurePosixPath(name).is_absolute():
        raise ManifestError(f"Noncanonical or unsafe manifest path: {name!r}")
    return name


def create(args):
    root = evidence_root(args.root)
    output = local_path(args.output)
    if output == root or root in output.parents:
        raise ManifestError("Manifest output must be outside the evidence root.")
    if not output.parent.is_dir():
        raise ManifestError("Manifest output parent directory must already exist.")
    if output.exists():
        raise ManifestError("Manifest output already exists; refusing to overwrite it.")
    paths = tree_files(root)
    if not paths:
        raise ManifestError("Evidence root contains no regular files.")
    entries = [{"path": safe_relative_name(p.relative_to(root).as_posix()), **fingerprint(p)} for p in paths]
    if paths != tree_files(root):
        raise ManifestError("Evidence file inventory changed during collection; retry on a stable tree.")
    manifest = {
        "schema_version": 1,
        "algorithm": "sha256",
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "files": entries,
    }
    payload = json.dumps(manifest, indent=2, ensure_ascii=True) + "\n"
    with output.open("x", encoding="utf-8") as stream:
        stream.write(payload)
    print(json.dumps({"status": "created", "files": len(entries), "manifest": str(output)}))
    return 0


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ManifestError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_manifest(path):
    if not stat.S_ISREG(path.lstat().st_mode):
        raise ManifestError("Manifest must be a regular file.")
    with path.open(encoding="utf-8") as stream:
        manifest = json.load(stream, object_pairs_hook=unique_keys)
    if not isinstance(manifest, dict):
        raise ManifestError("Manifest must be a JSON object.")
    if type(manifest.get("schema_version")) is not int or manifest["schema_version"] != 1:
        raise ManifestError("Unsupported manifest schema_version.")
    if manifest.get("algorithm") != "sha256":
        raise ManifestError("Unsupported manifest algorithm.")
    generated = manifest.get("generated_at_utc")
    if not isinstance(generated, str) or not generated.endswith("Z"):
        raise ManifestError("generated_at_utc must be an ISO 8601 UTC timestamp ending in Z.")
    try:
        parsed = datetime.fromisoformat(generated[:-1] + "+00:00")
        if parsed.tzinfo is None or parsed.utcoffset().total_seconds() != 0:
            raise ValueError("UTC timezone is required")
    except ValueError as error:
        raise ManifestError("Invalid generated_at_utc timestamp.") from error
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        raise ManifestError("Manifest files must be a nonempty array.")
    expected = {}
    for item in entries:
        if not isinstance(item, dict):
            raise ManifestError("Each manifest file entry must be an object.")
        name = safe_relative_name(item.get("path"))
        if name in expected:
            raise ManifestError(f"Duplicate manifest path: {name!r}")
        size, digest = item.get("bytes"), item.get("sha256")
        if type(size) is not int or size < 0:
            raise ManifestError(f"Invalid byte count for {name!r}")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ManifestError(f"Invalid SHA-256 for {name!r}")
        expected[name] = {"bytes": size, "sha256": digest}
    return expected


def verify(args):
    root = evidence_root(args.root)
    manifest_path = local_path(args.manifest)
    if manifest_path == root or root in manifest_path.parents:
        raise ManifestError("Manifest must be outside the evidence root.")
    expected = load_manifest(manifest_path)
    current = {p.relative_to(root).as_posix(): p for p in tree_files(root)}
    added = sorted(current.keys() - expected.keys())
    missing = sorted(expected.keys() - current.keys())
    modified = [name for name in sorted(current.keys() & expected.keys())
                if fingerprint(current[name]) != expected[name]]
    if set(current) != {p.relative_to(root).as_posix() for p in tree_files(root)}:
        raise ManifestError("Evidence file inventory changed during verification; retry on a stable tree.")
    match = not (added or missing or modified)
    print(json.dumps({"status": "match" if match else "mismatch", "files_expected": len(expected),
                      "files_present": len(current), "added": added, "missing": missing,
                      "modified": modified}, ensure_ascii=True))
    return 0 if match else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    make = subparsers.add_parser("create", help="Create a new manifest without modifying originals.")
    make.add_argument("--root", required=True)
    make.add_argument("--output", required=True)
    check = subparsers.add_parser("verify", help="Compare originals with a saved manifest.")
    check.add_argument("--root", required=True)
    check.add_argument("--manifest", required=True)
    args = parser.parse_args()
    try:
        return create(args) if args.command == "create" else verify(args)
    except (ManifestError, OSError, ValueError, UnicodeError) as error:
        print(json.dumps({"status": "error", "error": str(error)}, ensure_ascii=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
