---
title: "Docker Compose Health Monitor"
description: "The Docker Compose Health Monitor skill provides continuous health assessment of multi-container Docker Compose environments. It queries the Docker Engine API endpoint /containers/{id}/json to retrieve detailed container state including health check results, restart counts via the RestartCount field, and resource utilization through the /containers/{id}/stats stream. This skill parses docker-compose ps output to map service names to container IDs, then performs comprehensive health checks including TCP port probing, HTTP endpoint verification, and custom health check script execution. It correlates container health transitions with log entries retrieved through the /containers/{id}/logs endpoint using timestamp-based filtering. Automated diagnostics include detecting OOM-killed containers through the OOMKilled state flag, identifying port conflicts between services, monitoring volume mount availability, and tracking image digest changes that indicate unexpected updates. The skill supports Docker Compose v2 file format with profiles and service dependencies. Alerting capabilities include configurable thresholds for restart frequency, memory usage percentage, and health check failure rates. The skill generates dependency graphs showing service relationships and propagation paths for cascading failures across linked services."
source: "https://github.com/moby/moby"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Compose Health Monitor

The Docker Compose Health Monitor skill provides continuous health assessment of multi-container Docker Compose environments. It queries the Docker Engine API endpoint /containers/{id}/json to retrieve detailed container state including health check results, restart counts via the RestartCount field, and resource utilization through the /containers/{id}/stats stream. This skill parses docker-compose ps output to map service names to container IDs, then performs comprehensive health checks including TCP port probing, HTTP endpoint verification, and custom health check script execution. It correlates container health transitions with log entries retrieved through the /containers/{id}/logs endpoint using timestamp-based filtering. Automated diagnostics include detecting OOM-killed containers through the OOMKilled state flag, identifying port conflicts between services, monitoring volume mount availability, and tracking image digest changes that indicate unexpected updates. The skill supports Docker Compose v2 file format with profiles and service dependencies. Alerting capabilities include configurable thresholds for restart frequency, memory usage percentage, and health check failure rates. The skill generates dependency graphs showing service relationships and propagation paths for cascading failures across linked services.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
