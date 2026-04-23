---
title: "SonarQube Gate Checker"
description: "Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Templates &amp; Workflows"
framework:
  - "Claude Code"
---

# SonarQube Gate Checker

Queries the SonarQube Web API (/api/qualitygates/project_status) to evaluate quality gate conditions before merge. Reports code smells, coverage thresholds, and duplications against configurable SonarQube quality profiles.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sonarqube-gate-checker-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-gate-checker-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sonarqube-gate-checker-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-checker-2/)
