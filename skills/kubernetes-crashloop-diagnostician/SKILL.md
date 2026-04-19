---
title: "Kubernetes CrashLoop Diagnostician"
description: "The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go patterns) to gather comprehensive diagnostic data about failing containers, their events, and resource consumption. The diagnostic process starts by querying the Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container statuses, restart counts, last termination reasons, and exit codes. Common exit codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error), 127 (command not found), and 139 (segfault). Event analysis uses the Events API to correlate pod events with node-level events, identifying patterns like repeated OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints), and FailedMount (volume issues). The skill also inspects liveness and readiness probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds or overly aggressive failureThreshold settings. For deeper analysis, the skill leverages kubectl debug to attach ephemeral containers for live inspection, kubectl logs &#8211;previous to capture logs from the last crashed instance, and kubectl top pod for real-time resource usage. Remediation suggestions include specific resource limit adjustments, probe timing recommendations, and configuration fixes based on the diagnosed root cause."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnostician

The Kubernetes CrashLoop Diagnostician skill provides systematic troubleshooting for pods stuck in CrashLoopBackOff state. It uses the Kubernetes API (via client-go patterns) to gather comprehensive diagnostic data about failing containers, their events, and resource consumption. The diagnostic process starts by querying the Pod status via the /api/v1/namespaces/{ns}/pods/{name} endpoint to extract container statuses, restart counts, last termination reasons, and exit codes. Common exit codes are mapped to root causes: 137 (OOMKilled or SIGKILL), 1 (application error), 127 (command not found), and 139 (segfault). Event analysis uses the Events API to correlate pod events with node-level events, identifying patterns like repeated OOMKill events (indicating memory limit too low), FailedScheduling (resource constraints), and FailedMount (volume issues). The skill also inspects liveness and readiness probe configurations, checking for common misconfigurations like insufficient initialDelaySeconds or overly aggressive failureThreshold settings. For deeper analysis, the skill leverages kubectl debug to attach ephemeral containers for live inspection, kubectl logs &#8211;previous to capture logs from the last crashed instance, and kubectl top pod for real-time resource usage. Remediation suggestions include specific resource limit adjustments, probe timing recommendations, and configuration fixes based on the diagnosed root cause.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostician/)
