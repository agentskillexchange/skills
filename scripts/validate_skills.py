#!/usr/bin/env python3
"""validate_skills.py — Parser-backed canonical schema validator for ASE repo.

Usage:
  python3 scripts/validate_skills.py --all [--github-annotations] [--quiet]
  python3 scripts/validate_skills.py skills/my-skill/SKILL.md [--github-annotations]

Exit code 0 = all pass, 1 = one or more failures.
Deprecated compatibility warnings are reported but do not fail validation.
"""

import argparse
import re
import sys
from pathlib import Path

# ── Schema invariants ─────────────────────────────────────────────────────────
REQUIRED_FIELDS   = {"name", "slug", "description", "category", "framework", "verification"}
FORBIDDEN_FIELDS  = {"verification_status", "verified_metadata"}
VALID_VERIFICATION = {"listed", "security_reviewed"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
INSTALL_BOILERPLATE = "Copy this skill folder into your local skills directory"


def parse_frontmatter(text: str) -> tuple[dict, list[str]]:
    """Return (fields_dict, error_list). Values are raw stripped strings."""
    errors = []
    fields: dict = {}
    lines  = text.splitlines()

    if not lines or lines[0].strip() != "---":
        errors.append("Missing opening '---' frontmatter delimiter")
        return fields, errors

    end = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            end = i
            break

    if end is None:
        errors.append("Missing closing '---' frontmatter delimiter")
        return fields, errors

    fm_lines = lines[1:end]
    current_key = None
    current_list: list[str] = []

    def flush():
        nonlocal current_key, current_list
        if current_key:
            fields[current_key] = current_list if len(current_list) != 1 else current_list[0]
        current_key = None
        current_list = []

    for line in fm_lines:
        # list item
        if re.match(r"^  - ", line):
            current_list.append(line.strip()[2:].strip().strip('"').strip("'"))
            continue
        # key: value
        m = re.match(r'^([a-zA-Z_][a-zA-Z_0-9]*):\s*(.*)', line)
        if m:
            flush()
            current_key = m.group(1)
            val = m.group(2).strip().strip('"').strip("'")
            if val:
                current_list = [val]
            # else wait for sub-list
            continue
        # continuation / nested dict — keep current key
    flush()

    return fields, errors


def scalar(fields: dict, key: str) -> str:
    value = fields.get(key, "")
    if isinstance(value, list):
        value = value[0] if value else ""
    return str(value or "").strip()


def validate_file(path: Path, github_annotations: bool = False) -> tuple[list[str], list[str]]:
    """Return (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")

    fields, fm_errors = parse_frontmatter(text)
    errors.extend(fm_errors)

    # Forbidden fields (schema drift)
    for f in FORBIDDEN_FIELDS:
        if f in fields:
            errors.append(f"Schema drift: forbidden field '{f}' must not appear in public repo")

    # Required fields
    for f in REQUIRED_FIELDS:
        if f not in fields:
            errors.append(f"Missing required field: '{f}'")

    name = scalar(fields, "name")
    slug = scalar(fields, "slug")
    title = scalar(fields, "title")

    if name:
        if name == slug:
            errors.append("Field 'name' must be a human-readable display name, not the slug")
        if "\n" in name or not re.search(r"[A-Za-z0-9]", name):
            errors.append("Field 'name' must be non-empty human-readable text")

    if slug:
        expected_slug = path.parent.name
        if not SLUG_RE.match(slug):
            errors.append(f"Invalid slug '{slug}'; must be lowercase kebab-case")
        if slug != expected_slug:
            errors.append(f"Slug mismatch: frontmatter slug '{slug}' must equal containing directory '{expected_slug}'")

    if title:
        if not name:
            errors.append("Deprecated field 'title' may only appear with canonical 'name'")
        elif title != name:
            errors.append("Deprecated field 'title' must equal canonical 'name' while transition alias is allowed")
        else:
            warnings.append("Deprecated field 'title' is present; use 'name' only")

    # verification value
    ver = scalar(fields, "verification")
    if ver and ver not in VALID_VERIFICATION:
        errors.append(f"Invalid verification value '{ver}'; must be listed|security_reviewed")
    if ver == "security_reviewed" and INSTALL_BOILERPLATE in text:
        errors.append("Security-reviewed skill still contains generic skill-folder installation boilerplate")

    # H1 heading in body
    if "\n# " not in text and not text.startswith("# "):
        errors.append("Body missing H1 heading")

    # Scalar category / framework check (lists are allowed but flag if they contain > 1 in strict future)
    # Currently we allow lists; no error.

    if github_annotations and errors:
        rel = str(path)
        for err in errors:
            print(f"::error file={rel}::{err}")
    if github_annotations and warnings:
        rel = str(path)
        for warning in warnings:
            print(f"::warning file={rel}::{warning}")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="ASE parser-backed skill validator")
    parser.add_argument("files", nargs="*", help="SKILL.md files to validate")
    parser.add_argument("--all", action="store_true", dest="all_skills",
                        help="Validate all skills/ in repo")
    parser.add_argument("--github-annotations", action="store_true")
    parser.add_argument("--quiet", action="store_true",
                        help="Only print failures")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    targets: list[Path] = []

    if args.all_skills:
        targets = sorted((repo_root / "skills").glob("*/SKILL.md"))
    else:
        targets = [Path(f) for f in args.files]

    if not targets:
        print("No files to validate.", file=sys.stderr)
        sys.exit(0)

    pass_count = 0
    fail_count = 0
    warn_count = 0

    for path in targets:
        if not path.exists():
            print(f"MISSING: {path}")
            fail_count += 1
            continue
        errs, warns = validate_file(path, github_annotations=args.github_annotations)
        warn_count += len(warns)
        if errs:
            fail_count += 1
            if not args.quiet:
                print(f"FAIL  {path}")
                for e in errs:
                    print(f"      {e}")
            else:
                print(f"FAIL  {path}: {errs[0]}" + (f" (+{len(errs)-1} more)" if len(errs) > 1 else ""))
        else:
            pass_count += 1
            if not args.quiet:
                print(f"PASS  {path}")
                for w in warns:
                    print(f"      WARN: {w}")

    total = pass_count + fail_count
    print(f"\nValidation: {pass_count}/{total} passed, {fail_count} failed, {warn_count} warnings.")
    sys.exit(0 if fail_count == 0 else 1)


if __name__ == "__main__":
    main()
