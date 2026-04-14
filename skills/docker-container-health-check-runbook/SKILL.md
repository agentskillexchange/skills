---
title: "Docker Container Health Check Runbook"
description: "Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity."
verification: security_reviewed
source: "https://github.com/moby/moby"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-check-runbook/)
