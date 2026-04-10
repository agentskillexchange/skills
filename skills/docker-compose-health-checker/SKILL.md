---
title: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
slug: "docker-compose-health-checker"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/docker-compose-health-checker/"
---

# Docker Compose Health Checker

Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install docker-compose-health-checker
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment.
The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports.
Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
