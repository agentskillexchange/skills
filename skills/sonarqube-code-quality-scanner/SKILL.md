---
name: "SonarQube Code Quality Scanner"
description: "Runs SonarQube static analysis via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities across 30+ languages with quality gate enforcement."
category: "Code Quality &amp; Review"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
tool_ecosystem:
  tool: sonarqube
  github_repo: SonarSource/sonarqube
  github_stars: 10379
  license: LGPL-3.0
  maintained: true
---
# SonarQube Code Quality Scanner

Runs SonarQube static analysis via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities across 30+ languages with quality gate enforcement.

## Overview

The SonarQube Code Quality Scanner skill integrates with the SonarQube Web API (api/qualitygates, api/issues, api/measures) and the sonar-scanner CLI to perform comprehensive static code analysis. It supports configuration via sonar-project.properties files and can target specific branches or pull requests using the sonar.branch.name and sonar.pullrequest parameters.

The skill retrieves quality gate status through the api/qualitygates/project_status endpoint, fetches detailed issue breakdowns from api/issues/search with severity filtering (BLOCKER, CRITICAL, MAJOR, MINOR, INFO), and pulls code coverage metrics from api/measures/component. It supports SonarQube Community, Developer, Enterprise, and Data Center editions.

Key capabilities include automated PR decoration with inline code review comments, quality gate enforcement that blocks merges when thresholds are not met, historical trend analysis via api/measures/search_history, and custom quality profile management through api/qualityprofiles. The scanner supports Java, Python, JavaScript, TypeScript, C#, Go, PHP, Ruby, Kotlin, Swift, and 20+ additional languages through built-in analyzers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-quality-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-quality-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-quality-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sonarqube-code-quality-scanner -a codex
```

### OpenClaw

```bash
clawhub install sonarqube-code-quality-scanner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/)
