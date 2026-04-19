---
title: "SonarQube Quality Gate Agent"
description: "The SonarQube Quality Gate Agent skill integrates with SonarQube and SonarCloud instances via the SonarQube Web API to monitor and enforce code quality standards across pull requests and branches. It retrieves quality gate results, coverage metrics, and issue breakdowns for automated decision-making in CI/CD pipelines. The agent parses multiple coverage report formats including JaCoCo XML for Java/Kotlin projects, Istanbul JSON and lcov for JavaScript/TypeScript, and Cobertura XML for Python and .NET projects. It normalizes these into a unified coverage model for cross-language quality comparisons. For quality gate enforcement, the skill evaluates conditions against configurable thresholds including overall coverage percentage, new code coverage, duplicated line density, code smell count, bug count, vulnerability count, and security hotspot review percentage. It supports custom quality profiles and can apply different thresholds per project component. Integration with the GitHub Status API and GitLab Commit Status API enables automatic PR blocking when quality gates fail. The skill generates detailed HTML reports with drill-down links to specific SonarQube issues and provides trend analysis comparing current metrics against historical baselines."
source: "https://github.com/SonarSource/sonarqube"
verification: "security_reviewed"
category:
  - "Code Quality &amp; Review"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Quality Gate Agent

The SonarQube Quality Gate Agent skill integrates with SonarQube and SonarCloud instances via the SonarQube Web API to monitor and enforce code quality standards across pull requests and branches. It retrieves quality gate results, coverage metrics, and issue breakdowns for automated decision-making in CI/CD pipelines. The agent parses multiple coverage report formats including JaCoCo XML for Java/Kotlin projects, Istanbul JSON and lcov for JavaScript/TypeScript, and Cobertura XML for Python and .NET projects. It normalizes these into a unified coverage model for cross-language quality comparisons. For quality gate enforcement, the skill evaluates conditions against configurable thresholds including overall coverage percentage, new code coverage, duplicated line density, code smell count, bug count, vulnerability count, and security hotspot review percentage. It supports custom quality profiles and can apply different thresholds per project component. Integration with the GitHub Status API and GitLab Commit Status API enables automatic PR blocking when quality gates fail. The skill generates detailed HTML reports with drill-down links to specific SonarQube issues and provides trend analysis comparing current metrics against historical baselines.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/)
