---
title: Codecov Coverage Tracker Agent
description: The Codecov Coverage Tracker Agent integrates with Codecov REST API (api.codecov.io/api/v2)
  and processes coverage reports from lcov, Istanbul/nyc (JSON and Cobertura formats),
  and JaCoCo for Java projects. It provides real-time coverage tracking and enforcement.
  The agent uploads coverage data via codecov CLI uploader with proper flag management
  for parallel CI jobs and monorepo component tracking. It processes coverage diffs
  to identify newly added uncovered lines and generates targeted review comments on
  pull requests through the Codecov GitHub App. Coverage policies are enforced through
  codecov.yml configuration with project-level and patch-level thresholds. The agent
  monitors coverage trends via the API (repos/{owner}/{repo}/commits, repos/{owner}/{repo}/pulls)
  and generates weekly reports showing coverage changes by component. Advanced features
  include smart test selection based on coverage data to reduce CI time, sunburst
  visualization generation for coverage distribution across packages, and flaky test
  detection through coverage variance analysis. The agent integrates with status checks
  to block merges when coverage drops below configured thresholds.
verification: security_reviewed
source: https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/
category:
- Code Quality &amp; Review
framework:
- MCP
---

# Codecov Coverage Tracker Agent

The Codecov Coverage Tracker Agent integrates with Codecov REST API (api.codecov.io/api/v2) and processes coverage reports from lcov, Istanbul/nyc (JSON and Cobertura formats), and JaCoCo for Java projects. It provides real-time coverage tracking and enforcement. The agent uploads coverage data via codecov CLI uploader with proper flag management for parallel CI jobs and monorepo component tracking. It processes coverage diffs to identify newly added uncovered lines and generates targeted review comments on pull requests through the Codecov GitHub App. Coverage policies are enforced through codecov.yml configuration with project-level and patch-level thresholds. The agent monitors coverage trends via the API (repos/{owner}/{repo}/commits, repos/{owner}/{repo}/pulls) and generates weekly reports showing coverage changes by component. Advanced features include smart test selection based on coverage data to reduce CI time, sunburst visualization generation for coverage distribution across packages, and flaky test detection through coverage variance analysis. The agent integrates with status checks to block merges when coverage drops below configured thresholds.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/)
