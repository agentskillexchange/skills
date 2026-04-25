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
---

# Kubernetes Diagnostics Agent

The Kubernetes Diagnostics Agent skill provides comprehensive cluster troubleshooting capabilities. It queries the Kubernetes API server debug endpoints including /debug/pprof for CPU and memory profiling of API server performance. Ephemeral debug containers are deployed via kubectl-debug to inspect running pods without restarting them, providing access to networking tools, strace, and filesystem inspection. The skill analyzes resource pressure using the Metrics Server API for real-time CPU and memory utilization, combined with kube-state-metrics for desired vs actual state analysis. It performs systematic diagnosis of common issues: CrashLoopBackOff analysis through container log parsing, ImagePullBackOff resolution via registry connectivity checks, pending pod investigation through scheduler event analysis, and node pressure evaluation. Advanced diagnostics include network policy testing with ephemeral pods, persistent volume claim binding analysis, RBAC permission auditing, and certificate expiration monitoring across the cluster.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-diagnostics-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-diagnostics-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/)
