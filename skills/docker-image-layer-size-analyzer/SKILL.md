---
title: "Docker Image Layer Size Analyzer"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Identifies bloated layers, wasted space from deleted files, and suggests multi-stage build optimizations."
verification: security_reviewed
source: "https://github.com/moby/moby"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Image Layer Size Analyzer

The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip –no-cache-dir, npm prune –production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/docker-image-layer-size-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/docker-image-layer-size-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
