---
name: "Docker Compose Stack Analyzer"
description: "Analyzes Docker Compose configurations for security, networking, and resource optimization using the Docker Engine API and Compose specification parser. Detects misconfigurations and dependency issues."
category: "Developer Tools"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-compose-stack-analyzer/"
tool_ecosystem:
  tool: "docker"
  github_stars: 71560
  github_repo: "moby/moby"
  license: "Apache-2.0"
  maintained: true
---

# Docker Compose Stack Analyzer

Analyzes Docker Compose configurations for security, networking, and resource optimization using the Docker Engine API and Compose specification parser. Detects misconfigurations and dependency issues.

## Overview

The Docker Compose Stack Analyzer skill parses Docker Compose YAML files against the Compose specification to validate service definitions, network configurations, volume mounts, and dependency graphs. It connects to the Docker Engine API to compare declared configurations against running container states, identifying configuration drift and resource utilization mismatches. The skill performs security analysis including privileged container detection, host namespace sharing risks, sensitive environment variable exposure, and image vulnerability correlation using Docker Scout API. Features include service startup order optimization via depends_on health check analysis, network isolation verification across compose projects, and resource limit recommendations based on container runtime statistics from the Stats API. Supports multi-file compose configuration merging and override chain validation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-compose-stack-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-compose-stack-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-compose-stack-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-compose-stack-analyzer -a codex
```

### OpenClaw

```bash
clawhub install docker-compose-stack-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/docker-compose-stack-analyzer/
