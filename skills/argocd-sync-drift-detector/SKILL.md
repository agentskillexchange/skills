---
name: "ArgoCD Sync Drift Detector"
description: "Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/argocd-sync-drift-detector/"
tool_ecosystem:
  tool: "argocd"
  github_stars: 22391
  npm_weekly_downloads: 0
  github_repo: "argoproj/argo-cd"
  license: "Apache-2.0"
  maintained: true
---

# ArgoCD Sync Drift Detector

Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-drift-detector
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-drift-detector -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-drift-detector -a cursor
```

### OpenClaw
```bash
clawhub install argocd-sync-drift-detector
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill argocd-sync-drift-detector -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [argocd](https://github.com/argoproj/argo-cd) — ⭐ 22.4k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
