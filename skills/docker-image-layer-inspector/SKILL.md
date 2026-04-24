---
title: "Docker Image Layer Inspector"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and Dive CLI. Identifies wasted space, duplicate files, and optimizes Dockerfile instructions for smaller builds."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "CI/CD Integrations"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Image Layer Inspector

Analyzes Docker image layers using the Docker Registry HTTP API v2 and Dive CLI. Identifies wasted space, duplicate files, and optimizes Dockerfile instructions for smaller builds.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-image-layer-inspector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-image-layer-inspector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-image-layer-inspector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-inspector/)
