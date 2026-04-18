---
title: "Codecov Coverage Analyzer"
description: "Analyzes test coverage using the Codecov API v2 and codecov-cli uploader. Fetches per-file coverage from /api/v2/repos/{owner}/{repo}/report, computes diff coverage via /api/v2/repos/{owner}/{repo}/pulls/{pull}, and enforces configurable thresholds in CI pipelines."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codecov-coverage-analyzer/"
category:
  - "Code Quality & Review"
framework:
  - "Codex"
---

# Codecov Coverage Analyzer

The Codecov Coverage Analyzer automates test coverage tracking and enforcement by integrating with the Codecov platform. It uses the codecov-cli tool to upload coverage reports from popular test runners including pytest-cov (Python), jest –coverage (JavaScript), JaCoCo (Java), and go test -coverprofile (Go).

After upload, the skill queries the Codecov API v2 to retrieve detailed reports. The /api/v2/repos/{owner}/{repo}/report endpoint provides file-level coverage breakdowns including line hits, branch coverage, and complexity metrics. For pull requests, /api/v2/repos/{owner}/{repo}/pulls/{pull} returns diff coverage showing exactly which new lines are tested.

The agent enforces configurable thresholds via codecov.yml rules, supporting project-level targets, patch coverage minimums, and per-flag requirements for different test suites (unit, integration, e2e). When thresholds are not met, it generates detailed reports showing uncovered lines, suggests test scenarios, and can optionally block merges through GitHub commit status checks.

Additional features include coverage trend visualization, flaky test detection via Codecov’s test analytics, and component-level coverage tracking for monorepos using flag-based segmentation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/codecov-coverage-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/codecov-coverage-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-analyzer/)
