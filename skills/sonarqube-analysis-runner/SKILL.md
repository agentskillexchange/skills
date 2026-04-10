---
name: SonarQube Analysis Runner
description: Run SonarQube static analysis scans via the SonarQube Web API and sonar-scanner
  CLI. Detects code smells, bugs, and security vulnerabilities with configurable quality
  gates and branch analysis support.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-runner/)
