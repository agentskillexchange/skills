---
title: Kubernetes Diagnostics Agent
description: 'The Kubernetes Diagnostics Agent skill provides comprehensive cluster
  troubleshooting capabilities. It queries the Kubernetes API server debug endpoints
  including /debug/pprof for CPU and memory profiling of API server performance. Ephemeral
  debug containers are deployed via kubectl-debug to inspect running pods without
  restarting them, providing access to networking tools, strace, and filesystem inspection.
  The skill analyzes resource pressure using the Metrics Server API for real-time
  CPU and memory utilization, combined with kube-state-metrics for desired vs actual
  state analysis. It performs systematic diagnosis of common issues: CrashLoopBackOff
  analysis through container log parsing, ImagePullBackOff resolution via registry
  connectivity checks, pending pod investigation through scheduler event analysis,
  and node pressure evaluation. Advanced diagnostics include network policy testing
  with ephemeral pods, persistent volume claim binding analysis, RBAC permission auditing,
  and certificate expiration monitoring across the cluster.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Code
---

# Kubernetes Diagnostics Agent

The Kubernetes Diagnostics Agent skill provides comprehensive cluster troubleshooting capabilities. It queries the Kubernetes API server debug endpoints including /debug/pprof for CPU and memory profiling of API server performance. Ephemeral debug containers are deployed via kubectl-debug to inspect running pods without restarting them, providing access to networking tools, strace, and filesystem inspection. The skill analyzes resource pressure using the Metrics Server API for real-time CPU and memory utilization, combined with kube-state-metrics for desired vs actual state analysis. It performs systematic diagnosis of common issues: CrashLoopBackOff analysis through container log parsing, ImagePullBackOff resolution via registry connectivity checks, pending pod investigation through scheduler event analysis, and node pressure evaluation. Advanced diagnostics include network policy testing with ephemeral pods, persistent volume claim binding analysis, RBAC permission auditing, and certificate expiration monitoring across the cluster.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/)
