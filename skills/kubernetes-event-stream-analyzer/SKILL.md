---
name: "Kubernetes Event Stream Analyzer"
description: "Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage."
category: "Monitoring & Alerts"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# Kubernetes Event Stream Analyzer

Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage.

## Overview

The Kubernetes Event Stream Analyzer skill provides real-time monitoring and intelligent triage of Kubernetes cluster events through the Watch API. It maintains a persistent watch connection to the Events API, capturing pod scheduling decisions, container state transitions, volume mount failures, and node condition changes as they occur.

The skill correlates event streams with resource utilization data from the Kubernetes Metrics Server API, enabling detection of patterns like memory pressure leading to OOMKilled terminations, CPU throttling causing health check failures, and persistent volume claim binding delays impacting pod startup times. CrashLoopBackOff detection includes automatic log collection from previous container instances via the pod log API.

Advanced features include event deduplication with configurable time windows, anomaly detection based on historical event frequency baselines, and structured incident summaries that include the full event chain from scheduling through termination. The skill supports namespace filtering, label selector scoping, and field selector optimization to reduce API server load in large clusters with thousands of pods.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-event-stream-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-event-stream-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-event-stream-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-event-stream-analyzer -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-event-stream-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/
