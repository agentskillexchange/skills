---
name: Docker Compose Health Monitor
description: Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.3
reviews: 48
source: https://agentskillexchange.com/skill/docker-compose-health-monitor/
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Overview

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor
```

### OpenClaw

```bash
clawhub install docker-compose-health-monitor
```

### Claude Code

```bash
claude mcp add docker-compose-health-monitor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/docker-compose-health-monitor/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.3/5 (48 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/docker-compose-health-monitor/)
