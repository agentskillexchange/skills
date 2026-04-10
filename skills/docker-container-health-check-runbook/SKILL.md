---
title: "Docker Container Health Check Runbook"
description: "Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity."
slug: "docker-container-health-check-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/docker-container-health-check-runbook/"
listed: true
---

# Docker Container Health Check Runbook

Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity.

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
clawhub install docker-container-health-check-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides automated health diagnostics for Docker containers and Docker Compose stacks. It queries the Docker Engine API to inspect container states, resource consumption, and configuration details. The runbook checks container health status via HEALTHCHECK definitions, analyzes docker stats output for CPU throttling and memory pressure, and verifies network connectivity between containers using docker network inspect. It examines volume mounts for permission issues and disk space constraints, checks for zombie processes inside containers via docker top, and validates environment variable injection. The skill parses docker events streams to identify restart loops and OOM kills, analyzes Dockerfile layers for size optimization opportunities using dive, and checks for known vulnerabilities in base images via trivy scanning. It generates structured reports with container-specific remediation steps and can automatically restart unhealthy containers or scale services via Docker Compose.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-check-runbook/)
