---
name: Kubernetes Runbook Executor
description: Executes structured Kubernetes diagnostic runbooks using kubectl and the Kubernetes Python client (kubernetes-client/python). Performs pod health checks via /healthz endpoints, analyzes CrashLoopBackOff events, and generates incident timelines from the Events API.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.2
reviews: 74
source: https://agentskillexchange.com/skill/kubernetes-runbook-executor-4/
---

# Kubernetes Runbook Executor

Executes structured Kubernetes diagnostic runbooks using kubectl and the Kubernetes Python client (kubernetes-client/python). Performs pod health checks via /healthz endpoints, analyzes CrashLoopBackOff events, and generates incident timelines from the Events API.

## Overview

Executes structured Kubernetes diagnostic runbooks using kubectl and the Kubernetes Python client (kubernetes-client/python). Performs pod health checks via /healthz endpoints, analyzes CrashLoopBackOff events, and generates incident timelines from the Events API.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-4
```

### OpenClaw

```bash
clawhub install kubernetes-runbook-executor-4
```

### Claude Code

```bash
claude mcp add kubernetes-runbook-executor-4
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-runbook-executor-4/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.2/5 (74 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-runbook-executor-4/)
