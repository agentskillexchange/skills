---
title: "SonarQube Quality Gate Agent"
description: "Monitors SonarQube quality gate status via the SonarQube Web API and enforces code quality thresholds. Parses coverage reports from JaCoCo, Istanbul, and lcov formats for multi-language projects."
slug: "sonarqube-quality-gate-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/"
---

# SonarQube Quality Gate Agent

Monitors SonarQube quality gate status via the SonarQube Web API and enforces code quality thresholds. Parses coverage reports from JaCoCo, Istanbul, and lcov formats for multi-language projects.

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
clawhub install sonarqube-quality-gate-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Quality Gate Agent skill integrates with SonarQube and SonarCloud instances via the SonarQube Web API to monitor and enforce code quality standards across pull requests and branches. It retrieves quality gate results, coverage metrics, and issue breakdowns for automated decision-making in CI/CD pipelines.
The agent parses multiple coverage report formats including JaCoCo XML for Java/Kotlin projects, Istanbul JSON and lcov for JavaScript/TypeScript, and Cobertura XML for Python and .NET projects. It normalizes these into a unified coverage model for cross-language quality comparisons.
For quality gate enforcement, the skill evaluates conditions against configurable thresholds including overall coverage percentage, new code coverage, duplicated line density, code smell count, bug count, vulnerability count, and security hotspot review percentage. It supports custom quality profiles and can apply different thresholds per project component.
Integration with the GitHub Status API and GitLab Commit Status API enables automatic PR blocking when quality gates fail. The skill generates detailed HTML reports with drill-down links to specific SonarQube issues and provides trend analysis comparing current metrics against historical baselines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/)
