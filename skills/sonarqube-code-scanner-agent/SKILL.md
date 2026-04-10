---
title: "SonarQube Code Scanner Agent"
description: "Automated code quality scanning using SonarQube REST API and SonarScanner CLI. Detects code smells, bugs, and vulnerabilities across 30+ languages with configurable quality gates."
slug: "sonarqube-code-scanner-agent"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/"
---

# SonarQube Code Scanner Agent

Automated code quality scanning using SonarQube REST API and SonarScanner CLI. Detects code smells, bugs, and vulnerabilities across 30+ languages with configurable quality gates.

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
clawhub install sonarqube-code-scanner-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Code Scanner Agent integrates directly with SonarQube Server REST API (api/qualitygates, api/issues, api/measures) and SonarScanner CLI to perform comprehensive static code analysis. It supports Java, Python, JavaScript, TypeScript, C#, Go, and 25+ additional languages out of the box.
The agent triggers scans via sonar-scanner with configurable sonar-project.properties, monitors analysis progress through the ce/task endpoint, and retrieves detailed results including code smells, bugs, security vulnerabilities, and technical debt metrics. Quality gate status is checked via api/qualitygates/project_status.
Key capabilities include pull request decoration with inline comments on new issues, branch analysis comparison, and trend tracking across multiple project versions. The agent can enforce custom quality profiles and block merges when quality gates fail.
Integration with CI/CD pipelines is supported through webhook listeners that process analysis completion events and route results to Slack, Teams, or email notifications.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-scanner-agent/)
