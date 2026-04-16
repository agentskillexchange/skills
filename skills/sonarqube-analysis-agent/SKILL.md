---
title: "SonarQube Analysis Agent"
description: "Integrates with the SonarQube REST API to run static code analysis scans, retrieve quality gate results, and flag code smells. Supports SonarCloud and on-premise SonarQube instances via token-based authentication."
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  license: "LGPL-3.0"
---

# SonarQube Analysis Agent

The SonarQube Analysis Agent connects to your SonarQube or SonarCloud instance via the official REST API (api/qualitygates, api/issues, api/measures) to automate static code analysis workflows. It authenticates using project-scoped tokens and retrieves detailed quality gate status, code smell counts, vulnerability reports, and technical debt estimates.

Designed for CI/CD pipelines, the agent can be triggered after each commit or pull request to run incremental analysis. It parses the SonarQube webhook payload to determine pass/fail status and surfaces actionable findings directly in your development workflow. Supports multi-language projects including Java, Python, JavaScript, TypeScript, Go, and C#.

The agent also tracks quality trends over time by querying the measures API for metrics like cyclomatic complexity, duplicated lines percentage, and coverage ratios. Results can be formatted as markdown reports or posted as PR comments via the GitHub Checks API integration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-agent/)
