---
title: Kubernetes Pod Crash Diagnostician
description: The Kubernetes Pod Crash Diagnostician skill provides automated root
  cause analysis for pod crash loops in Kubernetes clusters. It connects to the Kubernetes
  API server to fetch pod events, container statuses, and recent restart history.
  For OOMKilled containers, it queries Prometheus via PromQL to retrieve historical
  memory usage patterns and container_memory_working_set_bytes metrics, identifying
  whether the OOM was caused by a memory leak, insufficient limits, or spike load.
  For CrashLoopBackOff pods, it analyzes container logs from the previous terminated
  instance, checks init container completion status, and validates volume mount accessibility.
  The skill inspects resource quotas, limit ranges, and pod disruption budgets that
  may constrain scheduling. Generates diagnostic reports with recommended resource
  limit adjustments based on P95 memory and CPU usage. Supports ephemeral debug containers
  via kubectl debug for live investigation. Integrates with Grafana dashboards for
  visual correlation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Code
---

# Kubernetes Pod Crash Diagnostician

The Kubernetes Pod Crash Diagnostician skill provides automated root cause analysis for pod crash loops in Kubernetes clusters. It connects to the Kubernetes API server to fetch pod events, container statuses, and recent restart history. For OOMKilled containers, it queries Prometheus via PromQL to retrieve historical memory usage patterns and container_memory_working_set_bytes metrics, identifying whether the OOM was caused by a memory leak, insufficient limits, or spike load. For CrashLoopBackOff pods, it analyzes container logs from the previous terminated instance, checks init container completion status, and validates volume mount accessibility. The skill inspects resource quotas, limit ranges, and pod disruption budgets that may constrain scheduling. Generates diagnostic reports with recommended resource limit adjustments based on P95 memory and CPU usage. Supports ephemeral debug containers via kubectl debug for live investigation. Integrates with Grafana dashboards for visual correlation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/)
