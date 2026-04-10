---
title: "SonarQube Quality Gate Checker"
description: "Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API."
slug: "sonarqube-quality-gate-checker"
category:
  - "Code Quality &amp; Review"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-checker/"
---

# SonarQube Quality Gate Checker

Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sonarqube-quality-gate-checker
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Quality Gate Checker skill monitors and enforces code quality standards by interfacing with the SonarQube Web API. It queries the /api/qualitygates/project_status endpoint to retrieve real-time quality gate pass/fail results and detailed condition evaluations for metrics like coverage, duplications, and maintainability rating.
The skill integrates with sonar-scanner CLI to trigger on-demand code analysis, supporting configuration via sonar-project.properties files and command-line parameter overrides. It reads analysis reports from the .scannerwork/report-task.txt file to track background task completion via the /api/ce/task endpoint before fetching results.
Key capabilities include retrieving project-level metrics through /api/measures/component with metricKeys for coverage, bugs, vulnerabilities, code_smells, and ncloc. It supports branch and pull request analysis via the /api/project_branches/list and /api/project_pull_requests/list endpoints. The skill also manages quality profiles through /api/qualityprofiles/search for language-specific rule configuration.
Advanced features include hotspot review tracking via /api/hotspots/search, security report generation using /api/issues/search with type filters, custom quality gate creation through /api/qualitygates/create, and webhook management for CI/CD callback integration via /api/webhooks/list.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-checker/)
