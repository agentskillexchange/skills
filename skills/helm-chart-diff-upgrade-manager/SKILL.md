---
name: "Helm Chart Diff & Upgrade Manager"
description: "Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/"
tool_ecosystem:
  tool: "helm"
  github_stars: 29603
  npm_weekly_downloads: 0
  github_repo: "helm/helm"
  license: "Apache-2.0"
  maintained: true
---

# Helm Chart Diff & Upgrade Manager

Uses helm-diff to compute a human-readable diff between deployed and candidate chart versions before upgrade. Automatically bumps image tags by querying the OCI registry, then executes helm upgrade –atomic with configurable rollback timeouts. Sends upgrade status to PagerDuty or Datadog.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a cursor
```

### OpenClaw
```bash
clawhub install helm-chart-diff-upgrade-manager
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill helm-chart-diff-upgrade-manager -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | MCP-compatible |
| **Verification** | 📋 Listed |
| **Tool** | [helm](https://github.com/helm/helm) — ⭐ 29.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/helm-chart-diff-upgrade-manager/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
