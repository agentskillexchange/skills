---
name: "Codecov Coverage Report Analyzer"
description: "Integrates with the Codecov API v2 and codecov-cli to upload coverage reports, analyze coverage deltas, and enforce minimum thresholds. Supports lcov, cobertura, and jacoco report formats."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "slack"  # from ase_tool_match
  github_stars: 2900  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 2433529  # from ase_npm_downloads
  github_repo: "slackapi/bolt-js"  # from ase_github_repo
  license: "MIT"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Codecov Coverage Report Analyzer

Integrates with the Codecov API v2 and codecov-cli to upload coverage reports, analyze coverage deltas, and enforce minimum thresholds. Supports lcov, cobertura, and jacoco report formats.

## Overview

The Codecov Coverage Report Analyzer skill integrates with the Codecov API v2 (api.codecov.io/api/v2) and the codecov-cli (codecovcli upload-process, codecovcli create-commit) to manage code coverage tracking across repositories. It processes coverage reports in multiple formats including lcov.info, cobertura XML, JaCoCo XML, and Clover XML.

The skill uploads coverage data using codecovcli upload-process –report-type coverage –file coverage.xml with support for flag-based coverage segmentation (–flag unit, –flag integration). It retrieves coverage analytics through the Codecov API endpoints: /repos/{owner}/{repo}/commits for commit-level coverage, /repos/{owner}/{repo}/pulls for PR coverage deltas, and /repos/{owner}/{repo}/flags for flag-based breakdown.

Key capabilities include codecov.yml configuration management with coverage status checks (project and patch targets), component-based coverage tracking with path-based filtering, GitHub check annotations showing uncovered lines directly in PR diffs, and Slack/Teams notification integration for coverage regressions. The analyzer supports carryforward flags for monorepo partial uploads, coverage trend visualization data extraction, and custom threshold enforcement with configurable failure conditions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-report-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-report-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-report-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill codecov-coverage-report-analyzer -a codex
```

### OpenClaw

```bash
clawhub install codecov-coverage-report-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/
