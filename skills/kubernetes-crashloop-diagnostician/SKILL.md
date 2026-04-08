---
title: Kubernetes CrashLoop Diagnostician
description: 'The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting
  for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go
  patterns) to gather comprehensive diagnostic data about failing containers, their
  events, and resource consumption. The diagnostic process starts by querying the
  Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container
  statuses, restart counts, last termination reasons, and exit codes. Common exit
  codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error),
  127 (command not found), and 139 (segfault). Event analysis uses the Events API
  to correlate pod events with node-level events, identifying patterns like repeated
  OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints),
  and FailedMount (volume issues). The skill also inspects liveness and readiness
  probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds
  or overly aggressive failureThreshold settings. For deeper analysis, the skill leverages
  kubectl debug to attach ephemeral containers for live inspection, kubectl logs –previous
  to capture logs from the last crashed instance, and kubectl top pod for real-time
  resource usage. Remediation suggestions include specific resource limit adjustments,
  probe timing recommendations, and configuration fixes based on the diagnosed root
  cause.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Kubernetes CrashLoop Diagnostician

The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go patterns) to gather comprehensive diagnostic data about failing containers, their events, and resource consumption. The diagnostic process starts by querying the Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container statuses, restart counts, last termination reasons, and exit codes. Common exit codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error), 127 (command not found), and 139 (segfault). Event analysis uses the Events API to correlate pod events with node-level events, identifying patterns like repeated OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints), and FailedMount (volume issues). The skill also inspects liveness and readiness probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds or overly aggressive failureThreshold settings. For deeper analysis, the skill leverages kubectl debug to attach ephemeral containers for live inspection, kubectl logs –previous to capture logs from the last crashed instance, and kubectl top pod for real-time resource usage. Remediation suggestions include specific resource limit adjustments, probe timing recommendations, and configuration fixes based on the diagnosed root cause.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/)
