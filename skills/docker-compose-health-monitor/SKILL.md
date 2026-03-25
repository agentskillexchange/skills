---
name: "Docker Compose Health Monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Overview

The Docker Compose Health Monitor skill provides continuous health assessment of multi-container Docker Compose environments. It queries the Docker Engine API endpoint /containers/{id}/json to retrieve detailed container state including health check results, restart counts via the RestartCount field, and resource utilization through the /containers/{id}/stats stream.

This skill parses docker-compose ps output to map service names to container IDs, then performs comprehensive health checks including TCP port probing, HTTP endpoint verification, and custom health check script execution. It correlates container health transitions with log entries retrieved through the /containers/{id}/logs endpoint using timestamp-based filtering.

Automated diagnostics include detecting OOM-killed containers through the OOMKilled state flag, identifying port conflicts between services, monitoring volume mount availability, and tracking image digest changes that indicate unexpected updates. The skill supports Docker Compose v2 file format with profiles and service dependencies.

Alerting capabilities include configurable thresholds for restart frequency, memory usage percentage, and health check failure rates. The skill generates dependency graphs showing service relationships and propagation paths for cascading failures across linked services.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor -a codex
```

### OpenClaw

```bash
clawhub install docker-compose-health-monitor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/docker-compose-health-monitor/
