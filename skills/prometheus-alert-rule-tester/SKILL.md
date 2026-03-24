---
name: "Prometheus Alert Rule Tester"
description: "Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/prometheus-alert-rule-tester/"
tool_ecosystem:
  tool: "prometheus"
  github_stars: 63278
  npm_weekly_downloads: 5319832
  github_repo: "prometheus/prometheus"
  license: "Apache-2.0"
  maintained: true
---

# Prometheus Alert Rule Tester

Tests Prometheus alerting rules against historical metrics using promtool and the Prometheus HTTP API query_range endpoint. Validates PromQL expressions, simulates alert firing, and checks routing configurations.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-tester
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-tester -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-tester -a cursor
```

### OpenClaw
```bash
clawhub install prometheus-alert-rule-tester
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill prometheus-alert-rule-tester -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Code |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [prometheus](https://github.com/prometheus/prometheus) — ⭐ 63.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/prometheus-alert-rule-tester/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
