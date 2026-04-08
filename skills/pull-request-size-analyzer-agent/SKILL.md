---
title: Pull Request Size Analyzer
description: 'The Pull Request Size Analyzer promotes healthy code review practices
  by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API,
  it fetches PR diff statistics, file change patterns, and review history to assess
  whether a PR is appropriately scoped for effective review. The agent calculates
  multiple size metrics beyond simple line counts: logical change units (related changes
  grouped by feature), cognitive load estimation based on file diversity and complexity
  scores, and test-to-code change ratios. It integrates with GitHub Checks API to
  provide inline PR feedback with specific size warnings and splitting suggestions.
  When a PR exceeds configurable thresholds, the agent suggests concrete splitting
  strategies based on the change types detected — separating refactoring from feature
  work, splitting database migrations from application changes, or breaking apart
  cross-cutting concerns. It tracks team-level metrics including average PR size,
  review turnaround time, and review thoroughness correlation with PR size. Dashboards
  show trends to help teams maintain healthy review practices.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# Pull Request Size Analyzer

The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review. The agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions. When a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/)
