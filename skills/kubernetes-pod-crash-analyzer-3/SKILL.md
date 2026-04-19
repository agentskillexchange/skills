---
title: "Kubernetes Pod Crash Analyzer"
description: "The Kubernetes Pod Crash Analyzer skill automates the diagnosis of pod failures in Kubernetes clusters. It uses the Kubernetes API (via kubectl or direct REST calls) to gather pod status, container states, event streams, and resource utilization data from metrics-server to build a comprehensive failure timeline. For CrashLoopBackOff scenarios, the skill retrieves logs from previous container instances using the &#8211;previous flag, analyzes exit codes against known signal mappings (SIGKILL=137, SIGSEGV=139), and checks liveness/readiness probe configurations for timing issues. For OOMKilled events, it correlates memory limits from pod specs with actual consumption patterns from metrics-server. The skill also inspects init container failures, volume mount permission issues via SecurityContext analysis, and network policy conflicts using Calico or Cilium CRDs. It can trace image pull failures through container runtime logs and validate imagePullSecrets against configured registry credentials. Output includes a structured diagnosis report with specific remediation steps and kubectl commands for applying fixes."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Analyzer

The Kubernetes Pod Crash Analyzer skill automates the diagnosis of pod failures in Kubernetes clusters. It uses the Kubernetes API (via kubectl or direct REST calls) to gather pod status, container states, event streams, and resource utilization data from metrics-server to build a comprehensive failure timeline. For CrashLoopBackOff scenarios, the skill retrieves logs from previous container instances using the &#8211;previous flag, analyzes exit codes against known signal mappings (SIGKILL=137, SIGSEGV=139), and checks liveness/readiness probe configurations for timing issues. For OOMKilled events, it correlates memory limits from pod specs with actual consumption patterns from metrics-server. The skill also inspects init container failures, volume mount permission issues via SecurityContext analysis, and network policy conflicts using Calico or Cilium CRDs. It can trace image pull failures through container runtime logs and validate imagePullSecrets against configured registry credentials. Output includes a structured diagnosis report with specific remediation steps and kubectl commands for applying fixes.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/)
