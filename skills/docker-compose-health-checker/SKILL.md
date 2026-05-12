---
title: "Docker Compose Health Checker"
slug: "docker-compose-health-checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Compose Health Checker

Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
