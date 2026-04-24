---
title: "SonarQube Scanner Skill"
description: "Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations."
verification: "security_reviewed"
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Scanner Skill

Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sonarqube-scanner-skill/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-scanner-skill
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sonarqube-scanner-skill`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-scanner-skill/)
