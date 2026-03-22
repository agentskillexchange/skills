---
name: "Kubernetes Runbook Executor"
description: "Executes diagnostic runbooks using kubectl commands and the Kubernetes API /api/v1/namespaces/{ns}/pods to triage cluster incidents. Collects pod logs, describes failing deployments, and checks resource quotas via /apis/policy/v1."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: "security_reviewed"
rating: 4.8
reviews: 46
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/kubernetes-runbook-executor-9/"
---

# Kubernetes Runbook Executor

Executes diagnostic runbooks using kubectl commands and the Kubernetes API /api/v1/namespaces/{ns}/pods to triage cluster incidents. Collects pod logs, describes failing deployments, and checks resource quotas via /apis/policy/v1.

## Installation

Install this skill across different agents:

### Any AI Agent (npx)
```bash
npx @anthropic/skills install kubernetes-runbook-executor-9
```

### Claude Code
```bash
claude skills install kubernetes-runbook-executor-9
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["kubernetes-runbook-executor-9"]
}
```

### OpenClaw
```bash
clawhub install kubernetes-runbook-executor-9
```

### Codex
```bash
codex skills install kubernetes-runbook-executor-9
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Cursor |
| **Verification** | 🔒 Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.8/5 (46 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-runbook-executor-9/)
- [Browse All Skills](https://agentskillexchange.com/)
