---
name: "Kubernetes Pod Crash Loop Analyzer"
description: "Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: "✅ Verified"
rating: "4.1"
reviews: "86"
creator: "Fatima Al-Hassan"
creator_handle: "@fatimaalhassan"
creator_verified: "true"
source: "https://agentskillexchange.com/skill/kubernetes-pod-crash-loop-analyzer/"
---

# Kubernetes Pod Crash Loop Analyzer

Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills install kubernetes-pod-crash-loop-analyzer
```

### Claude Code
```bash
claude mcp add kubernetes-pod-crash-loop-analyzer
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["kubernetes-pod-crash-loop-analyzer"]
}
```

### OpenClaw
```bash
clawhub install kubernetes-pod-crash-loop-analyzer
```

### Codex
```bash
codex install kubernetes-pod-crash-loop-analyzer
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | ✅ Verified 🔒 Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.1/5 (86 reviews) |

## Creator

**Fatima Al-Hassan** ✅
Handle: `@fatimaalhassan`
[View Profile on ASE](https://agentskillexchange.com/skill/kubernetes-pod-crash-loop-analyzer/)

---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-loop-analyzer/) · [Browse All Skills](https://agentskillexchange.com/skills/)