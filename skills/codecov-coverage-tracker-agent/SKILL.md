---
title: "Codecov Coverage Tracker Agent"
description: "Tracks and enforces code coverage using Codecov API, lcov, and Istanbul/nyc. Generates coverage reports, detects regressions, and blocks PRs below threshold."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/"
category:
  - "Code Quality &amp; Review"
framework:
  - "MCP"
---

# Codecov Coverage Tracker Agent

The Codecov Coverage Tracker Agent integrates with Codecov REST API (api.codecov.io/api/v2) and processes coverage reports from lcov, Istanbul/nyc (JSON and Cobertura formats), and JaCoCo for Java projects. It provides real-time coverage tracking and enforcement.

The agent uploads coverage data via codecov CLI uploader with proper flag management for parallel CI jobs and monorepo component tracking. It processes coverage diffs to identify newly added uncovered lines and generates targeted review comments on pull requests through the Codecov GitHub App.

Coverage policies are enforced through codecov.yml configuration with project-level and patch-level thresholds. The agent monitors coverage trends via the API (repos/{owner}/{repo}/commits, repos/{owner}/{repo}/pulls) and generates weekly reports showing coverage changes by component.

Advanced features include smart test selection based on coverage data to reduce CI time, sunburst visualization generation for coverage distribution across packages, and flaky test detection through coverage variance analysis. The agent integrates with status checks to block merges when coverage drops below configured thresholds.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/codecov-coverage-tracker-agent/)
