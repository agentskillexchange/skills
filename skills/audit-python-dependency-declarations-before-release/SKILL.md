---
title: "Audit Python dependency declarations for unused, missing, and transitive imports before release"
description: "Use Deptry when an agent needs to verify that a Python project’s declared dependencies still match the imports the code actually uses. The agent scans the codebase, flags unused direct dependencies, missing declarations, and transitive imports that only work by accident, then turns the findings into cleanup commits or release blockers."
verification: security_reviewed
source: "https://github.com/osprey-oss/deptry"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
---

# Audit Python dependency declarations for unused, missing, and transitive imports before release

This ASE entry is built around Deptry, the open source Python dependency checker maintained in the osprey-oss/deptry project. The agent job here is narrow and practical: inspect a Python repository, compare real imports against pyproject.toml or other package declarations, and tell you where the dependency graph has drifted away from reality. That includes direct dependencies that are no longer used, imports that are missing from the declared dependency set, and transitive dependencies that currently resolve only because another package happens to pull them in.

You invoke this skill when normal product usage is not enough because the task is not simply “run a linter” or “install a package checker.” The real task is to clean up dependency declarations before a release, harden a build so it stops relying on accidental transitive imports, or prepare a refactor branch for safer packaging and reproducible installs. An agent can run Deptry, classify the findings, decide which issues are safe auto-fixes versus which need human review, update manifests, and then rerun tests to confirm the cleanup did not break runtime behavior.

The scope boundary keeps this from collapsing into a generic package-manager listing. This entry is specifically for dependency declaration hygiene in Python projects, not for full environment solving, vulnerability scanning, or generic static analysis. Integration points include Poetry and pyproject.toml-based repositories, CI quality gates, release preparation checklists, and pull request review loops where agents need a reliable way to surface dependency drift with concrete file-level findings. Upstream evidence is solid: official GitHub repository, PyPI package, dedicated docs site, tagged releases, MIT license, and active maintenance with recent commits.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-dependency-declarations-before-release/)
