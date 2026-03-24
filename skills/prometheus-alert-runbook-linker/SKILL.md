---
name: "Prometheus Alert Runbook Linker"
description: "Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/"
tool_ecosystem:
  tool: "prometheus"
  github_stars: 63278
  npm_weekly_downloads: 5319832
  github_repo: "prometheus/prometheus"
  license: "Apache-2.0"
  maintained: true
---

# Prometheus Alert Runbook Linker

Links Prometheus alerting rules to operational runbooks by parsing AlertManager configurations and PrometheusRule CRDs. Validates runbook_url annotations exist and are reachable, and generates stub runbooks for undocumented alerts.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a cursor
```

### OpenClaw
```bash
clawhub install prometheus-alert-runbook-linker
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-runbook-linker -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 📋 Listed |
| **Tool** | [prometheus](https://github.com/prometheus/prometheus) — ⭐ 63.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-runbook-linker/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
