---
name: "Kubernetes Pod Diagnostic Runbook"
description: "Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Pod Diagnostic Runbook

Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states.

## Overview

This skill provides an automated diagnostic runbook for Kubernetes pod issues, executing systematic troubleshooting steps through kubectl and the Kubernetes API. When triggered, it identifies the pod state and runs targeted diagnostic sequences: for CrashLoopBackOff it pulls container logs, previous container logs, and checks resource limits; for ImagePullBackOff it verifies image existence via the container registry API and checks imagePullSecrets; for OOMKilled it analyzes memory usage patterns from metrics-server and suggests limit adjustments. The runbook queries the Kubernetes Events API for related warnings, checks node conditions via kubectl describe node, and examines resource quotas and limit ranges in the namespace. It integrates with crictl for container runtime-level diagnostics when kubectl logs are insufficient. The skill generates structured diagnostic reports with root cause analysis and recommended remediation steps, and can automatically apply fixes like restarting deployments or scaling resource limits.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-runbook -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-diagnostic-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/
