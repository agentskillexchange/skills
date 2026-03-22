---
name: "Kubernetes Pod Crashloop Runbook"
description: "Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.8
reviews: 61
creator: Priya Sharma
creator_handle: priyasharma
creator_verified: true
source: https://agentskillexchange.com/skill/kubernetes-pod-crashloop-runbook/
---

# Kubernetes Pod Crashloop Runbook

Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crashloop-runbook
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | 4.8/5 (61 reviews) |

## Creator

**Priya Sharma** (Verified Creator ✓)
- Profile: [@priyasharma](https://agentskillexchange.com/browse-skills/?creator=priyasharma)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crashloop-runbook/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
