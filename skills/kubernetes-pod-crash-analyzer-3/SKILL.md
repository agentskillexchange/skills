---
title: "Kubernetes Pod Crash Analyzer"
description: "Investigates CrashLoopBackOff and OOMKilled pod failures using kubectl and the Kubernetes API. Correlates container logs, event streams, and resource metrics from metrics-server to diagnose root causes automatically."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Pod Crash Analyzer

The Kubernetes Pod Crash Analyzer skill automates the diagnosis of pod failures in Kubernetes clusters. It uses the Kubernetes API (via kubectl or direct REST calls) to gather pod status, container states, event streams, and resource utilization data from metrics-server to build a comprehensive failure timeline.


For CrashLoopBackOff scenarios, the skill retrieves logs from previous container instances using the –previous flag, analyzes exit codes against known signal mappings (SIGKILL=137, SIGSEGV=139), and checks liveness/readiness probe configurations for timing issues. For OOMKilled events, it correlates memory limits from pod specs with actual consumption patterns from metrics-server.


The skill also inspects init container failures, volume mount permission issues via SecurityContext analysis, and network policy conflicts using Calico or Cilium CRDs. It can trace image pull failures through container runtime logs and validate imagePullSecrets against configured registry credentials. Output includes a structured diagnosis report with specific remediation steps and kubectl commands for applying fixes.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-analyzer-3/)
