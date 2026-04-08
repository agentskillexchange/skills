---
title: Docker Image Layer Size Analyzer
description: The Docker Image Layer Size Analyzer connects to container registries
  via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without
  downloading full images. It integrates with the dive CLI tool for deep layer-by-layer
  filesystem analysis, identifying wasted space from files added then deleted in subsequent
  layers, oversized package manager caches, and unnecessary build dependencies included
  in runtime images. The skill calculates an image efficiency score based on the ratio
  of actual content to total layer bytes, benchmarking against base image sizes. It
  generates specific Dockerfile optimization recommendations including multi-stage
  build patterns to separate build and runtime dependencies, .dockerignore improvements,
  package manager cache cleanup commands (apt-get clean, pip –no-cache-dir, npm prune
  –production), and layer ordering suggestions to maximize build cache hit rates.
  Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and
  Google Artifact Registry.
verification: security_reviewed
source: https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/
category:
- CI/CD Integrations
framework:
- Gemini
---

# Docker Image Layer Size Analyzer

The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip –no-cache-dir, npm prune –production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
