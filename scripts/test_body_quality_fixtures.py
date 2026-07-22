#!/usr/bin/env python3
"""Regression fixtures for generated SKILL.md Installation quality."""

from __future__ import annotations

import tempfile
from pathlib import Path

from ase_body_quality_gate import scan_file


def skill_markdown(slug: str, verification: str, installation: str, *, source: str, repo: str = "") -> str:
    tool_ecosystem = f'\ntool_ecosystem:\n  github_repo: "{repo}"' if repo else ""
    return f'''---
name: "Fixture {slug}"
slug: "{slug}"
description: "A focused body-quality regression fixture for installation guidance."
category: "Developer Tools"
framework: "Multi-Framework"
verification: "{verification}"
source: "{source}"{tool_ecosystem}
---

# Fixture {slug}

## Installation

{installation.strip()}

## Usage

Run the documented workflow in a sandbox and verify its output.
'''


CASES = [
    {
        "name": "elves_prose_as_install_command_security_reviewed_fails",
        "slug": "elves-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/aigorahub/elves",
        "repo": "aigorahub/elves",
        "installation": "- make mistakes. Always review the PR before merging.",
        "pass": False,
        "reason": "prose or non-install text classified as command",
    },
    {
        "name": "gaai_duplicate_truncated_details_security_reviewed_fails",
        "slug": "gaai-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/Fr-e-d/GAAI-framework",
        "repo": "Fr-e-d/GAAI-framework",
        "installation": """- git clone https://github.com/Fr-e-d/GAAI-framework.git /tmp/gaai
- git clone https://github.com/Fr-e-d/GAAI-framework.git /tmp/gaai
- git clone https://github.com/Fr-e-d/GAAI-framework.git /tmp/gaai && \\
- <details open>""",
        "pass": False,
        "reason": "raw README/HTML fragment in Installation section",
    },
    {
        "name": "honey_unrelated_packages_security_reviewed_fails",
        "slug": "honey-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/Green-PT/honey-for-devs",
        "repo": "Green-PT/honey-for-devs",
        "installation": """- npx pxpipe-proxy export --json src/
- pip install ecologits""",
        "pass": False,
        "reason": "package/tool command is not source-aligned",
    },
    {
        "name": "hcom_build_test_uninstall_only_security_reviewed_fails",
        "slug": "hcom-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/aannoo/hcom",
        "repo": "aannoo/hcom",
        "installation": """- brew uninstall hcom
- cargo build
- cargo test""",
        "pass": False,
        "reason": "only uninstall/test/benchmark/build commands found",
    },
    {
        "name": "socraticode_badges_features_links_security_reviewed_fails",
        "slug": "socraticode-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/giancarloerra/SocratiCode",
        "repo": "giancarloerra/SocratiCode",
        "installation": """- <a href=\"https://nodejs.org/\"><img src=\"https://img.shields.io/badge/node-18-green.svg\"></a>
- Features: private and local by default
- [Quick Start](#quick-start)""",
        "pass": False,
        "reason": "raw README/HTML fragment in Installation section",
    },
    {
        "name": "stitch_valid_commands_with_details_security_reviewed_fails",
        "slug": "stitch-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/google-labs-code/stitch-skills",
        "repo": "google-labs-code/stitch-skills",
        "installation": """- npx skills add google-labs-code/stitch-skills
- <details open>""",
        "pass": False,
        "reason": "raw README/HTML fragment in Installation section",
    },
    {
        "name": "valid_npm_install_security_reviewed_passes",
        "slug": "widget-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/acme/widget",
        "repo": "acme/widget",
        "installation": "```bash\nnpm install widget\n```",
        "pass": True,
    },
    {
        "name": "valid_pip_uv_install_security_reviewed_passes",
        "slug": "widget-cli-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/acme/widget-cli",
        "repo": "acme/widget-cli",
        "installation": "```bash\nuv tool install widget-cli\n```",
        "pass": True,
    },
    {
        "name": "valid_git_clone_copy_destination_security_reviewed_passes",
        "slug": "clone-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/acme/clone-tool",
        "repo": "acme/clone-tool",
        "installation": """```bash
git clone https://github.com/acme/clone-tool.git
```
Copy the configuration file into your agent workspace.""",
        "pass": True,
    },
    {
        "name": "valid_manual_setup_no_shell_security_reviewed_passes",
        "slug": "manual-setup-install-quality-fixture",
        "verification": "security_reviewed",
        "source": "https://github.com/acme/manual-setup",
        "repo": "acme/manual-setup",
        "installation": "Copy the plugin folder into your agent workspace and configure the API key as an environment variable.",
        "pass": True,
    },
    {
        "name": "listed_safe_fallback_passes",
        "slug": "listed-fallback-install-quality-fixture",
        "verification": "listed",
        "source": "https://github.com/acme/listed-fallback",
        "repo": "acme/listed-fallback",
        "installation": "No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.",
        "pass": True,
    },
]


def main() -> int:
    mismatches: list[str] = []
    with tempfile.TemporaryDirectory(prefix="ase-body-quality-fixtures-") as temp:
        root = Path(temp)
        for case in CASES:
            path = root / case["slug"] / "SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                skill_markdown(
                    case["slug"],
                    case["verification"],
                    case["installation"],
                    source=case["source"],
                    repo=case["repo"],
                ),
                encoding="utf-8",
            )
            report = scan_file(path)
            issues = report["installation_issues"]
            passed = not issues
            expected = case["pass"]
            print(f'{case["name"]}: {"PASS" if passed else "FAIL"} (expected {"PASS" if expected else "FAIL"})')
            if passed != expected:
                mismatches.append(f'{case["name"]}: expected pass={expected}, issues={issues}')
                continue
            expected_reason = case.get("reason")
            if expected_reason and expected_reason not in {issue["reason"] for issue in issues}:
                mismatches.append(f'{case["name"]}: missing reason {expected_reason!r}, issues={issues}')

    if mismatches:
        print("\nFixture mismatches:")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1
    print(f"\nPASS: {len(CASES)}/{len(CASES)} body-quality fixture(s) matched expected results")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
