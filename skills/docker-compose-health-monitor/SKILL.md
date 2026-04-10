---
title: "Docker Compose Health Monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
slug: "docker-compose-health-monitor"
category:
  - "Runbooks &amp; Diagnostics"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install docker-compose-health-monitor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
