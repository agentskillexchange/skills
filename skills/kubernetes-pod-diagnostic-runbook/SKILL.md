---
name: Kubernetes Pod Diagnostic Runbook
description: Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes
  API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled,
  and pending pod states.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/)
