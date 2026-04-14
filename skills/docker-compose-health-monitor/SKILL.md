---
title: "Docker Compose Health Monitor"
slug: "docker-compose-health-monitor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
---
# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
