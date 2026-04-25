---
title: "SonarQube Rule Enforcement Agent"
description: "Integrates with SonarQube Web API and sonar-scanner CLI to enforce code quality gates across pull requests. Automatically blocks merges when critical code smells, security hotspots, or duplications exceed configurable thresholds."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality &amp; Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
---

# SonarQube Rule Enforcement Agent

Integrates with SonarQube Web API and sonar-scanner CLI to enforce code quality gates across pull requests. Automatically blocks merges when critical code smells, security hotspots, or duplications exceed configurable thresholds.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-rule-enforcement-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-rule-enforcement-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-rule-enforcement-agent/)
