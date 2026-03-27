---
name: "Pull Request Size Analyzer"
description: "Analyzes PR size and reviewability using the GitHub GraphQL API and git diff-stat. Enforces size limits, suggests PR splitting strategies, and tracks team review velocity metrics via GitHub Checks API."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/"
tool_ecosystem:
  tool: graphql
  github_stars: 20332
  npm_weekly_downloads: 32010306
  github_repo: graphql/graphql-js
  license: MIT
  maintained: true
---

# Pull Request Size Analyzer

Analyzes PR size and reviewability using the GitHub GraphQL API and git diff-stat. Enforces size limits, suggests PR splitting strategies, and tracks team review velocity metrics via GitHub Checks API.

## Overview

The Pull Request Size Analyzer promotes healthy code review practices by analyzing PR size, complexity, and reviewability. Using the GitHub GraphQL API, it fetches PR diff statistics, file change patterns, and review history to assess whether a PR is appropriately scoped for effective review.

The agent calculates multiple size metrics beyond simple line counts: logical change units (related changes grouped by feature), cognitive load estimation based on file diversity and complexity scores, and test-to-code change ratios. It integrates with GitHub Checks API to provide inline PR feedback with specific size warnings and splitting suggestions.

When a PR exceeds configurable thresholds, the agent suggests concrete splitting strategies based on the change types detected — separating refactoring from feature work, splitting database migrations from application changes, or breaking apart cross-cutting concerns. It tracks team-level metrics including average PR size, review turnaround time, and review thoroughness correlation with PR size. Dashboards show trends to help teams maintain healthy review practices.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pull-request-size-analyzer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pull-request-size-analyzer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pull-request-size-analyzer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pull-request-size-analyzer-agent -a codex
```

### OpenClaw

```bash
clawhub install pull-request-size-analyzer-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pull-request-size-analyzer-agent/
