---
name: Kubernetes Pod Crash Analyzer
description: Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl
  and the Kubernetes API. Correlates container logs, event streams, and resource metrics
  from metrics-server to diagnose root causes automatically.
category: "Runbooks &amp; Diagnostics"
framework: Gemini
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/"
---
# Kubernetes Pod Crash Analyzer

Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically.

The Kubernetes Pod Crash Analyzer skill automates the diagnosis of pod failures in Kubernetes clusters. It uses the Kubernetes API (via kubectl or direct REST calls) to gather pod status, container states, event streams, and resource utilization data from metrics-server to build a comprehensive failure timeline.

For CrashLoopBackOff scenarios, the skill retrieves logs from previous container instances using the –previous flag, analyzes exit codes against known signal mappings (SIGKILL=137, SIGSEGV=139), and checks liveness/readiness probe configurations for timing issues. For OOMKilled events, it correlates memory limits from pod specs with actual consumption patterns from metrics-server.

The skill also inspects init container failures, volume mount permission issues via SecurityContext analysis, and network policy conflicts using Calico or Cilium CRDs. It can trace image pull failures through container runtime logs and validate imagePullSecrets against configured registry credentials. Output includes a structured diagnosis report with specific remediation steps and kubectl commands for applying fixes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-analyzer-3 -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-analyzer-3
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/)
