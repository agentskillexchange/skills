---
title: "Kubernetes Pod Diagnostic Runbook"
description: "This skill provides an automated diagnostic runbook for Kubernetes pod issues, executing systematic troubleshooting steps through kubectl and the Kubernetes API. When triggered, it identifies the pod state and runs targeted diagnostic sequences: for CrashLoopBackOff it pulls container logs, previous container logs, and checks resource limits; for ImagePullBackOff it verifies image existence via the container registry API and checks imagePullSecrets; for OOMKilled it analyzes memory usage patterns from metrics-server and suggests limit adjustments. The runbook queries the Kubernetes Events API for related warnings, checks node conditions via kubectl describe node, and examines resource quotas and limit ranges in the namespace. It integrates with crictl for container runtime-level diagnostics when kubectl logs are insufficient. The skill generates structured diagnostic reports with root cause analysis and recommended remediation steps, and can automatically apply fixes like restarting deployments or scaling resource limits."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostic Runbook

This skill provides an automated diagnostic runbook for Kubernetes pod issues, executing systematic troubleshooting steps through kubectl and the Kubernetes API. When triggered, it identifies the pod state and runs targeted diagnostic sequences: for CrashLoopBackOff it pulls container logs, previous container logs, and checks resource limits; for ImagePullBackOff it verifies image existence via the container registry API and checks imagePullSecrets; for OOMKilled it analyzes memory usage patterns from metrics-server and suggests limit adjustments. The runbook queries the Kubernetes Events API for related warnings, checks node conditions via kubectl describe node, and examines resource quotas and limit ranges in the namespace. It integrates with crictl for container runtime-level diagnostics when kubectl logs are insufficient. The skill generates structured diagnostic reports with root cause analysis and recommended remediation steps, and can automatically apply fixes like restarting deployments or scaling resource limits.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/)
