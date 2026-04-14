---
title: "Docker Compose Stack Analyzer"
description: "Analyzes Docker Compose configurations for security, networking, and resource optimization using the Docker Engine API and Compose specification parser. Detects misconfigurations and dependency issues."
verification: security_reviewed
source: "https://github.com/moby/moby"
category:
  - "Developer Tools"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Compose Stack Analyzer

The Docker Compose Stack Analyzer skill parses Docker Compose YAML files against the Compose specification to validate service definitions, network configurations, volume mounts, and dependency graphs. It connects to the Docker Engine API to compare declared configurations against running container states, identifying configuration drift and resource utilization mismatches. The skill performs security analysis including privileged container detection, host namespace sharing risks, sensitive environment variable exposure, and image vulnerability correlation using Docker Scout API. Features include service startup order optimization via depends_on health check analysis, network isolation verification across compose projects, and resource limit recommendations based on container runtime statistics from the Stats API. Supports multi-file compose configuration merging and override chain validation.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-stack-analyzer/)
