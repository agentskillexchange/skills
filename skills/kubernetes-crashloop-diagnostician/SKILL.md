---
title: "Kubernetes CrashLoop Diagnostician"
description: "Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions."
slug: "kubernetes-crashloop-diagnostician"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/"
---

# Kubernetes CrashLoop Diagnostician

Diagnoses CrashLoopBackOff pods using the Kubernetes client-go API and kubectl debug. Analyzes container exit codes, OOMKill events, and liveness probe failures with automated remediation suggestions.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install kubernetes-crashloop-diagnostician
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go patterns) to gather comprehensive diagnostic data about failing containers, their events, and resource consumption.
The diagnostic process starts by querying the Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container statuses, restart counts, last termination reasons, and exit codes. Common exit codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error), 127 (command not found), and 139 (segfault).
Event analysis uses the Events API to correlate pod events with node-level events, identifying patterns like repeated OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints), and FailedMount (volume issues). The skill also inspects liveness and readiness probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds or overly aggressive failureThreshold settings.
For deeper analysis, the skill leverages kubectl debug to attach ephemeral containers for live inspection, kubectl logs –previous to capture logs from the last crashed instance, and kubectl top pod for real-time resource usage. Remediation suggestions include specific resource limit adjustments, probe timing recommendations, and configuration fixes based on the diagnosed root cause.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/)
