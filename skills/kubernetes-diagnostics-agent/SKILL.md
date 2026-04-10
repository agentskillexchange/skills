---
title: "Kubernetes Diagnostics Agent"
description: "Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics."
slug: "kubernetes-diagnostics-agent"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/"
---

# Kubernetes Diagnostics Agent

Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics.

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
clawhub install kubernetes-diagnostics-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes Diagnostics Agent skill provides comprehensive cluster troubleshooting capabilities. It queries the Kubernetes API server debug endpoints including /debug/pprof for CPU and memory profiling of API server performance. Ephemeral debug containers are deployed via kubectl-debug to inspect running pods without restarting them, providing access to networking tools, strace, and filesystem inspection. The skill analyzes resource pressure using the Metrics Server API for real-time CPU and memory utilization, combined with kube-state-metrics for desired vs actual state analysis. It performs systematic diagnosis of common issues: CrashLoopBackOff analysis through container log parsing, ImagePullBackOff resolution via registry connectivity checks, pending pod investigation through scheduler event analysis, and node pressure evaluation. Advanced diagnostics include network policy testing with ephemeral pods, persistent volume claim binding analysis, RBAC permission auditing, and certificate expiration monitoring across the cluster.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/)
