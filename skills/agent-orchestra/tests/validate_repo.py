#!/usr/bin/env python3
"""Dependency-free structural checks for the public skill repository."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path}: missing YAML frontmatter"
    block = text.split("---\n", 2)[1]
    values = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            values[key] = value.strip()
    return values


def main() -> None:
    required = ["README.md", "SKILL.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md"]
    for rel in required:
        assert (ROOT / rel).is_file(), f"missing {rel}"

    skill = frontmatter(ROOT / "SKILL.md")
    assert skill["name"] == "agent-orchestra"
    assert len(skill["name"]) <= 64
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill["name"])
    assert 1 <= len(skill["description"]) <= 1024
    variant = ROOT / "variants" / "token-efficient" / "SKILL.md"
    variant_skill = frontmatter(variant)
    assert variant_skill["name"] == "token-efficient-orchestra"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", variant_skill["name"])
    assert 1 <= len(variant_skill["description"]) <= 1024

    public_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.rglob("*")
        if path.is_file() and path != Path(__file__) and ".git" not in path.parts
        and "__pycache__" not in path.parts
    )
    # Detect leak *classes* without committing private project or host names as
    # fixtures in the public repository.
    forbidden = [
        r"/(?:Users|home)/[^/\s]+",
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][^'\"]+",
    ]
    for pattern in forbidden:
        assert not re.search(pattern, public_text, re.IGNORECASE), f"private/provider leak: {pattern}"
    print("agent-orchestra repository validation: ok")


if __name__ == "__main__":
    main()
