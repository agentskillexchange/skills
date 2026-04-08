---
title: Kubernetes Pod Diagnostic Runbook
description: 'This skill provides an automated diagnostic runbook for Kubernetes pod
  issues, executing systematic troubleshooting steps through kubectl and the Kubernetes
  API. When triggered, it identifies the pod state and runs targeted diagnostic sequences:
  for CrashLoopBackOff it pulls container logs, previous container logs, and checks
  resource limits; for ImagePullBackOff it verifies image existence via the container
  registry API and checks imagePullSecrets; for OOMKilled it analyzes memory usage
  patterns from metrics-server and suggests limit adjustments. The runbook queries
  the Kubernetes Events API for related warnings, checks node conditions via kubectl
  describe node, and examines resource quotas and limit ranges in the namespace. It
  integrates with crictl for container runtime-level diagnostics when kubectl logs
  are insufficient. The skill generates structured diagnostic reports with root cause
  analysis and recommended remediation steps, and can automatically apply fixes like
  restarting deployments or scaling resource limits.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---

# Kubernetes Pod Diagnostic Runbook

This skill provides an automated diagnostic runbook for Kubernetes pod issues, executing systematic troubleshooting steps through kubectl and the Kubernetes API. When triggered, it identifies the pod state and runs targeted diagnostic sequences: for CrashLoopBackOff it pulls container logs, previous container logs, and checks resource limits; for ImagePullBackOff it verifies image existence via the container registry API and checks imagePullSecrets; for OOMKilled it analyzes memory usage patterns from metrics-server and suggests limit adjustments. The runbook queries the Kubernetes Events API for related warnings, checks node conditions via kubectl describe node, and examines resource quotas and limit ranges in the namespace. It integrates with crictl for container runtime-level diagnostics when kubectl logs are insufficient. The skill generates structured diagnostic reports with root cause analysis and recommended remediation steps, and can automatically apply fixes like restarting deployments or scaling resource limits.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/)
