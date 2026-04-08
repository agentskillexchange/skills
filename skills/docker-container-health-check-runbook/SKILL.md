---
title: Docker Container Health Check Runbook
description: This skill provides automated health diagnostics for Docker containers
  and Docker Compose stacks. It queries the Docker Engine API to inspect container
  states, resource consumption, and configuration details. The runbook checks container
  health status via HEALTHCHECK definitions, analyzes docker stats output for CPU
  throttling and memory pressure, and verifies network connectivity between containers
  using docker network inspect. It examines volume mounts for permission issues and
  disk space constraints, checks for zombie processes inside containers via docker
  top, and validates environment variable injection. The skill parses docker events
  streams to identify restart loops and OOM kills, analyzes Dockerfile layers for
  size optimization opportunities using dive, and checks for known vulnerabilities
  in base images via trivy scanning. It generates structured reports with container-specific
  remediation steps and can automatically restart unhealthy containers or scale services
  via Docker Compose.
verification: security_reviewed
source: https://agentskillexchange.com/skills/docker-container-health-check-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---

# Docker Container Health Check Runbook

This skill provides automated health diagnostics for Docker containers and Docker Compose stacks. It queries the Docker Engine API to inspect container states, resource consumption, and configuration details. The runbook checks container health status via HEALTHCHECK definitions, analyzes docker stats output for CPU throttling and memory pressure, and verifies network connectivity between containers using docker network inspect. It examines volume mounts for permission issues and disk space constraints, checks for zombie processes inside containers via docker top, and validates environment variable injection. The skill parses docker events streams to identify restart loops and OOM kills, analyzes Dockerfile layers for size optimization opportunities using dive, and checks for known vulnerabilities in base images via trivy scanning. It generates structured reports with container-specific remediation steps and can automatically restart unhealthy containers or scale services via Docker Compose.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-check-runbook/)
