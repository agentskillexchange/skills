---
name: "Codecov Coverage Diff Analyzer"
description: "Analyzes code coverage diffs on pull requests using the Codecov API v2 /repos/{owner}/{repo}/commits endpoint. Identifies untested code paths and generates coverage improvement suggestions."
category: "Code Quality & Review"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codecov-coverage-diff-analyzer-2/"
---
# Codecov Coverage Diff Analyzer

Analyzes code coverage diffs on pull requests using the Codecov API v2 /repos/{owner}/{repo}/commits endpoint. Identifies untested code paths and generates coverage improvement suggestions.

The Codecov Coverage Diff Analyzer provides detailed coverage analysis for pull requests by querying the Codecov API v2. It fetches commit-level coverage data via the /repos/{owner}/{repo}/commits endpoint and compares base and head coverage to identify regression areas. The analyzer uses the /repos/{owner}/{repo}/compare endpoint to generate line-by-line coverage diffs, highlighting new code paths that lack test coverage. It integrates with the Codecov Flags API to analyze coverage by component, identifying which test suites (unit, integration, e2e) cover specific code areas. The skill generates actionable suggestions for improving coverage, including specific test case templates based on uncovered branches and conditions. It supports coverage threshold configuration via codecov.yml validation, ensuring proper flag-based and path-based coverage targets. Automated PR comments are generated via the GitHub API with coverage badges, trend charts, and links to the Codecov dashboard.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-diff-analyzer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-diff-analyzer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-diff-analyzer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-diff-analyzer-2 -a codex
```

### OpenClaw

```bash
clawhub install codecov-coverage-diff-analyzer-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-diff-analyzer-2/)
