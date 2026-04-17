---
title: "SonarQube PR Gate"
description: "Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API."
verification: security_reviewed
source: "https://github.com/SonarSource/sonarqube"
category:
  - "Code Quality & Review"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "sonarsource/sonarqube"
  github_stars: 10433
  license: "LGPL-3.0"
---

# SonarQube PR Gate

Overview Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API.

Key Features

- Automated detection and reporting with structured output formats for downstream integrations

- Configurable thresholds and rule sets that adapt to project-specific requirements and team conventions

- Real-time feedback loops integrated into developer workflows for immediate actionable insights

- Comprehensive logging and audit trails for compliance tracking and historical trend analysis

How It Works SonarQube PR Gate connects directly to your existing infrastructure through well-documented API endpoints. It authenticates using standard token-based methods (API keys, OAuth tokens, or service account credentials) and operates within your existing permission boundaries. The skill processes incoming data streams, applies configurable analysis rules, and produces structured reports that integrate with notification systems, dashboards, and issue trackers.

Requirements

- Valid API credentials with appropriate read/write scopes for the target service

- Network access to the relevant API endpoints from the agent runtime environment

- Compatible agent framework installed and configured with the necessary SDK dependencies

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sonarqube-pr-gate-skill
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/sonarqube-pr-gate-skill` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/)
