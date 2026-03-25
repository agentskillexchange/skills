---
name: "Kubernetes Incident Runbook"
description: "Executes structured incident response procedures for Kubernetes clusters using kubectl, kube-state-metrics, and the Kubernetes Events API. Automates pod crash diagnosis, OOMKill analysis, and node pressure triage."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-incident-runbook/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Incident Runbook

Executes structured incident response procedures for Kubernetes clusters using kubectl, kube-state-metrics, and the Kubernetes Events API. Automates pod crash diagnosis, OOMKill analysis, and node pressure triage.

## Overview

The Kubernetes Incident Runbook skill provides automated incident response procedures for Kubernetes cluster issues. It uses kubectl commands, the Kubernetes API, and kube-state-metrics to systematically diagnose common failure modes including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and node NotReady conditions.

When triggered, the skill follows a structured diagnostic tree. For pod failures, it inspects container exit codes, retrieves previous container logs via kubectl logs –previous, checks resource requests/limits against actual usage from metrics-server, and examines events for scheduling or volume mount failures.

For node-level issues, it analyzes node conditions (MemoryPressure, DiskPressure, PIDPressure), checks kubelet logs, inspects systemd service status, and correlates with cloud provider instance health. The skill understands taints, tolerations, and affinity rules that may cause scheduling failures.

Advanced capabilities include tracing network connectivity issues using CoreDNS logs and NetworkPolicy analysis, diagnosing PersistentVolumeClaim binding failures across storage classes, and identifying resource quota exhaustion across namespaces. All findings are compiled into structured incident reports with remediation steps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-incident-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-incident-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-incident-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-incident-runbook -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-incident-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-incident-runbook/
