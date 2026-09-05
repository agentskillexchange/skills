#!/usr/bin/env python3
"""Validate the public Bitwarden Lease skill without third-party packages."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    ".github/workflows/ci.yml",
    ".gitignore",
    "CONTRIBUTING.md",
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "SKILL.md",
    "agents/openai.yaml",
    "references/security-contract.md",
    "scripts/bitwarden_lease_broker.py",
    "scripts/bitwarden_lease_client.py",
    "scripts/install_bitwarden_lease_broker.py",
    "scripts/self_test.py",
    "scripts/validate_package.py",
}
FORBIDDEN_NAMES = {".env", "id_rsa", "id_ed25519", "secrets.json"}
FORBIDDEN_MARKERS = (
    "Olym" + "pus credential lease",
    "Application Support/" + "Axi" + "otic",
    "ai." + "axi" + "otic.bitwarden-lease",
    "Axi" + "otic",
    "Olym" + "pus",
    "Hephae" + "stus",
    "/" + "Users/",
)
SECRET_PATTERNS = (
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def fail(message: str) -> None:
    raise SystemExit(f"validation failed: {message}")


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.is_symlink():
            fail(f"symlink is not allowed: {path.relative_to(ROOT)}")
        if path.is_file():
            files.append(path)
    return files


def validate_frontmatter() -> None:
    lines = (ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        fail("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        fail("SKILL.md frontmatter is not closed")
    keys = {line.split(":", 1)[0] for line in lines[1:end] if ":" in line}
    if keys != {"name", "description"}:
        fail(f"unexpected SKILL.md frontmatter keys: {sorted(keys)}")
    if "name: bitwarden-lease" not in lines[1:end]:
        fail("SKILL.md name must be bitwarden-lease")


def main() -> None:
    files = text_files()
    relative_files = {str(path.relative_to(ROOT)) for path in files}
    missing = REQUIRED_FILES - relative_files
    if missing:
        fail(f"missing required files: {sorted(missing)}")
    for path in files:
        relative = path.relative_to(ROOT)
        if path.name in FORBIDDEN_NAMES:
            fail(f"forbidden file name: {relative}")
        data = path.read_text(encoding="utf-8")
        for marker in FORBIDDEN_MARKERS:
            if marker in data:
                fail(f"private marker {marker!r} in {relative}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(data):
                fail(f"credential-shaped content in {relative}")
    validate_frontmatter()
    metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "display_name: \"Bitwarden Lease\"" not in metadata:
        fail("agents/openai.yaml has stale display metadata")
    if "$bitwarden-lease" not in metadata:
        fail("agents/openai.yaml default prompt must invoke $bitwarden-lease")
    print("bitwarden_lease_package_validation=pass")


if __name__ == "__main__":
    main()
