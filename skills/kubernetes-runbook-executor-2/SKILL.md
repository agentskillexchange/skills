---
name: Kubernetes Runbook Executor
description: Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.7
reviews: 78
source: https://agentskillexchange.com/skill/kubernetes-runbook-executor-2/
---

# Kubernetes Runbook Executor

Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.

## Overview

Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-2
```

### OpenClaw

```bash
clawhub install kubernetes-runbook-executor-2
```

### Claude Code

```bash
claude mcp add kubernetes-runbook-executor-2
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-runbook-executor-2/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.7/5 (78 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-runbook-executor-2/)
