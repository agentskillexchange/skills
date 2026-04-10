---
title: "Kubernetes Pod Crash Analyzer"
description: "Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically."
slug: "kubernetes-pod-crash-analyzer-3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/"
---

# Kubernetes Pod Crash Analyzer

Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically.

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
clawhub install kubernetes-pod-crash-analyzer-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes Pod Crash Analyzer skill automates the diagnosis of pod failures in Kubernetes clusters. It uses the Kubernetes API (via kubectl or direct REST calls) to gather pod status, container states, event streams, and resource utilization data from metrics-server to build a comprehensive failure timeline.
For CrashLoopBackOff scenarios, the skill retrieves logs from previous container instances using the –previous flag, analyzes exit codes against known signal mappings (SIGKILL=137, SIGSEGV=139), and checks liveness/readiness probe configurations for timing issues. For OOMKilled events, it correlates memory limits from pod specs with actual consumption patterns from metrics-server.
The skill also inspects init container failures, volume mount permission issues via SecurityContext analysis, and network policy conflicts using Calico or Cilium CRDs. It can trace image pull failures through container runtime logs and validate imagePullSecrets against configured registry credentials. Output includes a structured diagnosis report with specific remediation steps and kubectl commands for applying fixes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/)
