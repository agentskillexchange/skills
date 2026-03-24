---
name: "Docker Compose Health Monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
rating: 4.3
reviews: 48
creator: "Priya Sharma"
creator_handle: "@priyasharma"
creator_verified: true
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
---
# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor -a cursor
```

### OpenClaw

```bash
clawhub install docker-compose-health-monitor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-monitor -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP-compatible |
| Verification | Security Reviewed |
| Rating | 4.3/5 (48 reviews) |

## Creator

**Priya Sharma** (Verified Creator ✓)
- Profile: [@priyasharma](https://agentskillexchange.com/browse-skills/?creator=priyasharma)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
