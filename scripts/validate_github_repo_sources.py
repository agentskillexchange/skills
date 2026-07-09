#!/usr/bin/env python3
"""Validate GitHub repo-root source claims in changed ASE skill files.

This is intentionally narrow and network-backed: use it in PR/import gates for
changed files, not as part of full-catalog offline schema validation.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


SOURCE_RE = re.compile(r'^source:\s*["\']?([^"\'\s]+)["\']?\s*$')
GITHUB_REPO_RE = re.compile(r'^\s*github_repo:\s*["\']?([^"\'\s]+)["\']?\s*$')


def github_repo_from_root_url(url: str) -> str | None:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [p for p in parsed.path.strip("/").split("/") if p]
    if len(parts) != 2:
        return None
    repo = f"{parts[0]}/{parts[1]}"
    if repo.endswith(".git"):
        repo = repo[:-4]
    return repo


def parse_claims(path: Path) -> tuple[str | None, str | None]:
    source = None
    github_repo = None
    in_frontmatter = False
    frontmatter_seen = False
    in_tool_ecosystem = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.strip() == "---":
            if not frontmatter_seen:
                frontmatter_seen = True
                in_frontmatter = True
                continue
            break
        if not in_frontmatter:
            continue

        source_match = SOURCE_RE.match(line)
        if source_match:
            source = source_match.group(1)
            in_tool_ecosystem = False
            continue
        if re.match(r"^tool_ecosystem:\s*$", line):
            in_tool_ecosystem = True
            continue
        if line and not line.startswith(" "):
            in_tool_ecosystem = False
        if in_tool_ecosystem:
            repo_match = GITHUB_REPO_RE.match(line)
            if repo_match:
                github_repo = repo_match.group(1)

    return source, github_repo


def repo_exists(repo: str) -> tuple[bool, str]:
    url = f"https://api.github.com/repos/{repo}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ASE source validator",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return 200 <= resp.status < 300, str(resp.status)
    except urllib.error.HTTPError as exc:
        return False, str(exc.code)
    except Exception as exc:  # network/DNS errors should block source-backed imports
        return False, exc.__class__.__name__


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Changed SKILL.md files to check")
    args = parser.parse_args()

    errors: list[str] = []
    checked: set[str] = set()
    for file_name in args.files:
        path = Path(file_name)
        if not path.exists() or path.name != "SKILL.md":
            continue
        source, github_repo = parse_claims(path)

        source_repo = github_repo_from_root_url(source or "")
        claims = []
        if source_repo:
            claims.append(("source", source_repo))
        if github_repo:
            claims.append(("tool_ecosystem.github_repo", github_repo))

        for field, repo in claims:
            normalized = repo.strip().removeprefix("https://github.com/").strip("/")
            key = normalized.lower()
            if key in checked:
                continue
            checked.add(key)
            ok, status = repo_exists(normalized)
            if not ok:
                errors.append(f"{path}: {field} claims GitHub repo '{normalized}', but API returned {status}")

    if errors:
        for error in errors:
            print(f"FAIL  {error}")
        return 1

    print(f"GitHub source validation passed for {len(checked)} repo claim(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
