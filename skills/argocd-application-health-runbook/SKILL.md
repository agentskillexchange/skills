---
name: "ArgoCD Application Health Runbook"
description: "Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-application-health-runbook/"
tool_ecosystem:
  tool: "argocd"
  github_stars: 22391
  npm_weekly_downloads: 0
  github_repo: "argoproj/argo-cd"
  license: "Apache-2.0"
  maintained: true
---

# ArgoCD Application Health Runbook

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a cursor
```

### OpenClaw
```bash
clawhub install argocd-application-health-runbook
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [argocd](https://github.com/argoproj/argo-cd) — ⭐ 22.4k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
