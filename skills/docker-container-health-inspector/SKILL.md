---
title: "Docker Container Health Inspector"
description: "The Docker Container Health Inspector skill automates the diagnosis of Docker container runtime issues using the Docker Engine API v1.45. It connects to the Docker daemon via the Unix socket or TCP endpoint to query container state, resource usage, and health check results. The skill retrieves detailed container inspection data from /containers/{id}/json including State.OOMKilled, RestartCount, and HealthCheck.Status fields. It streams real-time resource metrics from /containers/{id}/stats to identify memory leaks (growing RSS without release), CPU throttling (nr_throttled periods), and I/O bottlenecks (blkio service bytes). Diagnostic capabilities include analyzing container logs via /containers/{id}/logs with timestamps and tail parameters to pinpoint crash sequences, inspecting Docker network configurations through /networks/{id} for DNS resolution and inter-container connectivity issues, checking volume mount permissions and disk space via /system/df, and reviewing image layer history with /images/{id}/history for bloated or vulnerable base images. The skill generates structured health reports with remediation steps including docker-compose.yml fixes for resource limits, healthcheck interval tuning, restart policy recommendations (unless-stopped vs. on-failure with max-retry), and Dockerfile optimization suggestions for multi-stage builds."
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

# Docker Container Health Inspector

The Docker Container Health Inspector skill automates the diagnosis of Docker container runtime issues using the Docker Engine API v1.45. It connects to the Docker daemon via the Unix socket or TCP endpoint to query container state, resource usage, and health check results. The skill retrieves detailed container inspection data from /containers/{id}/json including State.OOMKilled, RestartCount, and HealthCheck.Status fields. It streams real-time resource metrics from /containers/{id}/stats to identify memory leaks (growing RSS without release), CPU throttling (nr_throttled periods), and I/O bottlenecks (blkio service bytes). Diagnostic capabilities include analyzing container logs via /containers/{id}/logs with timestamps and tail parameters to pinpoint crash sequences, inspecting Docker network configurations through /networks/{id} for DNS resolution and inter-container connectivity issues, checking volume mount permissions and disk space via /system/df, and reviewing image layer history with /images/{id}/history for bloated or vulnerable base images. The skill generates structured health reports with remediation steps including docker-compose.yml fixes for resource limits, healthcheck interval tuning, restart policy recommendations (unless-stopped vs. on-failure with max-retry), and Dockerfile optimization suggestions for multi-stage builds.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/)
