---
name: "Kubernetes Pod Crash Diagnostics"
description: "Diagnoses CrashLoopBackOff and OOMKilled pods using kubectl and the Kubernetes API /api/v1/pods endpoint. Correlates container logs, resource limits, and node conditions for root cause analysis."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
rating: 4.9
reviews: 43
creator: Maya Johnson
creator_handle: mayaj
creator_verified: false
source: https://agentskillexchange.com/skill/kubernetes-pod-crash-diagnostics/
---

# Kubernetes Pod Crash Diagnostics

Diagnoses CrashLoopBackOff and OOMKilled pods using kubectl and the Kubernetes API /api/v1/pods endpoint. Correlates container logs, resource limits, and node conditions for root cause analysis.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-diagnostics
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | 4.9/5 (43 reviews) |

## Creator

**Maya Johnson**
- Profile: [@mayaj](https://agentskillexchange.com/browse-skills/?creator=mayaj)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-diagnostics/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
