---
title: SonarQube Gate Enforcer
description: Enforces SonarQube quality gate conditions in CI pipelines using the
  SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when
  coverage drops, duplications exceed thresholds, or new bugs are introduced.
verification: security_reviewed
source: https://github.com/SonarSource/sonarqube
category:
- Code Quality & Review
framework:
- Cursor
tool_ecosystem:
  github_repo: sonarsource/sonarqube
  github_stars: 10433
---

# SonarQube Gate Enforcer

Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sonarqube-gate-enforcer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-gate-enforcer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sonarqube-gate-enforcer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/)
