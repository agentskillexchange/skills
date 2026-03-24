---
name: "Nginx Error Log Analyzer"
description: "Parses and diagnoses Nginx error logs and access logs using pattern matching against known error signatures. Integrates with the Nginx Plus REST API /api/8/ endpoints for real-time upstream health, connection metrics, and SSL certificate expiration monitoring."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-analyzer/"
tool_ecosystem:
  tool: "nginx"
  github_stars: 29762
  npm_weekly_downloads: 0
  github_repo: "nginx/nginx"
  license: "BSD-2-Clause"
  maintained: true
---

# Nginx Error Log Analyzer

Parses and diagnoses Nginx error logs and access logs using pattern matching against known error signatures. Integrates with the Nginx Plus REST API /api/8/ endpoints for real-time upstream health, connection metrics, and SSL certificate expiration monitoring.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer -a cursor
```

### OpenClaw
```bash
clawhub install nginx-error-log-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-analyzer -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [nginx](https://github.com/nginx/nginx) — ⭐ 29.8k · BSD-2-Clause |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
