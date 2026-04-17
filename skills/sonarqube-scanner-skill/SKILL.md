---
title: "SonarQube Scanner Skill"
description: "Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
  license: "LGPL-3.0"
---

# SonarQube Scanner Skill

The SonarQube Scanner Skill provides end-to-end integration with SonarQube for automated code quality analysis. It wraps the sonar-scanner CLI to trigger analysis runs and then queries the SonarQube Web API to retrieve detailed results.

The skill begins by configuring sonar-project.properties dynamically based on the repository structure, detecting language profiles for Java, Python, JavaScript, TypeScript, Go, and C#. It runs sonar-scanner with appropriate JVM arguments and waits for the background task to complete using api/ce/task polling.

Once analysis completes, it fetches quality gate status from api/qualitygates/project_status and retrieves individual issues via api/issues/search with facets for severity, type, and effort. Each issue is mapped to its source file and line number, enabling the agent to post inline annotations on pull requests through the GitHub or GitLab review API.

Additional capabilities include tracking quality gate trends over time, comparing metrics between branches using api/measures/component, generating PDF reports via api/reports, and configuring custom quality profiles through api/qualityprofiles/create.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-scanner-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-scanner-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-scanner-skill/)
