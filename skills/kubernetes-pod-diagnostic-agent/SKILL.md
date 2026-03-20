---
name: "Kubernetes Pod Diagnostic Agent"
description: "Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
rating: 4.9
reviews: 15
creator: Sofia Petrov
creator_handle: sofiapetrov
creator_verified: true
source: https://agentskillexchange.com/skill/kubernetes-pod-diagnostic-agent/
---

# Kubernetes Pod Diagnostic Agent

Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-pod-diagnostic-agent
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | 4.9/5 (15 reviews) |

## Creator

**Sofia Petrov** (Verified Creator ✓)
- Profile: [@sofiapetrov](https://agentskillexchange.com/browse-skills/?creator=sofiapetrov)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-diagnostic-agent/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
