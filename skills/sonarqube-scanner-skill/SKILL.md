---
title: "SonarQube Scanner Skill"
description: "Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations."
slug: "sonarqube-scanner-skill"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/sonarqube-scanner-skill/"
---

# SonarQube Scanner Skill

Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations.

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
clawhub install sonarqube-scanner-skill
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SonarQube Scanner Skill provides end-to-end integration with SonarQube for automated code quality analysis. It wraps the sonar-scanner CLI to trigger analysis runs and then queries the SonarQube Web API to retrieve detailed results.
The skill begins by configuring sonar-project.properties dynamically based on the repository structure, detecting language profiles for Java, Python, JavaScript, TypeScript, Go, and C#. It runs sonar-scanner with appropriate JVM arguments and waits for the background task to complete using api/ce/task polling.
Once analysis completes, it fetches quality gate status from api/qualitygates/project_status and retrieves individual issues via api/issues/search with facets for severity, type, and effort. Each issue is mapped to its source file and line number, enabling the agent to post inline annotations on pull requests through the GitHub or GitLab review API.
Additional capabilities include tracking quality gate trends over time, comparing metrics between branches using api/measures/component, generating PDF reports via api/reports, and configuring custom quality profiles through api/qualityprofiles/create.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-scanner-skill/)
