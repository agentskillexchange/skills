---
title: Docker Image Layer Size Analyzer
description: Analyzes Docker image layers using the Docker Registry HTTP API v2 and
  dive CLI tool. Identifies bloated layers, wasted space from deleted files, and suggests
  multi-stage build optimizations.
verification: security_reviewed
source: https://github.com/moby/moby
category:
- CI/CD Integrations
framework:
- Gemini
tool_ecosystem:
  github_repo: moby/moby
  github_stars: 71492
---

# Docker Image Layer Size Analyzer

Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Identifies bloated layers, wasted space from deleted files, and suggests multi-stage build optimizations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-image-layer-size-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-image-layer-size-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
