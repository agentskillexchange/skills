---
name: "Prometheus Alert Resolver"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
tool_ecosystem:
  tool: "prometheus"
  github_stars: 63278
  npm_weekly_downloads: 5319832
  github_repo: "prometheus/prometheus"
  license: "Apache-2.0"
  maintained: true
---

# Prometheus Alert Resolver

Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-resolver-skill
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-resolver-skill -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-resolver-skill -a cursor
```

### OpenClaw
```bash
clawhub install prometheus-alert-resolver-skill
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-resolver-skill -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [prometheus](https://github.com/prometheus/prometheus) — ⭐ 63.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
