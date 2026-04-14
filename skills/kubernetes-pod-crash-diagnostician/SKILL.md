---
title: "Kubernetes Pod Crash Diagnostician"
description: "Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Diagnostician

The Kubernetes Pod Crash Diagnostician skill provides automated root cause analysis for pod crash loops in Kubernetes clusters. It connects to the Kubernetes API server to fetch pod events, container statuses, and recent restart history. For OOMKilled containers, it queries Prometheus via PromQL to retrieve historical memory usage patterns and container_memory_working_set_bytes metrics, identifying whether the OOM was caused by a memory leak, insufficient limits, or spike load. For CrashLoopBackOff pods, it analyzes container logs from the previous terminated instance, checks init container completion status, and validates volume mount accessibility. The skill inspects resource quotas, limit ranges, and pod disruption budgets that may constrain scheduling. Generates diagnostic reports with recommended resource limit adjustments based on P95 memory and CPU usage. Supports ephemeral debug containers via kubectl debug for live investigation. Integrates with Grafana dashboards for visual correlation.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/)
