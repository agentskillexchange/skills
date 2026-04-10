---
title: "Kubernetes Pod Diagnostic Runbook"
description: "Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states."
slug: "kubernetes-pod-diagnostic-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/"
listed: true
---

# Kubernetes Pod Diagnostic Runbook

Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states.

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
clawhub install kubernetes-pod-diagnostic-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill provides an automated diagnostic runbook for Kubernetes pod issues, executing systematic troubleshooting steps through kubectl and the Kubernetes API. When triggered, it identifies the pod state and runs targeted diagnostic sequences: for CrashLoopBackOff it pulls container logs, previous container logs, and checks resource limits; for ImagePullBackOff it verifies image existence via the container registry API and checks imagePullSecrets; for OOMKilled it analyzes memory usage patterns from metrics-server and suggests limit adjustments. The runbook queries the Kubernetes Events API for related warnings, checks node conditions via kubectl describe node, and examines resource quotas and limit ranges in the namespace. It integrates with crictl for container runtime-level diagnostics when kubectl logs are insufficient. The skill generates structured diagnostic reports with root cause analysis and recommended remediation steps, and can automatically apply fixes like restarting deployments or scaling resource limits.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/)
