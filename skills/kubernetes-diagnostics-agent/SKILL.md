---
name: "Kubernetes Diagnostics Agent"
description: "Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics."
category: "Runbooks &amp; Diagnostics"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/"
---
# Kubernetes Diagnostics Agent

Performs deep cluster troubleshooting using the Kubernetes API server /debug/pprof endpoints and kubectl-debug ephemeral containers. Analyzes resource pressure via the Metrics Server API and kube-state-metrics.

The Kubernetes Diagnostics Agent skill provides comprehensive cluster troubleshooting capabilities. It queries the Kubernetes API server debug endpoints including /debug/pprof for CPU and memory profiling of API server performance. Ephemeral debug containers are deployed via kubectl-debug to inspect running pods without restarting them, providing access to networking tools, strace, and filesystem inspection. The skill analyzes resource pressure using the Metrics Server API for real-time CPU and memory utilization, combined with kube-state-metrics for desired vs actual state analysis. It performs systematic diagnosis of common issues: CrashLoopBackOff analysis through container log parsing, ImagePullBackOff resolution via registry connectivity checks, pending pod investigation through scheduler event analysis, and node pressure evaluation. Advanced diagnostics include network policy testing with ephemeral pods, persistent volume claim binding analysis, RBAC permission auditing, and certificate expiration monitoring across the cluster.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostics-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostics-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostics-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostics-agent -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-diagnostics-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostics-agent/)
