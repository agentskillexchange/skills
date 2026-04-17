---
title: "Pull Request Size Analyzer"
description: "The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review.\nThe agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions.\nWhen a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/"
framework:
  - "OpenClaw"
---

# Pull Request Size Analyzer

The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review.
The agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions.
When a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/pull-request-size-analyzer-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/pull-request-size-analyzer-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/)
