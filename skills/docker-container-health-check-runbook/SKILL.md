---
title: "Docker Container Health Check Runbook"
description: "Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity."
verification: security_reviewed
source: "https://github.com/moby/moby"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Container Health Check Runbook

Runs systematic health diagnostics on Docker containers using docker inspect, docker stats, and the Docker Engine API. Checks resource limits, network connectivity, and volume mount integrity.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-container-health-check-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docker-container-health-check-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-check-runbook/)
