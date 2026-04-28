---
title: Docker Container Health Inspector
description: Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json
  and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network
  connectivity issues with automated log analysis via /containers/{id}/logs streaming.
verification: security_reviewed
source: https://github.com/moby/moby
category:
- Runbooks & Diagnostics
framework:
- MCP
tool_ecosystem:
  github_repo: moby/moby
  github_stars: 71492
---

# Docker Container Health Inspector

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-container-health-inspector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-container-health-inspector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-container-health-inspector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/)
