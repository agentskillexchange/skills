---
name: "Kubernetes Pod Crash Analyzer"
description: "Investigates CrashLoopBackOff pods using kubectl logs, describe, and the Kubernetes Events API. Correlates container exit codes with OOMKilled signals, liveness probe failures, and image pull error..."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-2/"
---
# Kubernetes Pod Crash Analyzer

Investigates CrashLoopBackOff pods using kubectl logs, describe, and the Kubernetes Events API. Correlates container exit codes with OOMKilled signals, liveness probe failures, and image pull errors to suggest targeted fixes.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-2
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-2 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-2 -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-pod-crash-analyzer-2
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-2 -a codex
```
## Details

| Property | Value |
|----------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | security_reviewed |
| **Rating** | 0/5 (0 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-2/)
- [Browse All Skills](https://agentskillexchange.com/)
