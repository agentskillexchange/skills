---
title: "SonarQube Quality Gate Enforcer"
description: "Enforces SonarQube quality gates in pull request workflows using the SonarQube Web API and ce/task endpoint. Blocks merges when code coverage drops, duplications exceed thresholds, or security hotspots are unreviewed."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality & Review"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
  license: "LGPL-3.0"
---

# SonarQube Quality Gate Enforcer

The SonarQube Quality Gate Enforcer skill integrates SonarQube quality gate enforcement into pull request workflows. It queries the SonarQube Web API measures/component endpoint to fetch real-time quality metrics including code coverage, duplicated lines percentage, cognitive complexity, and security hotspot counts. The skill monitors the ce/task endpoint for analysis completion and evaluates results against configurable quality gate profiles. When violations are detected, it posts detailed PR comments breaking down each failed condition with specific file-level metrics and remediation guidance. Supports multi-language projects with per-language threshold overrides. Can enforce differential quality gates that apply stricter standards to new code versus legacy code. Integrates with GitHub Check Runs API to create blocking status checks. Generates trend reports showing quality metric trajectories across releases. Works with SonarQube Community, Developer, and Enterprise editions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-quality-gate-enforcer-14
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-quality-gate-enforcer-14` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-quality-gate-enforcer-14/)
