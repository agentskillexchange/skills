---
name: "Kubernetes Rollback Runbook"
description: "Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Rollback Runbook

Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3 -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-rollback-runbook-3
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3 -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
