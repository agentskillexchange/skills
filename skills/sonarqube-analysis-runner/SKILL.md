---
title: SonarQube Analysis Runner
description: The SonarQube Analysis Runner skill integrates with SonarQube Server
  or SonarCloud to perform comprehensive static code analysis directly from your agent
  workflow. It leverages the SonarQube Web API (api/qualitygates, api/measures, api/issues)
  alongside the sonar-scanner CLI to trigger project scans, monitor analysis tasks
  via api/ce/task, and retrieve results programmatically. The skill supports configuring
  quality profiles per language, setting custom quality gate conditions, and filtering
  issues by severity (BLOCKER, CRITICAL, MAJOR). It handles multi-branch analysis
  with proper sonar.branch.name parameters, pull request decoration via api/project_pull_requests,
  and can export findings in SARIF format for GitHub Advanced Security integration.
  Authentication is managed through sonar.login tokens with granular project-level
  permissions. The runner automatically waits for background task completion and parses
  the analysis report to provide actionable summaries of new issues introduced.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-analysis-runner/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# SonarQube Analysis Runner

The SonarQube Analysis Runner skill integrates with SonarQube Server or SonarCloud to perform comprehensive static code analysis directly from your agent workflow. It leverages the SonarQube Web API (api/qualitygates, api/measures, api/issues) alongside the sonar-scanner CLI to trigger project scans, monitor analysis tasks via api/ce/task, and retrieve results programmatically. The skill supports configuring quality profiles per language, setting custom quality gate conditions, and filtering issues by severity (BLOCKER, CRITICAL, MAJOR). It handles multi-branch analysis with proper sonar.branch.name parameters, pull request decoration via api/project_pull_requests, and can export findings in SARIF format for GitHub Advanced Security integration. Authentication is managed through sonar.login tokens with granular project-level permissions. The runner automatically waits for background task completion and parses the analysis report to provide actionable summaries of new issues introduced.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-runner/)
