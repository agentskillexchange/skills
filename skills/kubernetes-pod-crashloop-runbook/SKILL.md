---
name: "Kubernetes Pod Crashloop Runbook"
description: "Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Pod Crashloop Runbook

Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook.

## Overview

This skill queries the Kubernetes API server (typically at /api/v1 and /apis/apps/v1) using a kubeconfig or in-cluster service account token. When a pod enters CrashLoopBackOff, the skill fetches the last 100 lines of container logs via the pods/log subresource, retrieves pod events from the Events API, and checks resource quota limits in the namespace. It distinguishes between OOMKilled (memory limit exceeded), probe failures (liveness/readiness misconfiguration), and missing dependencies (ConfigMap or Secret not found). The skill cross-references the pod spec against the namespace ResourceQuota and LimitRange objects. A step-by-step Markdown runbook is generated with specific kubectl commands to apply, including suggested resource limit adjustments and probe timeout fixes. Compatible with Kubernetes 1.25+.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crashloop-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/
