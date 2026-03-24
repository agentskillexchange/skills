---
name: "Kubernetes Pod Crash Investigator"
description: "Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: listed
rating: 4.0
reviews: 81
creator: "Aisha Patel"
creator_handle: "@aishap"
creator_verified: true
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator/"
---
# Kubernetes Pod Crash Investigator

Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-investigator
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Listed |
| Rating | 4.0/5 (81 reviews) |

## Creator

**Aisha Patel** (Verified Creator ✓)
- Profile: [@aishap](https://agentskillexchange.com/browse-skills/?creator=aishap)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
