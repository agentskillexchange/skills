---
name: "Kubernetes CrashLoopBackOff Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
rating: 4.8
reviews: 85
creator: David Kim
creator_handle: dkim
creator_verified: false
source: https://agentskillexchange.com/skill/k8s-crashloopbackoff-diagnoser/
---

# Kubernetes CrashLoopBackOff Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser -a cursor
```

### OpenClaw

```bash
clawhub install k8s-crashloopbackoff-diagnoser
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | 4.8/5 (85 reviews) |

## Creator

**David Kim**
- Profile: [@dkim](https://agentskillexchange.com/browse-skills/?creator=dkim)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/k8s-crashloopbackoff-diagnoser/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
