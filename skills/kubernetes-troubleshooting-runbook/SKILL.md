---
name: "Kubernetes Troubleshooting Runbook"
description: "Use this skill to systematically diagnose and resolve Kubernetes issues including pod failures, CrashLoopBackOff errors, OOMKills, and resource constraints. It guides agents through kubectl commands and diagnostic steps to identify root causes. Trigger when Kubernetes workloads are failing, pods are restarting, or cluster resources are being exhausted."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-troubleshooting-runbook/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121313
  npm_weekly_downloads: 0
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Troubleshooting Runbook

Use this skill to systematically diagnose and resolve Kubernetes issues including pod failures, CrashLoopBackOff errors, OOMKills, and resource constraints. It guides agents through kubectl commands and diagnostic steps to identify root causes. Trigger when Kubernetes workloads are failing, pods are restarting, or cluster resources are being exhausted.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook -a cursor
```

### OpenClaw
```bash
clawhub install kubernetes-troubleshooting-runbook
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill kubernetes-troubleshooting-runbook -a codex
```

## Details

| | |
|---|---|
| **Category** | Monitoring & Alerts |
| **Framework** | Custom Agents |
| **Verification** | 📋 Listed |
| **Tool** | [kubernetes](https://github.com/kubernetes/kubernetes) — ⭐ 121.3k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-troubleshooting-runbook/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
