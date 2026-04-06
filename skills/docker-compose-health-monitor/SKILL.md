---
title: "Docker Compose Health Monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
slug: "docker-compose-health-monitor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

You can install this skill in any of these ways:

1. Install from Agent Skill Exchange in the OpenClaw UI
2. Clone or copy the skill folder into your local skills directory
3. Add it to your workspace-managed skills collection
4. Install via any compatible skill package manager or sync workflow
5. Copy the `SKILL.md` and any referenced files into a compatible AgentSkills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
