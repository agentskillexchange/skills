---
title: "SonarQube Code Scanner Agent"
description: "Automated code quality scanning using SonarQube REST API and SonarScanner CLI. Detects code smells, bugs, and vulnerabilities across 30+ languages with configurable quality gates."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Code Scanner Agent

The SonarQube Code Scanner Agent integrates directly with SonarQube Server REST API (api/qualitygates, api/issues, api/measures) and SonarScanner CLI to perform comprehensive static code analysis. It supports Java, Python, JavaScript, TypeScript, C#, Go, and 25+ additional languages out of the box.

The agent triggers scans via sonar-scanner with configurable sonar-project.properties, monitors analysis progress through the ce/task endpoint, and retrieves detailed results including code smells, bugs, security vulnerabilities, and technical debt metrics. Quality gate status is checked via api/qualitygates/project_status.

Key capabilities include pull request decoration with inline comments on new issues, branch analysis comparison, and trend tracking across multiple project versions. The agent can enforce custom quality profiles and block merges when quality gates fail.

Integration with CI/CD pipelines is supported through webhook listeners that process analysis completion events and route results to Slack, Teams, or email notifications.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-code-scanner-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-code-scanner-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/)
