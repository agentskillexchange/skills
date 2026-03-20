---
name: SonarQube Quality Gate Checker
description: Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQ
category: Code Quality & Review
framework: Gemini
verification: security_reviewed
rating: 4.9
reviews: 86
source: https://agentskillexchange.com/skill/sonarqube-quality-gate-checker/
---

# SonarQube Quality Gate Checker

Queries SonarQube Web API for project quality gate status, code coverage metrics, and technical debt analysis. Integrates with sonar-scanner CLI for on-demand analysis and pr-decoration via the SonarQube ALM integration API.

## Overview

The SonarQube Quality Gate Checker skill monitors and enforces code quality standards by interfacing with the SonarQube Web API. It queries the /api/qualitygates/project_status endpoint to retrieve real-time quality gate pass/fail results and detailed condition evaluations for metrics like coverage, duplications, and maintainability rating.
The skill integrates with sonar-scanner CLI to trigger on-demand code analysis, supporting configuration via sonar-project.properties files and command-line parameter overrides. It reads analysis reports from the .scannerwork/report-task.txt file to track background task completion via the /api/ce/task endpoint before fetching results.
Key capabilities include retrieving project-level metrics through /api/measures/component with metricKeys for coverage, bugs, vulnerabilities, code_smells, and ncloc. It supports branch and pull request analysis via the /api/project_branches/list and /api/project_pull_requests/list endpoints. The skill also manages quality profiles through /api/qualityprofiles/search for language-specific rule configuration.
Advanced features include hotspot review tracking via /api/hotspots/search, security report generation using /api/issues/search with type filters, custom quality gate creation through /api/qualitygates/create, and webhook management for CI/CD callback integration via /api/webhooks/list.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-checker
```

### OpenClaw

```bash
openclaw install sonarqube-quality-gate-checker
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Code Quality & Review |
| Framework | Gemini |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (86 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/sonarqube-quality-gate-checker/)*
