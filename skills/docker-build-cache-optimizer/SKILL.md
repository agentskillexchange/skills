---
title: "Docker Build Cache Optimizer"
description: "Optimizes Docker build performance using BuildKit cache mount analysis, docker history layer inspection, and Dockerfile linting via hadolint. Reduces build times by restructuring layer ordering and implementing multi-stage build patterns."
verification: "security_reviewed"
source: "https://github.com/moby/moby"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "moby/moby"
  github_stars: 71492
  license: "Apache-2.0"
---

# Docker Build Cache Optimizer

The Docker Build Cache Optimizer analyzes Dockerfiles and build processes to minimize build times and image sizes. It uses hadolint to lint Dockerfiles against best practice rules, checking for issues like installing packages without version pinning, using ADD instead of COPY, and running apt-get update without apt-get install in the same RUN layer.


The agent inspects existing image layers using docker history to identify cache invalidation patterns, detecting cases where frequently changing files (source code) are copied before rarely changing dependencies (package.json, requirements.txt). It analyzes BuildKit cache mount usage via –mount=type=cache directives, recommending cache mount points for package manager caches (pip, npm, apt, maven).


For multi-stage builds, the agent maps the dependency graph between stages using docker buildx bake HCL definitions, identifying opportunities to parallelize independent stages. It integrates with container registries via the Docker Registry HTTP API v2 to analyze remote cache sources for –cache-from optimization, calculates layer sharing efficiency across related images, and benchmarks build times with and without BuildKit parallelism. Output includes a rewritten Dockerfile with optimized layer ordering and estimated time savings.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-build-cache-optimizer/)
