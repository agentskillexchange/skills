---
name: "Docker Container Health Inspector"
description: "Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming."
category: "Runbooks & Diagnostics"
framework: "MCP-compatible"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/docker-container-health-inspector/"
tool_ecosystem:
  tool: "docker"
  github_stars: 71560
  npm_weekly_downloads: 0
  github_repo: "moby/moby"
  license: "Apache-2.0"
  maintained: true
---

# Docker Container Health Inspector

Inspects Docker container health using the Docker Engine API v1.45 /containers/{id}/json and /containers/{id}/stats endpoints. Diagnoses OOM kills, restart loops, and network connectivity issues with automated log analysis via /containers/{id}/logs streaming.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | MCP-compatible |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [docker](https://github.com/moby/moby) — ⭐ 71.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/docker-container-health-inspector/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
