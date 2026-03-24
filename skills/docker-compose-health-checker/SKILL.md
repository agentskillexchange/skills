---
name: "Docker Compose Health Checker"
description: "Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docker-compose-health-checker/"
tool_ecosystem:
  tool: "docker"
  github_stars: 71560
  npm_weekly_downloads: 0
  github_repo: "moby/moby"
  license: "Apache-2.0"
  maintained: true
---

# Docker Compose Health Checker

Validates docker-compose.yml files against the Compose Specification, checks image vulnerability status via Docker Scout API, and verifies healthcheck configurations.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [docker](https://github.com/moby/moby) — ⭐ 71.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/docker-compose-health-checker/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
