---
title: "Kubernetes Diagnostics Agent"
description: "Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Diagnostics Agent

The Kubernetes Diagnostics Agent skill provides comprehensive cluster troubleshooting capabilities. It queries the Kubernetes API server debug endpoints including /debug/pprof for CPU and memory profiling of API server performance. Ephemeral debug containers are deployed via kubectl-debug to inspect running pods without restarting them, providing access to networking tools, strace, and filesystem inspection. The skill analyzes resource pressure using the Metrics Server API for real-time CPU and memory utilization, combined with kube-state-metrics for desired vs actual state analysis. It performs systematic diagnosis of common issues: CrashLoopBackOff analysis through container log parsing, ImagePullBackOff resolution via registry connectivity checks, pending pod investigation through scheduler event analysis, and node pressure evaluation. Advanced diagnostics include network policy testing with ephemeral pods, persistent volume claim binding analysis, RBAC permission auditing, and certificate expiration monitoring across the cluster.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/)
