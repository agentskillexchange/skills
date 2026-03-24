---
name: "Prometheus Alert Resolver"
description: "Resolves Prometheus alerts by querying the /api/v1/alerts and /api/v1/query_range endpoints for metric time series analysis. Executes playbook steps for common alerts like HighCPUUsage and DiskSpaceLow, validates PromQL recording rules, and silences alerts via Alertmanager /api/v2/silences."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: verified_metadata
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/"
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
| **Verification** | verified_metadata |
| **Rating** |  (0/5 from 0 reviews) |

## Creator

**Community**

[View on Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)

---

[Browse more skills](https://agentskillexchange.com) | [Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-resolver-skill/)