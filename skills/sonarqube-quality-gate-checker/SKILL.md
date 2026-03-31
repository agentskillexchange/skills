---
name: "SonarQube Quality Gate Checker"
description: "Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API."
category: "Code Quality &amp; Review"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/sonarsource/sonarqube"
tool_ecosystem:
  tool: sonarqube
  github_repo: sonarsource/sonarqube
  github_stars: 10379
  license: LGPL-3.0
  maintained: true
---
# SonarQube Quality Gate Checker

Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API.

## Overview

The SonarQube Quality Gate Checker skill monitors and enforces code quality standards by interfacing with the SonarQube Web API. It queries the /api/qualitygates/project_status endpoint to retrieve real-time quality gate pass/fail results and detailed condition evaluations for metrics like coverage, duplications, and maintainability rating.

The skill integrates with sonar-scanner CLI to trigger on-demand code analysis, supporting configuration via sonar-project.properties files and command-line parameter overrides. It reads analysis reports from the .scannerwork/report-task.txt file to track background task completion via the /api/ce/task endpoint before fetching results.

Key capabilities include retrieving project-level metrics through /api/measures/component with metricKeys for coverage, bugs, vulnerabilities, code_smells, and ncloc. It supports branch and pull request analysis via the /api/project_branches/list and /api/project_pull_requests/list endpoints. The skill also manages quality profiles through /api/qualityprofiles/search for language-specific rule configuration.

Advanced features include hotspot review tracking via /api/hotspots/search, security report generation using /api/issues/search with type filters, custom quality gate creation through /api/qualitygates/create, and webhook management for CI/CD callback integration via /api/webhooks/list.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-checker -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-quality-gate-checker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-checker/)
