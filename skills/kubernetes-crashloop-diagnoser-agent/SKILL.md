---
name: "Kubernetes CrashLoop Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
category: "Runbooks & Diagnostics"
framework: "Gemini"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Gemini |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
