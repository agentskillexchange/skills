---
name: "Docker Container Health Inspector"
description: "Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
rating: 4.5
reviews: 79
creator: Tom Anderson
creator_handle: tanderson
creator_verified: false
source: https://agentskillexchange.com/skill/docker-container-health-inspector/
---

# Docker Container Health Inspector

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector -a cursor
```

### OpenClaw

```bash
clawhub install docker-container-health-inspector
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-container-health-inspector -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP-compatible |
| Verification | Security Reviewed |
| Rating | 4.5/5 (79 reviews) |

## Creator

**Tom Anderson**
- Profile: [@tanderson](https://agentskillexchange.com/browse-skills/?creator=tanderson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/docker-container-health-inspector/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
