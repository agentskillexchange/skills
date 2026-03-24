---
name: "Kubernetes CrashLoopBackOff Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API to inspect container exit codes, OOMKilled events, and readiness probe failures. Generates runbook-style remediation steps."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
rating: 4.5
reviews: 20
creator: "Community"
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-2/"
---
# Kubernetes CrashLoopBackOff Diagnoser

Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API to inspect container exit codes, OOMKilled events, and readiness probe failures. Generates runbook-style remediation steps.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-2
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-2 -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-2 -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-crashloop-diagnoser-2
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-2 -a codex
```
## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | 4.5 ⭐⭐⭐⭐ (20 reviews) |

## Creator

**Community**

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-2/)
- [Browse All Skills](https://agentskillexchange.com/skills/)
