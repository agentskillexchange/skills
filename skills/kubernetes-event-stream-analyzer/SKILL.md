---
name: "Kubernetes Event Stream Analyzer"
description: "Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Gemini"
  - "Multi-Framework"
---

# Kubernetes Event Stream Analyzer

The Kubernetes Event Stream Analyzer skill provides real-time monitoring and intelligent triage of Kubernetes cluster events through the Watch API. It maintains a persistent watch connection to the Events API, capturing pod scheduling decisions, container state transitions, volume mount failures, and node condition changes as they occur.
The skill correlates event streams with resource utilization data from the Kubernetes Metrics Server API, enabling detection of patterns like memory pressure leading to OOMKilled terminations, CPU throttling causing health check failures, and persistent volume claim binding delays impacting pod startup times. CrashLoopBackOff detection includes automatic log collection from previous container instances via the pod log API.
Advanced features include event deduplication with configurable time windows, anomaly detection based on historical event frequency baselines, and structured incident summaries that include the full event chain from scheduling through termination. The skill supports namespace filtering, label selector scoping, and field selector optimization to reduce API server load in large clusters with thousands of pods.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/)
