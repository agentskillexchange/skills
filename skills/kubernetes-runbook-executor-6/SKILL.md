---
name: Kubernetes Runbook Executor
description: Executes predefined Kubernetes diagnostic runbooks using kubectl commands and the Kubernetes API. Automates pod restart analysis via kubectl get events, resource quota checks, and node condition troub
category: Runbooks & Diagnostics
framework: MCP
verification: verified_metadata
rating: 4.8
reviews: 50
source: https://agentskillexchange.com/skill/kubernetes-runbook-executor-6/
---

# Kubernetes Runbook Executor

Executes predefined Kubernetes diagnostic runbooks using kubectl commands and the Kubernetes API. Automates pod restart analysis via kubectl get events, resource quota checks, and node condition troubleshooting.

## Overview

Kubernetes Runbook Executor automates the execution of operational runbooks for diagnosing and resolving common Kubernetes cluster issues.
How It Works
The skill maintains a library of structured runbooks that map symptoms (CrashLoopBackOff, OOMKilled, ImagePullBackOff) to diagnostic kubectl command sequences. It executes these commands, interprets outputs, and suggests remediation steps.
Key Features

Pre-built runbooks for top 20 Kubernetes failure modes including pod eviction, node pressure, and network policy issues
Automated event analysis using kubectl get events –field-selector with correlation to pod lifecycle
Resource quota and LimitRange validation across namespaces
Node condition troubleshooting for DiskPressure, MemoryPressure, and PIDPressure

Automation
Runbooks are defined in YAML format with conditional branching based on diagnostic outputs. Supports dry-run mode for remediation commands. Integrates with PagerDuty and Opsgenie for incident-linked execution.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-6
```

### OpenClaw

```bash
openclaw install kubernetes-runbook-executor-6
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | MCP |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (50 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-runbook-executor-6/)*
