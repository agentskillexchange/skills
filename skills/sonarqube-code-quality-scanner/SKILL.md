---
title: SonarQube Code Quality Scanner
description: The SonarQube Code Quality Scanner skill integrates with the SonarQube
  Web API (api/qualitygates, api/issues, api/measures) and the sonar-scanner CLI to
  perform comprehensive static code analysis. It supports configuration via sonar-project.properties
  files and can target specific branches or pull requests using the sonar.branch.name
  and sonar.pullrequest parameters. The skill retrieves quality gate status through
  the api/qualitygates/project_status endpoint, fetches detailed issue breakdowns
  from api/issues/search with severity filtering (BLOCKER, CRITICAL, MAJOR, MINOR,
  INFO), and pulls code coverage metrics from api/measures/component. It supports
  SonarQube Community, Developer, Enterprise, and Data Center editions. Key capabilities
  include automated PR decoration with inline code review comments, quality gate enforcement
  that blocks merges when thresholds are not met, historical trend analysis via api/measures/search_history,
  and custom quality profile management through api/qualityprofiles. The scanner supports
  Java, Python, JavaScript, TypeScript, C#, Go, PHP, Ruby, Kotlin, Swift, and 20+
  additional languages through built-in analyzers.
verification: security_reviewed
source: https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/
category:
- Code Quality &amp; Review
framework:
- OpenClaw
---

# SonarQube Code Quality Scanner

The SonarQube Code Quality Scanner skill integrates with the SonarQube Web API (api/qualitygates, api/issues, api/measures) and the sonar-scanner CLI to perform comprehensive static code analysis. It supports configuration via sonar-project.properties files and can target specific branches or pull requests using the sonar.branch.name and sonar.pullrequest parameters. The skill retrieves quality gate status through the api/qualitygates/project_status endpoint, fetches detailed issue breakdowns from api/issues/search with severity filtering (BLOCKER, CRITICAL, MAJOR, MINOR, INFO), and pulls code coverage metrics from api/measures/component. It supports SonarQube Community, Developer, Enterprise, and Data Center editions. Key capabilities include automated PR decoration with inline code review comments, quality gate enforcement that blocks merges when thresholds are not met, historical trend analysis via api/measures/search_history, and custom quality profile management through api/qualityprofiles. The scanner supports Java, Python, JavaScript, TypeScript, C#, Go, PHP, Ruby, Kotlin, Swift, and 20+ additional languages through built-in analyzers.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-code-quality-scanner/)
