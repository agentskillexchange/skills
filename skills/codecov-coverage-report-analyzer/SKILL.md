---
title: "Codecov Coverage Report Analyzer"
description: "Integrates with the Codecov API v2 and codecov-cli to upload coverage reports, analyze coverage deltas, and enforce minimum thresholds. Supports lcov, cobertura, and jacoco report formats."
slug: "codecov-coverage-report-analyzer"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/"
listed: true
---

# Codecov Coverage Report Analyzer

Integrates with the Codecov API v2 and codecov-cli to upload coverage reports, analyze coverage deltas, and enforce minimum thresholds. Supports lcov, cobertura, and jacoco report formats.

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
clawhub install codecov-coverage-report-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Codecov Coverage Report Analyzer skill integrates with the Codecov API v2 (api.codecov.io/api/v2) and the codecov-cli (codecovcli upload-process, codecovcli create-commit) to manage code coverage tracking across repositories. It processes coverage reports in multiple formats including lcov.info, cobertura XML, JaCoCo XML, and Clover XML.
The skill uploads coverage data using codecovcli upload-process –report-type coverage –file coverage.xml with support for flag-based coverage segmentation (–flag unit, –flag integration). It retrieves coverage analytics through the Codecov API endpoints: /repos/{owner}/{repo}/commits for commit-level coverage, /repos/{owner}/{repo}/pulls for PR coverage deltas, and /repos/{owner}/{repo}/flags for flag-based breakdown.
Key capabilities include codecov.yml configuration management with coverage status checks (project and patch targets), component-based coverage tracking with path-based filtering, GitHub check annotations showing uncovered lines directly in PR diffs, and Slack/Teams notification integration for coverage regressions. The analyzer supports carryforward flags for monorepo partial uploads, coverage trend visualization data extraction, and custom threshold enforcement with configurable failure conditions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/)
