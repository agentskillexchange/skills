---
name: "Kubernetes Diagnostics Agent"
description: "Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: "Verified"
rating: 4.6
reviews: 35
creator: "Leo Park"
creator_handle: "@leopark_ai"
creator_verified: true
source: "https://agentskillexchange.com/skill/kubernetes-diagnostics-agent/"
---

# Kubernetes Diagnostics Agent

Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics.

## Installation

Install this skill in your preferred agent:

### Any Agent (npx)
```bash
npx @anthropic/skills install kubernetes-diagnostics-agent
```

### Claude Code
```bash
claude skills add kubernetes-diagnostics-agent
```

### Cursor
Add to your `.cursor/skills.json`:
```json
{
  "skills": ["kubernetes-diagnostics-agent"]
}
```

### OpenClaw
```bash
clawhub install kubernetes-diagnostics-agent
```

### Codex
```bash
codex skills add kubernetes-diagnostics-agent
```

## Details

| Property | Value |
|----------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Claude Code |
| **Verification** | Verified |
| **Rating** | ⭐⭐⭐⭐ 4.6/5 (35 reviews) |

## Creator

**Leo Park** (@leopark_ai)
✓ Verified Creator

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-diagnostics-agent/) | [Browse All Skills](https://agentskillexchange.com)
