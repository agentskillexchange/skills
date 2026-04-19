---
title: "Investigate failing GitHub Actions runs with CI Doctor"
description: "CI Doctor is a reusable workflow from the githubnext/agentics repository, built on top of GitHub Agentic Workflows. The agent job here is narrow and clear: watch selected GitHub Actions workflows, detect failures, collect logs, analyze likely root causes, look for historical patterns, and turn the findings into a structured investigation issue that a maintainer can act on. That is materially different from a plain product card for GitHub Actions or for the underlying gh aw tooling. Use this when a repository has recurring or noisy CI failures and you want an agent to do the first-pass diagnostic work automatically. It is a better fit than “using the product normally” when maintainers do not just need a runner to execute tests, but need an automation pattern that reads the failing run, summarizes the likely failure mode, and leaves behind an auditable issue with recommendations. In other words, the value is the investigative playbook, not the platform itself. The scope boundary matters. This entry is not “GitHub Agentic Workflows” in general, and it is not a generic GitHub Actions listing. It is specifically the CI Doctor workflow from GitHub Next’s sample pack. Its bounded job-to-be-done is CI failure investigation and reporting. It does not promise broad repository automation, code review, or arbitrary agent behavior outside that workflow. Integration points are concrete and upstream-backed: install the github/gh-aw extension, add the githubnext/agentics/ci-doctor workflow to a repository, compile it, and let it monitor selected workflows. Upstream docs show the workflow behavior, installation path, and human-in-the-loop review pattern. That makes this a real, source-backed operator skill rather than a catalog entry."
source: "https://github.com/githubnext/agentics/blob/main/docs/ci-doctor.md"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "githubnext/agentics"
  github_stars: 581
---

# Investigate failing GitHub Actions runs with CI Doctor

CI Doctor is a reusable workflow from the githubnext/agentics repository, built on top of GitHub Agentic Workflows. The agent job here is narrow and clear: watch selected GitHub Actions workflows, detect failures, collect logs, analyze likely root causes, look for historical patterns, and turn the findings into a structured investigation issue that a maintainer can act on. That is materially different from a plain product card for GitHub Actions or for the underlying gh aw tooling. Use this when a repository has recurring or noisy CI failures and you want an agent to do the first-pass diagnostic work automatically. It is a better fit than “using the product normally” when maintainers do not just need a runner to execute tests, but need an automation pattern that reads the failing run, summarizes the likely failure mode, and leaves behind an auditable issue with recommendations. In other words, the value is the investigative playbook, not the platform itself. The scope boundary matters. This entry is not “GitHub Agentic Workflows” in general, and it is not a generic GitHub Actions listing. It is specifically the CI Doctor workflow from GitHub Next’s sample pack. Its bounded job-to-be-done is CI failure investigation and reporting. It does not promise broad repository automation, code review, or arbitrary agent behavior outside that workflow. Integration points are concrete and upstream-backed: install the github/gh-aw extension, add the githubnext/agentics/ci-doctor workflow to a repository, compile it, and let it monitor selected workflows. Upstream docs show the workflow behavior, installation path, and human-in-the-loop review pattern. That makes this a real, source-backed operator skill rather than a catalog entry.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/investigate-failing-github-actions-runs-with-ci-doctor-2/)
