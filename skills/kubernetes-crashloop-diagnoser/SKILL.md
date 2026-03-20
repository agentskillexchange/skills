---
name: "Kubernetes CrashLoopBackOff Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes API (client-go or @kubernetes/client-node) to inspect pod events, container exit codes, and OOMKilled signals for root cause analysis."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: "Security Reviewed ✓"
rating: "4.9"
reviews: "80"
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/kubernetes-crashloop-diagnoser/"
---

# Kubernetes CrashLoopBackOff Diagnoser

Diagnoses CrashLoopBackOff pods using the Kubernetes API (client-go or @kubernetes/client-node) to inspect pod events, container exit codes, and OOMKilled signals for root cause analysis.

## Installation

**Any Agent (npx):**
```bash
npx @anthropic/skills install kubernetes-crashloop-diagnoser
```

**Claude Code:**
```bash
claude mcp add kubernetes-crashloop-diagnoser
```

**Cursor:**
Add to `.cursor/skills.json`:
```json
{
  "kubernetes-crashloop-diagnoser": "latest"
}
```

**OpenClaw:**
```bash
clawhub install kubernetes-crashloop-diagnoser
```

**Codex:**
```bash
codex install kubernetes-crashloop-diagnoser
```

## Details

| Field | Value |
|-------|-------|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Codex |
| **Verification** | Security Reviewed ✓ |
| **Rating** | ⭐ 4.9/5 (80 reviews) |

## Creator

**Community**


---

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-crashloop-diagnoser/) • [Browse All Skills](https://agentskillexchange.com/)