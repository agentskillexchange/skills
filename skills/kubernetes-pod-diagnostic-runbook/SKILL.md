---
title: "Kubernetes Pod Diagnostic Runbook"
description: "Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/)
