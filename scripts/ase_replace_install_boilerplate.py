#!/usr/bin/env python3
"""Replace generic ASE skill install boilerplate with source-backed guidance."""

from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path


PLACEHOLDER = "Copy this skill folder into your local skills directory"
INSTALL_HEADING_RE = re.compile(
    r"^(?:#{1,4}\s+)?(?:installation|install|setup|getting started|quick start|quickstart|usage|requirements|prerequisites)\b",
    re.I,
)
BAD_COMMAND_RE = re.compile(r"curl\b[^\n|]*\|\s*(?:sudo\s+)?(?:bash|sh)|sudo\s+(?:bash|sh)\b", re.I)
UNSAFE_EXTRACT_RE = re.compile(
    r"\bact\s+as\b|\b(?:run|execute)\s+(?:as|with)\s+(?:root|sudo|admin)\b|"
    r"\.kube/config\b|\b(?:admin|root|supervisor)\s+(?:override|authorization|approved)\b",
    re.I,
)
COMMAND_RE = re.compile(
    r"\b(?:brew|npm|pnpm|yarn|npx|pipx?|uv|cargo|go install|docker|docker compose|git clone|make|cmake|conda|gem|composer|pip install|python -m pip)\b",
    re.I,
)
COMMAND_START_RE = re.compile(
    r"^(?:\$+\s*)?(?:brew|npm|pnpm|yarn|npx|pipx?|uv|cargo|go install|docker|docker compose|git clone|make|cmake|conda|gem|composer|pip install|python -m pip)\b",
    re.I,
)
GENERIC_SENTENCES = (
    "copy this skill folder",
    "local skills directory",
    "symlink or copy the skill",
    "add the repo as a git submodule",
    "internal provisioning",
    "download the folder directly",
)
STRICT_NAV_LABELS = {
    "contents",
    "documentation",
    "installation",
    "introduction",
    "table of contents",
}
NUMBERED_TOC_RE = re.compile(r"^\d+(?:\.\d+)+\.?\s+[A-Z][^:]{0,90}\s*$")
DOTTED_TOC_RE = re.compile(r"^\S.{0,120}?\.{3,}\s*\d{1,4}\s*$")
MARKDOWN_HEADING_RE = re.compile(r"^#{1,6}\s+\S")
FENCE_LANGUAGE_RE = re.compile(
    r"^(?:bash|sh|shell|console|powershell|cmd|terminal|js|jsx|javascript|ts|tsx|typescript|json|yaml|yml|python|py)$",
    re.I,
)
CODE_ARTIFACT_RE = re.compile(
    r"^(?://|/\*|\*/)"
    r"|^(?:const|let|var|import|export|function|async\s+function|class)\b"
    r"|^module\.exports\b"
    r"|^require\("
)


def fetch_url(url: str, timeout: int = 10) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ASE boilerplate cleanup"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        raw = response.read(700_000)
    return raw.decode("utf-8", "replace")


def parse_frontmatter(text: str) -> tuple[list[str], dict[str, str], str]:
    if not text.startswith("---\n"):
        return [], {}, text
    end = text.find("\n---", 4)
    if end < 0:
        return [], {}, text
    frontmatter = text[4:end].splitlines()
    body = text[end + len("\n---") :].lstrip("\n")
    fields: dict[str, str] = {}
    for line in frontmatter:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match:
            value = match.group(2).strip().strip('"').strip("'")
            fields[match.group(1)] = value
    return frontmatter, fields, body


def render_frontmatter(lines: list[str], updates: dict[str, str]) -> str:
    rendered: list[str] = []
    seen = set()
    for line in lines:
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if match and match.group(1) in updates:
            key = match.group(1)
            rendered.append(f'{key}: "{updates[key]}"')
            seen.add(key)
        else:
            rendered.append(line)
    for key, value in updates.items():
        if key not in seen:
            rendered.append(f'{key}: "{value}"')
    return "---\n" + "\n".join(rendered) + "\n---\n\n"


def github_repo_from_url(source: str) -> str | None:
    parsed = urllib.parse.urlparse(source)
    if parsed.netloc.lower() not in {"github.com", "www.github.com"}:
        return None
    parts = [p for p in parsed.path.strip("/").split("/") if p]
    if len(parts) < 2:
        return None
    owner, repo = parts[0], parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    return f"{owner}/{repo}"


def candidate_urls(source: str) -> list[str]:
    repo = github_repo_from_url(source)
    if repo:
        names = [
            "README.md",
            "README.MD",
            "README.rst",
            "README.txt",
            "README",
            "docs/installation.md",
            "docs/install.md",
            "docs/getting-started.md",
            "docs/getting_started.md",
            "docs/quickstart.md",
            "docs/usage.md",
            "docs/usage/index.md",
            "docs/guide.md",
        ]
        urls = [
            f"https://raw.githubusercontent.com/{repo}/{branch}/{name}"
            for branch in ("HEAD", "main", "master")
            for name in names
        ]
        if repo.lower() == "nektos/act":
            urls = [
                "https://nektosact.com/installation/index.html",
                "https://nektosact.com/usage/index.html",
            ] + urls
        return urls
    return [source]


