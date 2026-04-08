---
title: Docker Container Health Inspector
description: The Docker Container Health Inspector skill automates the diagnosis of
  Docker container runtime issues using the Docker Engine API v1.45. It connects to
  the Docker daemon via the Unix socket or TCP endpoint to query container state,
  resource usage, and health check results. The skill retrieves detailed container
  inspection data from /containers/{id}/json including State.OOMKilled, RestartCount,
  and HealthCheck.Status fields. It streams real-time resource metrics from /containers/{id}/stats
  to identify memory leaks (growing RSS without release), CPU throttling (nr_throttled
  periods), and I/O bottlenecks (blkio service bytes). Diagnostic capabilities include
  analyzing container logs via /containers/{id}/logs with timestamps and tail parameters
  to pinpoint crash sequences, inspecting Docker network configurations through /networks/{id}
  for DNS resolution and inter-container connectivity issues, checking volume mount
  permissions and disk space via /system/df, and reviewing image layer history with
  /images/{id}/history for bloated or vulnerable base images. The skill generates
  structured health reports with remediation steps including docker-compose.yml fixes
  for resource limits, healthcheck interval tuning, restart policy recommendations
  (unless-stopped vs. on-failure with max-retry), and Dockerfile optimization suggestions
  for multi-stage builds.
verification: security_reviewed
source: https://agentskillexchange.com/skills/docker-container-health-inspector/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---

# Docker Container Health Inspector

The Docker Container Health Inspector skill automates the diagnosis of Docker container runtime issues using the Docker Engine API v1.45. It connects to the Docker daemon via the Unix socket or TCP endpoint to query container state, resource usage, and health check results. The skill retrieves detailed container inspection data from /containers/{id}/json including State.OOMKilled, RestartCount, and HealthCheck.Status fields. It streams real-time resource metrics from /containers/{id}/stats to identify memory leaks (growing RSS without release), CPU throttling (nr_throttled periods), and I/O bottlenecks (blkio service bytes). Diagnostic capabilities include analyzing container logs via /containers/{id}/logs with timestamps and tail parameters to pinpoint crash sequences, inspecting Docker network configurations through /networks/{id} for DNS resolution and inter-container connectivity issues, checking volume mount permissions and disk space via /system/df, and reviewing image layer history with /images/{id}/history for bloated or vulnerable base images. The skill generates structured health reports with remediation steps including docker-compose.yml fixes for resource limits, healthcheck interval tuning, restart policy recommendations (unless-stopped vs. on-failure with max-retry), and Dockerfile optimization suggestions for multi-stage builds.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/)
