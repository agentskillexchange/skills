---
title: "Docker Container Health Inspector"
description: "Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Container Health Inspector

The Docker Container Health Inspector skill automates the diagnosis of Docker container runtime issues using the Docker Engine API v1.45. It connects to the Docker daemon via the Unix socket or TCP endpoint to query container state, resource usage, and health check results.


The skill retrieves detailed container inspection data from /containers/{id}/json including State.OOMKilled, RestartCount, and HealthCheck.Status fields. It streams real-time resource metrics from /containers/{id}/stats to identify memory leaks (growing RSS without release), CPU throttling (nr_throttled periods), and I/O bottlenecks (blkio service bytes).


Diagnostic capabilities include analyzing container logs via /containers/{id}/logs with timestamps and tail parameters to pinpoint crash sequences, inspecting Docker network configurations through /networks/{id} for DNS resolution and inter-container connectivity issues, checking volume mount permissions and disk space via /system/df, and reviewing image layer history with /images/{id}/history for bloated or vulnerable base images. The skill generates structured health reports with remediation steps including docker-compose.yml fixes for resource limits, healthcheck interval tuning, restart policy recommendations (unless-stopped vs. on-failure with max-retry), and Dockerfile optimization suggestions for multi-stage builds.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/)
