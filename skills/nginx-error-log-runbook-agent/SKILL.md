---
name: "Nginx Error Log Runbook Agent"
description: "Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/"
tool_ecosystem:
  tool: "nginx"
  github_stars: 29762
  npm_weekly_downloads: 0
  github_repo: "nginx/nginx"
  license: "BSD-2-Clause"
  maintained: true
---

# Nginx Error Log Runbook Agent

Automates Nginx error diagnosis using nginx -T configuration dump, error.log pattern matching, and the Nginx Plus REST API /api/8/http/upstreams endpoint. Resolves 502 Bad Gateway, SSL handshake failures, and upstream timeout issues.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent -a cursor
```

### OpenClaw
```bash
clawhub install nginx-error-log-runbook-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-runbook-agent -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [nginx](https://github.com/nginx/nginx) — ⭐ 29.8k · BSD-2-Clause |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-runbook-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
