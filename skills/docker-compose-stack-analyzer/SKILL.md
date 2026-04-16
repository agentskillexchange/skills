---
title: "Docker Compose Stack Analyzer"
description: "Analyzes Docker Compose configurations for security, networking, and resource optimization using the Docker Engine API and Compose specification parser. Detects misconfigurations and dependency issues."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Developer Tools"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Compose Stack Analyzer

The Docker Compose Stack Analyzer skill parses Docker Compose YAML files against the Compose specification to validate service definitions, network configurations, volume mounts, and dependency graphs. It connects to the Docker Engine API to compare declared configurations against running container states, identifying configuration drift and resource utilization mismatches. The skill performs security analysis including privileged container detection, host namespace sharing risks, sensitive environment variable exposure, and image vulnerability correlation using Docker Scout API. Features include service startup order optimization via depends_on health check analysis, network isolation verification across compose projects, and resource limit recommendations based on container runtime statistics from the Stats API. Supports multi-file compose configuration merging and override chain validation.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-stack-analyzer/)
