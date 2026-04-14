---
title: "Pull Request Size Analyzer"
description: "Analyzes PR size and reviewability using the GitHub GraphQL API and git diff-stat. Enforces size limits, suggests PR splitting strategies, and tracks team review velocity metrics via GitHub Checks API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
---

# Pull Request Size Analyzer

The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review.

The agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions.

When a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/)
