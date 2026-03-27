---
name: "Codecov Coverage Tracker Agent"
description: "Tracks and enforces code coverage using Codecov API, lcov, and Istanbul/nyc. Generates coverage reports, detects regressions, and blocks PRs below threshold."
category: "Code Quality & Review"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/"
---

# Codecov Coverage Tracker Agent

Tracks and enforces code coverage using Codecov API, lcov, and Istanbul/nyc. Generates coverage reports, detects regressions, and blocks PRs below threshold.

## Overview

The Codecov Coverage Tracker Agent integrates with Codecov REST API (api.codecov.io/api/v2) and processes coverage reports from lcov, Istanbul/nyc (JSON and Cobertura formats), and JaCoCo for Java projects. It provides real-time coverage tracking and enforcement.

The agent uploads coverage data via codecov CLI uploader with proper flag management for parallel CI jobs and monorepo component tracking. It processes coverage diffs to identify newly added uncovered lines and generates targeted review comments on pull requests through the Codecov GitHub App.

Coverage policies are enforced through codecov.yml configuration with project-level and patch-level thresholds. The agent monitors coverage trends via the API (repos/{owner}/{repo}/commits, repos/{owner}/{repo}/pulls) and generates weekly reports showing coverage changes by component.

Advanced features include smart test selection based on coverage data to reduce CI time, sunburst visualization generation for coverage distribution across packages, and flaky test detection through coverage variance analysis. The agent integrates with status checks to block merges when coverage drops below configured thresholds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-tracker-agent -a codex
```

### OpenClaw

```bash
clawhub install codecov-coverage-tracker-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/
