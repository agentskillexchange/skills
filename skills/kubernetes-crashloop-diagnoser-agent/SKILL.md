---
name: "Kubernetes CrashLoop Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 4.8
reviews: 49
creator: "Lucy Zhang"
creator_handle: "@lucyzhang"
creator_verified: true
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/"
---

# Kubernetes CrashLoop Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-agent
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-agent -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-agent -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-crashloop-diagnoser-agent
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnoser-agent -a codex
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | Security Reviewed |
| **Rating** | ⭐ 4.8 (49 reviews) |

## Creator

**Lucy Zhang** ✓

- Handle: `@lucyzhang`
- Profile: [View on ASE](https://agentskillexchange.com/creator/lucyzhang/)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
- [Browse All Skills](https://agentskillexchange.com/)
