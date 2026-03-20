---
name: "Kubernetes Pod Crash Analyzer"
description: "Diagnoses CrashLoopBackOff and OOMKilled pods using the Kubernetes API and kubectl. Correlates container exit codes, resource limits, and event streams to pinpoint root causes."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed
rating: 4.3
reviews: 16
creator: Chris Lee
creator_handle: chrislee
creator_verified: false
source: https://agentskillexchange.com/skill/kubernetes-pod-crash-analyzer/
---

# Kubernetes Pod Crash Analyzer

Diagnoses CrashLoopBackOff and OOMKilled pods using the Kubernetes API and kubectl. Correlates container exit codes, resource limits, and event streams to pinpoint root causes.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-analyzer
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Code |
| Verification | Security Reviewed |
| Rating | 4.3/5 (16 reviews) |

## Creator

**Chris Lee**
- Profile: [@chrislee](https://agentskillexchange.com/browse-skills/?creator=chrislee)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-analyzer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
