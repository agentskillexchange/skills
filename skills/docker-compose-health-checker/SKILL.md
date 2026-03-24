---
name: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
category: "Runbooks & Diagnostics"
framework: "MCP"
verification: security_reviewed
rating: 4.4
reviews: 81
creator: "Alex Thompson"
creator_handle: "@alexthompson"
creator_verified: true
source: "https://agentskillexchange.com/skills/docker-compose-health-checker/"
---
# Docker Compose Health Checker

Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker -a cursor
```

### OpenClaw

```bash
clawhub install docker-compose-health-checker
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill docker-compose-health-checker -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP-compatible |
| Verification | Security Reviewed |
| Rating | 4.4/5 (81 reviews) |

## Creator

**Alex Thompson** (Verified Creator ✓)
- Profile: [@alexthompson](https://agentskillexchange.com/browse-skills/?creator=alexthompson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
