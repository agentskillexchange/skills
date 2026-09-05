#!/usr/bin/env python3
"""Validate the public Doppel package without third-party dependencies."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "SKILL.md",
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    ".gitignore",
    "agents/openai.yaml",
    "schema/voice-manifest.schema.json",
    "scripts/build_voice_context.py",
    "references/safety-and-consent.md",
}
SENSITIVE_PARTS = {"corpus", "corpora", "profiles", "profile_exports", "private_sources"}
PERSONAL_PATH_MARKERS = ("/" + "Users" + "/", "C:" + "\\Users\\")


def tracked_files(root: Path = ROOT) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"], cwd=root, check=False, capture_output=True, text=True
    )
    if result.returncode == 0:
        return [root / line for line in result.stdout.splitlines() if line]
    return [path for path in root.rglob("*") if path.is_file() and ".git" not in path.parts]


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    missing = sorted(item for item in REQUIRED if not (root / item).is_file())
    if missing:
        errors.append("Missing required files: " + ", ".join(missing))

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        if not skill.startswith("---\nname: doppel\ndescription: "):
            errors.append("SKILL.md needs valid name and description frontmatter")
        for phrase in ("final ratifier", "Refuse third-party impersonation", "Never send"):
            if phrase not in skill:
                errors.append(f"SKILL.md is missing safety phrase: {phrase}")

    for path in tracked_files(root):
        relative = path.relative_to(root)
        if any(part in SENSITIVE_PARTS for part in relative.parts):
            errors.append(f"Sensitive directory is tracked: {relative}")
        if re.fullmatch(r"voice-manifest(?:\..+)?\.local\.json", relative.name):
            errors.append(f"Local manifest is tracked: {relative}")
        if path.suffix.lower() in {".md", ".py", ".json", ".yml", ".yaml"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            if any(marker in text for marker in PERSONAL_PATH_MARKERS):
                errors.append(f"Personal absolute path found: {relative}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("doppel package validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
