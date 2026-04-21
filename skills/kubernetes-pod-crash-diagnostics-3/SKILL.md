---
title: "Kubernetes Pod Crash Diagnostics"
slug: "kubernetes-pod-crash-diagnostics-3"
description: "Runs kubectl describe pod, kubectl logs &#8211;previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Diagnostics

Runs kubectl describe pod, kubectl logs &#8211;previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/)
