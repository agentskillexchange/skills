---
title: "Codecov Coverage Tracker Agent"
description: "Tracks and enforces code coverage using Codecov API, lcov, and Istanbul/nyc. Generates coverage reports, detects regressions, and blocks PRs below threshold."
slug: "codecov-coverage-tracker-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/"
---

# Codecov Coverage Tracker Agent

Tracks and enforces code coverage using Codecov API, lcov, and Istanbul/nyc. Generates coverage reports, detects regressions, and blocks PRs below threshold.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install codecov-coverage-tracker-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Codecov Coverage Tracker Agent integrates with Codecov REST API (api.codecov.io/api/v2) and processes coverage reports from lcov, Istanbul/nyc (JSON and Cobertura formats), and JaCoCo for Java projects. It provides real-time coverage tracking and enforcement.
The agent uploads coverage data via codecov CLI uploader with proper flag management for parallel CI jobs and monorepo component tracking. It processes coverage diffs to identify newly added uncovered lines and generates targeted review comments on pull requests through the Codecov GitHub App.
Coverage policies are enforced through codecov.yml configuration with project-level and patch-level thresholds. The agent monitors coverage trends via the API (repos/{owner}/{repo}/commits, repos/{owner}/{repo}/pulls) and generates weekly reports showing coverage changes by component.
Advanced features include smart test selection based on coverage data to reduce CI time, sunburst visualization generation for coverage distribution across packages, and flaky test detection through coverage variance analysis. The agent integrates with status checks to block merges when coverage drops below configured thresholds.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/)
