---
name: "Kubernetes Runbook Generator"
description: "Auto-generates operational runbooks from Kubernetes cluster state using kubectl and the Kubernetes API. Produces step-by-step troubleshooting guides for common pod failure modes."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: "security_reviewed"
rating: "0"
reviews: "0"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/kubernetes-runbook-generator/"
---

# Kubernetes Runbook Generator

Auto-generates operational runbooks from Kubernetes cluster state using kubectl and the Kubernetes API. Produces step-by-step troubleshooting guides for common pod failure modes.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agentskill install kubernetes-runbook-generator
```

### Claude Code
```bash
claude mcp add kubernetes-runbook-generator
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "kubernetes-runbook-generator": {
    "source": "agentskillexchange",
    "enabled": true
  }
}
```

### OpenClaw
```bash
clawhub install kubernetes-runbook-generator
```

### Codex
```bash
codex install kubernetes-runbook-generator
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | security_reviewed |
| **Rating** | 0 ⭐ (0 reviews) |

## Creator

**Community** 



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-runbook-generator/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
