---
title: "Docker Image Layer Analyzer"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Calculates layer sizes, identifies wasted space, and suggests multi-stage build optimizations."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Image Layer Analyzer

The Docker Image Layer Analyzer skill provides deep inspection of container image structure for optimization and security review. Using the Docker Registry HTTP API v2, it retrieves image manifests and layer digests from any OCI-compliant registry. The dive CLI tool is leveraged for detailed layer-by-layer filesystem analysis, identifying files added, modified, or removed at each build step. Layer size calculations pinpoint the largest contributors to image bloat, flagging unnecessary build artifacts, cached package manager files, and development dependencies. Wasted space analysis detects files that are added in one layer and removed in a subsequent layer, still consuming space in the final image. The skill suggests multi-stage build patterns to separate build-time dependencies from runtime images. Dockerfile best practice analysis covers instruction ordering for cache optimization, USER directive security, and HEALTHCHECK configuration.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/docker-image-layer-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-image-layer-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/docker-image-layer-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-analyzer/)
