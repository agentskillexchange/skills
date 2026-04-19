---
title: "Codecov Coverage Analyzer"
description: "The Codecov Coverage Analyzer automates test coverage tracking and enforcement by integrating with the Codecov platform. It uses the codecov-cli tool to upload coverage reports from popular test runners including pytest-cov (Python), jest &#8211;coverage (JavaScript), JaCoCo (Java), and go test -coverprofile (Go). After upload, the skill queries the Codecov API v2 to retrieve detailed reports. The /api/v2/repos/{owner}/{repo}/report endpoint provides file-level coverage breakdowns including line hits, branch coverage, and complexity metrics. For pull requests, /api/v2/repos/{owner}/{repo}/pulls/{pull} returns diff coverage showing exactly which new lines are tested. The agent enforces configurable thresholds via codecov.yml rules, supporting project-level targets, patch coverage minimums, and per-flag requirements for different test suites (unit, integration, e2e). When thresholds are not met, it generates detailed reports showing uncovered lines, suggests test scenarios, and can optionally block merges through GitHub commit status checks. Additional features include coverage trend visualization, flaky test detection via Codecov&#8217;s test analytics, and component-level coverage tracking for monorepos using flag-based segmentation."
source: "https://agentskillexchange.com/skills/codecov-coverage-analyzer/"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "Codex"
---

# Codecov Coverage Analyzer

The Codecov Coverage Analyzer automates test coverage tracking and enforcement by integrating with the Codecov platform. It uses the codecov-cli tool to upload coverage reports from popular test runners including pytest-cov (Python), jest &#8211;coverage (JavaScript), JaCoCo (Java), and go test -coverprofile (Go). After upload, the skill queries the Codecov API v2 to retrieve detailed reports. The /api/v2/repos/{owner}/{repo}/report endpoint provides file-level coverage breakdowns including line hits, branch coverage, and complexity metrics. For pull requests, /api/v2/repos/{owner}/{repo}/pulls/{pull} returns diff coverage showing exactly which new lines are tested. The agent enforces configurable thresholds via codecov.yml rules, supporting project-level targets, patch coverage minimums, and per-flag requirements for different test suites (unit, integration, e2e). When thresholds are not met, it generates detailed reports showing uncovered lines, suggests test scenarios, and can optionally block merges through GitHub commit status checks. Additional features include coverage trend visualization, flaky test detection via Codecov&#8217;s test analytics, and component-level coverage tracking for monorepos using flag-based segmentation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-analyzer/)
