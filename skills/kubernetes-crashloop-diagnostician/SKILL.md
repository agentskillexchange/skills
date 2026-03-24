---
name: "Kubernetes CrashLoop Diagnostician"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes CrashLoop Diagnostician

Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-crashloop-diagnostician
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | OpenClaw |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
