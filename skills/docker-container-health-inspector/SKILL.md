---
title: "Docker Container Health Inspector"
slug: "docker-container-health-inspector"
description: "Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming."
verification: security_reviewed
source: "https://github.com/moby/moby"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Container Health Inspector

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/)
