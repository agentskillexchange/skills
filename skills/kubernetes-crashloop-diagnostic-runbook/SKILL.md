---
name: "Kubernetes Crashloop Diagnostic Runbook"
description: "Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
rating: 4.5
reviews: 59
creator: "Liam OBrien"
creator_handle: "@liamobrien"
creator_verified: true
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/"
---
# Kubernetes Crashloop Diagnostic Runbook

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostic-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostic-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostic-runbook -a cursor
```

### OpenClaw

```bash
clawhub install kubernetes-crashloop-diagnostic-runbook
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostic-runbook -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | 4.5/5 (59 reviews) |

## Creator

**Liam OBrien** (Verified Creator ✓)
- Profile: [@liamobrien](https://agentskillexchange.com/browse-skills/?creator=liamobrien)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
