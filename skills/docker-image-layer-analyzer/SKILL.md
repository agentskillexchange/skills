---
title: "Docker Image Layer Analyzer"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Calculates layer sizes, identifies wasted space, and suggests multi-stage build optimizations."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Image Layer Analyzer

The Docker Image Layer Analyzer skill provides deep inspection of container image structure for optimization and security review. Using the Docker Registry HTTP API v2, it retrieves image manifests and layer digests from any OCI-compliant registry. The dive CLI tool is leveraged for detailed layer-by-layer filesystem analysis, identifying files added, modified, or removed at each build step. Layer size calculations pinpoint the largest contributors to image bloat, flagging unnecessary build artifacts, cached package manager files, and development dependencies. Wasted space analysis detects files that are added in one layer and removed in a subsequent layer, still consuming space in the final image. The skill suggests multi-stage build patterns to separate build-time dependencies from runtime images. Dockerfile best practice analysis covers instruction ordering for cache optimization, USER directive security, and HEALTHCHECK configuration.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-image-layer-analyzer/)
