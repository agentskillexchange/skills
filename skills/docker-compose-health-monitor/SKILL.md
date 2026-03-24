---
name: "Docker Compose Health Monitor"
description: "Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docker-compose-health-monitor/"
tool_ecosystem:
  tool: "docker"
  github_stars: 71560
  npm_weekly_downloads: 0
  github_repo: "moby/moby"
  license: "Apache-2.0"
  maintained: true
---

# Docker Compose Health Monitor

Monitors Docker Compose service health using the Docker Engine API (/containers/{id}/json) and docker-compose ps parsing. Tracks container restart counts via the RestartCount field and logs analysis through the /containers/{id}/logs endpoint.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [docker](https://github.com/moby/moby) — ⭐ 71.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-monitor/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
