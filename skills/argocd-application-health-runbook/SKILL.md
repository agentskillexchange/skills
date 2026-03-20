---
name: ArgoCD Application Health Runbook
description: Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.8
reviews: 13
source: https://agentskillexchange.com/skill/argocd-application-health-runbook/
---

# ArgoCD Application Health Runbook

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Overview

Diagnoses ArgoCD application sync failures and degraded states using the ArgoCD REST API and argocd CLI. Queries /api/v1/applications/{name} for sync status, resource health, and operation state. Provides automated remediation steps for OutOfSync, Degraded, and Missing resource conditions.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill argocd-application-health-runbook
```

### OpenClaw

```bash
clawhub install argocd-application-health-runbook
```

### Claude Code

```bash
claude mcp add argocd-application-health-runbook
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/argocd-application-health-runbook/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.8/5 (13 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/argocd-application-health-runbook/)
