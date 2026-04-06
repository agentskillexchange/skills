---
name: "Docker Build Cache Optimizer"
description: "Optimizes Docker build performance using BuildKit cache mount analysis, docker history layer inspection, and Dockerfile linting via hadolint. Reduces build times by restructuring layer ordering and implementing multi-stage build patterns."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/docker-build-cache-optimizer/"
---
# Docker Build Cache Optimizer

Optimizes Docker build performance using BuildKit cache mount analysis, docker history layer inspection, and Dockerfile linting via hadolint. Reduces build times by restructuring layer ordering and implementing multi-stage build patterns.

The Docker Build Cache Optimizer analyzes Dockerfiles and build processes to minimize build times and image sizes. It uses hadolint to lint Dockerfiles against best practice rules, checking for issues like installing packages without version pinning, using ADD instead of COPY, and running apt-get update without apt-get install in the same RUN layer.



The agent inspects existing image layers using docker history to identify cache invalidation patterns, detecting cases where frequently changing files (source code) are copied before rarely changing dependencies (package.json, requirements.txt). It analyzes BuildKit cache mount usage via –mount=type=cache directives, recommending cache mount points for package manager caches (pip, npm, apt, maven).



For multi-stage builds, the agent maps the dependency graph between stages using docker buildx bake HCL definitions, identifying opportunities to parallelize independent stages. It integrates with container registries via the Docker Registry HTTP API v2 to analyze remote cache sources for –cache-from optimization, calculates layer sharing efficiency across related images, and benchmarks build times with and without BuildKit parallelism. Output includes a rewritten Dockerfile with optimized layer ordering and estimated time savings.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-build-cache-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-build-cache-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-build-cache-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-build-cache-optimizer -a codex
```

### OpenClaw

```bash
clawhub install docker-build-cache-optimizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/docker-build-cache-optimizer/)
