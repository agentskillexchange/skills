---
name: "Pulumi Drift Detector & Reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/"
tool_ecosystem:
  tool: "pulumi"
  github_stars: 0
  npm_weekly_downloads: 1484747
  github_repo: ""
  license: ""
  maintained: false
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up –target for specific resources.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a cursor
```

### OpenClaw
```bash
clawhub install pulumi-drift-detector-reconciler
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill pulumi-drift-detector-reconciler -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | Codex |
| **Verification** | 📋 Listed |
| **Tool** | pulumi |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
