---
name: "Docker Container Health Inspector"
description: "Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming."
category: "Runbooks &amp; Diagnostics"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-container-health-inspector/"
---
# Docker Container Health Inspector

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

The Docker Container Health Inspector skill automates the diagnosis of Docker container runtime issues using the Docker Engine API v1.45. It connects to the Docker daemon via the Unix socket or TCP endpoint to query container state, resource usage, and health check results.

The skill retrieves detailed container inspection data from /containers/{id}/json including State.OOMKilled, RestartCount, and HealthCheck.Status fields. It streams real-time resource metrics from /containers/{id}/stats to identify memory leaks (growing RSS without release), CPU throttling (nr_throttled periods), and I/O bottlenecks (blkio service bytes).

Diagnostic capabilities include analyzing container logs via /containers/{id}/logs with timestamps and tail parameters to pinpoint crash sequences, inspecting Docker network configurations through /networks/{id} for DNS resolution and inter-container connectivity issues, checking volume mount permissions and disk space via /system/df, and reviewing image layer history with /images/{id}/history for bloated or vulnerable base images. The skill generates structured health reports with remediation steps including docker-compose.yml fixes for resource limits, healthcheck interval tuning, restart policy recommendations (unless-stopped vs. on-failure with max-retry), and Dockerfile optimization suggestions for multi-stage builds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector -a codex
```

### OpenClaw

```bash
clawhub install docker-container-health-inspector
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/)
