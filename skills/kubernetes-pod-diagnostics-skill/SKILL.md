---
name: "Kubernetes Pod Diagnostics"
description: "Diagnoses Kubernetes pod failures using kubectl describe, logs –previous, and the Kubernetes API /api/v1/namespaces/{ns}/events endpoints. Identifies CrashLoopBackOff root causes, OOMKilled memory analysis, and generates remediation steps with resource limit recommendations."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-skill/"
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
| **Verification** | security_reviewed |
| **Rating** |  (0/5 from 0 reviews) |

## Creator

**Community**

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-diagnostics-skill/)

---

[Browse more skills](https://agentskillexchange.com) | [Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-diagnostics-skill/)