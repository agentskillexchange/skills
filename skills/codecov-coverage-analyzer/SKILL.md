---
name: "Codecov Coverage Analyzer"
description: "Analyzes test coverage using the Codecov API v2 and codecov-cli uploader. Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable thresholds in CI pipelines."
category: "Code Quality & Review"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codecov-coverage-analyzer/"
tool_ecosystem:
  tool: "jest"
  github_stars: 45332
  npm_weekly_downloads: 45503384
  github_repo: "jestjs/jest"
  license: "MIT"
  maintained: true
---

# Codecov Coverage Analyzer

Analyzes test coverage using the Codecov API v2 and codecov-cli uploader. Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable thresholds in CI pipelines.

## Overview

The Codecov Coverage Analyzer automates test coverage tracking and enforcement by integrating with the Codecov platform. It uses the codecov-cli tool to upload coverage reports from popular test runners including pytest-cov (Python), jest –coverage (JavaScript), JaCoCo (Java), and go test -coverprofile (Go).

After upload, the skill queries the Codecov API v2 to retrieve detailed reports. The /api/v2/repos/{owner}/{repo}/report endpoint provides file-level coverage breakdowns including line hits, branch coverage, and complexity metrics. For pull requests, /api/v2/repos/{owner}/{repo}/pulls/{pull} returns diff coverage showing exactly which new lines are tested.

The agent enforces configurable thresholds via codecov.yml rules, supporting project-level targets, patch coverage minimums, and per-flag requirements for different test suites (unit, integration, e2e). When thresholds are not met, it generates detailed reports showing uncovered lines, suggests test scenarios, and can optionally block merges through GitHub commit status checks.

Additional features include coverage trend visualization, flaky test detection via Codecov’s test analytics, and component-level coverage tracking for monorepos using flag-based segmentation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-analyzer -a codex
```

### OpenClaw

```bash
clawhub install codecov-coverage-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/codecov-coverage-analyzer/
