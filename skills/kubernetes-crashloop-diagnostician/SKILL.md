---
name: "Kubernetes CrashLoop Diagnostician"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes CrashLoop Diagnostician

Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions.

## Overview

The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go patterns) to gather comprehensive diagnostic data about failing containers, their events, and resource consumption.

The diagnostic process starts by querying the Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container statuses, restart counts, last termination reasons, and exit codes. Common exit codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error), 127 (command not found), and 139 (segfault).

Event analysis uses the Events API to correlate pod events with node-level events, identifying patterns like repeated OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints), and FailedMount (volume issues). The skill also inspects liveness and readiness probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds or overly aggressive failureThreshold settings.

For deeper analysis, the skill leverages kubectl debug to attach ephemeral containers for live inspection, kubectl logs –previous to capture logs from the last crashed instance, and kubectl top pod for real-time resource usage. Remediation suggestions include specific resource limit adjustments, probe timing recommendations, and configuration fixes based on the diagnosed root cause.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostician -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-crashloop-diagnostician
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/
