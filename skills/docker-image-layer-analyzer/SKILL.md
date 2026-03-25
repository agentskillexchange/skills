---
name: "Docker Image Layer Analyzer"
description: "Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Calculates layer sizes, identifies wasted space, and suggests multi-stage build optimizations."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docker-image-layer-analyzer/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Docker Image Layer Analyzer

Analyzes Docker image layers using the Docker Registry HTTP API v2 and dive CLI tool. Calculates layer sizes, identifies wasted space, and suggests multi-stage build optimizations.

## Overview

The Docker Image Layer Analyzer skill provides deep inspection of container image structure for optimization and security review. Using the Docker Registry HTTP API v2, it retrieves image manifests and layer digests from any OCI-compliant registry. The dive CLI tool is leveraged for detailed layer-by-layer filesystem analysis, identifying files added, modified, or removed at each build step. Layer size calculations pinpoint the largest contributors to image bloat, flagging unnecessary build artifacts, cached package manager files, and development dependencies. Wasted space analysis detects files that are added in one layer and removed in a subsequent layer, still consuming space in the final image. The skill suggests multi-stage build patterns to separate build-time dependencies from runtime images. Dockerfile best practice analysis covers instruction ordering for cache optimization, USER directive security, and HEALTHCHECK configuration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-image-layer-analyzer -a codex
```

### OpenClaw

```bash
clawhub install docker-image-layer-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/docker-image-layer-analyzer/
