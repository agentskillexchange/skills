#!/usr/bin/env python3
"""Parser-backed validator for Agent Skill Exchange SKILL.md files.

This replaces the older grep/sed validator with real YAML parsing, duplicate-key
checks, typed field validation, taxonomy/verification enums, body checks, and
GitHub Actions annotations.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

try:
    import yaml
except ImportError as exc:  # pragma: no cover - exercised in environments without PyYAML
    print("PyYAML is required. Install with: python3 -m pip install PyYAML", file=sys.stderr)
    raise SystemExit(2) from exc


VALID_VERIFICATION = {"listed", "security_reviewed"}

# Public categories documented in spec/SKILL_SPEC.md. `General` and
# `Uncategorized` are allowed as transitional live taxonomy buckets so the
# validator can gate generated output before the taxonomy backlog is fully gone.
VALID_CATEGORIES = {
    "Browser Automation",
    "Calendar, Email & Productivity",
    "CI/CD Integrations",
    "Code Quality & Review",
    "Content Writing & SEO",
    "Data Extraction & Transformation",
    "Developer Tools",
    "Image & Creative Automation",
    "Integrations & Connectors",
    "Library & API Reference",
    "Media & Transcription",
    "Monitoring & Alerts",
    "Research & Scraping",
    "Runbooks & Diagnostics",
    "Security & Verification",
    "Templates & Workflows",
    "WordPress & CMS",
    "General",
    "Uncategorized",
}

VALID_FRAMEWORKS = {
    "Any",
    "ChatGPT Agents",
    "Claude Agents",
    "Claude Code",
    "Codex",
    "Cursor",
    "Custom Agents",
    "Gemini",
    "Google Workspace",
    "MCP",
    "Multi-Framework",
    "OpenClaw",
    "WordPress",
}

REQUIRED_FIELDS = ("title", "slug", "description", "category", "framework", "verification")
DEPRECATED_PUBLIC_FIELDS = ("name", "verification_status", "verified_metadata")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
H1_RE = re.compile(r"^#\s+\S+", re.M)
WORD_RE = re.compile(r"\b[\w'-]+\b")


class UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate mapping keys."""


