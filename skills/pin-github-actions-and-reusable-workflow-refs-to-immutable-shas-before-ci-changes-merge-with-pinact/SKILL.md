---
title: "Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact"
description: "Use pinact when an agent needs to harden GitHub workflow files by replacing mutable action refs with immutable commit SHAs, not when the user is just browsing Actions docs or running a generic workflow linter. The workflow is specific: inspect workflow and composite action files, pin third-party actions and reusable workflows, and optionally verify version annotations before merge. That scope boundary, automated immutable-ref enforcement for GitHub Actions files, keeps it skill-shaped and distinct from broader CI tooling."
source: "https://github.com/suzuki-shunsuke/pinact"
verification: "listed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "suzuki-shunsuke/pinact"
  github_stars: 917
---

# Pin GitHub Actions and reusable workflow refs to immutable SHAs before CI changes merge with pinact

Use pinact when an agent needs to harden GitHub workflow files by replacing mutable action refs with immutable commit SHAs, not when the user is just browsing Actions docs or running a generic workflow linter. The workflow is specific: inspect workflow and composite action files, pin third-party actions and reusable workflows, and optionally verify version annotations before merge. That scope boundary, automated immutable-ref enforcement for GitHub Actions files, keeps it skill-shaped and distinct from broader CI tooling.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pin-github-actions-and-reusable-workflow-refs-to-immutable-shas-before-ci-changes-merge-with-pinact/)
