---
name: "Kubernetes CrashLoopBackOff Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes CrashLoopBackOff Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Codex |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
