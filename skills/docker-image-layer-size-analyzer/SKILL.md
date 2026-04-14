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
---

# Docker Image Layer Size Analyzer

The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip –no-cache-dir, npm prune –production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
