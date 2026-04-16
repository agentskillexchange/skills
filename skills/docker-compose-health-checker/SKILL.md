---
title: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Compose Health Checker

The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment.

The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports.

Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
