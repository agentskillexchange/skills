---
title: "SonarQube Analysis Agent"
description: "Integrates with the SonarQube REST API to run static code analysis scans, retrieve quality gate results, and flag code smells. Supports SonarCloud and on-premise SonarQube instances via token-based authentication."
slug: "sonarqube-analysis-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-analysis-agent/"
listed: true
---

# SonarQube Analysis Agent

Integrates with the SonarQube REST API to run static code analysis scans, retrieve quality gate results, and flag code smells. Supports SonarCloud and on-premise SonarQube instances via token-based authentication.

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
clawhub install sonarqube-analysis-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Analysis Agent connects to your SonarQube or SonarCloud instance via the official REST API (api/qualitygates, api/issues, api/measures) to automate static code analysis workflows. It authenticates using project-scoped tokens and retrieves detailed quality gate status, code smell counts, vulnerability reports, and technical debt estimates.
Designed for CI/CD pipelines, the agent can be triggered after each commit or pull request to run incremental analysis. It parses the SonarQube webhook payload to determine pass/fail status and surfaces actionable findings directly in your development workflow. Supports multi-language projects including Java, Python, JavaScript, TypeScript, Go, and C#.
The agent also tracks quality trends over time by querying the measures API for metrics like cyclomatic complexity, duplicated lines percentage, and coverage ratios. Results can be formatted as markdown reports or posted as PR comments via the GitHub Checks API integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-agent/)
