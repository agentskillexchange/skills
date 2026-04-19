---
title: "Generate conventional-commit release notes for automated ship workflows with semantic-release release-notes-generator"
description: "Use this skill when a release pipeline already has semantic-release in place and the missing job is dependable release-note generation from commit history. The boundary is narrow and operator-facing: configure the release-notes-generator plugin, choose the preset and parsing rules, and emit changelog-ready notes during CI. That keeps it from being a plain product listing. The skill is not about adopting semantic-release as a whole. It is about the specific release-artifact step that turns commit metadata into publishable notes during ship automation."
source: "https://github.com/semantic-release/release-notes-generator"
verification: "listed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "semantic-release/release-notes-generator"
  github_stars: 361
  npm_package: "@semantic-release/release-notes-generator"
  npm_weekly_downloads: 10982193
---

# Generate conventional-commit release notes for automated ship workflows with semantic-release release-notes-generator

Use this skill when a release pipeline already has semantic-release in place and the missing job is dependable release-note generation from commit history. The boundary is narrow and operator-facing: configure the release-notes-generator plugin, choose the preset and parsing rules, and emit changelog-ready notes during CI. That keeps it from being a plain product listing. The skill is not about adopting semantic-release as a whole. It is about the specific release-artifact step that turns commit metadata into publishable notes during ship automation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-conventional-commit-release-notes-for-automated-ship-workflows-with-semantic-release-release-notes-generator/)
