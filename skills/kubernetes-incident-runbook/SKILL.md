---
title: Kubernetes Incident Runbook
description: The Kubernetes Incident Runbook skill provides automated incident response
  procedures for Kubernetes cluster issues. It uses kubectl commands, the Kubernetes
  API, and kube-state-metrics to systematically diagnose common failure modes including
  CrashLoopBackOff, OOMKilled, ImagePullBackOff, and node NotReady conditions. When
  triggered, the skill follows a structured diagnostic tree. For pod failures, it
  inspects container exit codes, retrieves previous container logs via kubectl logs
  –previous, checks resource requests/limits against actual usage from metrics-server,
  and examines events for scheduling or volume mount failures. For node-level issues,
  it analyzes node conditions (MemoryPressure, DiskPressure, PIDPressure), checks
  kubelet logs, inspects systemd service status, and correlates with cloud provider
  instance health. The skill understands taints, tolerations, and affinity rules that
  may cause scheduling failures. Advanced capabilities include tracing network connectivity
  issues using CoreDNS logs and NetworkPolicy analysis, diagnosing PersistentVolumeClaim
  binding failures across storage classes, and identifying resource quota exhaustion
  across namespaces. All findings are compiled into structured incident reports with
  remediation steps.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-incident-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Code
---

# Kubernetes Incident Runbook

The Kubernetes Incident Runbook skill provides automated incident response procedures for Kubernetes cluster issues. It uses kubectl commands, the Kubernetes API, and kube-state-metrics to systematically diagnose common failure modes including CrashLoopBackOff, OOMKilled, ImagePullBackOff, and node NotReady conditions. When triggered, the skill follows a structured diagnostic tree. For pod failures, it inspects container exit codes, retrieves previous container logs via kubectl logs –previous, checks resource requests/limits against actual usage from metrics-server, and examines events for scheduling or volume mount failures. For node-level issues, it analyzes node conditions (MemoryPressure, DiskPressure, PIDPressure), checks kubelet logs, inspects systemd service status, and correlates with cloud provider instance health. The skill understands taints, tolerations, and affinity rules that may cause scheduling failures. Advanced capabilities include tracing network connectivity issues using CoreDNS logs and NetworkPolicy analysis, diagnosing PersistentVolumeClaim binding failures across storage classes, and identifying resource quota exhaustion across namespaces. All findings are compiled into structured incident reports with remediation steps.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-incident-runbook/)
