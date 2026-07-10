---
name: "Docker Compose Health Monitor"
slug: "docker-compose-health-monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
github_stars: 71492
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

Use the upstream install or setup path that matches your environment:
- Docker Engine releases are tagged with a **docker-** prefix (e.g. docker-v29.0.0 for Docker Engine 29.0.0).

Requirements and caveats from upstream:
- Moby is an open-source project created by Docker to enable and accelerate software containerization.
- ## Relationship with Docker
- The components and tools in the Moby Project are initially the open source components that Docker and the community have built for the Docker Project.

- Source: https://github.com/moby/moby
- Extracted from upstream docs: https://raw.githubusercontent.com/moby/moby/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
