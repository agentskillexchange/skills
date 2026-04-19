---
title: "Kubernetes Incident Runbook"
description: "The Kubernetes Incident Runbook skill provides automated incident response procedures for Kubernetes cluster issues. It uses kubectl commands, the Kubernetes API, and kube-state-metrics to systematically diagnose common failure modes including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and node NotReady conditions. When triggered, the skill follows a structured diagnostic tree. For pod failures, it inspects container exit codes, retrieves previous container logs via kubectl logs &#8211;previous, checks resource requests/limits against actual usage from metrics-server, and examines events for scheduling or volume mount failures. For node-level issues, it analyzes node conditions (MemoryPressure, DiskPressure, PIDPressure), checks kubelet logs, inspects systemd service status, and correlates with cloud provider instance health. The skill understands taints, tolerations, and affinity rules that may cause scheduling failures. Advanced capabilities include tracing network connectivity issues using CoreDNS logs and NetworkPolicy analysis, diagnosing PersistentVolumeClaim binding failures across storage classes, and identifying resource quota exhaustion across namespaces. All findings are compiled into structured incident reports with remediation steps."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Incident Runbook

The Kubernetes Incident Runbook skill provides automated incident response procedures for Kubernetes cluster issues. It uses kubectl commands, the Kubernetes API, and kube-state-metrics to systematically diagnose common failure modes including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and node NotReady conditions. When triggered, the skill follows a structured diagnostic tree. For pod failures, it inspects container exit codes, retrieves previous container logs via kubectl logs &#8211;previous, checks resource requests/limits against actual usage from metrics-server, and examines events for scheduling or volume mount failures. For node-level issues, it analyzes node conditions (MemoryPressure, DiskPressure, PIDPressure), checks kubelet logs, inspects systemd service status, and correlates with cloud provider instance health. The skill understands taints, tolerations, and affinity rules that may cause scheduling failures. Advanced capabilities include tracing network connectivity issues using CoreDNS logs and NetworkPolicy analysis, diagnosing PersistentVolumeClaim binding failures across storage classes, and identifying resource quota exhaustion across namespaces. All findings are compiled into structured incident reports with remediation steps.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-incident-runbook/)
