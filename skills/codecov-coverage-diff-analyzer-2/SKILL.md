---
title: "Codecov Coverage Diff Analyzer"
description: "Analyzes code coverage diffs on pull requests using the Codecov API v2 /repos/{owner}/{repo}/commits endpoint. Identifies untested code paths and generates coverage improvement suggestions."
slug: "codecov-coverage-diff-analyzer-2"
category:
  - "Code Quality &amp; Review"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codecov-coverage-diff-analyzer-2/"
listed: true
---

# Codecov Coverage Diff Analyzer

Analyzes code coverage diffs on pull requests using the Codecov API v2 /repos/{owner}/{repo}/commits endpoint. Identifies untested code paths and generates coverage improvement suggestions.

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
clawhub install codecov-coverage-diff-analyzer-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Codecov Coverage Diff Analyzer provides detailed coverage analysis for pull requests by querying the Codecov API v2. It fetches commit-level coverage data via the /repos/{owner}/{repo}/commits endpoint and compares base and head coverage to identify regression areas. The analyzer uses the /repos/{owner}/{repo}/compare endpoint to generate line-by-line coverage diffs, highlighting new code paths that lack test coverage. It integrates with the Codecov Flags API to analyze coverage by component, identifying which test suites (unit, integration, e2e) cover specific code areas. The skill generates actionable suggestions for improving coverage, including specific test case templates based on uncovered branches and conditions. It supports coverage threshold configuration via codecov.yml validation, ensuring proper flag-based and path-based coverage targets. Automated PR comments are generated via the GitHub API with coverage badges, trend charts, and links to the Codecov dashboard.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-diff-analyzer-2/)
