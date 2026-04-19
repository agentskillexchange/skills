---
title: "Generate release PRs and changelog updates from Conventional Commits"
description: "Tool: release-please (googleapis/release-please). This entry captures a bounded agent job: inspect commit history that follows the Conventional Commits convention, calculate the next release, and prepare the release pull request with version updates and changelog text. The agent behavior is concrete. It gathers release intent from existing commits, assembles the proposed release artifact, and hands a reviewable PR back to maintainers. That is meaningfully different from just saying &#8220;here is a release automation tool.&#8221; Invoke this when a team already uses Conventional Commits or a similar disciplined merge flow and wants repeatable release preparation without having an agent improvise version numbers or changelog prose from scratch. It is especially useful when the maintainer wants a human approval step before tags or package publication happen. If the user simply wants to publish a package manually, edit a changelog by hand, or browse CI results, they should use the product normally instead of invoking this skill. The scope boundary is clear: this is not a generic CI/CD platform card, GitHub App card, or package listing. The relevant job-to-be-done is release PR generation from commit history. Integration points include GitHub repositories, release PR workflows, changelog files, manifest-driven multi-package repositories, and CI pipelines that merge or publish after approval. Hide the product name and the skill still stands: an agent can prepare consistent release PRs and changelog updates from structured commit metadata, while leaving actual approval and publishing decisions to maintainers."
source: "https://github.com/googleapis/release-please"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "googleapis/release-please"
  github_stars: 6700
---

# Generate release PRs and changelog updates from Conventional Commits

Tool: release-please (googleapis/release-please). This entry captures a bounded agent job: inspect commit history that follows the Conventional Commits convention, calculate the next release, and prepare the release pull request with version updates and changelog text. The agent behavior is concrete. It gathers release intent from existing commits, assembles the proposed release artifact, and hands a reviewable PR back to maintainers. That is meaningfully different from just saying &#8220;here is a release automation tool.&#8221; Invoke this when a team already uses Conventional Commits or a similar disciplined merge flow and wants repeatable release preparation without having an agent improvise version numbers or changelog prose from scratch. It is especially useful when the maintainer wants a human approval step before tags or package publication happen. If the user simply wants to publish a package manually, edit a changelog by hand, or browse CI results, they should use the product normally instead of invoking this skill. The scope boundary is clear: this is not a generic CI/CD platform card, GitHub App card, or package listing. The relevant job-to-be-done is release PR generation from commit history. Integration points include GitHub repositories, release PR workflows, changelog files, manifest-driven multi-package repositories, and CI pipelines that merge or publish after approval. Hide the product name and the skill still stands: an agent can prepare consistent release PRs and changelog updates from structured commit metadata, while leaving actual approval and publishing decisions to maintainers.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-release-prs-and-changelog-updates-from-conventional-commits/)
