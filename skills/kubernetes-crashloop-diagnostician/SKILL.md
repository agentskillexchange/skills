---
title: "Kubernetes CrashLoop Diagnostician"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnostician

The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go patterns) to gather comprehensive diagnostic data about failing containers, their events, and resource consumption. The diagnostic process starts by querying the Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container statuses, restart counts, last termination reasons, and exit codes. Common exit codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error), 127 (command not found), and 139 (segfault). Event analysis uses the Events API to correlate pod events with node-level events, identifying patterns like repeated OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints), and FailedMount (volume issues). The skill also inspects liveness and readiness probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds or overly aggressive failureThreshold settings. For deeper analysis, the skill leverages kubectl debug to attach ephemeral containers for live inspection, kubectl logs –previous to capture logs from the last crashed instance, and kubectl top pod for real-time resource usage. Remediation suggestions include specific resource limit adjustments, probe timing recommendations, and configuration fixes based on the diagnosed root cause.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-crashloop-diagnostician
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-crashloop-diagnostician`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/)
