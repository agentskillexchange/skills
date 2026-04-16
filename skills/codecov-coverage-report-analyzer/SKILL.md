---
title: "Codecov Coverage Report Analyzer"
description: "Integrates with the Codecov API v2 and codecov-cli to upload coverage reports, analyze coverage deltas, and enforce minimum thresholds. Supports lcov, cobertura, and jacoco report formats."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/"
category:
  - "Code Quality & Review"
framework:
  - "Cursor"
---

# Codecov Coverage Report Analyzer

The Codecov Coverage Report Analyzer skill integrates with the Codecov API v2 (api.codecov.io/api/v2) and the codecov-cli (codecovcli upload-process, codecovcli create-commit) to manage code coverage tracking across repositories. It processes coverage reports in multiple formats including lcov.info, cobertura XML, JaCoCo XML, and Clover XML.


The skill uploads coverage data using codecovcli upload-process –report-type coverage –file coverage.xml with support for flag-based coverage segmentation (–flag unit, –flag integration). It retrieves coverage analytics through the Codecov API endpoints: /repos/{owner}/{repo}/commits for commit-level coverage, /repos/{owner}/{repo}/pulls for PR coverage deltas, and /repos/{owner}/{repo}/flags for flag-based breakdown.


Key capabilities include codecov.yml configuration management with coverage status checks (project and patch targets), component-based coverage tracking with path-based filtering, GitHub check annotations showing uncovered lines directly in PR diffs, and Slack/Teams notification integration for coverage regressions. The analyzer supports carryforward flags for monorepo partial uploads, coverage trend visualization data extraction, and custom threshold enforcement with configurable failure conditions.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-report-analyzer/)
