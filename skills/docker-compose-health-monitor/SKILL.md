---
name: Docker Compose Health Monitor
description: Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json)
  and docker-compose ps parsing. Tracks container restart counts via the RestartCount
  field and logs analysis through the /containers/{id}/logs endpoint.
verification: security_reviewed
source: https://agentskillexchange.com/skills/docker-compose-health-monitor/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---
# Docker Compose Health Monitor

The Docker Compose Health Monitor skill provides continuous health assessment of multi-container Docker Compose environments. It queries the Docker Engine API endpoint /containers/{id}/json to retrieve detailed container state including health check results, restart counts via the RestartCount field, and resource utilization through the /containers/{id}/stats stream.
This skill parses docker-compose ps output to map service names to container IDs, then performs comprehensive health checks including TCP port probing, HTTP endpoint verification, and custom health check script execution. It correlates container health transitions with log entries retrieved through the /containers/{id}/logs endpoint using timestamp-based filtering.
Automated diagnostics include detecting OOM-killed containers through the OOMKilled state flag, identifying port conflicts between services, monitoring volume mount availability, and tracking image digest changes that indicate unexpected updates. The skill supports Docker Compose v2 file format with profiles and service dependencies.
Alerting capabilities include configurable thresholds for restart frequency, memory usage percentage, and health check failure rates. The skill generates dependency graphs showing service relationships and propagation paths for cascading failures across linked services.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
