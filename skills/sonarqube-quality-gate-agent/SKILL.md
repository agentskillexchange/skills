---
title: SonarQube Quality Gate Agent
description: The SonarQube Quality Gate Agent skill integrates with SonarQube and
  SonarCloud instances via the SonarQube Web API to monitor and enforce code quality
  standards across pull requests and branches. It retrieves quality gate results,
  coverage metrics, and issue breakdowns for automated decision-making in CI/CD pipelines.
  The agent parses multiple coverage report formats including JaCoCo XML for Java/Kotlin
  projects, Istanbul JSON and lcov for JavaScript/TypeScript, and Cobertura XML for
  Python and .NET projects. It normalizes these into a unified coverage model for
  cross-language quality comparisons. For quality gate enforcement, the skill evaluates
  conditions against configurable thresholds including overall coverage percentage,
  new code coverage, duplicated line density, code smell count, bug count, vulnerability
  count, and security hotspot review percentage. It supports custom quality profiles
  and can apply different thresholds per project component. Integration with the GitHub
  Status API and GitLab Commit Status API enables automatic PR blocking when quality
  gates fail. The skill generates detailed HTML reports with drill-down links to specific
  SonarQube issues and provides trend analysis comparing current metrics against historical
  baselines.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/
category:
- Code Quality &amp; Review
framework:
- ChatGPT Agents
---

# SonarQube Quality Gate Agent

The SonarQube Quality Gate Agent skill integrates with SonarQube and SonarCloud instances via the SonarQube Web API to monitor and enforce code quality standards across pull requests and branches. It retrieves quality gate results, coverage metrics, and issue breakdowns for automated decision-making in CI/CD pipelines. The agent parses multiple coverage report formats including JaCoCo XML for Java/Kotlin projects, Istanbul JSON and lcov for JavaScript/TypeScript, and Cobertura XML for Python and .NET projects. It normalizes these into a unified coverage model for cross-language quality comparisons. For quality gate enforcement, the skill evaluates conditions against configurable thresholds including overall coverage percentage, new code coverage, duplicated line density, code smell count, bug count, vulnerability count, and security hotspot review percentage. It supports custom quality profiles and can apply different thresholds per project component. Integration with the GitHub Status API and GitLab Commit Status API enables automatic PR blocking when quality gates fail. The skill generates detailed HTML reports with drill-down links to specific SonarQube issues and provides trend analysis comparing current metrics against historical baselines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-agent/)
