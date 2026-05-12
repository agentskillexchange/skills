---
title: "Kubernetes Pod Crash Diagnostics"
slug: "kubernetes-pod-crash-diagnostics-3"
description: "Runs kubectl describe pod, kubectl logs --previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Developer Tools"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Diagnostics

Runs kubectl describe pod, kubectl logs --previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/)
