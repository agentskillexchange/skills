---
name: "Docker Image Layer Size Analyzer"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Identifies bloated layers, wasted space from deleted files, and suggests multi-stage build optimizations."
category: "CI/CD Integrations"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/"
---
# Docker Image Layer Size Analyzer

Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Identifies bloated layers, wasted space from deleted files, and suggests multi-stage build optimizations.

## Overview

The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip -no-cache-dir, npm prune -production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-size-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-size-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-size-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-size-analyzer -a codex
```

### OpenClaw

```bash
clawhub install docker-image-layer-size-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
