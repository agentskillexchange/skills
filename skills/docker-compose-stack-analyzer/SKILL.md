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
---

# Docker Compose Stack Analyzer

The Docker Compose Stack Analyzer skill parses Docker Compose YAML files against the Compose specification to validate service definitions, network configurations, volume mounts, and dependency graphs. It connects to the Docker Engine API to compare declared configurations against running container states, identifying configuration drift and resource utilization mismatches. The skill performs security analysis including privileged container detection, host namespace sharing risks, sensitive environment variable exposure, and image vulnerability correlation using Docker Scout API. Features include service startup order optimization via depends_on health check analysis, network isolation verification across compose projects, and resource limit recommendations based on container runtime statistics from the Stats API. Supports multi-file compose configuration merging and override chain validation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-compose-stack-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-compose-stack-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-compose-stack-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-stack-analyzer/)
