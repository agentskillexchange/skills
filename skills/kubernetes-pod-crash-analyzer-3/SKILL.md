---
name: "Kubernetes Pod Crash Analyzer"
description: "Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root ca..."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: "security_reviewed"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/kubernetes-pod-crash-analyzer-3/"
---

# Kubernetes Pod Crash Analyzer

Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/skills install kubernetes-pod-crash-analyzer-3
```

### Claude Code
```bash
claude mcp add kubernetes-pod-crash-analyzer-3
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "kubernetes-pod-crash-analyzer-3": {
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install kubernetes-pod-crash-analyzer-3
```

### Codex
```bash
codex install kubernetes-pod-crash-analyzer-3
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | security_reviewed |
| **Rating** | 0 (0 reviews) |

## Creator

**Community**


## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-analyzer-3/)
- [Browse All Skills](https://agentskillexchange.com/)
