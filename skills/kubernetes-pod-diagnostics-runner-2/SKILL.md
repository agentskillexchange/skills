---
name: "Kubernetes Pod Diagnostics Runner"
description: "Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Pod Diagnostics Runner

Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runner-2
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runner-2 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runner-2 -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-pod-diagnostics-runner-2
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runner-2 -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
