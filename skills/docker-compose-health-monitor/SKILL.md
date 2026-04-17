---
name: Docker Compose Health Monitor
description: Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json)
  and docker-compose ps parsing. Tracks container restart counts via the RestartCount
  field and logs analysis through the /containers/{id}/logs endpoint.
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
# Docker Compose Health Monitor
Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-compose-health-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docker-compose-health-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
