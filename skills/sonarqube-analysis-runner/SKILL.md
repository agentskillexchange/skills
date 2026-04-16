---
title: "SonarQube Analysis Runner"
description: "Run SonarQube static analysis scans via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities with configurable quality gates and branch analysis support."
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "LGPL-3.0"
---

# SonarQube Analysis Runner

The SonarQube Analysis Runner skill integrates with SonarQube Server or SonarCloud to perform comprehensive static code analysis directly from your agent workflow. It leverages the SonarQube Web API (api/qualitygates, api/measures, api/issues) alongside the sonar-scanner CLI to trigger project scans, monitor analysis tasks via api/ce/task, and retrieve results programmatically. The skill supports configuring quality profiles per language, setting custom quality gate conditions, and filtering issues by severity (BLOCKER, CRITICAL, MAJOR). It handles multi-branch analysis with proper sonar.branch.name parameters, pull request decoration via api/project_pull_requests, and can export findings in SARIF format for GitHub Advanced Security integration. Authentication is managed through sonar.login tokens with granular project-level permissions. The runner automatically waits for background task completion and parses the analysis report to provide actionable summaries of new issues introduced.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-runner/)
