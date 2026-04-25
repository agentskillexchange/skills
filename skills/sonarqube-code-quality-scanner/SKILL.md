---
title: "SonarQube Code Quality Scanner"
description: "Runs SonarQube static analysis via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities across 30+ languages with quality gate enforcement."
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality & Review"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Code Quality Scanner

The SonarQube Code Quality Scanner skill integrates with the SonarQube Web API (api/qualitygates, api/issues, api/measures) and the sonar-scanner CLI to perform comprehensive static code analysis. It supports configuration via sonar-project.properties files and can target specific branches or pull requests using the sonar.branch.name and sonar.pullrequest parameters.

The skill retrieves quality gate status through the api/qualitygates/project_status endpoint, fetches detailed issue breakdowns from api/issues/search with severity filtering (BLOCKER, CRITICAL, MAJOR, MINOR, INFO), and pulls code coverage metrics from api/measures/component. It supports SonarQube Community, Developer, Enterprise, and Data Center editions.

Key capabilities include automated PR decoration with inline code review comments, quality gate enforcement that blocks merges when thresholds are not met, historical trend analysis via api/measures/search_history, and custom quality profile management through api/qualityprofiles. The scanner supports Java, Python, JavaScript, TypeScript, C#, Go, PHP, Ruby, Kotlin, Swift, and 20+ additional languages through built-in analyzers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-code-quality-scanner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sonarqube-code-quality-scanner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/)
