---
name: "Nginx Error Log Classifier"
description: "Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/nginx-error-log-classifier/"
tool_ecosystem:
  tool: "nginx"
  github_stars: 29762
  npm_weekly_downloads: 0
  github_repo: "nginx/nginx"
  license: "BSD-2-Clause"
  maintained: true
---

# Nginx Error Log Classifier

Classifies and prioritizes Nginx error log entries using pattern matching against known error signatures and the GoAccess real-time log analyzer. Maps upstream timeout patterns to specific backend service degradation.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a cursor
```

### OpenClaw
```bash
clawhub install nginx-error-log-classifier
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill nginx-error-log-classifier -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | 📋 Listed |
| **Tool** | [nginx](https://github.com/nginx/nginx) — ⭐ 29.8k · BSD-2-Clause |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-classifier/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
