#!/usr/bin/env python3
"""Overlay generated aggregate verification values from cleaned SKILL.md files.

Generators may start from live ASE API data, but the public repo can make a
later trust decision after source-backed body cleanup. This script makes the
cleaned repo frontmatter canonical for generated aggregate files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


PLACEHOLDER = "Copy this skill folder into your local skills directory"
VALID_VERIFICATION = {"listed", "security_reviewed"}
DISPLAY_LABEL = {
    "listed": "Published",
    "security_reviewed": "Security Reviewed",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return fields


def frontmatter_map(repo: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for path in sorted((repo / "skills").glob("*/SKILL.md")):
        fields = parse_frontmatter(path.read_text(encoding="utf-8"))
        slug = fields.get("slug") or path.parent.name
        verification = fields.get("verification", "")
        if verification not in VALID_VERIFICATION:
            raise SystemExit(f"{path}: invalid verification value {verification!r}")
        values[slug] = verification
    return values


def update_json_file(path: Path, verification_by_slug: dict[str, str]) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    skills = data.get("skills")
    if not isinstance(skills, list):
        return 0
    changed = 0
    for item in skills:
        slug = item.get("slug")
        if slug in verification_by_slug and item.get("verification") != verification_by_slug[slug]:
            item["verification"] = verification_by_slug[slug]
            changed += 1
    if "total" in data:
        data["total"] = len(skills)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed


def replace_badge_count(text: str, security_reviewed: int) -> str:
    encoded = f"{security_reviewed:,}".replace(",", "%2C")
    text = re.sub(
        r"(security_reviewed-)([0-9%2C,]+)(-10b981\?style=for-the-badge)",
        rf"security--reviewed-{encoded}\g<3>",
        text,
    )
    return re.sub(
        r"(security--reviewed-)([0-9%2C,]+)(-10b981\?style=for-the-badge)",
        rf"\g<1>{encoded}\g<3>",
        text,
    )


def update_summary_docs(repo: Path, counts: Counter[str]) -> None:
    readme = repo / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        text = replace_badge_count(text, counts["security_reviewed"])
        text = re.sub(
            r"(\| 🛡️ \*\*Security Reviewed\*\* \| )([0-9,]+)( \| Scanned for malicious patterns, prompt injection, and unsafe instructions \|)",
            rf"\g<1>{counts['security_reviewed']:,}\g<3>",
            text,
        )
        readme.write_text(text, encoding="utf-8")

    catalog = repo / "CATALOG.md"
    if catalog.exists():
        text = catalog.read_text(encoding="utf-8")
        text = re.sub(
            r"(\*\*[0-9,]+ published skills\*\* across \*\*[0-9,]+ categories\*\* · )([0-9,]+)( security reviewed)",
            rf"\g<1>{counts['security_reviewed']:,}\g<3>",
            text,
            count=1,
        )
        catalog.write_text(text, encoding="utf-8")


def update_markdown_tier_tables(repo: Path, verification_by_slug: dict[str, str]) -> int:
    targets = [repo / "CATALOG.md"]
    targets.extend(sorted((repo / "categories").glob("**/README.md")))
    targets.extend([repo / "TOP-STARS.md", repo / "TOP-DOWNLOADS.md"])
    changed_files = 0
    link_re = re.compile(r"(\]\((?:\.\./)?(?:\.\./)?skills/([^/)]+)/\).*?\| )(?P<tier>Published|Security Reviewed)( \|)")
    for path in targets:
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")

        def repl(match: re.Match[str]) -> str:
            slug = match.group(2)
            expected = DISPLAY_LABEL.get(verification_by_slug.get(slug, "listed"), "Published")
            return match.group(1) + expected + match.group(4)

        updated = link_re.sub(repl, original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
    return changed_files


def update_llms(path: Path, verification_by_slug: dict[str, str]) -> int:
    if not path.exists():
        return 0
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = 0
    current_slug = ""
    for i, line in enumerate(lines):
        if line.startswith("slug: "):
            current_slug = line.split(":", 1)[1].strip()
        elif line.startswith("verification: ") and current_slug in verification_by_slug:
            expected = f"verification: {DISPLAY_LABEL[verification_by_slug[current_slug]]}"
            if line != expected:
                lines[i] = expected
                changed += 1
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def mismatch_counts(repo: Path, verification_by_slug: dict[str, str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for filename in ("skills.json", "openclaw.json", "codex.json"):
        path = repo / filename
        data = json.loads(path.read_text(encoding="utf-8"))
        skills = data.get("skills", [])
        counts[filename] = sum(
            1
            for item in skills
            if verification_by_slug.get(item.get("slug", "")) != item.get("verification")
        )
    return counts


def placeholder_counts(repo: Path) -> tuple[int, int]:
    placeholder = 0
    placeholder_security_reviewed = 0
    for path in (repo / "skills").glob("*/SKILL.md"):
        text = path.read_text(encoding="utf-8")
        if PLACEHOLDER in text:
            placeholder += 1
            if re.search(r'^verification:\s*"security_reviewed"', text, re.M):
                placeholder_security_reviewed += 1
    return placeholder, placeholder_security_reviewed


def stale_count_refs(repo: Path) -> list[str]:
    targets = ["README.md", "CATALOG.md", "skills.json", "openclaw.json", "codex.json", "llms.txt"]
    hits: list[str] = []
    pattern = re.compile(r"2,466|2466|2%2C466")
    for name in targets:
        path = repo / name
        if not path.exists():
            continue
        for idx, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                hits.append(f"{name}:{idx}:{line.strip()}")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    verification_by_slug = frontmatter_map(repo)
    counts = Counter(verification_by_slug.values())

    if not args.check:
        json_updates = {
            name: update_json_file(repo / name, verification_by_slug)
            for name in ("skills.json", "openclaw.json", "codex.json")
        }
        update_summary_docs(repo, counts)
        md_files = update_markdown_tier_tables(repo, verification_by_slug)
        llms_updates = update_llms(repo / "llms.txt", verification_by_slug)
    else:
        json_updates = {}
        md_files = 0
        llms_updates = 0

    mismatches = mismatch_counts(repo, verification_by_slug)
    placeholder, placeholder_security_reviewed = placeholder_counts(repo)
    stale_refs = stale_count_refs(repo)
    ok = (
        all(value == 0 for value in mismatches.values())
        and placeholder == 0
        and placeholder_security_reviewed == 0
        and not stale_refs
    )
    result: dict[str, Any] = {
        "ok": ok,
        "total": len(verification_by_slug),
        "verification_counts": dict(counts),
        "json_updates": json_updates,
        "markdown_files_touched": md_files,
        "llms_verification_updates": llms_updates,
        "mismatches": mismatches,
        "placeholder_count": placeholder,
        "placeholder_security_reviewed_count": placeholder_security_reviewed,
        "stale_count_refs": stale_refs,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
