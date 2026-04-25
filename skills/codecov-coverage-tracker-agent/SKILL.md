---
title: "Codecov Coverage Tracker Agent"
description: "Tracks and enforces code coverage using Codecov API, lcov, and Istanbul/nyc. Generates coverage reports, detects regressions, and blocks PRs below threshold."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/"
category:
  - "Code Quality & Review"
framework:
  - "MCP"
---

# Codecov Coverage Tracker Agent

The Codecov Coverage Tracker Agent integrates with Codecov REST API (api.codecov.io/api/v2) and processes coverage reports from lcov, Istanbul/nyc (JSON and Cobertura formats), and JaCoCo for Java projects. It provides real-time coverage tracking and enforcement. The agent uploads coverage data via codecov CLI uploader with proper flag management for parallel CI jobs and monorepo component tracking. It processes coverage diffs to identify newly added uncovered lines and generates targeted review comments on pull requests through the Codecov GitHub App. Coverage policies are enforced through codecov.yml configuration with project-level and patch-level thresholds. The agent monitors coverage trends via the API (repos/{owner}/{repo}/commits, repos/{owner}/{repo}/pulls) and generates weekly reports showing coverage changes by component. Advanced features include smart test selection based on coverage data to reduce CI time, sunburst visualization generation for coverage distribution across packages, and flaky test detection through coverage variance analysis. The agent integrates with status checks to block merges when coverage drops below configured thresholds.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/codecov-coverage-tracker-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/codecov-coverage-tracker-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/)