def strip_html(text: str) -> str:
    text = re.sub(r"<script\b[\s\S]*?</script>", " ", text, flags=re.I)
    text = re.sub(r"<style\b[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"</(?:p|div|li|h[1-6]|tr)>", "\n", text, flags=re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return html.unescape(text)


def normalize_lines(text: str) -> list[str]:
    if "<html" in text[:500].lower() or "<body" in text[:1000].lower():
        text = strip_html(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = []
    in_frontmatter = False
    for line in text.split("\n"):
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue
        clean = re.sub(r"^\s*>\s?", "", line).strip()
        clean = clean.replace(chr(96), "")
        clean = re.sub(r"\s+", " ", clean).strip()
        if clean:
            lines.append(clean)
    return lines


def extract_candidate_block(text: str) -> tuple[list[str], list[str], list[str]]:
    lines = normalize_lines(text)
    commands: list[str] = []
    caveats: list[str] = []
    usage: list[str] = []
    heading_score = 0
    fence = chr(96) * 3
    for raw in lines:
        line = raw.strip()
        if line.startswith(fence):
            continue
        if INSTALL_HEADING_RE.search(line):
            heading_score = 28
            continue
        score = heading_score
        command_like = bool(COMMAND_START_RE.search(line) or re.search(r"\b(?:install|run|use)\s+(?:with\s+)?(?:brew|npm|pnpm|yarn|npx|pipx?|uv|cargo|docker|git clone|make)\b", line, re.I))
        if command_like:
            score += 8
        if re.search(r"\b(?:requires?|prerequisites?|depends on|need to install|docker|node|python|go toolchain)\b", line, re.I):
            score += 4
        if re.search(r"\b(?:usage|run|example|quick start|getting started)\b", line, re.I):
            score += 3
        if score <= 0:
            heading_score = max(0, heading_score - 1)
            continue
        normalized = clean_extracted_line(line)
        if not normalized:
            heading_score = max(0, heading_score - 1)
            continue
        if len(normalized) > 220:
            normalized = normalized[:217].rstrip() + "..."
        low = normalized.lower()
        if any(g in low for g in GENERIC_SENTENCES):
            continue
        if BAD_COMMAND_RE.search(normalized):
            continue
        if UNSAFE_EXTRACT_RE.search(normalized):
            continue
        if command_like:
            if normalized not in commands:
                commands.append(normalized)
        elif re.search(r"\b(?:requires?|prerequisites?|depends on|docker|node|python|go toolchain|not supported|must)\b", normalized, re.I):
            if normalized not in caveats:
                caveats.append(normalized)
        else:
            if normalized not in usage:
                usage.append(normalized)
        heading_score = max(0, heading_score - 1)
        if len(commands) >= 5 and len(caveats) >= 2 and len(usage) >= 2:
            break
    return commands[:5], caveats[:3], usage[:3]


def clean_extracted_line(line: str) -> str | None:
    normalized = re.sub(r"^[-*+]\s+", "", line.strip())
    normalized = re.sub(r"^\d+[.)]\s+", "", normalized).strip()
    normalized = normalized.strip()
    if not normalized:
        return None
    label = re.sub(r"\s+", " ", normalized)
    label = re.sub(r"^(?:#+\s*)+", "", label).strip("*_ :").lower()
    if label in STRICT_NAV_LABELS:
        return None
    if MARKDOWN_HEADING_RE.match(normalized):
        return None
    if NUMBERED_TOC_RE.match(normalized):
        return None
    if DOTTED_TOC_RE.match(normalized):
        return None
    if FENCE_LANGUAGE_RE.match(normalized) or re.fullmatch(r"-{3,}|={3,}", normalized):
        return None
    if CODE_ARTIFACT_RE.match(normalized):
        return None
    return normalized


def fetch_source_material(source: str) -> tuple[str, str]:
    errors: list[str] = []
    for url in candidate_urls(source):
        try:
            text = fetch_url(url)
            if len(text.strip()) >= 120:
                return url, text
        except Exception as exc:
            errors.append(f"{url}: {exc}")
    raise RuntimeError("; ".join(errors[:3]) or "no source material fetched")


def source_link(source: str) -> str:
    return f"- Source: {source}"


def install_section(source: str, fetched_url: str, commands: list[str], caveats: list[str], usage: list[str]) -> str:
    bullets: list[str] = []
    if commands:
        bullets.append("Use the upstream install or setup path that matches your environment:")
        for cmd in commands[:4]:
            bullets.append(f"- {cmd}")
    if caveats:
        bullets.append("")
        bullets.append("Requirements and caveats from upstream:")
        for caveat in caveats[:3]:
            bullets.append(f"- {caveat}")
    if usage:
        bullets.append("")
        bullets.append("Basic usage or getting-started notes:")
        for item in usage[:3]:
            bullets.append(f"- {item}")
    bullets.append("")
    bullets.append(source_link(source))
    if fetched_url != source:
        bullets.append(f"- Extracted from upstream docs: {fetched_url}")
    return "## Installation\n\n" + "\n".join(bullets).strip() + "\n"


def weak_install(commands: list[str], caveats: list[str], usage: list[str]) -> bool:
    material = " ".join(commands + caveats + usage).lower()
    if PLACEHOLDER.lower() in material:
        return True
    if commands:
        return False
    return len(caveats) + len(usage) < 2


def replace_installation(body: str, section: str) -> str:
    pattern = re.compile(r"(^## Installation\s*\n[\s\S]*?)(?=^##\s+|\Z)", re.M)
    if pattern.search(body):
        return pattern.sub(section.rstrip() + "\n\n", body, count=1)
    source_match = re.search(r"^## Source\s*$", body, flags=re.M)
    if source_match:
        return body[: source_match.start()] + section.rstrip() + "\n\n" + body[source_match.start() :]
    return body.rstrip() + "\n\n" + section.rstrip() + "\n"


def process_file(path: Path, dry_run: bool = False, downgrade_only: bool = False) -> dict:
    if not path.exists():
        return {"path": str(path), "changed": False, "reason": "missing file skipped"}
    text = path.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        return {"path": str(path), "changed": False, "reason": "no placeholder"}
    frontmatter, fields, body = parse_frontmatter(text)
    source = fields.get("source", "").strip()
    original_verification = fields.get("verification", "").strip()
    result = {
        "path": str(path),
        "source": source,
        "original_verification": original_verification,
        "changed": False,
        "enriched": False,
        "downgraded": False,
        "error": "",
    }
    try:
        if downgrade_only:
            raise RuntimeError("forced downgrade for unresolved boilerplate after extraction pass")
        if not source:
            raise RuntimeError("missing source frontmatter")
        fetched_url, source_text = fetch_source_material(source)
        commands, caveats, usage = extract_candidate_block(source_text)
        if weak_install(commands, caveats, usage):
            raise RuntimeError("no substantive install or usage guidance extracted")
        body = replace_installation(body, install_section(source, fetched_url, commands, caveats, usage))
        verification = original_verification
        result.update({"enriched": True, "fetched_url": fetched_url, "commands": commands[:3]})
    except Exception as exc:
        verification = "listed"
        result.update({"downgraded": original_verification != "listed", "error": str(exc)[:500]})
        fallback = (
            "## Installation\n\n"
            "No source-backed install or usage instructions could be extracted automatically. "
            "Review the upstream project before running this skill in a sensitive workflow.\n\n"
            f"{source_link(source) if source else '- Source: not available'}\n"
        )
        body = replace_installation(body, fallback)
    new_text = render_frontmatter(frontmatter, {"verification": verification}) + body
    if PLACEHOLDER in new_text:
        result["error"] = (result["error"] + "; " if result["error"] else "") + "placeholder remained after rewrite"
        new_text = new_text.replace(PLACEHOLDER, "Review the upstream source instructions before installing or invoking this tool")
    if new_text != text:
        result["changed"] = True
        if not dry_run:
            if not path.exists():
                result["changed"] = False
                result["reason"] = "missing file skipped before write"
                return result
            path.write_text(new_text, encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="*", help="Specific SKILL.md files to process")
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--downgrade-only", action="store_true", help="Do not fetch; replace remaining boilerplate with fallback and set verification listed")
    parser.add_argument("--report", default="boilerplate-cleanup-report.json")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parent.parent
    if args.only:
        targets = [Path(p) if Path(p).is_absolute() else repo / p for p in args.only]
    else:
        targets = sorted(p for p in (repo / "skills").glob("*/SKILL.md") if PLACEHOLDER in p.read_text(encoding="utf-8"))

    results: list[dict] = []
    if len(targets) <= 1 or args.workers <= 1:
        for target in targets:
            results.append(process_file(target, dry_run=args.dry_run, downgrade_only=args.downgrade_only))
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [executor.submit(process_file, target, args.dry_run, args.downgrade_only) for target in targets]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())

    results.sort(key=lambda item: item["path"])
    summary = {
        "targets": len(targets),
        "changed": sum(1 for item in results if item.get("changed")),
        "enriched": sum(1 for item in results if item.get("enriched")),
        "downgraded": sum(1 for item in results if item.get("downgraded")),
        "failed_extraction": sum(1 for item in results if item.get("error") and not item.get("enriched")),
        "results": results,
    }
    report_path = Path(args.report)
    if not report_path.is_absolute():
        report_path = repo / report_path
    if not args.dry_run:
        report_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=2))
    if args.dry_run:
        for item in results[:20]:
            print(json.dumps(item, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
