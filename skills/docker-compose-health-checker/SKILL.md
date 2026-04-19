---
title: "Docker Compose Health Checker"
description: "The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment. The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports. Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports."
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

# Docker Compose Health Checker

The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment. The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports. Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
