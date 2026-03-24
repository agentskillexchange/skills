---
name: "ArgoCD Application Health Runbook"
description: "Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 4.8
reviews: 13
creator: "Ava Wilson"
creator_handle: "@avawilson"
creator_verified: true
source: "https://agentskillexchange.com/skills/argocd-application-health-runbook/"
---
# ArgoCD Application Health Runbook

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a cursor
```

### OpenClaw

```bash
clawhub install argocd-application-health-runbook
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | 4.8/5 (13 reviews) |

## Creator

**Ava Wilson** (Verified Creator ✓)
- Profile: [@avawilson](https://agentskillexchange.com/browse-skills/?creator=avawilson)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-health-runbook/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
