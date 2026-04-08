---
title: Docker Compose Health Checker
description: The Docker Compose Health Checker agent validates Docker Compose configurations
  for correctness, security, and operational readiness. It parses docker-compose.yml
  files against the official Compose Specification to detect configuration errors
  before deployment. The agent validates service definitions including network configurations,
  volume mount permissions, port binding conflicts, and dependency ordering with depends_on
  conditions. It checks image references against Docker Hub API to verify image existence
  and tag availability, and uses the Docker Scout API to scan referenced images for
  known CVEs, providing severity-rated vulnerability reports. Healthcheck validation
  ensures all services have appropriate health checks defined with reasonable intervals,
  timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources)
  against common workload profiles, recommending appropriate CPU and memory limits.
  It validates environment variable references, detecting missing .env file entries
  and insecure secrets passed via environment. The agent also checks for common anti-patterns
  like running containers as root, using latest tags, and exposing unnecessary ports.
verification: security_reviewed
source: https://agentskillexchange.com/skills/docker-compose-health-checker/
category:
- Runbooks &amp; Diagnostics
framework:
- MCP
---

# Docker Compose Health Checker

The Docker Compose Health Checker agent validates Docker Compose configurations for correctness, security, and operational readiness. It parses docker-compose.yml files against the official Compose Specification to detect configuration errors before deployment. The agent validates service definitions including network configurations, volume mount permissions, port binding conflicts, and dependency ordering with depends_on conditions. It checks image references against Docker Hub API to verify image existence and tag availability, and uses the Docker Scout API to scan referenced images for known CVEs, providing severity-rated vulnerability reports. Healthcheck validation ensures all services have appropriate health checks defined with reasonable intervals, timeouts, and retry counts. The checker analyzes resource constraints (deploy.resources) against common workload profiles, recommending appropriate CPU and memory limits. It validates environment variable references, detecting missing .env file entries and insecure secrets passed via environment. The agent also checks for common anti-patterns like running containers as root, using latest tags, and exposing unnecessary ports.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
