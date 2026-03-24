---
name: "Kubernetes Pod Crash Diagnostician"
description: "Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Pod Crash Diagnostician

Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-pod-crash-diagnostician
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Code |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
