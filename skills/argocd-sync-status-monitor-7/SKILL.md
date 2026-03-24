---
name: "ArgoCD Sync Status Monitor"
description: "Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/"
tool_ecosystem:
  tool: "argocd"
  github_stars: 22391
  npm_weekly_downloads: 0
  github_repo: "argoproj/argo-cd"
  license: "Apache-2.0"
  maintained: true
---

# ArgoCD Sync Status Monitor

Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor-7
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor-7 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor-7 -a cursor
```

### OpenClaw
```bash
clawhub install argocd-sync-status-monitor-7
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor-7 -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [argocd](https://github.com/argoproj/argo-cd) — ⭐ 22.4k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
