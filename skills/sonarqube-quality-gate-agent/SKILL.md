---
name: "SonarQube Quality Gate Agent"
description: "Monitors SonarQube quality gate status via the SonarQube Web API and enforces code quality thresholds. Parses coverage reports from JaCoCo, Istanbul, and lcov formats for multi-language projects."
category: "Code Quality & Review"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/"
tool_ecosystem:
  tool: sonarqube
  github_stars: 10358
  github_repo: SonarSource/sonarqube
  license: LGPL-3.0
  maintained: true
---

# SonarQube Quality Gate Agent

Monitors SonarQube quality gate status via the SonarQube Web API and enforces code quality thresholds. Parses coverage reports from JaCoCo, Istanbul, and lcov formats for multi-language projects.

## Overview

The SonarQube Quality Gate Agent skill integrates with SonarQube and SonarCloud instances via the SonarQube Web API to monitor and enforce code quality standards across pull requests and branches. It retrieves quality gate results, coverage metrics, and issue breakdowns for automated decision-making in CI/CD pipelines.

The agent parses multiple coverage report formats including JaCoCo XML for Java/Kotlin projects, Istanbul JSON and lcov for JavaScript/TypeScript, and Cobertura XML for Python and .NET projects. It normalizes these into a unified coverage model for cross-language quality comparisons.

For quality gate enforcement, the skill evaluates conditions against configurable thresholds including overall coverage percentage, new code coverage, duplicated line density, code smell count, bug count, vulnerability count, and security hotspot review percentage. It supports custom quality profiles and can apply different thresholds per project component.

Integration with the GitHub Status API and GitLab Commit Status API enables automatic PR blocking when quality gates fail. The skill generates detailed HTML reports with drill-down links to specific SonarQube issues and provides trend analysis comparing current metrics against historical baselines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-quality-gate-agent -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-quality-gate-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/
