---
title: "Docker Container Health Check Runbook"
description: "This skill provides automated health diagnostics for Docker containers and Docker Compose stacks. It queries the Docker Engine API to inspect container states, resource consumption, and configuration details. The runbook checks container health status via HEALTHCHECK definitions, analyzes docker stats output for CPU throttling and memory pressure, and verifies network connectivity between containers using docker network inspect. It examines volume mounts for permission issues and disk space constraints, checks for zombie processes inside containers via docker top, and validates environment variable injection. The skill parses docker events streams to identify restart loops and OOM kills, analyzes Dockerfile layers for size optimization opportunities using dive, and checks for known vulnerabilities in base images via trivy scanning. It generates structured reports with container-specific remediation steps and can automatically restart unhealthy containers or scale services via Docker Compose."
source: "https://github.com/moby/moby"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Container Health Check Runbook

This skill provides automated health diagnostics for Docker containers and Docker Compose stacks. It queries the Docker Engine API to inspect container states, resource consumption, and configuration details. The runbook checks container health status via HEALTHCHECK definitions, analyzes docker stats output for CPU throttling and memory pressure, and verifies network connectivity between containers using docker network inspect. It examines volume mounts for permission issues and disk space constraints, checks for zombie processes inside containers via docker top, and validates environment variable injection. The skill parses docker events streams to identify restart loops and OOM kills, analyzes Dockerfile layers for size optimization opportunities using dive, and checks for known vulnerabilities in base images via trivy scanning. It generates structured reports with container-specific remediation steps and can automatically restart unhealthy containers or scale services via Docker Compose.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-check-runbook/)
