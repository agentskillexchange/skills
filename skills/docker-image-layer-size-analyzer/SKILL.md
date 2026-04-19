---
title: "Docker Image Layer Size Analyzer"
description: "The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip &#8211;no-cache-dir, npm prune &#8211;production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry."
source: "https://github.com/moby/moby"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
---

# Docker Image Layer Size Analyzer

The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip &#8211;no-cache-dir, npm prune &#8211;production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
