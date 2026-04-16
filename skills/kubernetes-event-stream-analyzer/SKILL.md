---
title: "Kubernetes Event Stream Analyzer"
description: "Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Event Stream Analyzer

The Kubernetes Event Stream Analyzer skill provides real-time monitoring and intelligent triage of Kubernetes cluster events through the Watch API. It maintains a persistent watch connection to the Events API, capturing pod scheduling decisions, container state transitions, volume mount failures, and node condition changes as they occur.

The skill correlates event streams with resource utilization data from the Kubernetes Metrics Server API, enabling detection of patterns like memory pressure leading to OOMKilled terminations, CPU throttling causing health check failures, and persistent volume claim binding delays impacting pod startup times. CrashLoopBackOff detection includes automatic log collection from previous container instances via the pod log API.

Advanced features include event deduplication with configurable time windows, anomaly detection based on historical event frequency baselines, and structured incident summaries that include the full event chain from scheduling through termination. The skill supports namespace filtering, label selector scoping, and field selector optimization to reduce API server load in large clusters with thousands of pods.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/)
