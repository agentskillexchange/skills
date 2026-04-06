---
name: "docker-compose-health-monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
category: "Runbooks &amp; Diagnostics"
framework: "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

You can install this skill using one of these common methods:

1. **ClawHub** — install from the marketplace if available.
2. **Git clone** — clone the skill folder into your local skills directory.
3. **Download ZIP** — download and extract the skill files manually.
4. **Copy files** — copy the skill directory into your agent skills path.
5. **Package manager / upstream installer** — use the original project installer if the source provides one.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