def construct_mapping(loader: UniqueKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key ({key!r})",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


@dataclass
class ValidationError:
    path: Path
    message: str
    line: int = 1


def github_escape(value: str) -> str:
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A").replace(":", "%3A").replace(",", "%2C")


def split_frontmatter(text: str, path: Path) -> tuple[str | None, str, list[ValidationError]]:
    errors: list[ValidationError] = []
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text, [ValidationError(path, "Missing YAML frontmatter opening delimiter (---)", 1)]

    end_line = None
    for idx, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            end_line = idx
            break

    if end_line is None:
        return None, text, [ValidationError(path, "Missing YAML frontmatter closing delimiter (---)", 1)]

    frontmatter = "".join(lines[1 : end_line - 1])
    body = "".join(lines[end_line:])
    if not frontmatter.strip():
        errors.append(ValidationError(path, "Empty YAML frontmatter", 1))
    return frontmatter, body, errors


def field_line(frontmatter: str, field: str) -> int:
    for i, line in enumerate(frontmatter.splitlines(), start=2):
        if re.match(rf"^{re.escape(field)}\s*:", line):
            return i
    return 2


def scalar_string(value: Any, field: str, path: Path, line: int, errors: list[ValidationError]) -> str | None:
    if not isinstance(value, str):
        errors.append(ValidationError(path, f"Field `{field}` must be a string", line))
        return None
    if not value.strip():
        errors.append(ValidationError(path, f"Field `{field}` must not be empty", line))
        return None
    return value.strip()


def labels_for_enum(value: str, allowed: set[str]) -> list[str]:
    # The canonical shape is scalar. A small amount of generated legacy data uses
    # comma-separated multi-label values; first honor exact labels like
    # `Calendar, Email & Productivity`, then validate split multi-label fallbacks.
    if value in allowed:
        return [value]
    return [part.strip() for part in value.split(", ") if part.strip()]


def is_url_like(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_skill(path: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []
    if not path.exists():
        return [ValidationError(path, "File not found", 1)]
    if not path.is_file():
        return [ValidationError(path, "Path is not a file", 1)]

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return [ValidationError(path, "File must be valid UTF-8", 1)]

    if not text.strip():
        return [ValidationError(path, "File is empty", 1)]

    frontmatter, body, fm_errors = split_frontmatter(text, path)
    errors.extend(fm_errors)
    if frontmatter is None:
        return errors

    try:
        data = yaml.load(frontmatter, Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        line = int(mark.line + 2) if mark is not None else 2
        errors.append(ValidationError(path, f"Invalid YAML frontmatter: {exc}", line))
        return errors

    if not isinstance(data, dict):
        errors.append(ValidationError(path, "YAML frontmatter must be a mapping/object", 2))
        return errors

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(ValidationError(path, f"Missing required field: `{field}`", 2))

    for field in DEPRECATED_PUBLIC_FIELDS:
        if field in data:
            errors.append(ValidationError(path, f"Deprecated public field present: `{field}`", field_line(frontmatter, field)))

    title = scalar_string(data.get("title"), "title", path, field_line(frontmatter, "title"), errors) if "title" in data else None
    slug = scalar_string(data.get("slug"), "slug", path, field_line(frontmatter, "slug"), errors) if "slug" in data else None
    description = scalar_string(data.get("description"), "description", path, field_line(frontmatter, "description"), errors) if "description" in data else None
    category = scalar_string(data.get("category"), "category", path, field_line(frontmatter, "category"), errors) if "category" in data else None
    framework = scalar_string(data.get("framework"), "framework", path, field_line(frontmatter, "framework"), errors) if "framework" in data else None
    verification = scalar_string(data.get("verification"), "verification", path, field_line(frontmatter, "verification"), errors) if "verification" in data else None

    if slug:
        if not SLUG_RE.match(slug):
            errors.append(ValidationError(path, "Field `slug` must be lowercase kebab-case", field_line(frontmatter, "slug")))
        if path.parent.name != slug:
            errors.append(ValidationError(path, f"Field `slug` must match directory name `{path.parent.name}`", field_line(frontmatter, "slug")))

    if category:
        labels = labels_for_enum(category, VALID_CATEGORIES)
        unknown = [label for label in labels if label not in VALID_CATEGORIES]
        if unknown:
            errors.append(ValidationError(path, f"Unknown category value(s): {', '.join(unknown)}", field_line(frontmatter, "category")))

    if framework:
        labels = labels_for_enum(framework, VALID_FRAMEWORKS)
        unknown = [label for label in labels if label not in VALID_FRAMEWORKS]
        if unknown:
            errors.append(ValidationError(path, f"Unknown framework value(s): {', '.join(unknown)}", field_line(frontmatter, "framework")))

    if verification and verification not in VALID_VERIFICATION:
        if verification == "verified_metadata":
            msg = "Invalid public verification value: `verified_metadata` must export as `listed`"
        else:
            msg = "Invalid verification value: must be `listed` or `security_reviewed`"
        errors.append(ValidationError(path, msg, field_line(frontmatter, "verification")))

    source = data.get("source")
    if source is not None:
        source_value = scalar_string(source, "source", path, field_line(frontmatter, "source"), errors)
        if source_value and not is_url_like(source_value):
            errors.append(ValidationError(path, "Field `source` must be an http(s) URL", field_line(frontmatter, "source")))

    github_stars = data.get("github_stars")
    if github_stars is not None and (not isinstance(github_stars, int) or isinstance(github_stars, bool) or github_stars < 0):
        errors.append(ValidationError(path, "Field `github_stars` must be a non-negative number", field_line(frontmatter, "github_stars")))

    tool_ecosystem = data.get("tool_ecosystem")
    if tool_ecosystem is not None:
        if not isinstance(tool_ecosystem, dict):
            errors.append(ValidationError(path, "Field `tool_ecosystem` must be an object", field_line(frontmatter, "tool_ecosystem")))
        else:
            for numeric in ("github_stars", "npm_weekly_downloads"):
                if numeric in tool_ecosystem:
                    value = tool_ecosystem[numeric]
                    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                        errors.append(ValidationError(path, f"tool_ecosystem.{numeric} must be a non-negative number", field_line(frontmatter, "tool_ecosystem")))
            for string_field in ("tool", "github_repo", "npm_package", "license"):
                if string_field in tool_ecosystem and not isinstance(tool_ecosystem[string_field], str):
                    errors.append(ValidationError(path, f"tool_ecosystem.{string_field} must be a string", field_line(frontmatter, "tool_ecosystem")))
            if "maintained" in tool_ecosystem and not isinstance(tool_ecosystem["maintained"], bool):
                errors.append(ValidationError(path, "tool_ecosystem.maintained must be a boolean", field_line(frontmatter, "tool_ecosystem")))

    if not body.strip():
        errors.append(ValidationError(path, "Markdown body is empty", 1))
    else:
        if not H1_RE.search(body):
            errors.append(ValidationError(path, "Markdown body must contain an H1 heading (`# ...`)", 1))
        word_count = len(WORD_RE.findall(body))
        if word_count < 30:
            errors.append(ValidationError(path, f"Markdown body is too thin ({word_count} words; minimum 30)", 1))

    return errors


def discover_skill_files(inputs: Iterable[str]) -> list[Path]:
    files: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            files.extend(sorted(path.glob("*/SKILL.md")))
        else:
            files.append(path)
    return files


def print_errors(errors: list[ValidationError], github_annotations: bool) -> None:
    for err in errors:
        if github_annotations:
            print(f"::error file={github_escape(str(err.path))},line={err.line},title=Skill validation::{github_escape(err.message)}")
        print(f"❌ {err.path}:{err.line}: {err.message}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate ASE SKILL.md files with a real YAML parser.")
    parser.add_argument("paths", nargs="*", help="SKILL.md files or directories containing skill folders")
    parser.add_argument("--all", action="store_true", help="Validate all skills under ./skills")
    parser.add_argument("--github-annotations", action="store_true", help="Emit GitHub Actions ::error annotations")
    parser.add_argument("--quiet", action="store_true", help="Only print errors and summary")
    args = parser.parse_args(argv)

    inputs = list(args.paths)
    if args.all:
        inputs.append("skills")
    if not inputs:
        parser.error("provide one or more SKILL.md paths/directories, or use --all")

    files = discover_skill_files(inputs)
    if not files:
        print("No SKILL.md files found", file=sys.stderr)
        return 1

    all_errors: list[ValidationError] = []
    for path in files:
        errors = validate_skill(path)
        if errors:
            all_errors.extend(errors)
        elif not args.quiet:
            print(f"✅ {path}")

    if all_errors:
        print_errors(all_errors, args.github_annotations)
        print(f"\nFAIL — {len(all_errors)} error(s) across {len(files)} file(s)")
        return 1

    print(f"✅ PASS — {len(files)} file(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
