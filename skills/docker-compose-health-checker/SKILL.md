---
name: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-compose-health-checker/"
tool_ecosystem:
  tool: docker
  github_stars: 71560
  github_repo: moby/moby
  license: Apache-2.0
  maintained: true
---

# Docker Compose Health Checker

Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Overview

The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment.

The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports.

Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker -a codex
```

### OpenClaw

```bash
clawhub install docker-compose-health-checker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/docker-compose-health-checker/
