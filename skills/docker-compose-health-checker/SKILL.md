---
name: Docker Compose Health Checker
description: Validates docker-compose.yml files against the Compose Specification,
  checks image vulnerability status via Docker Scout API, and verifies healthcheck
  configurations.
category: Runbooks & Diagnostics
framework: MCP
verification: security_reviewed
source: https://github.com/moby/moby
tool_ecosystem:
  github_repo: moby/moby
  github_stars: 71492
  tool: moby
  license: Apache-2.0
  maintained: true
---
# Docker Compose Health Checker
Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-compose-health-checker
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docker-compose-health-checker` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
