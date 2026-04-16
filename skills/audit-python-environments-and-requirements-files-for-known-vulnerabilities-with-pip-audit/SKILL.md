---
title: "Audit Python environments and requirements files for known vulnerabilities with pip-audit"
description: "Check Python environments and requirements files for published vulnerabilities before shipping, upgrading, or approving dependency changes."
verification: "listed"
source: "https://github.com/pypa/pip-audit"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pypa/pip-audit"
  github_stars: 1260
---

# Audit Python environments and requirements files for known vulnerabilities with pip-audit

Use pip-audit when an agent needs to review a Python environment or requirements set for known vulnerabilities before release, deployment, or dependency approval. The agent can audit an installed environment or a requirements file, surface affected packages, and recommend upgrade paths or remediations. The scope is a Python dependency vulnerability check with actionable output, not a generic security platform or package index listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-environments-and-requirements-files-for-known-vulnerabilities-with-pip-audit/)
