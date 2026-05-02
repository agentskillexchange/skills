---
title: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Runbooks & Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Compose Health Checker

The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment.

The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports.

Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-compose-health-checker/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-compose-health-checker
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-compose-health-checker`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
