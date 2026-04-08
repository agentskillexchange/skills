---
title: SonarQube Analysis Agent
description: The SonarQube Analysis Agent connects to your SonarQube or SonarCloud
  instance via the official REST API (api/qualitygates, api/issues, api/measures)
  to automate static code analysis workflows. It authenticates using project-scoped
  tokens and retrieves detailed quality gate status, code smell counts, vulnerability
  reports, and technical debt estimates. Designed for CI/CD pipelines, the agent can
  be triggered after each commit or pull request to run incremental analysis. It parses
  the SonarQube webhook payload to determine pass/fail status and surfaces actionable
  findings directly in your development workflow. Supports multi-language projects
  including Java, Python, JavaScript, TypeScript, Go, and C#. The agent also tracks
  quality trends over time by querying the measures API for metrics like cyclomatic
  complexity, duplicated lines percentage, and coverage ratios. Results can be formatted
  as markdown reports or posted as PR comments via the GitHub Checks API integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-analysis-agent/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# SonarQube Analysis Agent

The SonarQube Analysis Agent connects to your SonarQube or SonarCloud instance via the official REST API (api/qualitygates, api/issues, api/measures) to automate static code analysis workflows. It authenticates using project-scoped tokens and retrieves detailed quality gate status, code smell counts, vulnerability reports, and technical debt estimates. Designed for CI/CD pipelines, the agent can be triggered after each commit or pull request to run incremental analysis. It parses the SonarQube webhook payload to determine pass/fail status and surfaces actionable findings directly in your development workflow. Supports multi-language projects including Java, Python, JavaScript, TypeScript, Go, and C#. The agent also tracks quality trends over time by querying the measures API for metrics like cyclomatic complexity, duplicated lines percentage, and coverage ratios. Results can be formatted as markdown reports or posted as PR comments via the GitHub Checks API integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-agent/)
