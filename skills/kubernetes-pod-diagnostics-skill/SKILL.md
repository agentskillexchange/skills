---
name: "Kubernetes Pod Diagnostics"
description: "Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-skill/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Pod Diagnostics

Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-pod-diagnostics-skill
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-skill -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-skill/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
