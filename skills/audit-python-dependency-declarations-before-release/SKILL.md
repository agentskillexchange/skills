---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
description: "This ASE entry is built around Deptry, the open source Python dependency checker maintained in the osprey-oss/deptry project. The agent job here is narrow and practical: inspect a Python repository, compare real imports against pyproject.toml or other package declarations, and tell you where the dependency graph has drifted away from reality. That includes direct dependencies that are no longer used, imports that are missing from the declared dependency set, and transitive dependencies that currently resolve only because another package happens to pull them in. You invoke this skill when normal product usage is not enough because the task is not simply “run a linter” or “install a package checker.” The real task is to clean up dependency declarations before a release, harden a build so it stops relying on accidental transitive imports, or prepare a refactor branch for safer packaging and reproducible installs. An agent can run Deptry, classify the findings, decide which issues are safe auto-fixes versus which need human review, update manifests, and then rerun tests to confirm the cleanup did not break runtime behavior. The scope boundary keeps this from collapsing into a generic package-manager listing. This entry is specifically for dependency declaration hygiene in Python projects, not for full environment solving, vulnerability scanning, or generic static analysis. Integration points include Poetry and pyproject.toml -based repositories, CI quality gates, release preparation checklists, and pull request review loops where agents need a reliable way to surface dependency drift with concrete file-level findings. Upstream evidence is solid: official GitHub repository, PyPI package, dedicated docs site, tagged releases, MIT license, and active maintenance with recent commits."
source: "https://github.com/osprey-oss/deptry"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "osprey-oss/deptry"
  github_stars: 1359
---

# Audit Python dependency declarations for unused, missing, and transitive imports before release

This ASE entry is built around Deptry, the open source Python dependency checker maintained in the osprey-oss/deptry project. The agent job here is narrow and practical: inspect a Python repository, compare real imports against pyproject.toml or other package declarations, and tell you where the dependency graph has drifted away from reality. That includes direct dependencies that are no longer used, imports that are missing from the declared dependency set, and transitive dependencies that currently resolve only because another package happens to pull them in. You invoke this skill when normal product usage is not enough because the task is not simply “run a linter” or “install a package checker.” The real task is to clean up dependency declarations before a release, harden a build so it stops relying on accidental transitive imports, or prepare a refactor branch for safer packaging and reproducible installs. An agent can run Deptry, classify the findings, decide which issues are safe auto-fixes versus which need human review, update manifests, and then rerun tests to confirm the cleanup did not break runtime behavior. The scope boundary keeps this from collapsing into a generic package-manager listing. This entry is specifically for dependency declaration hygiene in Python projects, not for full environment solving, vulnerability scanning, or generic static analysis. Integration points include Poetry and pyproject.toml -based repositories, CI quality gates, release preparation checklists, and pull request review loops where agents need a reliable way to surface dependency drift with concrete file-level findings. Upstream evidence is solid: official GitHub repository, PyPI package, dedicated docs site, tagged releases, MIT license, and active maintenance with recent commits.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
