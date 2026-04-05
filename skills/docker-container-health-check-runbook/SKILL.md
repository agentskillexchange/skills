---
name: "Docker Container Health Check Runbook"
description: "Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity."
category: "Runbooks &amp; Diagnostics"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-container-health-check-runbook/"
---
# Docker Container Health Check Runbook

Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-check-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-check-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-check-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-check-runbook -a codex
```

### OpenClaw

```bash
clawhub install docker-container-health-check-runbook
```

## Details

This skill provides automated health diagnostics for Docker containers and Docker Compose stacks. It queries the Docker Engine API to inspect container states, resource consumption, and configuration details. The runbook checks container health status via HEALTHCHECK definitions, analyzes docker stats output for CPU throttling and memory pressure, and verifies network connectivity between containers using docker network inspect. It examines volume mounts for permission issues and disk space constraints, checks for zombie processes inside containers via docker top, and validates environment variable injection. The skill parses docker events streams to identify restart loops and OOM kills, analyzes Dockerfile layers for size optimization opportunities using dive, and checks for known vulnerabilities in base images via trivy scanning. It generates structured reports with container-specific remediation steps and can automatically restart unhealthy containers or scale services via Docker Compose.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-check-runbook/)
