---
title: "Pull Request Size Analyzer"
description: "The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review. The agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions. When a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices."
source: "https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
---

# Pull Request Size Analyzer

The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review. The agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions. When a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/)
