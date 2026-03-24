---
name: "Prometheus Alert Tuner"
description: "Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-tuner/"
tool_ecosystem:
  tool: "prometheus"
  github_stars: 63278
  npm_weekly_downloads: 5319832
  github_repo: "prometheus/prometheus"
  license: "Apache-2.0"
  maintained: true
---

# Prometheus Alert Tuner

Tunes Prometheus alerting rules using the Prometheus HTTP API and PromQL query analysis. Reduces alert fatigue by analyzing firing history, adjusting thresholds via histogram_quantile, and configuring inhibition rules.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner -a cursor
```

### OpenClaw
```bash
clawhub install prometheus-alert-tuner
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-tuner -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [prometheus](https://github.com/prometheus/prometheus) — ⭐ 63.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-tuner/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
