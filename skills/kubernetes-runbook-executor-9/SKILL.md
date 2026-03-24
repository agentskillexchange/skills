---
name: "Kubernetes Runbook Executor"
description: "Executes diagnostic runbooks using kubectl commands and the Kubernetes API /api/v1/namespaces/{ns}/pods to triage cluster incidents. Collects pod logs, describes failing deployments, and checks resource quotas via /apis/policy/v1."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
rating: 4.8
reviews: 46
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-runbook-executor-9/"
---
# Kubernetes Runbook Executor

Executes diagnostic runbooks using kubectl commands and the Kubernetes API /api/v1/namespaces/{ns}/pods to triage cluster incidents. Collects pod logs, describes failing deployments, and checks resource quotas via /apis/policy/v1.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-9
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-9 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-9 -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-runbook-executor-9
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-9 -a codex
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

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-executor-9/)
- [Browse All Skills](https://agentskillexchange.com/)
