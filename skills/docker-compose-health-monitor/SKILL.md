---
title: "Docker Compose Health Monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Compose Health Monitor

The Docker Compose Health Monitor skill provides continuous health assessment of multi-container Docker Compose environments. It queries the Docker Engine API endpoint /containers/{id}/json to retrieve detailed container state including health check results, restart counts via the RestartCount field, and resource utilization through the /containers/{id}/stats stream.

This skill parses docker-compose ps output to map service names to container IDs, then performs comprehensive health checks including TCP port probing, HTTP endpoint verification, and custom health check script execution. It correlates container health transitions with log entries retrieved through the /containers/{id}/logs endpoint using timestamp-based filtering.

Automated diagnostics include detecting OOM-killed containers through the OOMKilled state flag, identifying port conflicts between services, monitoring volume mount availability, and tracking image digest changes that indicate unexpected updates. The skill supports Docker Compose v2 file format with profiles and service dependencies.

Alerting capabilities include configurable thresholds for restart frequency, memory usage percentage, and health check failure rates. The skill generates dependency graphs showing service relationships and propagation paths for cascading failures across linked services.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
