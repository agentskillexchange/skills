---
title: "SonarQube Gate Checker"
description: "Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Gate Checker

Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-gate-checker-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-gate-checker-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-checker-2/)
