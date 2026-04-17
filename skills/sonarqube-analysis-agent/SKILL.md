---
title: "SonarQube Analysis Agent"
description: "The SonarQube Analysis Agent connects to your SonarQube or SonarCloud instance via the official REST API (api/qualitygates, api/issues, api/measures) to automate static code analysis workflows. It authenticates using project-scoped tokens and retrieves detailed quality gate status, code smell counts, vulnerability reports, and technical debt estimates.\nDesigned for CI/CD pipelines, the agent can be triggered after each commit or pull request to run incremental analysis. It parses the SonarQube webhook payload to determine pass/fail status and surfaces actionable findings directly in your development workflow. Supports multi-language projects including Java, Python, JavaScript, TypeScript, Go, and C#.\nThe agent also tracks quality trends over time by querying the measures API for metrics like cyclomatic complexity, duplicated lines percentage, and coverage ratios. Results can be formatted as markdown reports or posted as PR comments via the GitHub Checks API integration."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Analysis Agent

The SonarQube Analysis Agent connects to your SonarQube or SonarCloud instance via the official REST API (api/qualitygates, api/issues, api/measures) to automate static code analysis workflows. It authenticates using project-scoped tokens and retrieves detailed quality gate status, code smell counts, vulnerability reports, and technical debt estimates.
Designed for CI/CD pipelines, the agent can be triggered after each commit or pull request to run incremental analysis. It parses the SonarQube webhook payload to determine pass/fail status and surfaces actionable findings directly in your development workflow. Supports multi-language projects including Java, Python, JavaScript, TypeScript, Go, and C#.
The agent also tracks quality trends over time by querying the measures API for metrics like cyclomatic complexity, duplicated lines percentage, and coverage ratios. Results can be formatted as markdown reports or posted as PR comments via the GitHub Checks API integration.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-analysis-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-analysis-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-analysis-agent/)
