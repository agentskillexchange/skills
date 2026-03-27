---
name: "SonarQube Analysis Runner"
description: "Run SonarQube static analysis scans via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities with configurable quality gates and branch analysis support."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sonarqube-analysis-runner/"
tool_ecosystem:
  tool: sonarqube
  github_stars: 10358
  github_repo: SonarSource/sonarqube
  license: LGPL-3.0
  maintained: true
---

# SonarQube Analysis Runner

Run SonarQube static analysis scans via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities with configurable quality gates and branch analysis support.

## Overview

The SonarQube Analysis Runner skill integrates with SonarQube Server or SonarCloud to perform comprehensive static code analysis directly from your agent workflow. It leverages the SonarQube Web API (api/qualitygates, api/measures, api/issues) alongside the sonar-scanner CLI to trigger project scans, monitor analysis tasks via api/ce/task, and retrieve results programmatically. The skill supports configuring quality profiles per language, setting custom quality gate conditions, and filtering issues by severity (BLOCKER, CRITICAL, MAJOR). It handles multi-branch analysis with proper sonar.branch.name parameters, pull request decoration via api/project_pull_requests, and can export findings in SARIF format for GitHub Advanced Security integration. Authentication is managed through sonar.login tokens with granular project-level permissions. The runner automatically waits for background task completion and parses the analysis report to provide actionable summaries of new issues introduced.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-analysis-runner -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-analysis-runner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-analysis-runner/
