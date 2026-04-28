---
title: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
verification: security_reviewed
source: "https://github.com/moby/moby"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Compose Health Checker

Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-compose-health-checker/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-compose-health-checker
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-compose-health-checker`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
