---
name: "ArgoCD Sync Status Monitor"
description: "Polls ArgoCD application sync status via its REST API, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git and outputs a diff-style summary for GitOps teams."
category: "CI/CD Integrations"
framework: "OpenClaw"
verification: listed
rating: 4.6
reviews: 57
creator: "Sarah Chen"
creator_handle: "@sarahchen"
creator_verified: true
source: "https://agentskillexchange.com/skills/argocd-sync-status-monitor/"
---
# ArgoCD Sync Status Monitor

Polls ArgoCD application sync status via its REST API, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git and outputs a diff-style summary for GitOps teams.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor -a cursor
```

### OpenClaw

```bash
clawhub install argocd-sync-status-monitor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | OpenClaw |
| Verification | Listed |
| Rating | 4.6/5 (57 reviews) |

## Creator

**Sarah Chen** (Verified Creator ✓)
- Profile: [@sarahchen](https://agentskillexchange.com/browse-skills/?creator=sarahchen)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-status-monitor/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
