---
title: "Codecov Coverage Report Analyzer"
description: "The Codecov Coverage Report Analyzer skill integrates with the Codecov API v2 (api.codecov.io/api/v2) and the codecov-cli (codecovcli upload-process, codecovcli create-commit) to manage code coverage tracking across repositories. It processes coverage reports in multiple formats including lcov.info, cobertura XML, JaCoCo XML, and Clover XML. The skill uploads coverage data using codecovcli upload-process &#8211;report-type coverage &#8211;file coverage.xml with support for flag-based coverage segmentation (&#8211;flag unit, &#8211;flag integration). It retrieves coverage analytics through the Codecov API endpoints: /repos/{owner}/{repo}/commits for commit-level coverage, /repos/{owner}/{repo}/pulls for PR coverage deltas, and /repos/{owner}/{repo}/flags for flag-based breakdown. Key capabilities include codecov.yml configuration management with coverage status checks (project and patch targets), component-based coverage tracking with path-based filtering, GitHub check annotations showing uncovered lines directly in PR diffs, and Slack/Teams notification integration for coverage regressions. The analyzer supports carryforward flags for monorepo partial uploads, coverage trend visualization data extraction, and custom threshold enforcement with configurable failure conditions."
source: "https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Cursor"
---

# Codecov Coverage Report Analyzer

The Codecov Coverage Report Analyzer skill integrates with the Codecov API v2 (api.codecov.io/api/v2) and the codecov-cli (codecovcli upload-process, codecovcli create-commit) to manage code coverage tracking across repositories. It processes coverage reports in multiple formats including lcov.info, cobertura XML, JaCoCo XML, and Clover XML. The skill uploads coverage data using codecovcli upload-process &#8211;report-type coverage &#8211;file coverage.xml with support for flag-based coverage segmentation (&#8211;flag unit, &#8211;flag integration). It retrieves coverage analytics through the Codecov API endpoints: /repos/{owner}/{repo}/commits for commit-level coverage, /repos/{owner}/{repo}/pulls for PR coverage deltas, and /repos/{owner}/{repo}/flags for flag-based breakdown. Key capabilities include codecov.yml configuration management with coverage status checks (project and patch targets), component-based coverage tracking with path-based filtering, GitHub check annotations showing uncovered lines directly in PR diffs, and Slack/Teams notification integration for coverage regressions. The analyzer supports carryforward flags for monorepo partial uploads, coverage trend visualization data extraction, and custom threshold enforcement with configurable failure conditions.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/)
