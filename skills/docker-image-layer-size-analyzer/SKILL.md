---
name: Docker Image Layer Size Analyzer
description: Analyzes Docker image layers using the Docker Registry HTTP API v2 and
  dive CLI tool. Identifies bloated layers, wasted space from deleted files, and suggests
  multi-stage build optimizations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/
category:
- CI/CD Integrations
framework:
- Gemini
---
# Docker Image Layer Size Analyzer

The Docker Image Layer Size Analyzer connects to container registries via the Docker Registry HTTP API v2 to pull image manifests and layer metadata without downloading full images. It integrates with the dive CLI tool for deep layer-by-layer filesystem analysis, identifying wasted space from files added then deleted in subsequent layers, oversized package manager caches, and unnecessary build dependencies included in runtime images. The skill calculates an image efficiency score based on the ratio of actual content to total layer bytes, benchmarking against base image sizes. It generates specific Dockerfile optimization recommendations including multi-stage build patterns to separate build and runtime dependencies, .dockerignore improvements, package manager cache cleanup commands (apt-get clean, pip -no-cache-dir, npm prune -production), and layer ordering suggestions to maximize build cache hit rates. Supports analysis of images in Docker Hub, GitHub Container Registry, AWS ECR, and Google Artifact Registry.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-size-analyzer/)
