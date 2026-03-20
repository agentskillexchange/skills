---
name: Docker Container Health Inspector
description: Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.5
reviews: 79
source: https://agentskillexchange.com/skill/docker-container-health-inspector/
---

# Docker Container Health Inspector

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

## Overview

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector
```

### OpenClaw

```bash
clawhub install docker-container-health-inspector
```

### Claude Code

```bash
claude mcp add docker-container-health-inspector
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/docker-container-health-inspector/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.5/5 (79 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/docker-container-health-inspector/)
