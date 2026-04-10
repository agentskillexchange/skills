---
title: "SonarQube Code Quality Scanner"
description: "Runs SonarQube static analysis via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities across 30+ languages with quality gate enforcement."
slug: "sonarqube-code-quality-scanner"
category:
  - "Code Quality &amp; Review"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/"
---

# SonarQube Code Quality Scanner

Runs SonarQube static analysis via the SonarQube Web API and sonar-scanner CLI. Detects code smells, bugs, and security vulnerabilities across 30+ languages with quality gate enforcement.

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
clawhub install sonarqube-code-quality-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Code Quality Scanner skill integrates with the SonarQube Web API (api/qualitygates, api/issues, api/measures) and the sonar-scanner CLI to perform comprehensive static code analysis. It supports configuration via sonar-project.properties files and can target specific branches or pull requests using the sonar.branch.name and sonar.pullrequest parameters.
The skill retrieves quality gate status through the api/qualitygates/project_status endpoint, fetches detailed issue breakdowns from api/issues/search with severity filtering (BLOCKER, CRITICAL, MAJOR, MINOR, INFO), and pulls code coverage metrics from api/measures/component. It supports SonarQube Community, Developer, Enterprise, and Data Center editions.
Key capabilities include automated PR decoration with inline code review comments, quality gate enforcement that blocks merges when thresholds are not met, historical trend analysis via api/measures/search_history, and custom quality profile management through api/qualityprofiles. The scanner supports Java, Python, JavaScript, TypeScript, C#, Go, PHP, Ruby, Kotlin, Swift, and 20+ additional languages through built-in analyzers.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/)
