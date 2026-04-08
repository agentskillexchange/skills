---
title: SonarQube Code Scanner Agent
description: The SonarQube Code Scanner Agent integrates directly with SonarQube Server
  REST API (api/qualitygates, api/issues, api/measures) and SonarScanner CLI to perform
  comprehensive static code analysis. It supports Java, Python, JavaScript, TypeScript,
  C#, Go, and 25+ additional languages out of the box. The agent triggers scans via
  sonar-scanner with configurable sonar-project.properties, monitors analysis progress
  through the ce/task endpoint, and retrieves detailed results including code smells,
  bugs, security vulnerabilities, and technical debt metrics. Quality gate status
  is checked via api/qualitygates/project_status. Key capabilities include pull request
  decoration with inline comments on new issues, branch analysis comparison, and trend
  tracking across multiple project versions. The agent can enforce custom quality
  profiles and block merges when quality gates fail. Integration with CI/CD pipelines
  is supported through webhook listeners that process analysis completion events and
  route results to Slack, Teams, or email notifications.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# SonarQube Code Scanner Agent

The SonarQube Code Scanner Agent integrates directly with SonarQube Server REST API (api/qualitygates, api/issues, api/measures) and SonarScanner CLI to perform comprehensive static code analysis. It supports Java, Python, JavaScript, TypeScript, C#, Go, and 25+ additional languages out of the box. The agent triggers scans via sonar-scanner with configurable sonar-project.properties, monitors analysis progress through the ce/task endpoint, and retrieves detailed results including code smells, bugs, security vulnerabilities, and technical debt metrics. Quality gate status is checked via api/qualitygates/project_status. Key capabilities include pull request decoration with inline comments on new issues, branch analysis comparison, and trend tracking across multiple project versions. The agent can enforce custom quality profiles and block merges when quality gates fail. Integration with CI/CD pipelines is supported through webhook listeners that process analysis completion events and route results to Slack, Teams, or email notifications.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/)
